---
layout: default
title: Engine running queries
description: Use this reference to learn about the metadata available for running queries in Firebolt using the information schema.
parent: Information schema
grand_parent: SQL reference
---

# Information schema for engine running queries

You can use the `information_schema.engine_running_queries` view to return information about queries currently running in a database. The view is available in each database and contains one row for each running query in the database. You can use a `SELECT` query to return information about each running query as shown in the example below.
The table is limited to contain at max 10'000 queries per engine cluster.

```sql
SELECT
  *
FROM
   information_schema.engine_running_queries
LIMIT
  100;
```

## Columns in information_schema.engine_running_queries

Each row has the following columns with information about each running query.

| Column Name    | Data Type   | Description                                                                                                                                            |
|:---------------|:------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|
| account_name   | TEXT        | The name of the account in which the query was executed.                                                                                               |
| user_name      | TEXT        | The user that executed the query                                                                                                                       |
| submitted_time | TIMESTAMPTZ | The time when the query was submitted by a user (UTC)                                                                                                  |
| start_time     | TIMESTAMPTZ | The query execution start time (UTC).                                                                                                                  |
| duration_us    | BIGINT      | The elapsed time in microseconds between `<START_TIME>` and the time that the query over `information_schema.engine_running_queries` returns results.  |
| status         | TEXT        | The status of the query.                                                                                                                               |
| request_id     | TEXT        | The ID of the request from which the query originates.                                                                                                 |
| query_id       | TEXT        | The query id of this query.                                                                                                                            |
| query_label    | TEXT        | User provided query label (query_label parameter)                                                                                                      |
| query_text     | TEXT        | Text of the SQL statement.                                                                                                                             |
| scanned_rows   | BIGINT      | The number of rows scanned to return query results.                                                                                                    |
| scanned_bytes  | BIGINT      | The number of bytes scanned from cache and storage.                                                                                                    |
| inserted_rows  | BIGINT      | The number of rows written                                                                                                                             |
| inserted_bytes | BIGINT      | The number of bytes written.                                                                                                                           |
| retries        | BIGINT      | The total number of retries to execute a given query after a failure (by default, the number of retries is 0 and the number increases with each retry) |
