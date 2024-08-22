---
layout: default
title: ALTER DATABASE
description: Reference and syntax for the ALTER DATABASE command.
parent: Data definition
---

# ALTER DATABASE

Updates the configuration of the specified database.

## ALTER DATABASE DESCRIPTION

### Syntax

```sql
ALTER DATABASE <database_name> WITH
    [DESCRIPTION = <description>]
```

### Parameters 
{: .no_toc} 

| Parameter | Description |
| :--- | :--- |
| `<database_name>`                  | The name of the database to be altered. |
| `<description>`      | The description of the database. |

### Example
The following example alters a description of the database: 

```sql
ALTER DATABASE my_database WITH DESCRIPTION = 'Database for query management';
```

## ALTER DATABASE OWNER TO

Change the owner of a database. The current owner of a database can be viewed in the [information_schema.catalogs](../../information-schema/catalogs.md) view on `catalog_owner` column.

check [ownership](../../../Guides/security/ownership.md) page for more info.

### Syntax

```sql
ALTER DATABASE <database_name> OWNER TO <user>
```

### Parameters 
{: .no_toc}

| Parameter | Description |
| :--- | :--- |
| `<database_name>` | The name of the database to change the owner of. |
| `<user>` | The new owner of the database. |