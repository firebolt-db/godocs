---
layout: default
title: Default System Roles
description: Learn about the default system roles in Firebolt, their permissions, and how they help manage access control across different database objects and operations.
parent: Role Management
grand_parent: Role-Based Access Control
nav_order: 2
---

# Default system roles

In Firebolt, **system-defined** roles are automatically created for each organization and account. These roles provide predefined privileges and serve specific purposes. While system-defined roles **cannot** be modified or dropped, you can grant them additional privileges as needed.

## Organization system roles

| Role Name | Description                                                              |
|---|---|
| organization_admin | Enables all the permissions and the ability to manage the organization. |

{: .note}
The [organization_admin]({% link Overview/organizations-accounts.md %}#organizational-administrative-role) role cannot be granted using SQL. It can only be granted using the [Firebolt Workspace](https://go.firebolt.io/signup) user interface (UI). To manage resources at the organization level, you must assign the `organization_admin` role to your login using the UI.

## Account system roles

| Role Name      | Description                                                                                                                                               |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| public         | Includes `USAGE` on all databases and both `USAGE` and `CREATE` on every public schema.                                                                  |
| system_admin   | Enables managing databases, engines, schemas, tables, and views. This includes setting database and engine properties as well as access to the observability functionality on all engines. |
| account_admin  | Grants full permissions to manage the organization.                                                                                        |

{: .note}
By default, every newly created user is granted the [public]({% link Overview/organizations-accounts.md %}#public-role) role. You can also revoke this role from a user.