---
layout: default
title: Role-based access control (RBAC)
description: Learn about managing RBAC authorization for Firebolt users.
parent: Configure security
nav_order: 7
---

# Manage role-based access control
{: .no_toc}

Role-Based Access Control (RBAC) allows you to manage user permissions by controlling who can access or perform operations on specific objects in Firebolt. This guide provides a step-by-step process for setting RBAC in Firebolt.

## Prerequisites
The following material can help you understand key concepts related to organizations and RBAC in Firebolt:
* [Organizations and accounts]({% link Overview/organizations-accounts.md %}) &ndash; How Firebolt provides a structure for managing users, resources, and permissions.
* [Role-Based Access Control]({% link Overview/Security/Role-Based Access Control/index.md %}) &ndash; How administrators manage user permissions and control access to resources based on predefined roles.


## View all roles 

To view all roles using the **Firebolt Workspace**, do the following:

1. Login to the [Firebolt Workspace](https://firebolt.go.firebolt.io/signup).
2. Select the **Govern** icon (<img src="../../assets/images/govern-icon.png" alt="The Firebolt Govern Space icon." width="20">)from the left navigation bar to open the **Govern Space**.
3. Choose **Roles** from the left panel under **Govern**.

To view all roles using SQL, query the [information_schema.applicable_roles]({% link sql_reference/information-schema/applicable-roles.md %}) view as shown in the following code example:

```sql
SELECT
  *
FROM
  information_schema.applicable_roles;
```

## Create a role

You can create a role using the **Firebolt Workspace** user interface (UI) or using SQL.

### Create a role using SQL
The following code example uses [CREATE ROLE]({% link sql_reference/commands/access-control/create-role.md %}) to create the role `user_role`:

```sql
CREATE ROLE user_role;
```

### Create a role using the UI
To create a custom role using the UI:


1. Select the **Govern** icon (<img src="../../assets/images/govern-icon.png" alt="The Firebolt Govern Space icon." width="20">) from the left navigation bar to open the **Govern Space**.
2. Choose **Roles** from the left panel under **Govern**.
3. Choose the **+ New Role** button in the upper-right corner of the page.
4. Under **Define role**, enter a role name.
5. Select **Configure permissions**.
6. Under **Configure permissions** for each category you can select objects that you want to grant permissions for. For each category you can have multiple groups of permissions. To add additional group use **Add another group** button.
7. Configure permissions for each group:
  * Grant permissions to **operate**, **usage**, **modify**, etc group of objects, using the **Add permissions** button.
8. Select **Assign role**.
9. Select the users for which you want to assign this role or create the role without any assignment.
10. Select **Create role*


## Delete a role

You can delete a role using either the UI in the **Govern Workspace** or using SQL.
### Delete a role using SQL

To delete a role using SQL, use [DROP ROLE]({% link sql_reference/commands/access-control/drop-role.md %}) as shown in the following code example:

```sql
DROP ROLE user_role;
```

### Delete a role using the UI
To delete a role via the UI:

1. Select the **Govern** icon (<img src="../../assets/images/govern-icon.png" alt="The Firebolt Govern Space icon." width="20">) from the left navigation bar to open the **Govern Space**.
2. Choose **Roles** from the left panel under **Govern**.
2. Search for the relevant role using the top search filters or by scrolling through the list. Hover over the right-most column to make the role menu appear, then choose **Delete role**. 
3. Choose **Confirm**.


## Grant permissions to a role

### Grant permissions using SQL
To grant a permission to a role using SQL, use [GRANT]({% link sql_reference/commands/access-control/grant.md %}) as shown in the following code example:

```sql
GRANT USAGE ON DATABASE my_db TO user_role;
```

### Grant permissions using the UI
To grant a permission to a role via the UI:
1. Select **Govern** to open the govern space, then choose **Roles** from the menu:


2. Search for the relevant role either by using the search filters at the top of the page, or by scrolling through the list of logins. Hover over the right-most column to make the role menu appear, then choose **Edit role**.
3. Navigate to the **Configure permissions** tab to add or remove permissions.
4. Navigate to the **Configure database permissions** tab and select the database for which you want to edit permissions.
   * Edit the desired permissions, relevant to the selected database.
   * Choose a different database if you need to edit its permissions. Repeat this step as many times as needed.
4. Select **Assign role**.
5. Select checkbox next to the users that you want to grant role to.
6. Select **Save role**



## Grant a role to users

### Grant a role to users using SQL
To grant a role to a user or another role using SQL, use [GRANT ROLE]({% link sql_reference/commands/access-control/grant.md %}) as shown in the following code example:

```sql
GRANT ROLE user_role TO ROLE user2_role;
```

### Grant a role using the UI
To grant a role to a user via the UI:
1. Select **Govern**, then choose **Users** from the menu:


2. In the user's row, select the three horizontal dots to the right.
3. Select **Edit user details**. 
4. Select the drop-down list next to **Role**.
5. Select the checkbox next to the roles that you want to grant.
6. Select **Edit user**.


## Revoke permissions

You can revoke permissions using the UI in the **Govern Space** or using SQL.

### Revoke permissions using SQL 
To revoke a permission from a role using SQL, use [REVOKE]({% link sql_reference/commands/access-control/revoke.md %}) as shown in the following example:

```sql
REVOKE USAGE ON DATABASE my_db FROM user_role;
```

### Revoke permissions using the UI
To revoke permissions, follow the same steps described in [Grant permissions to a role](#grant-permissions-to-a-role).

## Revoke role

You can revoke a role from either a user or another role using either the UI in the **Govern Space** or SQL.

### Revoke a role using SQL 
To revoke a role from a user or another role using SQL, use the [REVOKE ROLE]({% link sql_reference/commands/access-control/revoke.md %}) statement. For example:

```sql
REVOKE ROLE user_role FROM USER alex;
```

### Revoke a role using the UI
To revoke a role, follow the steps in [Grant a role to users](#grant-a-role-to-users).


### Check assigned privileges using SQL

To check the effective privileges for the current user, run the following example query:

```sql
SELECT
  AR.grantee,
  AR.role_name,
  OP.privilege_type,
  OP.object_type,
  OP.object_name
FROM information_schema.transitive_applicable_roles AS AR
JOIN information_schema.object_privileges AS OP
ON (AR.role_name = OP.grantee)
WHERE
  AR.grantee = session_user();
```

**Returns**: 

| grantee   | role_name     | privilege_type | object_type | object_name |
|:----------|:--------------|:---------------|:------------|:------------|
| test_user | account_admin | USAGE | engine | engine1 | 
| test_user | account_admin | USAGE | database | db1 |

#### Owner rights

When a query is run on a view, the database checks and uses the permissions of the view's owner to access the underlying objects that view references, rather than the permissions of the user that ran the query on the view. The view's owner is the user that created the view. 

The following code example shows how granting and revoking privileges affects access to a base table and its view, ultimately causing an authorization failure when the view's owner loses schema usage privileges:

```sql
CREATE USER user1 WITH ROLE=role1;
CREATE USER user2 WITH ROLE=role2;

CREATE TABLE base_table (a int); -- executed by user1
CREATE VIEW view_over_base_table AS SELECT * FROM base_table; -- executed by user1

GRANT SELECT ON VIEW view_over_base_table TO role2;
REVOKE SELECT ON TABLE base_table FROM role2;

SELECT * FROM base_table; -- executed by user2, fails with an authorization error
SELECT * FROM view_over_base_table; -- executed by user2, successfully

REVOKE USAGE ON SCHEMA public FROM role1;
-- role1 no longer has no access to the table due to missing schema usage privileges
SELECT * FROM view_over_base_table; -- executed by user2 and fails because the view owner's role1 cannot access table t
```
If the view owner's privileges are revoked, the query will fail even if the user has access to the view.

