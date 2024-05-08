---
layout: default
title: Role-based access control (RBAC)
description: Learn about managing RBAC authorization for Firebolt users.
parent: Configure security
nav_order: 7
grand_parent: Guides
---

# Manage role-based access control
{: .no_toc}

Role-based access control provides the ability to control permissions and determine who can access and perform operations on specific objects in Firebolt. Permissions are assigned to roles which are, in turn, assigned to users or other roles. A user can be assigned multiple roles. 

A user interacting with Firebolt must have the appropriate permissions to use an object. Permissions from all roles assigned to a user are considered in each interaction in Firebolt. 

To view all roles, click **Govern** to open the govern space, then choose **Roles** from the menu, or query the [information_schema.applicable_roles](../../sql_reference/information-schema/applicable-roles.md) view.

## System-defined roles

Roles are assigned to users to allow them to complete tasks on relevant objects to fulfill their business needs. Firebolt comes with system-defined roles per account.

| Role Name      | Description                                                                                                                                                                                                             | 
|:---------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| public         | Enables querying any database in the account.                                                   |
| security_admin | Enables managing all account roles (with the ability to manage grants) and users. |
| system_admin   | Enables managing databases, engines, schemas, tables, views, external tables, and grants, as well as setting database and engine properties. In addition, the system_admin role enables access to the observability functionality on all engines. |
| account_admin  | Enables all the permissions of the system_admin and security_admin roles alongside the ability to manage the account. |

System defined roles can neither be modified nor dropped. Users with the `account_admin` role can grant roles to other users.

## Custom roles

A user with either the `account_admin` or `security_admin` role can create custom roles. You can create a custom role using SQL, or via the UI.  

## Permissions
A set of permissions can be granted for every securable object. See which permissions are available for accounts, databases and engines below. To view all permissions, query the [information_schema.object_privileges](../../sql_reference/information-schema/object-privileges.md) view. 

### Account
Permissions can be granted for accounts to allow creating databases and engines.

| Permission           | Description                                                                    |
|:--------------------|:-------------------------------------------------------------------------------|
| CREATE DATABASE     | Enables creating new databases in the account.                                 |
| USAGE ANY DATABASE  | Enables using all current and future databases in the account.  |
| MODIFY ANY DATABASE | Enables editing all current and future databases in the account. |
| CREATE ENGINE       | Enables creating new engines in the account.                                   |
| USAGE ANY ENGINE    | Enables using all current and future engines in the account.    |
| OPERATE ANY ENGINE  | Enables starting and stopping all current and future engines in the account.  |
| MODIFY ANY ENGINE   | Enables editing all current and future engines in the account.    |

#### Database
Permissions can be granted for databases to allow usage and modification of databases per account. 

| Permission          | Description |
| :---------------   | :---------- |
| USAGE              | Enables querying tables and views, and attaching engines to the database. |
| MODIFY             | Enables:<br>Creating or dropping tables, views, and indexes on the database.<br>Inserting data into the database's tables.<br>Altering the properties of a database.<br>Dropping a database. |

#### Engine
Permissions can be granted for engines to allow usage, operation and modification of engines per account. 

| Permission          | Description |
| :---------------   | :---------- |
| USAGE              | Enables using the engine to execute queries. |
| OPERATE            | Enables stopping and starting the engine. |
| MODIFY             | Enables dropping or altering any properties of the engine. |

## Create role

### SQL
To create a custom role using SQL, use the [`CREATE ROLE`](../../sql_reference/commands/access-control/create-role.md) statement. For example:

```sql
CREATE ROLE user_role;
```

### UI
To create a custom role via the UI:

![Govern > Roles](../../assets/images/rolespage.png)

1. Click **Govern** to open the govern space, then choose **Roles** from the menu.
2. From the Roles management page, choose **New role**. 
3. Enter a role name. 
4. Choose the object type you want to grant permissions on for the role from the left-hand list; databases or engines.
4. Choose the permissions you want to grant for each object type. You can use the toggles at the top to grant permissions over all databases or engines, or you can define permissions more granularly on existing databases or engines using the table views, where you can also search by database or engine name.

<img src="../../assets/images/createrole.png" alt="Create role" width="500"/>

## Delete role
To delete a custom role using SQL, use the [`DROP ROLE`](../../sql_reference/commands/access-control/drop-role.md) statement. For example:

```sql
DROP ROLE user_role;
```

### UI
To delete a custom role via the UI:

1. Click **Govern** to open the govern space, then choose **Roles** from the menu.
2. Search for the relevant role using the top search filters or by scrolling through the list. Hover over the right-most column to make the role menu appear, then choose **Delete role**. 
3. Choose **Confirm**.

<img src="../../assets/images/deleterole.png" alt="Delete role" width="500"/>

## Grant permissions to a role

### SQL 
To grant a permission to a role using SQL, use the [`GRANT`](../../sql_reference/commands/access-control/grant.md) statement. For example:

```sql
GRANT USAGE ON DATABASE my_db TO user_role;
```

### UI
To grant a permission to a role via the UI:
1. Click **Govern** to open the govern space, then choose **Roles** from the menu:

![Govern > Roles](../../assets/images/govern_roles.png)

2. Search for the relevant role using the top search filters, or by scrolling through the list of logins. Hover over the right-most column to make the role menu appear, then choose **Edit role**. 
3. Choose the permissions tab for the object type you want to manage permissions for, then select the desired permissions. To grant permissions over all objects of that type, choose the topmost line.
4. Click **Update**.

<img src="../../assets/images/create_edit_role.png" alt="Edit role" width="500"/>

## Grant role

### SQL
To grant a role to a user or another role using SQL, use the [`GRANT ROLE`](../../sql_reference/commands/access-control/grant.md) statement. For example:

```sql
GRANT ROLE user_role TO ROLE user2_role;
```

### UI
To grant a role to a user via the UI:
1. Click **Govern** to open the govern space, then choose **Users** from the menu:

![Govern > Users](../../assets/images/govern_users.png)

2. Search for the relevant user using the top search filters, or by scrolling through the list of logins. Hover over the right-most column to make the user menu appear, then choose **Edit user details**. 
3. Check all the roles you want assigned to the user.
4. Click **Update**.

<img src="../../assets/images/create_edit_user.png" alt="Edit user" width="500"/>

## Revoke permissions 

### SQL 
To revoke a permission from a role using SQL, use the [`REVOKE`](../../sql_reference/commands/access-control/revoke.md) statement. For example:

```sql
REVOKE USAGE ON DATABASE my_db FROM user_role;
```

### UI
To revoke a permission from a role via the UI, follow the [same steps above](#grant-permissions-to-a-role) that you would to grant permissions. 

## Revoke role 

### SQL 
To revoke a role from a user or another role using SQL, use the [`REVOKE ROLE`](../../sql_reference/commands/access-control/revoke.md) statement. For example:

```sql
REVOKE ROLE user_role FROM USER alex;
```

### UI
To revoke a role from a user or another role via the UI, follow the [same steps above](#grant-role) that you would to grant a role.  
