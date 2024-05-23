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
    [AUTO_STOP = <minutes>]
    [DEFAULT_DATABASE = <database_name>]
    [INITIALLY_STOPPED = <true/false>]
    [CLUSTERS = <clusters>]
    [NODES = <nodes>]
    [TYPE = <type>]
    [AUTO_START = <true/false>]]
```
## Options
{: .no_toc}  

| Property                             | Description           |
| :----------------------------------- | :-------------------- |
| `<engine_name>`                      | The name of the engine to be created. |
| `AUTO_STOP = <minutes>`              | The amount of idle time (in minutes) after which the engine automatically stops. <br><br>If not specified, `20` is used as default. Setting the minutes to `0` indicates that `AUTO_STOP` is disabled. |
| `DEFAULT_DATABASE = <database_name>` | The database an engine will attempt to use by default when dealing with queries that require a database.<br><br>If not specified, `NULL` is used as default. |
| `INITIALLY_STOPPED = <true/false>`   | When `false`, the newly created engine will be started as part of the `CREATE ENGINE` command.<br><br>If not specified, `false` is used as default. |
| `CLUSTERS = <clusters>`   | Collection of nodes, where each node is of a certain type. All the clusters in an engine have the same type and same number of nodes. If not specified, `1` is used as default. |
| `NODES = <nodes>`                    | The number of nodes for each cluster in an engine. Can be an integer ranging from `1` to `128`. <br><br>If not specified, `1` is used as default. |
| `TYPE = <type>`                       | The type of node used by the engine. Can be one of 'S', 'M', 'L' or 'XL' <br><br>If not specified, `S` is used as default. |
| `AUTO_START = <true/false>`                       | When `true`, If the engine is stopped, it will be automatically started when a query is sent to the engine endpoint.<br><br>If not specified, `true` is used as default. |

**Preview Limitations:**  
* The number of clusters per engine is limited to one. 
* While you can dynamically resize an engine, any currently running queries may not run to completion. 
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

## Example 5
The following example creates an engine with one cluster, using node type 'S' and 4 nodes per cluster. In case it's stopped, the engine will not start automatically upon query, because AUTO_START is set to `false`.

```sql
CREATE ENGINE my_engine
WITH TYPE="S" NODES=4 AUTO_START=false;
```
