---
layout: default
title: Role-based access control
description: Learn about managing RBAC authorization for Firebolt users.
parent: Managing your organization
nav_order: 6
grand_parent: Guides
---

# Role-based access control
{: .no_toc}

Role-based access control provides the ability to control privileges and determine who can access and perform operations on specific objects in Firebolt. Access privileges are assigned to roles which are, in turn, assigned to users. 

A user interacting with Firebolt must have the appropriate privileges to use an object. Privileges from all roles assigned to a user are considered in each interaction with a secured object. 

The key concepts to understanding access control in Firebolt with database-level RBAC are: < this should be a visualization > 

  **Secured object:** an entity to which access can be granted: database, engine subscription.

  **Role:** An entity to which privileges can be granted. Roles are assigned to users.

  **Privilege:** a defined level of access to an object.

  **User:** A user identity recognized by Firebolt. It can be associated with a person or a program. A user can be assigned multiple roles.


## System-defined roles

Roles are assigned to users to allow them to complete tasks on relevant objects to fulfill their business needs. Firebolt comes with system-defined roles per account.

| Role Name      | Description                                                                                                                                                                                                             | 
|:---------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| public         | Enables using any database in the account. In addition, the public role allows creating tables (external tables) and views in the public schema and selecting from information_schema views.                                                    |
| security_admin | Enables managing all account roles (with the ability to manage grants) and users. |
| system_admin   | Enables managing databases, engines, schemas, tables, views, external tables, and grants, as well as setting database and engine properties. In addition, the system_admin role enables access to the observability functionality on all engines. |
| account_admin  | Enables all the privileges of the system_admin and security_admin roles alongside the ability to manage the account. |

System defined roles cannot be modified nor dropped. Users granted the `account_admin` role can grant roles to other users.

## Custom roles

A user granted the `account_admin` or `security_admin` roles can create custom roles. You can create a custom role using SQL, or via the UI.  

### Create role

#### SQL
To create a custom role using SQL, use the [`CREATE ROLE`] statement. For example:

```CREATE ROLE <role>```

To verify success, execute: 
```SELECT grantee, role_name FROM information_schema.applicable_roles WHERE role_name = '<role>'```
result set should include a single row, `null, <role>` since the role is not yet assigned

#### UI
To create a custom role via the UI:



### Delete role
To delete a custom role using SQL, use the [`DROP ROLE`] statement. For example:

```DROP ROLE <role>```

To verify success, execute: 
```SELECT grantee, role_name FROM information_schema.applicable_roles WHERE role_name = '<role>'```
result set should be empty.

### Grant privileges

#### SQL 
To grant a privilege to a role using SQL, use the [`GRANT`] statement. For example:

```GRANT USAGE ON DATABASE my_db TO my_role``

To verify success, execute: 
```sql
SELECT object_type, privilege_type FROM information_schema.object_privileges WHERE grantee = '<role>'
```
result set should include the following row: `my_db, USAGE` 

#### UI
To grant a privilege to a role via the UI:
1. Click **Govern** to open the govern space, then choose **Roles** from the menu:

![Govern > Roles](../assets/images/govern_roles.png)

2. Search for the relevant role using the top search filters, or by scrolling through the list of logins. Hover over the right-most column to make the role menu appear, then choose **Edit role**. 
3. In the **Edit role** window, choose the privileges tab for the object type you want to manage privileges for, then select the desired privileges. To grant privileges over all objects of that type, choose the topmost line.
When done, press the **Update** button:

![Create/Edit Role](../assets/images/create_edit_role.png)

### Revoke privileges 
To revoke a privilege from a role using SQL, use the [`REVOKE`] statement. For example:

```REVOKE USAGE ON DATABASE my_db FROM my_role```


To verify success, execute: 
```sql
SELECT object_type, privilege_type FROM information_schema.object_privileges WHERE grantee = '<role>'
```
result set will not include following row: `my_db, USAGE` 

### Grant role

#### SQL
To grant a role to a user or another role using SQL, use the [`GRANT ROLE`] statement. For example:

```GRANT ROLE <role> TO { USER <user_name> | ROLE <another_role> }```

To verify success, execute: 
```sql
SELECT grantee, role_name FROM information_schema.applicable_roles WHERE role_name = '<role>'
```
result set should include a row per each assigned user or role, e.g. `<user_name>, <role>'.

#### UI
To grant a role to a user or another role via the UI:
1. Click **Govern** to open the govern space, then choose **Users** from the menu:

![Govern > Users](../assets/images/govern_users.png)

2. Search for the relevant user using the top search filters, or by scrolling through the list of logins. Hover over the right-most column to make the user menu appear, then choose **Edit User Details**. 
3. Edit the desired fields and choose **Save**.




In the `Create/Edit User` window opened, check all the roles you want assigned to the user.
When done, press the `Create/Update` button

![Create/Edit User](../assets/images/create_edit_user.png)

see [User Reference Page](ask roy about it) for more information.

### Revoke role 
To revoke a role from a user or another role using SQL, use the [`REVOKE ROLE`] statement. For example:

```REVOKE ROLE <role> FROM { USER <user_name> | ROLE <another_role> }```

To verify success, execute: 
```sql
SELECT grantee, role_name FROM information_schema.applicable_roles WHERE role_name = '<role>'
```
result set should include a single row, `null, <role>` if it was the last role or user that was revoked from the role,
otherwise, result set should include a row per each assigned user or role, without the revoked role/user in the `grantee` column

## Role management from the UI

#### applicable_roles

shows all roles in the account, full definition in [information_schema.applicable_roles](../general-reference/information-schema/applicable-roles.md).

## Privileges
A set of privileges can be granted for every securable object. See below for which privileges are available for which objects. 

### Account

| Privilege         | Description                                    |
|:------------------|:-----------------------------------------------|
| CREATE ENGINE     | Enables creating new engines in the account.   |
| CREATE DATABASE   | Enables creating new databases in the account. |

### Database

| Privilege          | Description |
| :---------------   | :---------- |
| USAGE              | Enables running SELECT on the database's tables, views, and ATTACH engines. |
| MODIFY              | Enables:<br>Running CREATE/DROP tables, views, and indexes on a database's tables.<br>Running INSERT data into a database's tables.<br>Altering the properties of a database.<br>Dropping a database. |

### Engine

| Privilege          | Description |
| :---------------   | :---------- |
| USAGE              | Enables using an engine and, therefore, executing queries on it. |
| OPERATE            | Enables changing the state of an engine (stop, start). |
| MODIFY             | Enables dropping or altering any properties of an engine. |

#### object_privileges

shows all privileges in the account, full definition in [information_schema.object_privileges](../general-reference/information-schema/object-privileges.md).
