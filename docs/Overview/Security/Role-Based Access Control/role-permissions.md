---
layout: default
title: Role Permissions
description: Learn about role-level permissions in Firebolt.
parent: Role-Based Access Control
grand_parent: Overview
nav_order: 3
---

# Role permissions

In Firebolt, a [role]({% link Overview/organizations-accounts.md %}#roles) is a group of permissions that can have privileges assigned to it. You can [grant]({% link sql_reference/commands/access-control/grant.md %}#grant-role) a role to another role or to users.

The following table outlines the privileges that can be granted for roles within a particular account:

| Privilege             | Description                                                                 | GRANT Syntax                                                     | REVOKE Syntax                                                    |
|---------------------------|---------------------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|
| MODIFY                 | Grants the ability to drop the specified role.                       | `GRANT MODIFY ON ROLE <role_name> TO <role>;`                       | `REVOKE MODIFY ON ROLE <role_name> FROM <role>;`                    |


## Examples of granting role permissions

### MODIFY permission
The following code example grants the role `developer_role` permission to drop the `my_role` role:

```sql
GRANT MODIFY ON ROLE my_role TO developer_role;
```