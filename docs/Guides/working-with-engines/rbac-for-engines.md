---
layout: default
title: RBAC for Governing Engines
description: Learn how to use Role Based Access Control to govern engines
parent: Work with engines
grand_parent: Guides
---

Use Role [Based Access Control](../../Guides/security/rbac.md) (RBAC) to granularly control which users within an account can create new engines, use, operate, monitor and modify existing engines. Accordingly, Firebolt provides CREATE, USAGE, OPERATE, MONITOR and MODIFY permissions to control these actions. You can use RBAC to control whether a user has permissions to perform these actions for specific engines or for all engines in a given account. Note that permissions for CREATE ENGINE can only be granted at the account level. <br />

Follow the below steps to control what permissions a user has for a given engine or for any engine within an account:
* Create a new role
* Grant permissions to the role
* Assign role to a user

**Example 1:**  We want to provide a user kate with permissions to create and operate engines

```sql
CREATE ROLE prodAdminRole;

GRANT CREATE ENGINE ON ACCOUNT myAccount IN ORGANIZATION myOrg TO prodAminRole; 

GRANT OPERATE ENGINE ON myEngine IN ACCOUNT myAccount TO prodAdminRole; 

GRANT ROLE prodAdminRole TO USER kate;  
```

**Example 2:** We want to provide a user kate with permissions to only use and operate engines

```sql
CREATE ROLE prodAdminRole;

GRANT USAGE ENGINE ON myEngine IN ACCOUNT myAccount TO prodAminRole; 

GRANT OPERATE ENGINE ON myEngine IN ACCOUNT myAccount TO prodAdminRole; 

GRANT ROLE prodAdminRole TO USER kate;  
```



