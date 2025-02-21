---
layout: default
title: Asynchronous queries
description: Learn how to submit async queries and get their status. 
parent: API reference
nav_order: 2
---

# Asynchronous queries

An asynchronous query runs in the background and returns a successful response once it is accepted by the computing cluster, so that a client can proceed with other tasks without waiting for the statement to finish. The status of an asynchronous query can be checked at specified intervals, which provides flexibility, so that you can check the query's status at meaningful times based on the expected duration of the operation. For example, a user can avoid unnecessary resource consumption by only checking the status periodically, rather than maintaining an open connection for the entire duration of the query, which might be unreliable or unnecessary for certain tasks.

Asynchronous queries are ideal for long-running sql statements, such as `INSERT`, `VACUUM`, or `COPY INTO`, where keeping an HTTP connection open is both unreliable and unnecessary, and where the statement might return zero rows. While these operations continue running even if the connection drops, tracking them can be challenging. Using an asynchronous query allows you to check the status of operations at intervals, based on the expected duration.

You should use asynchronous queries for any supported operation that may take more than a few minutes for which there are no results.

**Supported asynchronous queries**

- Insert statements
- Engine operations (START ENGINE, STOP ENGINE, ALTER ENGINE, etc.)

## How to submit an asynchronous query

You can only submit a synchronous query programmatically using the Firebolt API. Every sql statement submitted using the Firebolt **Develop Space** user interface is a synchronous query. 

The following are required prerequisites to submit a query programmatically:

- **Firebolt account** &ndash; You need an active Firebolt account. If you do not have one, you can [sign up](https://go.firebolt.io/signup) for one.
- **Firebolt database and engine** &ndash; You must have access to a Firebolt database. If you do not have access, you can [create a database]({% link Guides/getting-started/get-started-sql.md %}#create-a-database) and then [create an engine]({% link Guides/getting-started/get-started-sql.md %}#create-an-engine).
- **Firebolt service account** &ndash; You must have an active Firebolt [service account]({% link Guides/managing-your-organization/service-accounts.md %}) for programmatic access, along with its ID and secret.
- **Permissions** &ndash; You will need to have [USAGE permission]({% link Overview/Security/Role-Based Access Control/engine-permissions.md %}#engine-permissions) on the engine that runs the query. A user always has permission to view their own queries. To see another user's queries, you must have `MONITOR ENGINE` or `MONITOR ALL` privileges. A user calling `fb_GetAsyncStatus` must have permissions to view the query.

To submit an asynchronous query via a raw HTTP request, you must use Firebolt protocol version 2.3 or later, while query status can be checked with any client using protocol version 2.1 or later. You can verify the protocol version by checking the X-Firebolt-Protocol-Version header in API response.

## Use a Firebolt Driver

Use a Firebolt driver to connect to a Firebolt database, authenticate securely, and run sql statements with minimal setup. The driver provides built-in methods for running sql statements, handling responses, and managing connections. Only some Firebolt drivers support synchronous queries. See the documentation for each driver for specific details on how to submit asynchronous queries programmatically:

* [Python SDK]({% link Guides/developing-with-firebolt/connecting-with-Python.md %}) &ndash; Firebolt Python SDK
* [SQLAlchemy]({% link Guides/developing-with-firebolt/connecting-with-sqlalchemy.md %}) &ndash; Firebolt SQLAlchemy adapter
* [Go SDK]({% link Guides/developing-with-firebolt/connecting-with-go.md %}) &ndash; Firebolt Go SDK

## Python example API call

The following code example establishes a connection to a Firbolt database using a service account, submits an asynchronous `INSERT` statement that groups generated numbers, periodically checks its run status, and then retrieves the row count from the `example` table:

```python
from time import sleep

from firebolt.db import connect
from firebolt.client.auth import ClientCredentials

id = "service_account_id"
secret = "service_account_secret"
engine_name = "your_engine_name"
database_name = "your_test_db"
account_name = "your_account_name"

query = """
    INSERT INTO example SELECT idMod7 as id
    FROM (
        SELECT id%7 as idMod7
        FROM GENERATE_SERIES(1, 10000000000) s(id)
    )
    GROUP BY idMod7;
    """

with connect(
    engine_name=engine_name,
    database=database_name,
    account_name=account_name,
    auth=ClientCredentials(id, secret),
) as connection:
    cursor = connection.cursor()

    cursor.execute_async(query) # Needs firebolt-sdk 1.9.0 or later
    # Token lets us check the status of the query later
    token = cursor.async_query_token
    print(f"Query Token: {token}")

    # Block until the query is done
    # You can also do other work here
    while connection.is_async_query_running(token):
        print("Checking query status...")
        sleep(5)

    status = "Success" if connection.is_async_query_successful(token) else "Failed"
    print(f"Query Status: {status}")

    cursor.execute("SELECT count(*) FROM example;")  # Should contain 7 rows
    for row in cursor.fetchall():
        print(row)
```

### How to check the status of an async query

The query status token is included in the initial response when the query is submitted. If needed, you can also retrieve the token from the [engine_running_queries](../../sql_reference/information-schema/engine-running-queries.md) view.

To check the status of an asynchronous query, use the token with the `CALL fb_GetAsyncStatus` function as follows:

```sql
CALL fb_GetAsyncStatus('<async_token>');
```

The previous code example returns a single row with the following schema:

| Column Name                 | Data Type   | Description |
| :---------------------------| :-----------| :-----------|
| account_name                | TEXT        | Name of the account where the async query was submitted. |
| user_name                   | TEXT        | Name of the user who submitted the async query. |
| request_id                  | TEXT        | Unique ID of the request which submitted the async query. |
| query_id                    | TEXT        | Unique ID of the async query. |
| status                      | TEXT        | Current status of the query: SUSPENDED, RUNNING, CANCELLED, FAILED, SUCCEEDED or IN_DOUBT. |
| submitted_time              | TIMESTAMPTZ | Time the async query was submitted. |
| start_time                  | TIMESTAMPTZ | Time the async query was most recently started. |
| end_time                    | TIMESTAMPTZ | If the async query is completed, the time it finished. |
| error_message               | TEXT        | If the async query failed, the error message from the failure. |
| retries                     | LONG        | Number of times the async query has retried. |
| scanned_bytes               | LONG        | Number of bytes scanned by the async query. |
| scanned_rows                | LONG        | Number of rows scanned by the async query. |

### Query cancelation

A running asynchronous query can be cancelled using the [cancel]({% link sql_reference/commands/queries/cancel.md %}) statement as follows:

```sql
CANCEL QUERY '<query_id>';
```

In the previous code example, retrieve the query ID from the [engine_running_queries]({% link sql_reference/information-schema/engine-running-queries.md %}) view or from the original query submission response.

## Error handling

| Error Type          | Cause                                           | Solution |
|---------------------|------------------------------------------------|----------|
| **Protocol version mismatch** | Using an outdated Firebolt protocol version. | Make sure your driver supports async queries. |
| **Query failure**  | The query encounters an execution error. | Check the error message in `fb_GetAsyncStatus` and validate the query syntax. |
| **Token not found** | The provided async query token is invalid or expired. | Verify that the correct token is being used and that the query has not expired. |
| **Engine does not exist or you don't have permission to access it** | The specified Firebolt engine is not running or you don't have permission to access it. | Start the engine before submitting the query and double check permissions. |
