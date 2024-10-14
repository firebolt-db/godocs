---
layout: default
title: Applicable roles
description: Use this reference to learn about the metadata available about roles using the information schema.
parent: Information schema
grand_parent: SQL reference
---

# Information schema for applicable_roles

`information_schema.transitive_applicable_roles` shows every role in the account and its grantees (i.e. users or other roles whom the role is granted to).

You can use a `SELECT` query to return information about each role as shown in the example below.
```sql
SELECT
  *
FROM
  information_schema.applicable_roles;
```

See also `information_schema.transitive_applicable_roles` [here](transitive-applicable-roles.md).

{: .note}
Read more about RBAC roles [here](../../Guides/security/rbac.md).

## Columns in information_schema.applicable_roles

Each row has the following columns with information about the role.

|  Column Name    | Data Type   | Description                                                         |
|:----------------|:------------|:--------------------------------------------------------------------|
| grantee         | TEXT        | User or role to whom the role is granted.                           |
| role_name       | TEXT        | Name of the role.                                                   |
| is_grantable    | TEXT        | `YES` if the grantee has the admin option on the role, `NO` if not. |
| created         | TIMESTAMPTZ | Creation time of the role.                                          |
