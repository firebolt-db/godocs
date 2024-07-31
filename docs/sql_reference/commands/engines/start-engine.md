---
layout: default
title: START ENGINE
description: Reference and syntax for the START ENGINE command.
grand_parent:  SQL commands
parent: Engine commands
---

# START ENGINE

Starts a stopped engine.

## Syntax

```sql
START ENGINE <engine_name>
```
## Parameters 
{: .no_toc}   

| Parameter       | Description                          |
| :--------------- | :------------------------------------ |
| `<engine_name>` | The name of the engine to be started. |

## Example
The following example starts my_engine:

```sql
START ENGINE my_engine
```