---
layout: default
title: ALTER DATABASE
description: Reference and syntax for the ALTER DATABASE command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Database object commands
---

# ALTER DATABASE

Updates the configuration of the specified database `<database>`.

## Syntax

```sql
ALTER DATABASE <database_name> WITH
    [ATTACHED_ENGINES = ( '<expression1>' [, ... ] )]
    [DEFAULT_ENGINE = 'expression2']
    [DESCRIPTION = 'expression3']
```

## Parameters 
{: .no_toc} 

| Parameter | Description |
| :--- | :--- |
| `<database>`                  | Name of the  database to be altered. |
| `ATTACHED_ENGINES = <expression1>` | Name(s) of  Firebolt engine(s) attached to the database. |
| `DEFAULT_ENGINE = <expression2>`   | Name of the default engine. |
| `DESCRIPTION = <expression3>`      | Description of the database. |

## Example
The following example alters a current database with a new default engine, `my_new_default_engine`: 

```sql
ALTER DATABASE my_database WITH DEFAULT_ENGINE = 'my_new_default_engine';
```
