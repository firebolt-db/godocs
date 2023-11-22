---
layout: default
title: ATTACH ENGINE
description: Reference and syntax for the ATTACH ENGINE command.
<<<<<<< HEAD:docs/sql_reference/commands/engines/attach-engine.md
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Engine commands
=======
parent:  SQL commands
>>>>>>> rn/gh-pages:docs/sql-reference/commands/attach-engine.md
---

# ATTACH ENGINE

The `ATTACH ENGINE` statement enables you to attach an engine to a database.

## Syntax

```sql
ATTACH ENGINE <engine_name> TO <database_name>
```

## Parameters 
{: .no_toc}   

| Parameter         | Description                                                   |
| :----------------- | :------------------------------------------------------------- |
| `<engine_name>`   | The name of the engine to attach.                             |
| `<database_name>` | The name of the database to attach engine `<engine_name>` to. |

## Example
The following example attaches my_engine to the `players` database: 
```sql
ATTACH ENGINE my_engine TO players
```