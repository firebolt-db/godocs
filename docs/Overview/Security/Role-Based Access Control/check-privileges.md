---
layout: default
title: Check Assigned Privileges
description: Learn how to view and verify assigned privileges for users and roles in Firebolt.
parent: Role-Based Access Control
nav_order: 8
---

# Check assigned privileges

The Firebolt information schema provides system views that allow you to view metadata and permissions for objects within your current account or database. This page explains how to query and validate user and role privileges at both the **account** and **database** levels.

## Viewing effective privileges
The following code example shows how to view the effective privileges of the current user:

```sql
SELECT
  AR.grantee,
  AR.role_name,
  OP.privilege_type,
  OP.object_type,
  OP.object_name
FROM information_schema.transitive_applicable_roles AS AR
JOIN information_schema.object_privileges AS OP
ON (AR.role_name = OP.grantee)
WHERE
  AR.grantee = session_user();
```

## Usage examples

The following examples demonstrate how to validate privileges at both the **account** level and the **database** level. By running a query against the `information_schema` views, you can check the effective permissions granted to a user or role. Each scenario includes an example query and output to illustrate the scope of the retrieved privileges.


### Validating privileges at the account level
If no database is selected, the query runs at the account level and shows account-scoped privileges.

**Example**
       
In the following code example, a user `test_user` with an [account_admin]({% link Overview/organizations-accounts.md %}#account-administrative-role) role retrieves their privileges and associated roles for their current user session:

```sql
SELECT
  AR.grantee,
  AR.role_name,
  OP.privilege_type,
  OP.object_type,
  OP.object_name
FROM information_schema.transitive_applicable_roles AS AR
JOIN information_schema.object_privileges AS OP
ON (AR.role_name = OP.grantee)
WHERE
  AR.grantee = session_user();
```

**Returns**  

| Grantee | role_name | privilege_type | object_type | object_name |
|---|---|---|---|---|
| test_user | account_admin | `MODIFY ANY ENGINE` | account | account-1 |
| test_user | account_admin | `MODIFY ANY DATABASE` | account | account-1 |
| test_user | account_admin | `OPERATE ANY ENGINE` | account | account-1 |
| test_user | account_admin | `MODIFY ANY ROLE` | account | account-1 |
| test_user | account_admin | `USAGE ANY DATABASE` | account | account-1 |
| test_user | account_admin | `MONITOR ANY USAGE` | account | account-1 |
| test_user | account_admin | `MANAGE GRANTS` | account | account-1 |
| test_user | account_admin | `USAGE ANY ENGINE` | account | account-1 |
| test_user | account_admin | `MODIFY ANY USER` | account | account-1 |
| test_user | account_admin | `METER USAGE` | account | account-1 |
| test_user | account_admin | `CREATE SCHEMA` | database | UltraFast |
| test_user | account_admin | `CREATE USER` | account | account-1 |
| test_user | account_admin | `CREATE DATABASE` | account | account-1 |
| test_user | account_admin | `CREATE ROLE` | account | account-1 |
| test_user | account_admin | `CREATE ENGINE` | account | account-1 |

The previous table confirms that `test_user` has account-level privileges, such as permission to create engines, roles, and databases, as well as permission to modify users and engines.

### Validating privileges at the database level
When a specific database is selected, the query retrieves privileges scoped to that database.

**Example**
     
The following code example retrieves the applicable roles and associated privileges, object types, and object names for `test_user`, who holds an `account_admin` role from the information schema.

```sql
SELECT
  AR.grantee,
  AR.role_name,
  OP.privilege_type,
  OP.object_type,
  OP.object_name
FROM information_schema.transitive_applicable_roles AS AR
JOIN information_schema.object_privileges AS OP
ON (AR.role_name = OP.grantee)
WHERE
  AR.grantee = session_user();
```

**Returns** 

| Grantee | role_name | privilege_type | object_type | object_name |
|---|---|---|---|---|
| test_user | account_admin | `SELECT ANY` | schema | public |
| test_user | account_admin | `DELETE ANY` | schema | public |
| test_user | account_admin | `VACUUM ANY` | schema | public |
| test_user | account_admin | `INSERT ANY` | schema | public |
| test_user | account_admin | `MODIFY` | schema | public |
| test_user | account_admin | `CREATE` | schema | public |
| test_user | account_admin | `USAGE` | schema | public |
| test_user | account_admin | `MODIFY ANY` | schema | public |
| test_user | account_admin | `TRUNCATE ANY` | schema | public |

The previous output confirms that `test_user` has database-level privileges, such as `SELECT`, `INSERT`, `DELETE`, and schema-level `MODIFY` permissions.