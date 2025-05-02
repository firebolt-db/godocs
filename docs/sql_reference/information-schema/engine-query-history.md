---
redirect_from:
  - /general-reference/information-schema/query-history-view.html
layout: default
title: Engine query history
description: Use this reference to learn about the metadata available for historical queries in Firebolt.
parent: Information schema
grand_parent: SQL reference
---

# Information schema for engine query history

You can use the `information_schema.engine_query_history` view to return information about queries saved to query history. The view is available in each database and contains two rows, the starting and ending row for each historical query in the database. The table includes the last ten thousand queries per engine cluster.
You can run a `SELECT` query to retrieve details about recent queries, as shown in the following example:

```sql
SELECT
  *
FROM
  information_schema.engine_query_history
LIMIT
  100;
```

{: .note}
The `information_schema.engine_query_history` view retains only the most recent 10,000 queries. Queries exceeding this limit are excluded and will not appear in the query history. This limitation is important for high-volume workloads and tools like the [OTEL exporter]({% link Guides/integrations/otel-exporter.md %}), which can rapidly fill the query history. To retain critical query data, regularly export or archive query history.

## Columns in information_schema.engine_query_history

Each row has the following columns with information about each query in query history.

| Column Name                | Data Type   | Description |
|:---------------------------|:------------|:------------|
| account_name               | TEXT        | The name of the account that ran the query.|
| user_name                  | TEXT        | The user name that was used to run the query. The `user_name` is present for account-level operations, and `NULL` for organization-level operations.|
| login_name                 | TEXT        | The login name that was used to run the query. The `login_name` is present for organization-level statements, and otherwise `NULL`.|
| service_account_name       | TEXT        | The service account name that was used to run the query. The `service_account_name` is present for organization-level statements, and otherwise `NULL`.|
| submitted_time             | TIMESTAMPTZ | The time that the user submitted the query.|
| start_time                 | TIMESTAMPTZ | The time that the query started running in Coordinated Universal Time (UTC).|
| end_time                   | TIMESTAMPTZ | The time that the query stopped running in UTC.|
| duration_us                | BIGINT      | The duration of query run time in microseconds.|
| e2e_duration_us            | BIGINT      | The end-to-end duration of query run time. Starting from the time the query was submitted and ending when the result was fully returned in microseconds. |
| status                     | TEXT        | Can be one of the following values:<br>`STARTED_EXECUTION`&ndash;Successful start of query execution.<br>`ENDED_SUCCESSFULLY`&ndash;Successful end of query execution.<br>`CANCELED_EXECUTION`&ndash;Query was canceled.<br>`PARSE_ERROR`&ndash;Query could not be parsed.<br>`EXECUTION_ERROR`&ndash;Query could not be executed successfully.|
| request_id                 | TEXT        | The ID of the request from which the query originates.|
| query_id                   | TEXT        | The unique identifier of the SQL query.|
| query_label                | TEXT        | A user-provided query label.|
| query_text                 | TEXT        | The text of the SQL statement.|
| query_text_normalized      | TEXT        | The normalized text of the SQL statement.|
| query_text_normalized_hash | TEXT        | The hash of the normalized text of the SQL statement.|
| error_message              | TEXT        | The returned error message.|
| scanned_rows               | BIGINT      | The total number of rows scanned.|
| scanned_bytes              | BIGINT      | The total number of uncompressed bytes scanned.|
| scanned_cache_bytes        | BIGINT      | The total number of compressed bytes scanned from disk-based cache.|
| scanned_storage_bytes      | BIGINT      | The total number of compressed bytes scanned from Firebolt-managed storage. Does not apply to [EXTERNAL tables]({% link Overview/indexes/using-indexes.md %}#external-tables).|
| inserted_rows              | BIGINT      | The total number of rows written.|
| inserted_bytes             | BIGINT      | The total number of bytes written to both cache and storage.|
| spilled_bytes              | BIGINT      | The total number of uncompressed bytes spilled.|
| returned_rows              | BIGINT      | The total number of rows returned from the query.|
| returned_bytes             | BIGINT      | The total number of bytes returned from the query.|
| time_in_queue_us           | BIGINT      | The number of microseconds the query spent in queue.|
| retries                    | BIGINT      | The number of retried attempts in case of query failure. Defaults to 0.|
| telemetry                  | TEXT        | Displays additional telemetry information about the query in JSON format. This data is currently only available for VACUUM queries and jobs.|