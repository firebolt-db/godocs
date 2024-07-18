---
layout: default
title: STOP ENGINE
description: Reference and syntax for the STOP ENGINE command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Engine commands
---

# STOP ENGINE

Stops a running engine.

## Syntax

```sql
STOP ENGINE [IF EXISTS] <engine_name>
[WITH 
    [TERMINATE = <true/false>]]
```
## Parameters 
{: .no_toc}   

| Parameter        | Description                           |
| :--------------- | :------------------------------------ |
| `<engine_name>`  | The name of the engine to be stopped. |
| `<TERMINATE>`    | When `false`, the engine will wait for running queries to finish before stopping.<br>When `true`, the engine will stop without waiting for running queries to complete.<br><br>If not specified, `false` is used as default. |

**Limitations:**
* When `TERMINATE=false` (default), the engine will wait for up to 24 hours for running queries to finish before stopping. After 24 hours, the engine will finish shutting down. Any queries still running may not run to completion.

If you would like to remove any of these limitations, reach out to Firebolt Support.

## Example 1
The following example waits for queries on my_engine to finish before stopping:

```sql
STOP ENGINE my_engine
```

## Example 2
The following example stops my_engine without waiting for running queries to finish:

```sql
STOP ENGINE my_engine WITH TERMINATE=true
```