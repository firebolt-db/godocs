---
layout: default
title: Engine query history
description: Use this reference to learn about the metadata available for historical queries in Firebolt.
parent: Information schema
grand_parent: SQL reference
---

# Information schema for engine query history

You can use the `information_schema.engine_query_history` view to return information about queries saved to query history. The view is available in each database and contains two rows (start and finish) for each historical query in the database. You can use a `SELECT` query to return information about each query as shown in the example below.


```sql
SELECT
  *
FROM
  information_schema.engine_query_history
LIMIT
  100;
```

## Columns in information_schema.engine_query_history

Each row has the following columns with information about each query in query history.

| Column Name            | Data Type   | Description                                                                                                                                                                                                                                                                                                                                  |
|:-----------------------|:------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| account_name           | TEXT        | The ID of the account in which the query was executed. |
| user_name              | TEXT        | The user name that was used to execute the query. (present for account level operations otherwise NULL for org level ones) |
| logina_name              | TEXT      | The login name that was used to execute the query (present for org level statements otherwise NULL) |
| service_account_name   | TEXT        | The service account name that was used to execute the query (present for org level statements otherwise NULL) |
| submitted_time         | TIMESTAMPTZ | the time when the query was submitted by the user                                                                                                                                                                                                                                                                              |
| start_time             | TIMESTAMPTZ | The query execution start time (UTC).                                                                                                                                                                                                                                                                                                        |
| end_time               | TIMESTAMPTZ | The query execution end time (UTC)                                                                                                                                                                                                                                                                                                           |
| duration_usec          | BIGINT      | Duration of query execution (in microseconds).                                                                                                                                                                                                                                                                                               |
| status                 | TEXT        | Can be one of the following values:<br>`STARTED_EXECUTION`&ndash;Successful start of query execution.<br>`ENDED_SUCCESSFULLY`&ndash;Successful end of query execution.<br>`CANCELED_EXECUTION`&ndash;Query was canceled<br>`PARSE_ERROR`&ndash;Query could not be parsed<br>`EXECUTION_ERROR`&ndash;Query could not be executed successfully |
| query_label            | TEXT        | user provided query label (query_label parameter)                                                                                                                                                                                                                                                                                            |
| request_id             | TEXT        | The ID of the request from which the query originates.                                                                                                                                                                                                                                                                                       |
| query_id               | TEXT        | The unique identifier of the SQL query.                                                                                                                                                                                                                                                                                                      |
| query_text             | TEXT        | Text of the SQL statement.                                                                                                                                                                                                                                                                                                                   |
| error_message          | TEXT        | The error message that was returned.                                                                                                                                                                                                                                                                                                         |
| scanned_rows           | BIGINT      | The total number of rows scanned.                                                                                                                                                                                                                                                                                                            |
| scanned_bytes          | BIGINT      | The total number of bytes scanned (both from cache and storage).                                                                                                                                                                                                                                                                             |
| scanned_bytes_cache    | BIGINT      | The total number of compressed bytes scanned from the engine’s cache.                                                                                                                                                                                                                                                                        |
| scanned_bytes_storage  | BIGINT      | The total number of compressed bytes scanned from F3 storage.                                                                                                                                                                                                                                                                                |
| inserted_rows          | BIGINT      | The total number of rows written.                                                                                                                                                                                                                                                                                                            |
| inserted_bytes         | BIGINT      | The total number of bytes written (both to cache and storage).                                                                                                                                                                                                                                                                               |
| inserted_bytes_storage | BIGINT      | The total number of compressed bytes written to F3 storage.                                                                                                                                                                                                                                                                                  |
| spilled_bytes          | BIGINT      | The total number of bytes spilled (uncompressed).                                                                                                                                                                                                                                                                                            |
| total_ram_consumed     | BIGINT      | The total number of engine bytes in RAM consumed during query execution.                                                                                                                                                                                                                                                                     |
| returned_rows          | BIGINT      | The total number of rows returned from the query.                                                                                                                                                                                                                                                                                            |
| returned_bytes         | BIGINT      | The total number of bytes returned from the query.                                                                                                                                                                                                                                                                                           |
| cpu_usage_us           | BIGINT      | The query time spent on the CPU as reported by Linux kernel scheduler                                                                                                                                                                                                                                                                        |
| cpu_delay_us           | BIGINT      | The query time spent on the runqueue as reported by Linux kernel scheduler - The value may be greater than overall execution time of the query because query’s execution is parallelized and CPU times across all threads and nodes is summarized.                                                                                           |
| time_in_queue_ms       | BIGINT      | The number of milliseconds the query spent in queue.                                                                                                                                                                                                                                                                                         |
| retries        | BIGINT      | The total number of retries to execute a given query after a failure (by default, the number of retries is 0 and the number increases with each retry) |