---
layout: default
title: Transitive applicable roles
description: Use this reference to learn about the metadata available about roles using the information schema.
parent: Information schema
grand_parent: SQL reference
---

# Information schema for transitive_applicable_roles

`information_schema.transitive_applicable_roles` shows every role in the account and all its grantees (i.e. users or other roles to whom the role is granted).

Unlike, `information_schema.applicable_roles` that shows only direct grantees, `information_schema.transitive_applicable_roles` also shows indirect grantees.
For example, if role `engineer` is granted to role `manager` and role `manager` is granted to user `alice` then user `alice` is a direct grantee of `manager` and an indirect grantee of `engineer`.

You can use a `SELECT` query to return information about each role as shown in the example below.
```sql
SELECT
  *
FROM
  information_schema.transitive_applicable_roles;
```

See also `information_schema.applicable_roles` [here](applicable-roles.md).

{: .note}
Read more about RBAC roles [here](../../Guides/security/rbac.md#check-assigned-privileges-using-sql).

## Columns in information_schema.transitive_applicable_roles

Each row has the following columns with information about the role.

|  Column Name    | Data Type   | Description                                                         |
|:----------------|:------------|:--------------------------------------------------------------------|
| grantee         | TEXT        | User or role to whom the role is granted (directly or indirectly).  |
| role_name       | TEXT        | Name of the role.                                                   |
| is_grantable    | TEXT        | `YES` if the grantee has the admin option on the role, `NO` if not. |
| created         | TIMESTAMPTZ | Creation time of the role.                                          |
