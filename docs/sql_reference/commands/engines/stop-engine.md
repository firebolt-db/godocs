---
layout: default
title: STOP ENGINE
description: Reference and syntax for the STOP ENGINE command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Engine commands
---

# STOP ENGINE

The `STOP ENGINE` statement enables you to stop a running engine.

## Syntax

```sql
STOP ENGINE <engine>
```
## Parameters 
{: .no_toc}   

| Parameter       | Description                          | Mandatory? Y/N |
| :--------------- | :------------------------------------ | :-------------- |
| `<engine>` | The name of the engine to be stopped | Y              |

## Example
The following example stops the `players` engine: 

```sql
STOP ENGINE <players>
```