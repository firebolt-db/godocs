---
layout: default
title: CREATE ROLE
description: Reference and syntax for the CREATE ROLE command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Access control
---

# CREATE ROLE
Creates a new role.

For more information, see [Role-based access control](../../../Guides/security/rbac.md).

## Syntax

```sql
CREATE ROLE [ IF NOT EXISTS ] <role_name>
```

## Parameters 
{: .no_toc} 

| Parameter  | Description |
| :--------- | :---------- |
| `<role_name>` | The name of the role. |

## Example

The following command will create a role "user_role" 

```sql
CREATE ROLE user_role;
```

## Example 2

The following command will create a role "user_role_2"

```
CREATE ROLE IF NOT EXISTS my_role_2
```

If "my_role_2" exists, no error message is thrown.