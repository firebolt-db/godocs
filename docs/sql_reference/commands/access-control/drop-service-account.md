---
layout: default
title: DROP SERVICE ACCOUNT
description: Reference and syntax for the DROP SERVICE ACCOUNT command.
grand_parent:  SQL commands
parent: Access control
---

# DROP SERVICE ACCOUNT
Deletes a service account.

For more information, see [Service accounts](../../../Guides/managing-your-organization/service-accounts.md).

## Syntax

```sql
DROP SERVICE ACCOUNT <service_account_name>;
```
{: .note}
If the service account is linked to a user, it can not be dropped. In order to drop a service account linked to a user, the link must be reset `alter user foo set service_account=new_service_account|DEFAULT` or the user dropped.


## Parameters 
{: .no_toc} 

| Parameter  | Description |
| :--------- | :---------- |
| `<service_account_name>`  | The name of the service account to delete. |

## Example

The following command will delete the "sa1" service account. 

```sql
DROP SERVICE ACCOUNT "sa1";
```
