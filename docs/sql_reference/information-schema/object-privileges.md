---
layout: default
title: Object privileges
description: Use this reference to learn about the metadata available about privileges using the information schema.
parent: Information schema
grand_parent: SQL reference
---

# Information schema for object_privileges

You can use the `information_schema.object_privileges` view to return information about permissions granted to each role.  
You can use a `SELECT` query to return information about each privilege as shown in the example below.
```sql
SELECT
  *
FROM
  information_schema.object_privileges;
```

Read more about RBAC privileges [here](../../Guides/security/rbac.md).

## Columns in information_schema.object_privileges

Each row has the following columns with information about the role.

| Column Name    | Data Type | Description                                                       |
|:---------------|:----------|:------------------------------------------------------------------|
| grantor        | TEXT      | Name of the user that granted the privilege.                      |
| grantee        | TEXT      | Name of the role that the privilege was granted to (TO ROLE).     |
| object_catalog | TEXT      | Database containing the object on which the privilege is granted. |
| object_schema  | TEXT      | Schema containing the object on which the privilege is granted.   |
| object_name    | TEXT      | Name of the object on which the privilege is granted.             |
| object_type    | TEXT      | Type of the object on which the privilege is granted.             |
| privilege_type | TEXT      | Type of the privilege granted over the object.                     |
| is_grantable   | TEXT      | YES if the privilege is grantable, NO if not.                     |
| created        | TIMESTAMPTZ | Creation time of the privilege.                                 |
