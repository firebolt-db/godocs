---
layout: default
title: Asynchronous queries
description: Learn how to submit async queries and get their status. 
parent: API reference
nav_order: 2
---

# Asynchronous queries

An asynchronous query runs in the background and returns a successful response once it is accepted by the computing cluster, so that a client can proceed with other tasks without waiting for the statement to finish. The status of an asynchronous query can be checked at specified intervals, which provides flexibility, so that you can check the query's status at meaningful times based on the expected duration of the operation. For example, a user can avoid unnecessary resource consumption by only checking the status periodically, rather than maintaining an open connection for the entire duration of the query, which might be unreliable or unnecessary for certain tasks.

Asynchronous queries are ideal for long-running SQL statements, such as `INSERT`, `STOP ENGINE`, and `ALTER ENGINE`, where keeping an HTTP connection open is both unreliable and unnecessary, and where the statement might return zero rows. In addition, tracking them can be challenging. Using an asynchronous query allows you to check the status of operations at intervals, based on the expected duration.

You should use asynchronous queries for any supported operation that may take more than a few minutes for which there are no results.

**Supported asynchronous queries**

- [INSERT]({% link sql_reference/commands/data-management/insert.md %}) &ndash; Inserts one or more values into a specified table.
- [COPY FROM]({% link sql_reference/commands/data-management/copy-from.md %}) &ndash; Loads data from an Amazon S3 bucket into Firebolt.
- [COPY TO]({% link sql_reference/commands/data-management/copy-to.md %}) &ndash; Copies the result of a `SELECT` query to an Amazon S3 location.
- [VACUUM]({% link sql_reference/commands/data-management/vacuum.md %}) &ndash; Optimizes tablets for query performance.
- [CREATE AGGREGATING INDEX]({% link sql_reference/commands/data-definition/create-aggregating-index.md %}) &ndash; Creates an index for precomputing and storing frequent aggregations.
- [CREATE AS SELECT]({% link sql_reference/commands/data-definition/create-fact-dimension-table-as-select.md %}) &ndash; Creates a table and loads data into it based on a `SELECT` query.
- [Engine commands]({% link sql_reference/commands/engines/index.md %}) including [ALTER ENGINE]({% link sql_reference/commands/engines/alter-engine.md %}), [STOP ENGINE]({% link sql_reference/commands/engines/stop-engine.md %}), and [START ENGINE]({% link sql_reference/commands/engines/start-engine.md %}). By default, Firebolt engines finish running queries before returning results, which can take significant time. Starting an engine can also take more than a few minutes.

## How to submit an asynchronous query

You can only submit a synchronous query programmatically using the Firebolt API or the following listed drivers. Every SQL statement submitted using the Firebolt **Develop Space** user interface is a synchronous query. 

The following are required prerequisites to submit a query programmatically:

1. **A Firebolt account** &ndash; Ensure that you have access to an active Firebolt account. If you don't have access, you can [sign up for an account](https://www.firebolt.io/sign-up). For more information about how to register with Firebolt, see [Get started with Firebolt]({% link Guides/getting-started/index.md %}).
2. **A Firebolt service account** &ndash; You must have access to an active Firebolt [service account]({% link Guides/managing-your-organization/service-accounts.md %}), which facilitates programmatic access to Firebolt.
3. **A user associated with the Firebolt service account** &ndash; You must associate a [user]({% link Guides/managing-your-organization/managing-users.md %}#-users) with your service account, and the user must have the necessary permissions to run the query on the specified database using the specified engine.
4. **Sufficient permissions** If you want to query user data through a specific engine, you must have sufficient permissions on the engine, as well as on any tables and databases you access.

To submit an asynchronous query via a raw HTTP request, you must use Firebolt protocol version 2.3 or later, while query status can be checked with any client. You can verify the protocol version by checking the X-Firebolt-Protocol-Version header in API response.

## Use a Firebolt Driver

Use a Firebolt driver to connect to a Firebolt database, authenticate securely, and run SQL statements with minimal setup. The driver provides built-in methods for running SQL statements, handling responses, and managing connections. Only some Firebolt drivers support synchronous queries. See the documentation for each driver for specific details on how to submit asynchronous queries programmatically:

* [Python SDK]({% link Guides/developing-with-firebolt/connecting-with-Python.md %}) &ndash; Firebolt Python SDK
* [Node.js]({% link Guides/developing-with-firebolt/connecting-with-nodejs.md %}) &ndash; Firebolt Node SDK

## Submit a query

Submitting a query through a Firebolt drivers and SDKs have similar formats. The following code example shows how to submit an asynchronous query using the [Python SDK]({% link Guides/developing-with-firebolt/connecting-with-Python.md %}). For other languages, consult the specific driver for details:

The following code example establishes a connection to a Firebolt database using a service account, submits an asynchronous `INSERT` statement that groups generated numbers, periodically checks its run status, and then retrieves the row count from the `example` table:

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

### Check query statusy

The query status token is included in the initial response when the query is submitted. If needed, you can also retrieve the token from the [engine_running_queries]({% link sql_reference/information-schema/engine-running-queries.md %}) view.

To check the status of an asynchronous query, use the token with the `CALL fb_GetAsyncStatus` function as follows:

```sql
CALL fb_GetAsyncStatus('<async_token>');
```

The previous code example returns a single row with the following schema:

| Column Name                 | Data Type   | Description |
| :---------------------------| :-----------| :-----------|
| account_name                | TEXT        | The name of the account where the asynchronous query was submitted. |
| user_name                   | TEXT        | The name of the user who submitted the asynchronous query. |
| request_id                  | TEXT        | Unique ID of the request which submitted the asynchronous query. |
| query_id                    | TEXT        | Unique ID of the asynchronous query. |
| status                      | TEXT        | Current status of the query: SUSPENDED, RUNNING, CANCELLED, FAILED, SUCCEEDED or IN_DOUBT. |
| submitted_time              | TIMESTAMPTZ | The time the asynchronous query was submitted. |
| start_time                  | TIMESTAMPTZ | The time the async query was most recently started. |
| end_time                    | TIMESTAMPTZ | If the asynchronous query is completed, the time it finished. |
| error_message               | TEXT        | If the asynchronous query failed, the error message from the failure. |
| retries                     | LONG        | The number of times the asynchronous query has retried. |
| scanned_bytes               | LONG        | The number of bytes scanned by the asynchronous query. |
| scanned_rows                | LONG        | The number of rows scanned by the asynchronous query. |

### Cancel a query

A running asynchronous query can be cancelled using the [CANCEL]({% link sql_reference/commands/queries/cancel.md %}) statement as follows:

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
