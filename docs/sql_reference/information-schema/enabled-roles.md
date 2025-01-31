---
layout: default
title: Enabled roles
description: Use this reference to learn about the metadata available about roles using the information schema.
parent: Information schema
grand_parent: SQL reference
---

# Information schema for enabled_roles

The `information_schema.enabled_roles` view lists roles in a Firebolt account that is either owned by a user or comes with [role privileges]({% link Overview/Security/Role-Based Access Control/role-permissions.md %}#role-permissions) to access. 

The following code example uses a `SELECT` query to return information about each role:

```sql
SELECT
  *
FROM
  information_schema.enabled_roles;
```

{: .note}
For more information about permissions to access and perform operations on specific objects by role, see [Manage role-based access control]({% link Guides/security/rbac.md %}). 

## Columns in information_schema.enabled_roles

Each row contains the following columns with information about the role:

|  Column Name    | Data Type | Description                                                     |
|:----------------|:----------|:----------------------------------------------------------------|
| role_name       | TEXT        | The name of the role.                                         |
| created         | TIMESTAMPTZ | The time that the role was created.                                    |
| role_owner      | TEXT        | The name of the user who created the role.                        |
