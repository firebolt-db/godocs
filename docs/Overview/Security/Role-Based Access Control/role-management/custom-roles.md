---
layout: default
title: Custom Roles
description: Learn how to create and manage custom roles in Firebolt, allowing you to define tailored access controls for users based on specific permissions.
parent: Role Management
grand_parent: Role-Based Access Control
nav_order: 3
---

# Custom roles

In Firebolt, custom roles can be created at the account level to manage access control and permissions. Only users with the [account_admin]({% link Overview/organizations-accounts.md %}#account-administrative-role) system role or those granted the [CREATE ROLE]({% link sql_reference/commands/access-control/create-role.md %}) privilege can create custom roles. Once created, custom roles can be assigned to any user or existing role by the `account_admin` or the resource owner. 

Privileges can be granted to custom roles by `account_admin` or the [resource owner](../ownership.md). For example, the owner of a table can grant `SELECT` privileges on that table to a custom role. 

For more information about creating roles, see [creating a custom role via SQL or the Firebolt UI]({% link Guides/managing-your-organization/managing-users.md %}#create-a-role). 