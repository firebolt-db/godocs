---
layout: default
title: REVOKE
description: Reference and syntax for the REVOKE command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Access control
---

# REVOKE

Revokes permissions from a role. `REVOKE` can also be used to revoke a role from another role or a user. 

For more information, see [Role-based access control]({% link Guides/security/rbac.md %}).

## REVOKE PRIVILEGE

Revokes a permission from a role.

{: .note}
Only account_admin or a role owner can revoke a permission to a role.

### Syntax

```sql
REVOKE <permission> ON <object_type> <object_name> [IN <object_type> <object_name>] FROM <role_name>
```

### Parameters 
{: .no_toc} 

| Parameter  | Description |
| :--------- | :---------- |
| `<permission>` | The name of the permission to revoke from a role. Permissions that can be revoked vary depending on the object that they apply to. For a full list, see [Permissions]({% link Overview/Security/Role-Based Access Control/index.md %}). |
| `<object_type>` | The type of the object to revoke permissions from. |
| `<object_name>` | The name of the object to revoke permissions from. |
| `<role_name>` | The name of the role from which the permission will be revoked. |

### Examples

**Revoke `MODIFY` permission on a database**

The following code example revokes the `MODIFY` permission on the `db` database from the role `user_role`, preventing it from making changes to the database:

```sql
REVOKE MODIFY ON DATABASE db FROM user_role;
```

**Revoke all permissions on a database**

The following code example revokes the all permissions on the `db` database from the role `user_role`, preventing all operations on it:

```sql
REVOKE ALL ON DATABASE db FROM user_role;
```

**Revoke `USAGE` permissions on all databases in an account**

The following code example revokes `USAGE` permissions on all databases in the `dev` account from the role `user_role`, preventing it from accessing metadata or using those databases:

```sql
REVOKE USAGE ANY DATABASE ON ACCOUNT dev FROM user_role;
```

**Revoke `SELECT` permission on a specific table**

The following code example sets the active database to `db` and revokes `user_role`'s permission to read data from the `my_table` table in the `public` schema.:

```sql
USE DATABASE db;
REVOKE SELECT ON TABLE my_table IN SCHEMA public TO user_role;
```
**Revoke `SELECT` permission on all tables in a schema**

The following code revokes `user_role`'s permission to read data from all existing and future tables in the `public` schema of the `db` database:

```sql
REVOKE SELECT ANY ON SCHEMA public  IN DATABASE db TO user_role;
```
**Revoke `MODIFY` permission on a database while retaining it on all other databases in the `dev` account**

The following code example revokes the `MODIFY` permission on the `db` database from the role `user_role`, while keeping it for any other existing and future databases of the account:

```sql
GRANT MODIFY ANY DATABASE ON ACCOUNT dev TO user_role;
REVOKE MODIFY ON DATABASE db FROM user_role;
```

## REVOKE ROLE

Revokes a role from a user or from another role.

### Syntax

```sql
REVOKE ROLE <role_name> FROM { USER <user_name> | ROLE <role_name_2> }
```

## Parameters 
{: .no_toc} 

| Parameter  | Description |
| :--------- | :---------- |
| `<role_name>` | The name of the role to revoke. |
| `<user_name>` | The name of the user from which to revoke the `<role_name>` role. |
| `<role_name_2>` | The name of the role from which to revoke the role. |

### Examples

**Revoke a role from another role**

The following code example removes the `role_name` role from `role_name_2`, revoking access to permissions granted to `role_name`:

```sql
REVOKE ROLE role_name FROM ROLE role_name_2;
```

**Revoke a role from a user**

The following command revokes role `role_name` from user `user_name`, removing the user's access to the permissions granted to `role_name`:

```sql
REVOKE ROLE role_name FROM USER user_name;
```
