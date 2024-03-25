---
layout: default
title: ALTER ACCOUNT
description: Reference and syntax for the ALTER ACCOUNT command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Data definition
---

# ALTER ACCOUNT

Updates the configuration of the specified database `<database_name>`.

For more information, see [Managing accounts](../../../Guides/managing-your-organization/managing-accounts.md).

## Syntax

```sql
ALTER ACCOUNT <account_name> RENAME TO <new_account_name>;
```

## Parameters 
{: .no_toc} 

| Parameter | Description |
| :--- | :--- |
| `<account_name>` | The name of the account to be altered. |
| `<new_account_name>` | The new name for the account. The account name must start with an alphabetic character and cannot contain spaces or special characters except for hyphens (-). |

## Example

The following command will rename the "dev" account to "staging".

```sql
ALTER ACCOUNT dev RENAME TO staging;
```
