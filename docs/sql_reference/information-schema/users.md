---
layout: default
title: Users
description: Use this reference to learn about the metadata available for Firebolt users using the information schema.
parent: Information schema and usage views
grand_parent: SQL reference
---

# Information schema for users
You can use the `information_schema.users` view to return information about users. You can use a `SELECT` query to return information about each user, as shown in the example below.

```sql
SELECT
  *
FROM
  information_schema.users;
```

For more information, see [Managing users](../../../Guides/managing-your-organization/managing-users.md).

## Columns in information_schema.users

Each row has the following columns with information about each user.

| Column Name                 | Data Type   | Description |
| :---------------------------| :-----------| :-----------|
| id                          | TEXT      | Unique identifier of the user. |
| organization_name           | TEXT      | Name of the organization. |
| account_name                | TEXT      | Name of the account. |
| user_name                   | TEXT      | Name of the user. |
| login_name                  | TEXT      | Name of the login linked to the user. Empty if the login is linked to a service account. |
| service_account_name        | TEXT      | Name of the service account linked to the user. Empty if the login is linked to a service account. |
| default_database            | TEXT      | Default database set for the user. |
| default_engine              | TEXT      | Default engine set for the user. |
| created                     | TIMESTAMP | Time the user was created. |
| user_owner                  | TEXT      | Name of the user who created the user. |
| last_altered                | TIMESTAMP | Time the user was last altered. |
| last_altered_by             | TEXT       | Name of the last user to edit the user. |





