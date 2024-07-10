---
layout: default
title: ALTER ENGINE
description: Reference and syntax for the ALTER ENGINE command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Engine commands
---

# ALTER ENGINE

## ALTER ENGINE SET

Updates the configuration of the specified engine.

### Syntax

```sql
ALTER ENGINE <engine_name> SET
    [AUTO_STOP = <minutes>]
    [DEFAULT_DATABASE = <database_name>]
    [CLUSTERS = <clusters>]
    [NODES = <nodes>]
    [TYPE = <type>]
    [RENAME TO <new_name>]
```
### Options 
{: .no_toc}  

| Parameter                            | Description                                  |
| :----------------------------------- | :------------------------------------------- |
| `<engine_name>`                      | The name of the engine to be altered.        |
| `AUTO_STOP = <minutes>`              | Indicates the amount of time (in minutes) after which the engine automatically stops. Setting the `minutes` to 0 indicates that `AUTO_STOP` is disabled. |
| `DEFAULT_DATABASE = <database_name>` | The database an engine will attempt to use by default when dealing with queries that require a database. To remove the default database, set `DEFAULT_DATABASE=default`. |
| `TYPE =<type>`                       | The type of node used by the engine. Can be one of 'S', 'M', 'L' or 'XL'. If not specified, `S` is used as default. |
| `NODES = <nodes>`                    | The number of nodes for each cluster in an engine. Can be an integer ranging from `1` to `128`. If not specified, `1` is used as default. |
| `CLUSTERS = <clusters>`              | Collection of nodes, where each node is of a certain type. All the clusters in an engine have the same type and same number of nodes. If not specified, `1` is used as default. |
| `RENAME TO <new_name>`               | Indicates the new name for the engine. No other parameters are allowed during an engine rename. |

**Preview Limitations:**  The number of clusters per engine is limited to one.  Modifying the TYPE or NODES attribute of a running engine may result in the failure of currently executing queries. If you would like to remove any of these limitations, reach out to Firebolt Support.

### Example 1
The following example allows the users to scale out an engine by setting the engine's `NODES` to `3`: 

```sql
ALTER ENGINE my_engine SET NODES = 3;
```

### Example 2
The following example allows the users to scale up an engine from Small to Large by setting the engine's `TYPE` to `L`: 

```sql
ALTER ENGINE my_engine SET TYPE = "L";
```

### Example 3
The following example allows the users to both scale up and scale out an engine by changing the number of nodes and the node type: 

```sql
ALTER ENGINE my_engine SET TYPE = "L" NODES = 5;
```

## ALTER ENGINE OWNER TO

Change the owner of an engine. The current owner of an engine can be viewed in the `information_schema.engines` view on `engine_owner` column.

check [ownership](../../../Guides/security/ownership.md) page for more info.

### Syntax

```sql
ALTER ENGINE <engine_name> OWNER TO <user>
```

### Parameters 
{: .no_toc}

| Parameter     | Description                                  |
| :------------ | :------------------------------------------- |
| `<engine_name>` | The name of the engine to change the owner of. |
| `<user>`       | The new owner of the engine.                 |