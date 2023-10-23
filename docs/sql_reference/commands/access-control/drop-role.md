---
layout: default
title: DROP ROLE
description: Reference and syntax for the DROP ROLE command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Access control
---

# DROP ROLE
Deletes a role.

For more information, see [Role-based access control](../../../Guides/managing-your-organization/rbac.md).

## Syntax

```sql
DROP ROLE [ IF EXISTS ] <role_name>
```

## Parameters 
{: .no_toc} 

| Parameter  | Description |
| :--------- | :---------- |
| `<role_name>` | The name of the role. |

## Example

The following command will delete the role "user_role"

```sql
DROP ROLE user_role;
```

### Example 2

The following command will delete the role "my_role_2"

```sql
DROP ROLE IF EXISTS my_role_2
```

If "my_role_2" does not exist, no error message is thrown