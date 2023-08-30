---
layout: default
title: Logins
description: Use this reference to learn about the metadata available for Firebolt logins using the information schema.
parent: Information schema
grand_parent: SQL reference
---

# Information schema for logins
You can use the `information_schema.logins` view to return information about logins.
 
You can use a `SELECT` query to return information about each login, as shown in the example below.

```sql
SELECT
  *
FROM
  information_schema.logins;
```

For more information, see [Managing logins](../../../Guides/managing-your-organization/managing-logins.md).

## Columns in information_schema.logins

Each row has the following columns with information about each login.

| Column Name                 | Data Type   | Description |
| :---------------------------| :-----------| :-----------|
| login_name                  | TEXT      | Name of the login (email address). |
| first_name                  | TEXT      | First name of the user linked to the login. |
| last_name                   | TEXT      | Last name of the user linked to the login. |
| organization_name           | TEXT      | Name of the organization. |
| network_policy_name         | TEXT      | Name of the network policy associated with the login. |
| is_mfa_enabled              | BOOLEAN   | Specifies if the login has multi-factor authentication enabled. |
| is_sso_provisioned          | BOOLEAN   | Specifies if the login was provisioned with an identity provider defined in the organization's SSO configuration. |
| is_password_enabled         | BOOLEAN   | Specifies if log in with password is enabled. |
| is_organization_admin       | BOOLEAN   | Specifies if the login is an organization admin. |
| created                     | TIMESTAMPTZ | Time the login was created. |
| login_owner               | TEXT      | Name of the login who created the login. If the login was created by a service account, the service account name appears instead. |
| last_altered                | TIMESTAMPTZ | Time the login was last altered. |
| last_altered_by             | TEXT       | Name of the login who edited the login. If the login was edited by a service account, the service account name appears instead. | 

