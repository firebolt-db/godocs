---
layout: default
title: Object Privileges
description: Use this reference to learn about the metadata available about privileges using the information schema.
nav_order: 9
parent: Information schema and usage views
grand_parent: General reference
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
{: .note}
Read more about RBAC privileges [here](../../managing-your-account/rbac.md).

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
| privilege_type | TEXT      | Defaulted to "USAGE" as this views shows only usage privilege.    |
| is_grantable   | TEXT      | YES if the privilege is grantable, NO if not.                     |
| created        | TIMESTAMP | Creation time of the privilege.                                   |
