---
layout: default
title: ALTER ORGANIZATION
description: Reference and syntax for the ALTER ORGANIZATION command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Access control
---

# ALTER v

Updates the specified organization to manage Single Sign-On configuration.

For more information, see [Setting up SSO](../../../Guides/managing-your-organization/sso/sso.md).

## Syntax

```ALTER ORGANIZATION SET SSO = ‘{
  “signOnUrl”: “<signOnUrl”,
  “signOutUrl”: “<signOutUrl”, 
  “issuer”: “<issuer>”,
  “provider”: “<idp”,
  “label”: “<label>”,
  “fieldMapping”: “<field_mapping>”,
  “certificate”: “<certficate>”,
}’;
```

| Parameter | Description |
| :--- | :--- |
| `<account_name>` | The name of the account to be altered. |
| `<new_account_name>` | The new name for the account. The account name must start with an alphabetic character and cannot contain spaces or special characters except for underscores (_). |

## Example

The following command will rename the "my_account" account to "my_dev_account".

```sql
ALTER ACCOUNT my_account RENAME TO my_dev_account;
```
