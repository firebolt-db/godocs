---
layout: default
title: USE ENGINE
description: Reference and syntax for the USE ENGINE command.
grand_parent:  SQL commands
parent: Engine commands
---

# USE ENGINE

Changes the client to direct queries against the specified engine. 

The client can be updated to direct queries against the system engine by using `system` for the `engine_name`.

Changing the engine used by the client will reset the user's session.

## Syntax

```sql
USE ENGINE <engine_name>
```
## Parameters 
{: .no_toc}   

| Parameter       | Description                           |
| :-------------- | :------------------------------------ |
| `<engine_name>` | The name of the engine to be used. |

## Example 1
The following example changes the client to use my_engine:

```sql
USE ENGINE my_engine
```

## Example 2
The following example changes the client to use system:

```sql
USE ENGINE system
```