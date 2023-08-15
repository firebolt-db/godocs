---
layout: default
title: DROP SERVICE ACCOUNT
description: Reference and syntax for the DROP SERVICE ACCOUNT command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Database object commands
---

# DROP SERVICE ACCOUNT
Deletes a service account.

For more information, see [Service accounts](../../../Guides/managing-your-organization/service-accounts.md).

## Syntax

```DROP SERVICE ACCOUNT <service_account_name>;```

| Parameter  | Description |
| :--------- | :---------- |
| `<service_account_name>`  | The name of the service account to delete. |

## Example

The following command will delete the "sa1" service account. 

```DROP SERVICE ACCOUNT "sa1";```
