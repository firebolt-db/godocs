---
layout: default
title: Schema permissions
description: Learn about the permissions that can be assigned to schemas in Firebolt, including the ability to manage schema-level objects and control access to underlying data.
parent: Database permissions
grand_parent: Role-Based Access Control
nav_order: 2
---

# Schema permissions

In Firebolt, a **schema** is a logical namespace within a database that organizes **tables**, **views**, and other objects. Schema-level permissions allow roles to perform specific actions, such as accessing, modifying, or managing objects within a schema.

{: .note}
To perform actions on a schema or its objects, the role must also have the **USAGE** privilege on the schema's parent database.

## Schema-level privileges 

| Privilege | Description                                                              | GRANT Syntax                                                                  | REVOKE Syntax                                                                 |
|---|---|---|---|
| USAGE      | Allows access to the schema and its objects                                                   | `GRANT USAGE ON SCHEMA public IN <database_name> TO <role_name>;`                     | `REVOKE USAGE ON SCHEMA public IN <database_name> FROM <role_name>;`                |
| MODIFY     | Allows altering the schema properties, including renaming or dropping the schema them.                                                 | `GRANT MODIFY ON SCHEMA public IN <database_name> TO <role_name>;`                    | `REVOKE MODIFY ON SCHEMA public IN <database_name> FROM <role_name>;`               |
| CREATE     | Allows creating new objects, such as tables and views, within the schema.                                        | `GRANT CREATE ON SCHEMA public IN <database_name> TO <role_name>;`                   | `REVOKE CREATE ON SCHEMA public IN <database_name> FROM <role_name>;`              |
| [DELETE]({% link sql_reference/commands/data-management/delete.md %}) ANY | Allows deleting rows and partitions from all current and future tables.               | `GRANT DELETE ANY ON SCHEMA public IN <database_name> TO <role_name>;`              | `REVOKE DELETE ANY ON SCHEMA public IN <database_name> FROM <role_name>;`         |
| [INSERT]({% link sql_reference/commands/data-management/insert.md %}) ANY | Allows inserting rows into all current and future tables within the schema.                | `GRANT INSERT ANY ON SCHEMA public IN <database_name> TO <role_name>;`              | `REVOKE INSERT ANY ON SCHEMA public IN <database_name> FROM <role_name>;`         |
| [UPDATE]({% link sql_reference/commands/data-management/update.md %}) ANY | Allows updating rows in all current and future tables within the schema.                | `GRANT UPDATE ANY ON SCHEMA public IN <database_name> TO <role_name>;`              | `REVOKE UPDATE ANY ON SCHEMA public IN <database_name> FROM <role_name>;`         |
| [TRUNCATE]({% link sql_reference/commands/data-management/truncate-table.md %}) ANY | Allows truncating all current and future tables within the schema.              | `GRANT TRUNCATE ANY ON SCHEMA public IN <database_name> TO <role_name>;`            | `REVOKE TRUNCATE ANY ON SCHEMA public IN <database_name> FROM <role_name>;`       |
| [VACUUM]({% link sql_reference/commands/data-management/vacuum.md %}) ANY | Allows running the `VACUUM` operation on all current and future tables.                | `GRANT VACUUM ANY ON SCHEMA public IN <database_name> TO <role_name>;`            | `REVOKE VACUUM ANY ON SCHEMA public IN <database_name> FROM <role_name>;`       |
| MODIFY ANY | Allows modifying or dropping all current and future objects in the schema.        | `GRANT MODIFY ANY ON SCHEMA public IN <database_name> TO <role_name>;`            | `REVOKE MODIFY ANY ON SCHEMA public IN <database_name> FROM <role_name>;`       |
| SELECT ANY | Allows reading data from all current and future objects within the schema.                | `GRANT SELECT ANY ON SCHEMA public IN <database_name> TO <role_name>;`             | `REVOKE SELECT ANY ON SCHEMA public IN <database_name> FROM <role_name>;`        |
| ALL [PRIVILEGES] | Grants all direct privileges over the schema to a role.	                | `GRANT ALL ON SCHEMA public IN <database_name> TO <role_name>;`             | `REVOKE ALL ON SCHEMA public IN <database_name> FROM <role_name>;`        |

## Examples of granting schema permissions

### USAGE permission 
The following code example [grants]({% link sql_reference/commands/access-control/grant.md %}) the role `developer_role` permission to use the specified schema.

```sql
GRANT USAGE ON SCHEMA "public" TO developer_role;
```

### MODIFY permission  
The following code example gives the role `developer_role` permission to alter properties or drop the specified schema.

```sql
GRANT MODIFY ON SCHEMA "public" TO developer_role;
```

### CREATE permission  
The following code example grants the role `developer_role` the ability to create new objects in the specified schema:

```sql
GRANT CREATE ON SCHEMA "public" TO developer_role;
```

### DELETE ANY permission
The following code example gives the role `developer_role` permission to [delete]({% link sql_reference/commands/data-management/delete.md %}) rows and partitions from all current and future tables in the specified schema:

```sql
GRANT DELETE ANY ON SCHEMA "public" TO developer_role;
```

### INSERT ANY permission 
The following code example grants the role `developer_role` permission to [insert]({% link sql_reference/commands/data-management/insert.md %}) rows into all current and future tables in the specified schema:

```sql
GRANT INSERT ANY ON SCHEMA "public" TO developer_role;
```

### UPDATE ANY permission
The following code example gives the role `developer_role` permission to [update]({% link sql_reference/commands/data-management/update.md %}) rows in all current and future tables in the specified schema:

```sql
GRANT UPDATE ANY ON SCHEMA "public" TO developer_role;
```

### TRUNCATE ANY permission
The following code example grants the role `developer_role` the ability to [truncate]({% link sql_reference/commands/data-management/truncate-table.md %}) all current and future tables in the specified schema:

```sql
GRANT TRUNCATE ANY ON SCHEMA "public" TO developer_role;
```

### VACUUM ANY permission
The following code example gives the role `developer_role` permission to run [`VACUUM`]({% link sql_reference/commands/data-management/vacuum.md %}) operations on all current and future tables in the specified schema:

```sql
GRANT VACUUM ANY ON SCHEMA "public" TO developer_role;
```

### MODIFY ANY permission
The following code example grants the role `developer_role` permission to modify or drop all current and future objects in the specified schema:

```sql
GRANT MODIFY ANY ON SCHEMA "public" TO developer_role;
```

### SELECT ANY permission  
The following code example gives the role `developer_role` permission to select data from all current and future objects in the specified schema:

```sql
GRANT SELECT ANY ON SCHEMA "public" TO developer_role;
```

### ALL permissions  
The following code example gives the role `developer_role` all the direct permissions over schema `public`:

```sql
GRANT ALL ON SCHEMA "public" TO developer_role;
```