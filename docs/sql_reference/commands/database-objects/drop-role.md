---
layout: default
title: DROP ROLE
description: Reference and syntax for the DROP ROLE command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Database object commands
---

# DROP ROLE
Deletes a role.

For more information, see [Role-based access control](../../../Guides/managing-your-organization/rbac.md).

## Syntax

```DROP ROLE <role_name>```


| Parameter  | Description |
| :--------- | :---------- |
| `<role_name>` | The name of the role. |

## Example

The following command will delete the role "user_role".

```DROP ROLE user_role;```
