---
layout: default
title: CREATE SERVICE ACCOUNT
description: Reference and syntax for the CREATE SERVICE ACCOUNT command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Access control
---

# CREATE SERVICE ACCOUNT
Creates a new service account.

For more information, see [Service accounts](../../../Guides/managing-your-organization/service-accounts.md).

## Syntax

```sql
CREATE SERVICE ACCOUNT [ IF NOT EXISTS ] <service_account_name> 
    [ WITH
    [ DESCRIPTION = <description> ] 
    [ NETWORK_POLICY = <network_policy_name> ]
    ]
```

| Parameter  | Description |
| :--------- | :---------- |
| `<service_account_name>`                              | The name of the service account. Must start with a letter and may contain only alphanumeric, digit, or underscore(_) characters.  |
| `<description>` | An optional description for the service account. |
| `<network_policy_name>`                      | An optional parameter to define the network policy to link to the created service account. |  


## Example

The following command will create a service account "sa1" linked to the "my_network_policy" network policy. 

```CREATE SERVICE ACCOUNT "sa1" WITH NETWORK_POLICY = my_network_policy```
