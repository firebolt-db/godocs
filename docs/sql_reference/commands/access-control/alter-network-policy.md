---
layout: default
title: ALTER NETWORK POLICY
description: Reference and syntax for the ALTER NETWORK POLICY command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Access control
---

# ALTER NETWORK POLICY
Updates the configuration of the specified network policy.

For more information, see [Network policies](../../../Guides/security/network-policies.md).

## Syntax

```sql
ALTER NETWORK POLICY [ IF EXISTS ] <network_policy_name>
SET  [ ALLOWED_IP_LIST = ( '<allowed_ip>', '<allowed_ip>' ... ) ]
     [ BLOCKED_IP_LIST = ( '<blocked_ip>', '<blocked_ip>' ... ) ]
     [ DESCRIPTION = '<description>' ] 
}
```

## Parameters 
{: .no_toc} 

| Parameter  | Description |
| :--------- | :---------- |
| `<network_policy_name>`                              | The name of the network policy to edit.  |
| `<allowed_ip>`                      | A comma-separated and quoted list of IP addresses to allow in the specified network policy.  |         
| `<blocked_ip>` | A comma-separated and quoted list of IP addresses to block in the specified network policy.  |
| `<description>` | An optional description for the specified network policy. | 

## Example

The following command will edit 'my_network_policy' to set new allowed and blocked IP lists and an updated description: 

```sql
ALTER NETWORK POLICY my_network_policy SET ALLOWED_IP_LIST = (‘4.5.6.7’, ‘2.4.5.7’) BLOCKED_IP_LIST = (‘6.7.8.9’) DESCRIPTION = 'updated network policy'
```
