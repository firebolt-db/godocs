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


# When to use async queries
Async queries should be used for any supported operation that may take more than a few minutes for which there are no results.

## List of supported kinds of queries 

- Insert queries
- Engine operations (START ENGINE, STOP ENGINE, ALTER ENGINE, etc.)

# How to submit an async query

## Using a firebolt SDK
Some firebolt SDKs have idiomatic async support built in. 

## Python Example
```python
from time import sleep

from firebolt.db import connect
from firebolt.client.auth import ClientCredentials

id = "service_account_id"
secret = "service_account_secret"
engine_name = "your_engine_name"
database_name = "your_test_db"
account_name = "your_account_name"

# Example insert query
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

## Using a HTTP request

A query can be marked as async by setting the query parameter `async=true`. The query will return as soon as the query is accepted by the engine with HTTP status 202, and the body will contain the token. 

## Example body
```
{
  "message": "the query was accepted for async processing",
  "token": ["<token>"],
  "monitorSql": "CALL fb_GetAsyncStatus('<async_token>');"
}
```

If using a raw HTTP request, you must use firebolt protocal version 2.3 or newer to submit an async query. Query status can be checked using any client at protocal version 2.1 or newer.

# How to check the status of an async query
## Token discovery
The token for checking the status is available in the original repsonse, but it is also available via the [engine_running_queries](../../sql_reference/information-schema/engine-running-queries.md) view. 

## Columns in the response of fb_GetAsyncStatus

`CALL fb_GetAsyncStatus` will return a single row in the following schema.

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


### Example queries
```sql
SELECT query_id, async_token 
FROM information_schema.engine_running_queries
LIMIT 100;

CALL fb_GetAsyncStatus('<async_token>');
```

# Permissions
Submitting an async query does not require any different permissions than the query would require if it were not async. The user calling `fb_GetAsyncStatus` must have permissions to view the query. A user always has permission to view their own queries. To see another user's queries, they must have MONITOR ENGINE or MONITOR ALL privileges.