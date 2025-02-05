---
layout: default
title: Table permissions
description: Learn about the permissions that can be assigned to tables in Firebolt, including controlling access to table data and managing table-level operations.
parent: Database permissions
grand_parent: Role-Based Access Control
nav_order: 3
---

# Table permissions

In Firebolt, a **table** is a structured data object within a database, composed of rows and columns. Tables are the foundational units for organizing, querying, and managing data in your Firebolt data warehouse. Table-level permissions allow roles to perform actions such as selecting, modifying, or managing data within specific tables.

{: .note}
To perform actions on a table, roles must also have **USAGE** permissions on both the parent schema and the parent database of the table.

## Table-level privileges 

| Privilege             | Description                                                                 | GRANT Syntax                                                     | REVOKE Syntax                                                   |
|---------------------------|---------------------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|
| SELECT     | Allows selecting rows from the table.                                       | `GRANT SELECT ON TABLE <table_name> TO <role_name>;`                                      | `REVOKE SELECT ON TABLE <table_name> FROM <role_name>;`                                    |
| [INSERT]({% link sql_reference/commands/data-management/insert.md %})     | Allows inserting rows into the table. Applies to managed tables only.     | `GRANT INSERT ON TABLE <table_name> TO <role_name>;`                                      | `REVOKE INSERT ON TABLE <table_name> FROM <role_name>;`                                   |
| MODIFY     | Allows modifying and dropping the table.                                   | `GRANT MODIFY ON TABLE <table_name> TO <role_name>;`                                      | `REVOKE MODIFY ON TABLE <table_name> FROM <role_name>;`                                   |
| [DELETE]({% link sql_reference/commands/data-management/delete.md %})     | Allows deleting rows and dropping partitions from the table. Applies to managed tables only. | `GRANT DELETE ON TABLE “<table_name>” TO <role_name>;`                             | `REVOKE DELETE ON TABLE “<table_name>” FROM <role_name>;`                           |
| [UPDATE]({% link sql_reference/commands/data-management/update.md %})     | Allows updating rows in the table. Applies to managed tables only.       | `GRANT UPDATE ON TABLE <table_name> TO <role_name>;`                                      | `REVOKE UPDATE ON TABLE <table_name> FROM <role_name>;`                                   |
| [TRUNCATE]({% link sql_reference/commands/data-management/truncate-table.md %})   | Allows truncating a table. Applies to managed tables only.             | `GRANT TRUNCATE ON TABLE <table_name> TO <role_name>;`                                    | `REVOKE TRUNCATE ON TABLE <table_name> FROM <role_name>;`                               |
| [VACUUM]({% link sql_reference/commands/data-management/vacuum.md %})     | Allows running the `VACUUM` operation. Applies to managed tables only.              | `GRANT VACUUM ON TABLE <table_name> TO <role_name>;`                                      | `REVOKE VACUUM ON TABLE <table_name> FROM <role_name>;`                                   |
| ALL [PRIVILEGES]     | Grants all privileges over the table to a role.	              | `GRANT ALL ON TABLE <table_name> TO <role_name>;`                                      | `REVOKE ALL ON TABLE <table_name> FROM <role_name>;`                                   |

{: .note}
To grant permissions across all tables in a schema, use [schema-level privileges](schema-permissions.md). For example, privileges like **SELECT ANY**, **INSERT ANY**, or **DELETE ANY** at the schema level will apply to all current and future tables within that schema.

## Aggregating Indexes

An [aggregating index]({% link Overview/indexes/aggregating-index.md %}) in Firebolt accelerates queries involving aggregate functions on large tables. This reduces compute usage and improves query performance.

To **create** or **drop** an aggregating index, a role must have the following permissions:

* `MODIFY` permission on the table.
* `CREATE` permission on the parent schema.
* `USAGE` permission on the parent schema.
* `USAGE` permission on the parent database.

To drop an aggregating index, the role requires:

* `MODIFY` permission on the table.
* `USAGE` permission on the parent schema.
* `USAGE` permission on the parent database.

## Examples of modifying table permissions

The following example use [`GRANT`]({% link sql_reference/commands/access-control/grant.md %}) to grant permissions. You can also replace `GRANT` with [REVOKE]({% link sql_reference/commands/access-control/revoke.md %}) in any of the examples to remove any granted privileges.

### SELECT permission
The following code example [grants]({% link sql_reference/commands/access-control/grant.md %}) the role `developer_role` permission to read data from the `games` table:

```sql
GRANT SELECT ON TABLE games TO developer_role;
```

### INSERT permission 
The following code example gives the role `developer_role` permissions to [insert]({% link sql_reference/commands/data-management/insert.md %})  rows into the `games` table:

```sql
GRANT INSERT ON TABLE games TO developer_role;
```

### MODIFY permission
The following code example grants the role `developer_role` permission to alter or drop the `games` table:

```sql
GRANT MODIFY ON TABLE games TO developer_role;
```

### DELETE permission
The following code example gives the role `developer_role` permission to [delete]({% link sql_reference/commands/data-management/delete.md %}) rows or partitions from the `games` table:

```sql
GRANT DELETE ON TABLE games TO developer_role;
```

### UPDATE permission
The following code example grants the role `developer_role` permission to [update]({% link sql_reference/commands/data-management/update.md %}) rows in the `games` table:

```sql
GRANT UPDATE ON TABLE games TO developer_role;
```

### TRUNCATE permission  
The following code example gives the role `developer_role` permission to [truncate]({% link sql_reference/commands/data-management/truncate-table.md %}) the `games` table, removing all rows:

```sql
GRANT TRUNCATE ON TABLE games TO developer_role;
```

### VACUUM permission  
The following code example grants the role `developer_role` permission to run the [`VACUUM`]({% link sql_reference/commands/data-management/vacuum.md %}) operation on the `games` table:

```sql
GRANT VACUUM ON TABLE games TO developer_role;
```

### ALL permissions
The following code example grants the role `developer_role` with all permissions on the table `games`:

```sql
GRANT ALL ON TABLE games TO developer_role;
```
## Considerations

* Use the [REVOKE]({% link sql_reference/commands/access-control/revoke.md %}) statement to remove any granted privileges. Replace [`GRANT`]({% link sql_reference/commands/access-control/grant.md %}) with [`REVOKE`]({% link sql_reference/commands/access-control/revoke.md %}) in the examples above.
* Table-level permissions apply only to the specified table. For broader control, consider granting schema-level privileges.
