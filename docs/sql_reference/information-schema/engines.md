---
layout: default
title: Engines
parent: Information Schema
grand_parent: SQL reference
---

# Information schema for engines

You can use the `information_schema.engines` view to return information about each engine in an account. The view is available for each database and contains one row for each engine in the account. You can use a `SELECT` query to return information about each engine as shown in the example below, which uses a `WHERE` clause to return all engines attached to databases that begin with `deng`.

```sql
SELECT
  *
FROM
  information_schema.engines
WHERE
  attached_to ILIKE 'deng%'
```

## Columns in information_schema.engines

Each row has the following columns with information about each engine.

| Column Name                 | Data Type   | Description |
| :---------------------------| :-----------| :-----------|
| engine_name                 | TEXT        | The name of the engine. |
| region                      | TEXT        | \[DEPRECATED\] The region in which the engine was created. |
| spec                        | TEXT        | \[DEPRECATED\] The specification of nodes comprising the engine. |
| scale                       | INTEGER     | \[DEPRECATED\] The number of nodes in the engine. |
| type                        | TEXT        | Determines the capability of the nodes in the engine. |
| nodes                       | INTEGER     | The number of nodes in a cluster. |
| clusters                    | INTEGER     | The number of node groupings in an engine. |
| status                      | TEXT        | The engine status. For more information, see [Viewing and understanding engine status](../../Overview/understanding-engine-fundamentals.md#viewing-and-understanding-engine-status). |
| attached_to                 | TEXT        | \[DEPRECATED\] The name of the database to which the engine is attached. |
| auto_start                  | BOOLEAN     | When true, queries issued to a stopped engine will attempt to start the engine first. |
| auto_stop                   | INTEGER     | Indicates the amount of time (in minutes) after which the engine automatically stops. |
| engine_type                 | TEXT        | \[DEPRECATED\] The type of the engine. |
| initially_stopped           | BOOLEAN     | When true, the engine will have attempted to start after creation. |
| url                         | TEXT        | A url which can be used to issue queries to this engine. |
| warmup                      | TEXT        | \[DEPRECATED\] The warmup method of the engine. |
| default_database            | TEXT        | The database an engine will attempt to use by default when dealing with queries that require a database. |
| version                     | TEXT        | The engine version. |
| last_started                | TIMESTAMPTZ | The last time this engine was started (UTC). |
| last_stopped                | TIMESTAMPTZ | The last time this engine was stopped (UTC). |
| description                 | TEXT        | A user defined description for the engine. |
| created                     | TIMESTAMPTZ | The time when this engine was created (UTC). |
| engine_owner                | TEXT        | The name of the user who created the engine. |
| last_altered_by             | TEXT        | The user who last altered this engine. |
| last_altered                | TIMESTAMPTZ | The time when this engine was last altered (UTC). |
| fbu_rate                    | NUMERIC     | Hourly FBU consumption rate of engines based on engine topology at the time the view is invoked by the user. |