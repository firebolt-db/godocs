---
layout: default
title: RBAC
nav_exclude: true
search_exclude: true
toc_exclude: true
description: Learn about managing RBAC authorization for Firebolt users.
parent: Account and user management
grand_parent: Guides
---

# Role-based access control
{: .no_toc}

Role-based access control provides the ability to control privileges and determine who can access and perform operations on specific objects in Firebolt. Access privileges are assigned to roles that are, in turn, assigned to users. 

A user interacting with Firebolt must have the appropriate privileges to use an object. Privileges from all roles assigned to a user are considered in each interaction with a secured object. 

The key concepts to understanding access control in Firebolt with DB-level RBAC are:

  **Secured object:** an entity to which access can be granted: database, engine subscription.

  **Role:** An entity to which privileges can be granted. Roles are assigned to users.

  **Privilege:** a defined level of access to an object.

  **User:** A user identity recognized by Firebolt. It can be associated with a person or a program. Each user can be assigned multiple roles.

## Role types
Roles are entities to which privileges on securable objects are assigned. Roles are assigned to users to allow them to achieve the required tasks on the relevant objects to fulfill their business needs.

Firebolt comes out of the box with system-defined roles per each account. Those roles cannot be deleted from your account, the same as the privileges granted to the system-defined roles, which cannot be revoked.

Users granted the account admin role can create custom roles to meet specific needs. Moreover, users granted the account admin role can grant roles to other users.

## Privileges
There is a set of privileges that can be granted for every securable object.
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

## System-defined roles

| Role Name      | Description                                                                                                                                                                                                             | 
|:---------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| public         | Enables using any database in the account. In addition, it allows creating tables (external tables) and views in the public schema and selecting from all I_S views.                                                    |
| security_admin | Enables managing all account roles (with the ability to manage grants) and users.                                                                                                                                       |
| system_admin   | Enables managing databases, engines, schemas, tables, views, external tables, and grants. In addition, it also enables access to observability functionality on all engines and setting database and engine properties. |
| account_admin  | Provides everything system_admin and security_admin roles do alongside the ability to manage the account.                                                                                                               |

System defined roles cannot be modified nor dropped.

**Custom roles**<br>
A user granted the `account_admin` or `security_admin` roles can create custom roles. 

## SQL Reference

Firebolt SQL includes statements for controlling roles and privileges

### information schema views
#### applicable_roles

shows all roles in the account, full definition in [information_schema.applicable_roles](../general-reference/information-schema/applicable-roles.md).

#### object_privileges

shows all privileges in the account, full definition in [information_schema.object_privileges](../general-reference/information-schema/object-privileges.md).

### Create Role
Creates a custom role.
```sql
CREATE ROLE <role>
```

To verify success, execute: 
```sql
SELECT grantee, role_name FROM information_schema.applicable_roles WHERE role_name = '<role>'
```
result set should include a single row, `null, <role>` since the role is not yet assigned

### Drop Role
Deletes a custom role.
```sql
DROP ROLE <role>
```

To verify success, execute: 
```sql
SELECT grantee, role_name FROM information_schema.applicable_roles WHERE role_name = '<role>'
```
result set should be empty.

### Grant Privilege to a Role
Grant a privilege over an object to a role.
```sql
GRANT <privilege> ON { <object_type> <object_name> | ANY <object_type> } TO <role>
```

E.g, to grant usage over the database `my_db` to role `my_role`, execute:
```sql
GRANT USAGE ON DATABASE my_db TO my_role
```

To verify success, execute: 
```sql
SELECT object_type, privilege_type FROM information_schema.object_privileges WHERE grantee = '<role>'
```
result set should include the following row: `my_db, USAGE` 

### Revoke Privileges to a Role 
Revokes a privilege from a role.
```sql
REVOKE <privilege> ON { <object_type> <object_name> | ANY <object_type> } FROM <role>
```

E.g, to revoke usage over the database `my_db` from role `my_role`, execute:
```sql
REVOKE USAGE ON DATABASE my_db FROM my_role
```

To verify success, execute: 
```sql
SELECT object_type, privilege_type FROM information_schema.object_privileges WHERE grantee = '<role>'
```
result set will not include following row: `my_db, USAGE` 

### Grant Role to a Role/User
Grants a role to a user or another role.
```sql
GRANT ROLE <role> TO { USER <user_name> | ROLE <another_role> }
```

To verify success, execute: 
```sql
SELECT grantee, role_name FROM information_schema.applicable_roles WHERE role_name = '<role>'
```
result set should include a row per each assigned user or role, e.g. `<user_name>, <role>'.

### Revoke Role from a Role/User
Revokes a role from a user or another role.
```sql
REVOKE ROLE <role> FROM { USER <user_name> | ROLE <another_role> }
```

To verify success, execute: 
```sql
SELECT grantee, role_name FROM information_schema.applicable_roles WHERE role_name = '<role>'
```
result set should include a single row, `null, <role>` if it was the last role or user that was revoked from the role,
otherwise, result set should include a row per each assigned user or role, without the revoked role/user in the `grantee` column

## Roles Management from UI
### Assigning Roles to a User
From the menu, choose `Govern` > `Users`. In the opened page, all users are listed.
Choose the user you wish to edit, press the menu icon on the right, and in the toggled window choose `Edit User Details`.
Alternatively, create a new one using `+ Create User` button on the top left.

![Govern > Users](../assets/images/govern_users.png)

In the `Create/Edit User` window opened, check all the roles you want assigned to the user.
When done, press the `Create/Update` button

![Create/Edit User](../assets/images/create_edit_user.png)

see [User Reference Page](ask roy about it) for more information.

### Assigning Privileges to a role
From the menu, choose `Govern` > `Roles`. In the opened page, all roles are listed.
choose the role you wish to edit, press the menu icon on the right, and in the toggled window choose `Edit role`
Alternatively, create a new one using `+ New Role` button on the top left

![Govern > Roles](../assets/images/govern_roles.png)

In the `Create/Edit role` window, choose the privileges tab for the object type you want to manage privileges for,
then select the desired privileges. if you want to grant privileges over all objects of that type, choose the topmost line.
When done, press the `Create/Update` button:

![Create/Edit Role](../assets/images/create_edit_role.png)