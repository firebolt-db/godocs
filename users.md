---
layout: default
title: Users
description: Use this reference to learn about the metadata available for Firebolt users using the information schema.
parent: Information schema
---

# Information schema for users
You can use the `information_schema.users` view to return information about users. You can use a `SELECT` query to return information about each user, as shown in the example below.

```sql
SELECT
  *
FROM
  information_schema.users;
```

For more information, see [Managing users](../../Guides/managing-your-organization/managing-users.md).

## Columns in information_schema.users

Each row has the following columns with information about each user.

| Column Name                 | Data Type   | Description |
| :---------------------------| :-----------| :-----------|
| user_name                   | TEXT      | The name of the user. |
| login_name                  | TEXT      | The name of the login linked to the user. Empty if the login is linked to a service account. |
| service_account_name        | TEXT      | The name of the service account linked to the user. Empty if the login is linked to a service account. |
| account_name                | TEXT      | The name of the account. |
| organization_name           | TEXT      | The name of the organization. |
| default_database            | TEXT      | The default database set for the user. |
| default_engine              | TEXT      | The default engine set for the user. |
| created                     | TIMESTAMPTZ | Time the user was created. |
| user_owner                  | TEXT      | The name of the user who created the user. |
| last_altered                | TIMESTAMPTZ | Time the user was last altered. |
| last_altered_by             | TEXT       | The name of the last user to edit the user. |





