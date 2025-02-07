---
layout: default
title: Database permissions
description: Understand the permissions that can be assigned at the database level in Firebolt, including controlling access to database objects and managing database-level operations.
parent: Role-Based Access Control
nav_order: 2
has_children: true
has_toc: true
---

# Database permissions

In Firebolt, a **database** is a logical container that organizes your data warehouse by holding components such as **tables**, **views**, **indexes**, and other database objects, as shown in the following diagram:

<img src="../../../../assets/images/database-hierarchy.png" width="700" alt="Firebolt's object model contains schema under databases, and tables, views, and indexes under schema.">

Database-level permissions define what actions roles can perform within a database and its associated objects.

## Database-level privileges 

| Privilege             | Description                                                                 | GRANT Syntax                                                     | REVOKE Syntax                                                   |
|---------------------------|---------------------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|
| USAGE                  | Allows access to the database and enables attaching engines to it.                          | `GRANT USAGE ON DATABASE <database_name> TO <role>;`                       | `REVOKE USAGE ON DATABASE <database_name> FROM <role>;`                    |
| MODIFY                 | Allows altering database properties and dropping the database.                  | `GRANT MODIFY ON DATABASE <database_name> TO <role>;`                       | `REVOKE MODIFY ON DATABASE <database_name> FROM <role>;`                    |
| USAGE ANY SCHEMA       | Allows access to all current and future schemas within the database.                   | `GRANT USAGE ANY SCHEMA ON DATABASE <database_name> TO <role>;`           | `REVOKE USAGE ANY SCHEMA ON DATABASE <database_name> FROM <role>;`     |
| [VACUUM]({% link sql_reference/commands/data-management/vacuum.md %}) ANY             | Allows running the `VACUUM` operation on all current and future tables.              | `GRANT VACUUM ANY ON DATABASE <database_name> TO <role>;`              | `REVOKE VACUUM ANY ON DATABASE <database_name> FROM <role>;`           |
| ALL [PRIVILEGES]             | Grants all direct privileges over the database to a role.              | `GRANT ALL ON DATABASE <database_name> TO <role>;`              | `REVOKE ALL ON DATABASE <database_name> FROM <role>;`           |

## Examples of granting database permissions

### USAGE permission
The following code example [grants]({% link sql_reference/commands/access-control/grant.md %}) the role `developer_role` access to use the specified database:

```sql
GRANT USAGE ON DATABASE "database-1" TO developer_role;
```

### MODIFY permission
The following code example gives the role `developer_role` permission to alter properties or drop the specified database:

```sql
GRANT MODIFY ON DATABASE "database-1" TO developer_role;
```

### USAGE ANY SCHEMA permission
The following code example grants the role `developer_role` access to all current and future schemas within the specified database:

```sql
GRANT USAGE ANY SCHEMA ON DATABASE "database-1" TO developer_role;
```

### VACUUM ANY permission
The following code example gives the role `developer_role` permission to run [VACUUM]({% link sql_reference/commands/data-management/vacuum.md %}) operations on all current and future tables in the specified database:

```sql
GRANT VACUUM ANY ON DATABASE "database-1" TO developer_role;
```

### ALL permissions
The following code example gives the role `developer_role` all the direct permissions over database `database-1`:

```sql
GRANT ALL ON DATABASE "database-1" TO developer_role;
```
{:toc}

