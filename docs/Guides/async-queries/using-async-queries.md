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
A query can be marked as async by setting the query parameter `async=true`. The query will return as soon as the query is accepted by the engine and will contain a response header `Firebolt-Async-Handler=<token>`. That token can then be used to look up the status.

If you are using the firebolt UI or a supported SDK, async handling in the client may already be implemented in an idiomatic way. 

## List of clients with async handling built in

- Firebolt UI
- JDBC driver

# How to check the status of an async query
The status of an async query can be checked via the built in stored procedure `get_async_query_status`. This will return all the information needed to evaluate if the query was successful or not:

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

CALL get_async_query_status('<token>'); -- This will return the status of the query.
```

## Columns in the response of get_async_query_status

`CALL get_async_query_status` will return a single row in the following schema.

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

# Permissions
The user calling `get_async_query_status` must have permissions to view the query. A user always has permission to view their own queries. To see another user's queries, they must have MONITOR ENGINE or MONITOR ALL privileges.