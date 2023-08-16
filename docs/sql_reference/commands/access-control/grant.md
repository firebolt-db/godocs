---
layout: default
title: GRANT
description: Reference and syntax for the GRANT command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Access control
---

# GRANT
Grants privileges to a role. Can also be used to grant a role to another role or a user. 

For more information, see [Role-based access control](../../../Guides/managing-your-organization/rbac.md).

## Syntax

```GRANT <privilege> ON <object_type> <object_name> TO <role_name>```

or

```GRANT ROLE <role_name> TO { USER <user_name> | ROLE <role2_name> }```


| Parameter  | Description |
| :--------- | :---------- |
| `<privilege>` | The name of the privilege to grant to a role. Privileges that can be granted depend on the object they are granted on - for a full list see [Privileges](../../../Guides/managing-your-organization/rbac.md#privileges). |
| `<object_type>` | The object to grant privileges on - either DATABASE or ENGINE. |
| `<object_name>` | The name of the database or engine to grant privileges on. |
| `<role_name>` | The name of the role. |
| `<user_name>` | The name of the user for the role grant. |
| `<role2_name>` | The name of the role for the role grant. |

## Example

The following command will grant USAGE privileges on the database "my_db" to the role "user_role".

```GRANT USAGE ON my_db TO user_role;```
