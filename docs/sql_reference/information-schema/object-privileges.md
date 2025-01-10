---
layout: default
title: Object privileges
description: Use this reference to learn about the metadata available about privileges using the information schema.
parent: Information schema
grand_parent: SQL reference
---

# Information schema for object_privileges

The `information_schema.object_privileges` view to provides information about permissions granted to each role.  

### View account, role, user, engine, and database permissions

To view account, role, user, engine and database permissions, make sure that current database is **not** selected. Then, query the `information_schema.object_privileges` view as shown in the following examples:

**View privileges directly under an account**

To view all privileges directly under an account, ensure that no database is selected, and query the `information_schema` as follows:

```sql
SELECT
  *
FROM
  information_schema.object_privileges;
```

You can also deselect the current database in the **Firebolt Develop Space** user interface (UI), by choosing `None` in [the current database selector](/assets/images/current_database_dropdown_none_option.png).

**View privileges in a specific database**

To view all privileges under a user defined database `db`, specify the database in the query as follows:

```sql
SELECT
  *
FROM
  db.information_schema.object_privileges;
```

### View object permissions in the current database

When the current database is selected,`information_schema.object_privileges` only shows permissions for objects within that database. It does not show permissions for accounts, roles, users, engines, databases, and objects in other databases.

To view permissions for schemas, tables and views in the current database, set the current database with [USE DATABASE]({% link sql_reference/commands/data-definition/use-database.md %}), then select and view privileges in a query as follows:

```sql
USE DATABASE db;

SELECT
  *
FROM
  information_schema.object_privileges;
```

You can also use the [database selector](/assets/images/current_database_dropdown.png) in the UI.

## Columns in `information_schema.object_privileges`

Each row in `information_schema.object_privileges` contains the following columns:

| Column Name    | Data Type   | Description                                                       |
|:---------------|:------------|:------------------------------------------------------------------|
| grantor        | TEXT        | The name of the user that granted the privilege.                      |
| grantee        | TEXT        | The name of the role that the privilege was granted to.     |
| object_catalog | TEXT        | The database containing the object on which the privilege is granted. |
| object_schema  | TEXT        | The schema containing the object on which the privilege is granted.   |
| object_name    | TEXT        | The name of the object on which the privilege is granted.             |
| object_type    | TEXT        | The type of the object on which the privilege is granted.             |
| privilege_type | TEXT        | The type of the privilege granted on the object.                    |
| is_grantable   | TEXT        | Specify `YES` if the privilege is grantable, and `NO` otherwise.                     |
| created        | TIMESTAMPTZ | The creation time of the privilege.                                   |