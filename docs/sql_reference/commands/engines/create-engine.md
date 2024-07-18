---
layout: default
title: CREATE ENGINE
description: Reference and syntax for the CREATE ENGINE command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Engine commands
---

# CREATE ENGINE
Creates an engine (compute cluster).

## Syntax

```sql
CREATE ENGINE [IF NOT EXISTS] <engine_name>
[WITH 
    [AUTO_START = <true/false>]
    [AUTO_STOP = <minutes>]
    [DEFAULT_DATABASE = <database_name>]
    [INITIALLY_STOPPED = <true/false>]
    [START_IMMEDIATELY = <true/false>]
    [CLUSTERS = <clusters>]
    [NODES = <nodes>]
    [TYPE = <type>]]
```
## Options
{: .no_toc}  

| Parameter                            | Description           |
| :----------------------------------- | :-------------------- |
| `<engine_name>`                      | The name of the engine to be created. |
| `AUTO_START = <true/false>`          | When `true`, sending a query to a stopped engine will start the engine before processing the query.<br><br>If not specified, `true` will be used as default. |
| `AUTO_STOP = <minutes>`              | The amount of idle time (in minutes) after which the engine automatically stops.<br>Setting the minutes to `0` indicates that `AUTO_STOP` is disabled.<br><br>If not specified, `20` is used as default. |
| `DEFAULT_DATABASE = <database_name>` | The database an engine will attempt to use by default when dealing with queries that require a database.<br><br>If not specified, `NULL` is used as default. |
| `INITIALLY_STOPPED = <true/false>`   | When `false`, the newly created engine will be started as part of the `CREATE ENGINE` command.<br>Cannot be used with `START_IMMEDIATELY`.<br><br>If not specified, `false` is used as default. |
| `START_IMMEDIATELY = <true/false>`   | When `true`, the newly created engine will be started as part of the `CREATE ENGINE` command.<br>Cannot be used with `INITIALLY_STOPPED`.<br><br>If not specified, `true` is used as default. |
| `CLUSTERS = <clusters>`              | Collection of nodes, where each node is of a certain type. All the clusters in an engine have the same type and same number of nodes. If not specified, `1` is used as default. |
| `NODES = <nodes>`                    | The number of nodes for each cluster in an engine. Can be an integer ranging from `1` to `128`. <br><br>If not specified, `1` is used as default. |
| `TYPE =<type>`                       | The type of node used by the engine. Can be one of 'S', 'M', 'L' or 'XL' <br><br>If not specified, `S` is used as default. |

**Limitations:**  
* The number of clusters per engine is limited to two. 
* The number of nodes per cluster is limited to ten.

If you would like to remove the above limitations, reach out to Firebolt Support.

## Example 1
The following example creates an engine with one cluster, using node type 'S' and 5 nodes per cluster : 

```sql
CREATE ENGINE my_engine
WITH TYPE="S" NODES = 5 CLUSTERS = 1;
```
## Example 2
The following example creates an engine with one cluster, using node type 'S' and 1 nodes per cluster : 

```sql
CREATE ENGINE my_engine;
```
## Example 3
The following example creates an engine with one cluster, using node type 'M' and 3 nodes per cluster. The engine will not be automatically started after creation because INITIALLY_STOPPED is set to true.

```sql
CREATE ENGINE my_engine
WITH TYPE="M" NODES=3 INITIALLY_STOPPED=true;
```
## Example 4
The following example creates an engine with one cluster, using node type 'L' and 2 nodes per cluster. The engine will be automatically stopped after 10 mins of idle time because AUTO_STOP is set to 10.

```sql
CREATE ENGINE my_engine
WITH TYPE="L" NODES=2 AUTO_STOP=10;
```