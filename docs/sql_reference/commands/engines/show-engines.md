---
layout: default
title: SHOW ENGINES
description: Reference and syntax for the SHOW ENGINES command.
parent: Engine commands
grand_parent: SQL commands
great_grand_parent: SQL reference
---

# SHOW ENGINES

Returns a table with a row for each Firebolt engine defined in the current Firebolt account, with columns containing information about each engine as listed below.

## Syntax

```sql
SHOW ENGINES;
```

## Returns

The returned table has the following columns.

| Column name                 | Data Type   | Description |
| :---------------------------| :-----------| :-----------|
| engine_name                 | TEXT      | The name of the engine. |
| engine_owner                | TEXT (5)  | Name of the user who created the engine. |
| type                        | TEXT      | The specification of nodes comprising the engine. |
| clusters                    | INT       | Collection of nodes, where each node is of a certain type. All the clusters in an engine have the same type and same number of nodes. |
| nodes                       | INT       | The number of nodes for each cluster in an engine. Can be an integer ranging from `1` to `128`. |
| status                      | TEXT      | The engine status. For more information, see [Viewing and understanding engine status](../../../Overview/understanding-engine-fundamentals.md#viewing-and-understanding-engine-status) |
| auto_stop                   | INT       | The amount of idle time (in minutes) after which the engine automatically stops. |
| url                         | TEXT      | Engine endpoint. |
| version                     | TEXT      | The engine version. |
| initially_stopped           | BOOLEAN   | If `false`, engine was started as part of the `CREATE ENGINE` command.|
| default_database | The database an engine will attempt to use by default when dealing with queries that require a database.<br><br>If not specified, `NULL` is used as default. |
| created                     | TIMESTAMPTZ | Creation time of the engine. |
| last_altered_by             | TEXT       | Name of the last user who edited the engine. |
| last_altered                | TIMESTAMPTZ | Last modified time of the engine. |
| fbu_rate                    | INT        | Hourly FBU consumption rate of running engines based on engine topology at the time the view is invoked by the user. |

