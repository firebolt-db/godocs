---
layout: default
title: DROP ROLE
description: Reference and syntax for the DROP ROLE command.
grand_parent:  SQL commands
parent: Access control
---

# DROP ROLE
Deletes a role. Note that role cannot be dropped if there are permissions granted to the role, in this case
error message will be displayed and you need manually to drop permissions granted to the role and retry.

For more information, see [Role-based access control](../../../Guides/security/rbac.md).

{: .warning}
A role cannot be dropped if there are permissions granted to the role. In this case, an error message will be displayed, and you need to manually drop the permissions granted to the role and retry.

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

If "my_role_2" does not exist, no error message is thrown.