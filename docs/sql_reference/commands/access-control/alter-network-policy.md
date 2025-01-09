---
layout: default
title: ALTER NETWORK POLICY
description: Reference and syntax for the ALTER NETWORK POLICY command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Access control
---

# ALTER NETWORK POLICY
Updates the configuration of the existing network policy by specifying its name, a list of internet protocol (IP) addresses to allow or block, and an optional description.

For more information, see [Network policies](../../../Guides/security/network-policies.md).

## Syntax

```sql
ALTER NETWORK POLICY [ IF EXISTS ] <network_policy_name>
    SET [ ALLOWED_IP_LIST = ( '<allowed_ip>', '<allowed_ip>' ... ) ]
        [ BLOCKED_IP_LIST = ( '<blocked_ip>', '<blocked_ip>' ... ) ]
        [ DESCRIPTION = '<description>' ]

ALTER NETWORK POLICY [ IF EXISTS ] <network_policy_name>
    ADD [ ALLOWED_IP_LIST = ( '<allowed_ip>', '<allowed_ip>' ... ) ]
        [ BLOCKED_IP_LIST = ( '<blocked_ip>', '<blocked_ip>' ... ) ]

ALTER NETWORK POLICY [ IF EXISTS ] <network_policy_name>
    REMOVE [ BLOCKED_IP_LIST = ( '<blocked_ip>', '<blocked_ip>' ... ) ]
           [ BLOCKED_IP_LIST = ( '<blocked_ip>', '<blocked_ip>' ... ) ]
```

## Parameters 
{: .no_toc} 

| Parameter  | Description |
| :--------- | :---------- |
| `<network_policy_name>`                              | The name of the network policy to edit.  |
| `<allowed_ip>`                      | A comma-separated and quoted list of IP addresses to **allow** in the specified network policy.  |         
| `<blocked_ip>` | A comma-separated and quoted list of IP addresses to **block** in the specified network policy.  |
| `<description>` | (Optional) A description for the specified network policy. | 

## Examples

**Example**

The following code example modifies the existing network policy 'my_network_policy' by replacing its allowed and blocked IP lists with specified values and an updating its description:

```sql
ALTER NETWORK POLICY my_network_policy SET ALLOWED_IP_LIST = ('4.5.6.7', '2.4.5.7') BLOCKED_IP_LIST = ('6.7.8.9') DESCRIPTION = 'updated network policy'
```
**Example**

The following code example adds an IP address `192.168.5.1` to the allowed list of the existing network policy `my_network_policy`:

```sql
ALTER NETWORK POLICY my_network_policy ADD ALLOWED_IP_LIST = ('192.168.5.1');
```
**Example**

The following code example removes the IP address `6.7.8.9` from the blocked list of the network policy `my_network_policy`:

```sql
ALTER NETWORK POLICY my_network_policy REMOVE BLOCKED_IP_LIST = ('6.7.8.9');
```