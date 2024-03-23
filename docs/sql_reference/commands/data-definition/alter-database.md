---
layout: default
title: ALTER DATABASE
description: Reference and syntax for the ALTER DATABASE command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Data definition
---

# ALTER DATABASE

Updates the configuration of the specified database.

## Syntax

```sql
ALTER DATABASE <database_name> WITH
    [DESCRIPTION = <description>]
```

## Parameters 
{: .no_toc} 

| Parameter | Description |
| :--- | :--- |
| `<database_name>`                  | The name of the database to be altered. |
| `<description>`      | The description of the database. |

## Example
The following example alters a description of the database: 

```sql
ALTER DATABASE my_database WITH DESCRIPTION = 'Database for query management';
```
