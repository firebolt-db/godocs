---
layout: default
title: ALTER SERVICE ACCOUNT
description: Reference and syntax for the ALTER SERVICE ACCOUNT command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Database object commands
---

# ALTER SERVICE ACCOUNT

Updates the configuration of the specified service account.

For more information, see [Service accounts](../../../Guides/managing-your-organization/service-accounts.md).

## Syntax

```sql
ALTER SERVICE ACCOUNT <service_account_name>
      SET [ NETWORK_POLICY = <network_policy_name> | DEFAULT ] 
      [ DESCRIPTION = <description> | DEFAULT ]
```

or 

```ALTER SERVICE ACCOUNT <service_account_name> RENAME TO <new_name>;```

| Parameter | Description |
| :--- | :--- |
| `<service_account_name>`                              | The name of the service account to edit.   |
| `<description>` | An optional description for the service account. |
| `<network_policy_name>`                      | An optional parameter to define the network policy to link to the edited service account. |
| `<new_name>`                              | The new name of the service account. Must start with a letter and may contain only alphanumeric, digit, or underscore(_) characters.  |

## Example

The following command will rename the "sa1" login to "serviceaccount1".

```ALTER SERVICE ACCOUNT "sa1" RENAME TO "serviceaccount1";```

This command will link the network policy "my_network_policy" to the "serviceaccount1" service account. 
```ALTER SERVICE ACCOUNT "serviceaccount1" SET NETWORK_POLICY = "my_network_policy";```
