---
redirect_from:
  - /sql-reference/commands/create-database.html
layout: default
title: CREATE DATABASE
description: Reference and syntax for the CREATE DATABASE command.
parent: Data definition
---

# CREATE DATABASE
Creates a new database.

{: .note}
Each account supports up to 100 databases. If you need more, contact Firebolt's support team at [support@firebolt.io](mailto:support@firebolt.io).

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
| `DESCRIPTION = 'description'`                  | (Optional) The database's description, which can contain up to 64 characters. |

## Example
The following code example creates a database named `my_db` with an optional description, `Testing database`: 

```sql
CREATE DATABASE IF NOT EXISTS my_db
WITH DESCRIPTION = 'Testing database'
```
