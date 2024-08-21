---
layout: default
title: Service accounts
description: Use this reference to learn about the metadata available about service accounts using the information schema.
parent: Information schema
---

# Information schema for service_accounts

You can use the `information_schema.service_accounts` view to return information about service accounts.
You can use a `SELECT` query to return information about each service account as shown in the example below.

```sql
SELECT
  *
FROM
  information_schema.service_accounts;
```

Read more about service accounts [here](../../Guides/managing-your-organization/service-accounts.md).

## Columns in information_schema.service_accounts

Each row has the following columns with information about a service account.

| Column Name                 | Data Type   | Description                                                                                                                                                |
|:----------------------------|:------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| service_account_id          | TEXT        | The ID of the service account.                                                                                                                             |
| service_account_name        | TEXT        | The name of the service account.                                                                                                                           |
| network_policy_name         | TEXT        | The name of the network policy used by this service account.                                                                                               |
| service_account_description | TEXT        | The description of the service account.                                                                                                                    |
| is_organization_admin       | BOOLEAN     | Specifies if the service account is an organization admin.                                                                                                 |
| is_enabled                  | BOOLEAN     | Specifies if the service account is allowed to authenticate.                                                                                               |
| created                     | TIMESTAMPTZ | Time of the service account creation.                                                                                                                      |
| service_account_owner       | TEXT        | The name of the login that created the service account. If the service account was created by a service account, the service account name appears instead. |
| last_altered                | TIMESTAMPTZ | Time the service account was last altered.                                                                                                                 |
| last_altered_by             | TEXT        | The name of the login that edited the service account. If the service account was edited by a service account, the service account name appears instead.   |
