---
layout: default
title: View permissions
description: Learn about the permissions that can be assigned to views in Firebolt, including controlling access to view data and managing view-level operations.
parent: Database permissions
grand_parent: Role-Based Access Control
nav_order: 5
---

# View permissions

In Firebolt, **views** are objects that allow users to query data from one or more underlying tables or views. Permissions on these views determine who can interact with the view and what actions they can perform.


{: .note}
To interact with a view, roles must also have **USAGE** permissions on the parent schema and the parent database.

## View-level privileges

| Privilege             | Description                                                                 | GRANT Syntax                                                     | REVOKE Syntax                                                   |
|---------------------------|---------------------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|
| SELECT     | Allows selecting data from a view.                                                   | `GRANT SELECT ON VIEW <view_name> TO <role_name>;`                                      | `REVOKE SELECT ON VIEW <view_name> FROM <role_name>;`                                    |                              |
| MODIFY     | Allows modifying and dropping a view.                                                 | `GRANT MODIFY ON VIEW <view_name> TO <role_name>;`                                      | `REVOKE MODIFY ON VIEW <view_name> FROM <role_name>;`                                   |                  |
| ALL [PRIVLEGES]     | Grants all privileges over the view to a role.                                                 | `GRANT ALL ON VIEW <view_name> TO <role_name>;`                                      | `REVOKE ALL ON VIEW <view_name> FROM <role_name>;`                                   |

{: .note} 
Views are created at the schema level. To grant privileges to create views, refer to the [schema-level privileges documentation](schema-permissions.md). 

## Examples of granting view permissions

### SELECT permission

To allow querying data from a view, the role must have **SELECT** privileges on the view. Additionally, the **view owner** must have **SELECT** privileges on all underlying tables or views referenced within the view.

The following examples [grant]({% link sql_reference/commands/access-control/grant.md %}) the role `read_role` permission to query data from the `viewtest` view and ensure the `view_owner` has the necessary permission to read data from the `referenced_table` table, allowing the view to function correctly.

```sql
-- Grant SELECT on the view to a user:
GRANT SELECT ON VIEW "viewtest" TO read_role;

-- Grant SELECT on the referenced table to the view owner:
GRANT SELECT ON TABLE "referenced_table" TO view_owner;
```

{: .warning} 
If the **view owner** loses access to any of these referenced objects, users with **SELECT** on the view will no longer be able to query it, even if their **SELECT** privilege remains.

### MODIFY permission
The following code example grants the role `developer_role` permission to alter or drop the `my_view` view:

```sql
GRANT MODIFY ON VIEW my_view TO read_role;
```

### ALL permissions
The following code example grants the role `developer_role` with all permissions over the `my_view` view:

```sql
GRANT ALL ON VIEW my_view TO read_role;
```
