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
| public         | Enables querying any database in the account.<br>This role is automatically granted to every new user, but can be revoked if desired. |
| system_admin   | Enables managing databases, engines, schemas, tables, views, external tables, and grants, as well as setting database and engine properties. In addition, the system_admin role enables access to the observability functionality on all engines. |
| account_admin  | Enables all the permissions and the ability to manage the account. |

System defined roles can neither be modified nor dropped. Users with the `account_admin` role can grant roles to other users.

## Custom roles

A user with either the `account_admin` role can create custom roles. You can create a custom role using SQL, or via the UI.  

## Permissions
A set of permissions can be granted for every securable object. See which permissions are available for accounts, databases and engines below. To view all permissions, query the [information_schema.object_privileges](../../sql_reference/information-schema/object-privileges.md) view. 

## Ownership
When a user creates an object, they become its owner. The owner of an object can perform any operation with the object, even if the privileges required for an operation aren't granted to one of the user's roles. See [Ownership](./ownership.md) for more information. 

Owners can also grant privileges over every object they own, and grant owned roles, without the requirement of being an admin.

### Account
Permissions can be granted on accounts to allow creating, modifying and using databases and engines.

| Permission          | Description                                                                   |
|:--------------------|:-------------------------------------------------------------------------------|
| CREATE DATABASE     | Enables creating new databases in the account.                                 |
| USAGE ANY DATABASE  | Enables using all current and future databases in the account.  |
| MODIFY ANY DATABASE | Enables editing all current and future databases in the account. |
| CREATE ENGINE       | Enables creating new engines in the account.                                   |
| USAGE ANY ENGINE    | Enables using all current and future engines in the account.    |
| OPERATE ANY ENGINE  | Enables starting and stopping all current and future engines in the account.  |
| MODIFY ANY ENGINE   | Enables editing all current and future engines in the account.    |

#### Engine
Permissions can be granted on engines to allow usage, operation and modification of engines per account. 

| Permission         | Description |
| :---------------   | :---------- |
| USAGE              | Enables using the engine to execute queries. |
| OPERATE            | Enables stopping and starting the engine. |
| MODIFY             | Enables dropping or altering any properties of the engine. |

#### Database
Permissions can be granted on databases to allow usage and modification of databases per account. 

| Permission         | Description |
| :---------------   | :---------- |
| USAGE              | Enables using the database and attaching engines to it. |
| MODIFY             | Enables altering the properties of a database and dropping it. |
| USAGE ANY SCHEMA   | Enables using all current and future schemas in the database.    |
| VACUUM ANY TABLE   | Enables [VACUUM](../../sql_reference/commands/data-management/vacuum.md) on all existing and future tables in the database.    |

#### Schema

Permissions can be granted on schemas to allow usage and modification of schemas and their tables and views. 

| Permission         | Description |
| :---------------   | :---------- |
| USAGE              | Enables using the schema.     |
| MODIFY             | Enables modifying the schema. |
| CREATE             | Enables creating objects in the schema. |
| DELETE ANY TABLE   | Enables delete on all existing and future tables in the schema.              |
| INSERT ANY TABLE   | Enables insert on all existing and future tables in the schema.              |
| UPDATE ANY TABLE   | Enables update on all existing and future tables in the schema.              |
| TRUNCATE ANY TABLE | Enables truncate on all existing and futureall tables in the schema.         |
| VACCUM ANY TABLE   | Enables [VACUUM](../../sql_reference/commands/data-management/vacuum.md) on all existing and future tables in the schema. |
| MODIFY ANY         | Enables modify and drop on all existing and future objects in the schema.    |
| SELECT ANY         | Enables select on all existing and future objects in the schema.             |

to access schemas, users must also have:
* the `USAGE` permission on the parent database.

#### Table

Permissions can be granted on tables to allow operations on them.

| Permission         | Description |
| :---------------   | :---------- |
| DELETE             | Enables deleting rows and [dropping partitions](../../sql_reference/commands/data-definition/alter-table.md) from the table. Applicable only on managed tables. |
| INSERT             | Enables inserting rows into the table. Applicable only on managed tables. |
| UPDATE             | Enables updating rows in the table. Applicable only on managed tables. |
| TRUNCATE           | Enables truncating the table. Applicable only on managed tables. |
| VACUUM             | Enables [VACUUM](../../sql_reference/commands/data-management/vacuum.md) on the table. Applicable only on managed tables. |
| MODIFY             | Enables modifying and dropping the table. |
| SELECT             | Enables selecting rows from the table. |

to access tables, users must also have:
* the `USAGE` permission on the parent schema.
* the `USAGE` permission on the parent database.

#### Aggregating Index

to create an aggregating index, the user must have:
* the `MODIFY` permission on the table.
* the `CREATE` permission on the parent schema.
* the `USAGE` permission on the parent schema.
* the `USAGE` permission on the parent database.

to drop an aggregating index, the user must have:
* the `MODIFY` permission on the table.
* the `USAGE` permission on the parent schema.
* the `USAGE` permission on the parent database.

#### View

Permissions can be granted on views to allow usage and modification of views.

| Permission         | Description |
| :---------------   | :---------- |
| SELECT             | Enables using the view. |
| MODIFY             | Enables modifying the view. |

to access views, users must also have:
* the `USAGE` permission on the parent schema.
* the `USAGE` permission on the parent database.

#### Owner rights

When selecting over a view, the executing user needs to have access rights to the view, but when determining the access rightd to the underly objects of the view, the view owner's rights are considered, instead of of the executing user's rights. e.g

```sql
CREATE TABLE t (a int); -- create by user1 assigned with role1;
CREATE VIEW v AS SELECT * FROM my_table -- create by user2 assigned with role2;
GRANT SELECT ON v TO role2 
REVOKE SELECT ON t FROM role2 ;
SELECT * FROM my_view; -- executed by user2 and succeeds
REVOKE USAGE ON SCHEMA public FROM role1;
SELECT * FROM my_view; -- executed by user2 and fails, because user1 has no access to the table, due to missing schema usage permission
```


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
