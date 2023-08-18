---
layout: default
title: CREATE NETWORK POLICY
description: Reference and syntax for the CREATE NETWORK POLICY command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Access control
---

# CREATE NETWORK POLICY
Creates a new network policy.

For more information, see [Network policies](../../../Guides/managing-your-organization/network-policies.md).

## Syntax

```sql
CREATE NETWORK POLICY [IF NOT EXISTS] <network_policy_name>
ALLOWED_IP_LIST = ( [ '<allowed_ip1>', '<allowed_ip2>', ... ] )
[ BLOCKED_IP_LIST = ( [ '<blocked_ip1>', '<blocked_ip2>', ... ] ) ]
[ COMMENT = '<comment>' ]
```

| Parameter  | Description |
| :--------- | :---------- |
| `<network_policy_name>`                              | The name of the network policy. Must start with a letter, and may contain only alphanumeric and underscore(_) characters.   |
| `<allowed_ip>`                      | The comma-separated and quoted list of IP addresses to allow in the created network policy.  |         
| `<blocked_ip>` | An optional comma-separated and quoted list of IP addresses to block in the created network policy.  |
| `<comment>` | An optional comment or description for the created network policy. | 

## Example

The following command will create a network policy that allows IPs ‘4.5.6.1’ and ‘2.4.5.1’ and blocks the IP address '6.7.8.1', with a description: 

```CREATE NETWORK POLICY my_network_policy ALLOWED_IP_LIST = (‘4.5.6.1’, ‘2.4.5.1’) BLOCKED_IP_LIST = ('6.7.8.1') COMMENT = 'my new network policy'```
