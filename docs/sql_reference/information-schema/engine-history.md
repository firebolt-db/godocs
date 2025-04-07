---
layout: default
title: Engine history
parent: Information schema
grand_parent: SQL reference
---

# Information schema for engine history

You can use the `information_schema.engine_history` view to return information about each engine's history in an account. The view shows operations performed on each engine, including creation, deletion, starts, stops, resizing, and logical operations like renames. It is often useful to filter this view to a particular engine. In the example below, a filter is applied to look at the history of engines starting with `capacity_test_`. By default, shows the events from the last 30 days.

```sql
SELECT
  *
FROM
  information_schema.engine_history
WHERE
  engine_name LIKE 'capacity_test_%'
```

## Columns in information_schema.engines_history

Each row has the following columns with information about each engine.

| Column Name                 | Data Type   | Description |
| :---------------------------| :-----------| :-----------|
| engine_name                 | TEXT        | The last known name of the engine. Either reflects the current name or the name at time of deletion. |
| engine_owner                | TEXT        | The name of the user who owns the engine. |
| cluster_id                  | INT         | Ordinal numbers to identify engine clusters. |
| type                        | TEXT(5)     | The node type used in a given engine (`S`, `M`, `L`, or `XL`). |
| family                      | TEXT        | The family of a given engine. Choose from `STORAGE_OPTIMIZED` or `COMPUTE_OPTIMIZED`. |
| nodes                       | INT         | The number of nodes in each of the cluster of the engine. |
| clusters                    | INT         | The number of clusters used in the engine. |
| auto_start                  | BOOLEAN     | If `TRUE`, automatically start the engine if it is in a stopped state when a query comes in. |
| auto_stop                   | INT         | Automatically stop the engine after specified number of minutes. |
| auto_vacuum                 | BOOLEAN     | Indicates whether [VACUUM]({% link sql_reference/commands/data-management/vacuum.md %}) is enabled or disabled by the user. Could also be `NULL` to indicate that `VACUUM` is automatically enabled by default. |
| initially_stopped           | BOOLEAN     | If `TRUE`, the engine will not be automatically started after creation. |
| url                         | TEXT        | The engine URL used by the users to issue queries to the engine. |
| default_database            | TEXT        | Default database for the engine as specified by the user. |
| version                     | TEXT        | The engine version. |
| event_type                  | TEXT        | The name of the event. |
| event_reason                | TEXT        | The reason that the engine event was triggered. |
| event_status                | TEXT        | The status of the event, indicating whether the action corresponding to the event has succeeded, failed or is in process. Can have one of the following values: `SUCCEEDED`, `FAILED` or `IN_PROGRESS`. |
| event_start_time            | TIMESTAMPTZ | The time when the event was initiated. |
| event_finish_time           | TIMESTAMPTZ | The time when the event was completed. |
| user_name                   | TEXT        | The user who triggered the event. |
| description                 | TEXT        | The description of the engine as specified by the user. |
| query_id                    | TEXT        | The unique identifier for the SQL query used for engine operations. |
