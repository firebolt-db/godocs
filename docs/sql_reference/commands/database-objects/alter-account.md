---
layout: default
title: ALTER ACCOUNT
description: Reference and syntax for the ALTER ACCOUNT command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Database object commands
---

# ALTER ACCOUNT

Updates the configuration of the specified database `<database_name>`.

## Syntax

```ALTER ACCOUNT <account_name> RENAME TO <new_account_name>;```

| Parameter | Description |
| :--- | :--- |
| `<account_name>` | The name of the account to be altered. |
| `<new_account_name>` | The new name for the account. The account name must start with an alphabetic character and cannot contain spaces or special characters except for underscores (_). |

## Example

The following command will rename the "my_account" account to "my_dev_account".

```sql
ALTER ACCOUNT my_account RENAME TO my_dev_account;
```
