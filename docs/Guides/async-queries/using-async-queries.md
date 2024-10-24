---
layout: default
title: Async Queries
description: Learn how to submit async queries and get their status. 
parent: Overview # FIXME
nav_order: 1 # FIXME
---

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

If you are using the firebolt UI or a supported SDK, async handling in the client may already be implemented in an idiomatic way. 

## List of clients with async handling built in

- Firebolt UI
- JDBC driver

# How to check the status of an async query
The status of an async query can be checked via the built in stored procedure `fb_GetAsyncStatus`. This will return all the information needed to evaluate if the query was successful or not:

## Example
```sql
USE DATABASE test_db;
CREATE TABLE test (
  id text
);
SELECT * FROM test; -- Should return 0 rows

SET async = true;

INSERT INTO test 
    SELECT idMod7 as id 
    FROM (
        SELECT id%7 as idMod7
        FROM GENERATE_SERIES(1, 10000000000) s(id)
    )
GROUP BY idMod7; -- This will return right away, even if the query isn't finished

SET async=false;

CALL fb_GetAsyncStatus('<token>'); -- This will return the status of the query.
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
The token for checking the status is available in the original repsonse, but it is also available via the [engine_running_queries](../../sql_reference/information-schema/engine-running-queries.md) and [engine_query_history](../../sql_reference/information-schema/engine-query-history.md) views. 

### Example queries
```sql
SELECT query_id, async_token 
FROM information_schema.engine_running_queries
LIMIT 100;

SELECT query_id, async_token 
FROM information_schema.engine_query_history
LIMIT 100;
```

# Permissions
The user calling `fb_GetAsyncStatus` must have permissions to view the query. A user always has permission to view their own queries. To see another user's queries, they must have MONITOR ENGINE or MONITOR ALL privileges.