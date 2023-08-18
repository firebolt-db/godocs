---
layout: default
title: DROP ENGINE
description: Reference and syntax for the DROP ENGINE command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Engine commands
---

# DROP ENGINE
Deletes an engine.

## Syntax

```sql
DROP ENGINE [IF EXISTS] <engine>
```
## Parameters 
{: .no_toc}   

| Parameter       | Description                           |
| :--------------- | :------------------------------------- |
| `<engine>` | The name of the engine to be deleted. |

## Example
The following example drops the `players` engine: 

```sql
DROP ENGINE [IF EXISTS] <players>
```