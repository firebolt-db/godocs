---
layout: default
title: Service account users
description: Use this reference to learn about the metadata available about service accounts users using the information schema.
nav_order: 10
parent: Information schema and usage views
grand_parent: General reference
---

# Information schema for service_account_users

You can use the `information_schema.service_account_users` view to return information about service account users in the account.
You can use a `SELECT` query to return information about each role as shown in the example below.
```sql
SELECT
  *
FROM
  information_schema.service_account_users;
```

{: .note}
Read more about service accounts [here](../../managing-your-account/service-accounts.md).

## Columns in information_schema.service_account_users

Each row has the following columns with information about the role.

|  Column Name    | Data Type | Description                                                     |
|:----------------|:----------|:----------------------------------------------------------------|
| service_account_id   | TEXT      | The ID of the service account. |
| service_account_name | TEXT      | Name of the service account.                                               |
| network_policy_name  | TEXT      | Name of the network policy used by this service account. |
| description     | TEXT      | Description of the service account.                                        |
| created         | TIMESTAMP | Creation time of the service account.                                      |
| service_account_owner      | TEXT      | Name of the login that created the service account. |
| last_altered    | TIMESTAMP | Time the service account was last altered.                                 |
| last_altered_by | TEXT      | Name of the last login to edit the role.                         |

