---
layout: default
title: Asynchronous queries
description: Learn how to submit async queries and get their status. 
parent: API reference
nav_order: 2
---

# Asynchronous queries

An asynchronous query runs in the background and returns a successful response once it is accepted by the computing cluster, so that a client can proceed with other tasks without waiting for the query to finish. The status of an asynchronous query can be checked at specified intervals, which provides flexibility, so that you can check the query's status at meaningful times based on the expected duration of the operation. For example, a user can avoid unnecessary resource consumption by only checking the status periodically, rather than maintaining an open connection for the entire duration of the query, which might be unreliable or unnecessary for certain tasks.

Asynchronous queries are ideal for long-running operations, such as `INSERT`, `VACUUM`, or `COPY INTO`, where keeping an HTTP connection open is both unreliable and unnecessary, and where the query might return zero rows. While these operations continue running even if the connection drops, tracking them can be challenging. Using an asynchronous query allows you to check the status of operations at intervals, based on the expected duration.

You should use asynchronous queries for any supported operation that may take more than a few minutes for which there are no results.

**Supported asynchronous queries**

- Insert queries
- Engine operations (START ENGINE, STOP ENGINE, ALTER ENGINE, etc.)

## How to submit an asynchronous query

You can only submit a synchronous query programmatically using the Firebolt API. Every query submitted using the Firebolt **Develop Space** user interface is a synchronous query. 

The following are required prerequisites to submit a query programmatically:

- **Firebolt account** &ndash; You need an active Firebolt account. If you do not have one, you can [sign up](https://go.firebolt.io/signup) for one.
- **Firebolt database and engine** &ndash; You must have access to a Firebolt database. If you do not have access, you can [create a database]({% link Guides/getting-started/get-started-sql.md %}#create-a-database) and then [create an engine]({% link Guides/getting-started/get-started-sql.md %}#create-an-engine).
- **Firebolt service account** &ndash; You must have an active Firebolt [service account]({% link Guides/managing-your-organization/service-accounts.md %}) for programmatic access, along with its ID and secret.
- **Permissions** &ndash; You will need to have [USAGE permission]({% link Overview/Security/Role-Based Access Control/engine-permissions.md %}#engine-permissions) on the engine that runs the query. A user always has permission to view their own queries. To see another user's queries, you must have `MONITOR ENGINE` or `MONITOR ALL` privileges. A user calling `fb_GetAsyncStatus` must have permissions to view the query.

To submit an asynchronous query via a raw HTTP request, you must use Firebolt protocol version 2.3 or later, while query status can be checked with any client using protocol version 2.1 or later. You can verify the protocol version by checking the X-Firebolt-Protocol-Version header in API response.

## Use a Firebolt SDK

Use a Firebolt SDK to connect to a Firebolt database, authenticate securely, and run queries with minimal setup. The SDK provides built-in methods for running queries, handling responses, and managing connections. Only some Firebolt SDKs support synchronous queries. See the documentation for each SDK or driver for specific details on how to submit asynchronous queries programmatically:

* [Python SDK]({% link Guides/developing-with-firebolt/connecting-with-Python.md %}) &ndash; Firebolt Python SDK
* [SQLAlchemy]({% link Guides/developing-with-firebolt/connecting-with-sqlalchemy.md %}) &ndash; Firebolt SQLAlchemy adapter
* [.NET SDK]({% link Guides/developing-with-firebolt/connecting-with-net-sdk.md %}) &ndash; Firebolt .NET SDK

### Firebolt API endpoint

To submit a synchronous query programmatically, use the following API endpoint:

- **API URL:** `https://api.app.firebolt.io/v1/query/run`
- **HTTP Method:** `POST`
- **Headers:**
  - `Authorization: Bearer <your_access_token>`
  - `Content-Type: application/json`
- **Authentication:** Use your Firebolt service account ID and secret to obtain an access token.

### **Request body format**

An asynchronous query request must be sent as a JSON object with the following structure:

```json
{
  "database": "<your_database_name>",
  "engine_name": "<your_engine_name>",
  "account": "<your_account_name>",
  "query": "INSERT INTO my_table SELECT * FROM another_table",
  "async": true
}
```
In the previous JSON request, the following apply:

| Field         | Type    | Required | Description |
|--------------|--------|----------|-------------|
| `database`   | String | Yes      | The Firebolt database where the query will run. |
| `engine_name` | String | Yes      | The Firebolt engine that will process the query. |
| `account`    | String | Yes      | The Firebolt account associated with the query. |
| `query`      | String | Yes      | The SQL query to be executed asynchronously. |
| `async`      | Boolean | Yes      | Must be set to `true` to indicate an asynchronous query. |

### Response body format

A successful response for an asynchronous query returns HTTP status 202 with JSON output containing:

* `message` &ndash; Confirmation that the query has been accepted for asynchronous execution.
* `token` &ndash; A unique identifier for tracking the query's progress.
* `monitorSql` &ndash; A SQL command that can be used to check the query status.

An example response follows:
{
  "message": "the query was accepted for async processing",
  "token": ["<token>"],
  "monitorSql": "CALL fb_GetAsyncStatus('<async_token>');"
}

## Python example API call

The following code example establishes a connection to a Firbolt database using a service account, submits an asynchronous `INSERT` query that groups generated numbers, periodically checks its run status, and then retrieves the row count from the `example` table:

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

## Error handling

| Error Type          | Cause                                           | Solution |
|---------------------|------------------------------------------------|----------|
| **Invalid request** | Missing or incorrect parameters in the request body. | Ensure the request includes `database`, `engine_name`, `query`, and other required fields. |
| **Protocol version mismatch** | Using an outdated Firebolt protocol version. | Use protocol version 2.3 or later to submit queries and 2.1 or later to check status. |
| **Query failure**  | The query encounters an execution error. | Check the error message in `fb_GetAsyncStatus` and validate the query syntax. |
| **Permission denied** | The user lacks required privileges. | Ensure the user has the necessary permissions to submit the query and view its status. |
| **Token not found** | The provided async query token is invalid or expired. | Verify that the correct token is being used and that the query has not expired. |
| **Engine unavailable** | The specified Firebolt engine is not running. | Start the engine before submitting the query. |


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