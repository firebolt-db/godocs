---
layout: default
title: ALTER NETWORK POLICY
description: Reference and syntax for the ALTER NETWORK POLICY command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Database object commands
---

# ALTER NETWORK POLICY
Updates the configuration of the specified network policy.

## Syntax

```sql
ALTER NETWORK POLICY [ IF EXISTS ] <network_policy_name>
SET  [ ALLOWED_IP_LIST = ( [ '<allowed_ip>' ] [, '<allowed_ip>' ... ] ) ]
[ BLOCKED_IP_LIST = ( [ '<blocked_ip>' ] [, '<blocked_ip>' ... ] ) ]
[ COMMENT = '<comment>' ] }
```

| Parameter  | Description |
| :--------- | :---------- |
| `<network_policy_name>`                              | The name of the network policy to edit.  |
| `<allowed_ip>`                      | A comma-separated and quoted list of IP addresses to allow in the specified network policy.  |         
| `<blocked_ip>` | A comma-separated and quoted list of IP addresses to block in the specified network policy.  |
| `<comment>` | A comment or description for the specified network policy. | 

## Example

The following command will edit 'my_network_policy' to set new allowed and blocked IP lists and an updated description: 

```ALTER NETWORK POLICY my_network_policy SET ALLOWED_IP_LIST = (‘4.5.6.7’, ‘2.4.5.7’) BLOCKED_IP_LIST = (‘6.7.8.9’) COMMENT = 'updated network policy'```
