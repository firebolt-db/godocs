---
layout: default
title: REVOKE
description: Reference and syntax for the REVOKE command.
parent: Access control
---

# REVOKE
Revokes permissions from a role. Can also be used to revoke a role from another role or a user. 

For more information, see [Role-based access control](../../../Guides/security/rbac.md).

## Syntax

```sql
REVOKE <privilege> ON <object_type> <object_name> FROM <role_name>
```

or

```sql
REVOKE ROLE <role_name> FROM { USER <user_name> | ROLE <role2_name> }
```

## Parameters 
{: .no_toc} 

| Parameter  | Description |
| :--------- | :---------- |
| `<permission>` | The name of the permission to revoke from a role. Permissions that can be revoked depend on the object they are revoked from - for a full list see [Permissions](../../../Guides/security/rbac.md#permissions). |
| `<object_type>` | The object to revoke permissions from - either DATABASE or ENGINE. |
| `<object_name>` | The name of the database or engine to revoke permissions from. |
| `<role_name>` | The name of the role. |
| `<user_name>` | The name of the user from whom to revoke the role. |
| `<role2_name>` | The name of the role from whom to revoke the role. |

## Example

The following command will revoke MODIFY permissions on the database "my_db" from the role "user_role".

```sql
REVOKE MODIFY ON DATABASE my_db FROM user_role;
```

## Example 2

The following command will revoke USAGE permissions on all databases in the account "dev" from the role "user_role".

```sql
REVOKE USAGE ANY DATABASE ON ACCOUNT dev FROM user_role;
```
