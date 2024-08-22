---
layout: default
title: Accounts
description: Use this reference to learn about the metadata available about accounts using the information schema.
parent: Information schema
---

# Information schema for accounts
You can use the `information_schema.accounts` view to return information about accounts. 

You can use a `SELECT` query to return information about each account, as shown in the example below.

```sql
SELECT
  *
FROM
  information_schema.accounts;
```

{: .note}
Read more about managing accounts [here](../../Guides/managing-your-organization/managing-accounts.md).

## Columns in information_schema.accounts

Each row has the following columns with information about the account.

| Column Name     | Data Type | Description                                                     |
|:----------------|:----------|:----------------------------------------------------------------|
| account_name    | TEXT      | The name of the account.                                        |
| organization_name | TEXT      | The name of the organization to which the account belongs. |
| region    | TEXT      | The region in which the account can be used. |
| url    | TEXT      | The account login page URL.                                       |
| account_id         | TEXT | The unique account ID.                                   |
| trust_policy_role | TEXT | Role provided by Firebolt to enable access to customer S3 buckets |
| created    | TIMESTAMP   | Time (UTC) that the account was created.               |
| account_owner   | TEXT | The name of the login that created the account.   |
| last_altered  | TIMESTAMP | Time (UTC) that the user was last edited. |
| last_altered_by | TEXT      | Name of the last user to edit the role. |

