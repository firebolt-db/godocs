---
layout: default
title: User Permissions
description: Learn about user-level permissions in Firebolt.
parent: Role-Based Access Control
grand_parent: Overview
nav_order: 5
---

# User permissions

In Firebolt, a [user]({% link Overview/organizations-accounts.md %}#users) is associated with a [login]({% link Guides/managing-your-organization/managing-logins.md %}) or [service account]({% link Guides/managing-your-organization/service-accounts.md %}), which grants them access to that account. You can assign a [role]({% link Overview/organizations-accounts.md %}#roles) to a user, and the role determines the specific actions they are authorized to perform within the account.

The following table outlines the privileges that can be granted for users within a particular account:

| Privilege             | Description                                                                 | GRANT Syntax                                                     | REVOKE Syntax                                                    |
|---------------------------|---------------------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|
| MODIFY                 | Grants the ability to drop the specified user.                       | `GRANT MODIFY ON USER <user_name> TO <role>;`                       | `REVOKE MODIFY ON USER <user_name> FROM <role>;`                    |

{: .note}
Users can modify most of their own account settings without requiring [RBAC]({% link Overview/Security/Role-Based Access Control/index.md %}#role-based-access-control-rbac) permissions, except when altering [LOGIN]({% link Guides/managing-your-organization/managing-logins.md %}) configurations or a [SERVICE ACCOUNT]({% link Guides/managing-your-organization/service-accounts.md %}).

## Examples of granting user permissions

### MODIFY permission
The following code example grants the role `developer_role` permission to drop the `my_user` user:

```sql
GRANT MODIFY ON USER my_user TO developer_role;
```