---
layout: default
title: START ENGINE
description: Reference and syntax for the START ENGINE command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Engine commands
---

# START ENGINE

The `START ENGINE` statement enables you to start a stopped engine.

## Syntax

```sql
START ENGINE <engine>
```
## Parameters 
{: .no_toc}   

| Parameter       | Description                          | Mandatory? Y/N |
| :--------------- | :------------------------------------ | :-------------- |
| `<engine>` | The name of the engine to be started | Y              |

## Example
The following example starts the `players` engine: 

```sql
START ENGINE <players>
```