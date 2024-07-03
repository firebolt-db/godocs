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
| type                        | TEXT(5)     | Node type used in a given engine (S, M, L or XL). |
| nodes                       | INT         | Number of nodes in each of the cluster of the engine. |
| clusters                    | INT         | The number of clusters used in the engine. |
| auto_start                  | BOOLEAN     | If True, automatically start the engine if in stopped state when a query comes in. |
| auto_stop                   | INT         | Automatically stop the engine after specified number of minutes. |
| initially_stopped           | BOOLEAN     | If True, Engine will not be automatically started after creation. |
| url                         | TEXT        | Engine URL used by the users to issue queries to the engine. |
| default_database            | TEXT        | Default database for the engine as specified by the user. |
| version                     | TEXT        | Engine version. |
| event_type                  | TEXT        | Name of the event. |
| event_reason                | TEXT        | Reason why the engine event was triggered. |
| event_status                | TEXT        | Status of the event, indicating whether the action corresponding to the event has succeeded, failed or is in process. Can have one of the following values: SUCCEEDED, FAILED or IN_PROGRESS. |
| event_start_time            | TIMESTAMPTZ | Time when the event was initiated. |
| event_finish_time           | TIMESTAMPTZ | Time when the event was completed. |
| user_name                   | TEXT        | User who triggered the event. |
| description                 | TEXT        | Description of the engine as specified by the user. |
| query_id                    | TEXT        | Unique identifier for the SQL query used for engine operations. |
