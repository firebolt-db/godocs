---
layout: default
title: GRANT
description: Reference and syntax for the GRANT command.
grand_parent:  SQL commands
parent: Access control
---

# GRANT
Grants permissions to a role. Can also be used to grant a role to another role or a user. 

For more information, see [Role-based access control](../../../Guides/security/rbac.md).

## Syntax

```sql
GRANT <permission> ON <object_type> <object_name> TO <role_name>
```

or

```sql
GRANT ROLE <role_name> TO { USER <user_name> | ROLE <role2_name> }
```

## Parameters 
{: .no_toc} 

| Parameter  | Description |
| :--------- | :---------- |
| `<permission>` | The name of the permission to grant to a role. Permissions that can be granted depend on the object they are granted on - for a full list see [Permissions](../../../Guides/security/rbac.md#permissions). |
| `<object_type>` | The object to grant permissions on - either DATABASE or ENGINE. |
| `<object_name>` | The name of the database or engine to grant permissions on. |
| `<role_name>` | The name of the role. |
| `<user_name>` | The name of the user for the role grant. |
| `<role2_name>` | The name of the role for the role grant. |

## Example

The following command will grant USAGE permissions on the database "my_db" to the role "user_role".

```sql
GRANT USAGE ON DATABASE my_db TO user_role;
```

## Example 2

The following command will grant USAGE permissions on all databases in the account "dev" to the role "user_role".

```sql
GRANT USAGE ANY DATABASE ON ACCOUNT dev TO user_role;
```
