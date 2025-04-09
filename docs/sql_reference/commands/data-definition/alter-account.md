---
layout: default
title: ALTER ACCOUNT
description: Reference and syntax for the ALTER ACCOUNT command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Data definition
---

# ALTER ACCOUNT

Updates the configuration of the specified account.

For more information, see [Managing accounts]({% link Guides/managing-your-organization/managing-accounts.md %}).

## ALTER ACCOUNT RENAME TO

Renames an account.

### Syntax

```sql
ALTER ACCOUNT <account_name> RENAME TO <new_account_name>;
```

### Parameters 

{: .no_toc} 

| Parameter | Description                                                                                                                                                            |
| :--- |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<account_name>` | The name of the account to be altered.                                                                                                                                 |
| `<new_account_name>` | The new name for the account. The account name must start and end with an alphabetic character and cannot contain spaces or special characters except for hyphens (-). |

## Example

The following command will rename the "dev" account to "staging".

```sql
ALTER ACCOUNT dev RENAME TO staging;
```

## ALTER ACCOUNT OWNER TO

Changes the owner of an account.

You can view the current owner in the `account_owner` column of the `information_schema.accounts` view.

For more information, see [ownership]({% link Guides/security/ownership.md %}).

### Syntax

```sql
ALTER ACCOUNT <account_name> OWNER TO <identity>
```

### Parameters

{: .no_toc}

| Parameter        | Description                                                        |
|:-----------------|:-------------------------------------------------------------------|
| `<account_name>` | The name of the account to change the owner of.                    |
| `<identity>`     | The new owner of the account, which can be the name of a login or service account. |

### Example

The following command will set account "dev" owner to "alice@acme.com".

```sql
ALTER ACCOUNT "dev" OWNER TO "alice@acme.com";
```
