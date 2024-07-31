---
layout: default
title: CREATE DATABASE
description: Reference and syntax for the CREATE DATABASE command.
grand_parent:  SQL commands
parent: Data definition
---

# CREATE DATABASE
Creates a new database.

## Syntax
{: .no_toc} 

```sql
CREATE DATABASE [IF NOT EXISTS] <database_name>
[ WITH 
[ DESCRIPTION = <description> ]
]
```

## Parameters 
{: .no_toc} 

| Parameter                                      | Description                     |
| :---------------------------------------------- | :---------------------------- |
| `<database_name>`                              | The name of the database. | 
| `DESCRIPTION = 'description'`                  | The engine's description (up to 64 characters). |

## Example
The following example creates a database with non-default properties: 

```sql
CREATE DATABASE IF NOT EXISTS my_db
WITH DESCRIPTION = 'Being used for testing'
```
