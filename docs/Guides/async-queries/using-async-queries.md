---
layout: default
title: Async Queries
description: Learn how to submit async queries and get their status. 
parent: Overview # FIXME
nav_order: 1 # FIXME
---

# What are async queries?
Usually, when a query is submitted to firebolt, the http connection is kept open for the duration of the query, with the status and results returned as they are available. For some operations though, this model doesn't make sense. Queries like insert, vacuum, or copy to may run for a long time, and return 0 rows at the end anyway. Keeping an HTTP connection open for a very long time can also be unreliable. By default, these types of queries continue to run on connection drops, but can be challenging to check and reason about after the connection has dropped.

The solution to this problem is async queries. When an async query is submitted, the client gets a successful response as soon as it is accepted by the cluster. The client can then check the status of the query at a frequency that is meaningful to them and dependent on the amount of time the query is expected to take.

# When to use async queries
Async queries should be used for any supported operation that may take more than a few minutes for which there are no results.

## List of supported kinds of queries 

- Insert queries
- Engine operations (START ENGINE, STOP ENGINE, ALTER ENGINE, etc.)

# How to submit an async query
A query can be marked as async by setting the query parameter `async=true`. The query will return as soon as the query is accepted by the engine with HTTP status 202, and the body will contain the token. 

## Example body
```
{
  "message": "the query was accepted for async processing",
  "token": ["<token>"],
  "monitorSql": "CALL fb_GetAsyncStatus('<token>');"
}
```

If you are using the firebolt UI or a supported SDK, async handling in the client may already be implemented in an idiomatic way. Your SDK or client should be using firebolt protocal version 2.3 or newer to submit an async query. Query status can be checked using any client at protocal version 2.1 or newer.

# How to check the status of an async query
The status of an async query can be checked via the built in stored procedure `fb_GetAsyncStatus`. This will return all the information needed to evaluate if the query was successful or not:

## Example
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

## Token discovery
The token for checking the status is available in the original repsonse, but it is also available via the [engine_running_queries](../../sql_reference/information-schema/engine-running-queries.md) view. 

### Example queries
```sql
SELECT query_id, async_token 
FROM information_schema.engine_running_queries
LIMIT 100;
```

# Permissions
The user calling `fb_GetAsyncStatus` must have permissions to view the query. A user always has permission to view their own queries. To see another user's queries, they must have MONITOR ENGINE or MONITOR ALL privileges.