---
layout: default
title: REVOKE
description: Reference and syntax for the REVOKE command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Access control
---

# REVOKE
Revokes privileges from a role. Can also be used to revoke a role from another role or a user. 

For more information, see [Role-based access control](../../../Guides/managing-your-organization/rbac.md).

## Syntax

```REVOKE <privilege> ON <object_type> <object_name> FROM <role_name>```

or

```REVOKE ROLE <role_name> FROM { USER <user_name> | ROLE <role2_name> }```


| Parameter  | Description |
| :--------- | :---------- |
| `<privilege>` | The name of the privilege to revoke from a role. Privileges that can be revoked depend on the object they are revoked from - for a full list see [Privileges](../../../Guides/managing-your-organization/rbac.md#privileges). |
| `<object_type>` | The object to revoke privileges from - either DATABASE or ENGINE. |
| `<object_name>` | The name of the database or engine to revoke privileges from. |
| `<role_name>` | The name of the role. |
| `<user_name>` | The name of the user from whom to revoke the role. |
| `<role2_name>` | The name of the role from whom to revoke the role. |

## Example

The following command will revoke MODIFY privileges on the database "my_db" from the role "user_role".

```REVOKE MODIFY ON DATABASE my_db FROM user_role;```

## Example 2

The following command will revoke USAGE privileges on all databases in the account "my_account" from the role "user_role".

```REVOKE USAGE ANY DATABASE ON ACCOUNT my_account FROM user_role;```