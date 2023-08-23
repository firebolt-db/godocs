---
layout: default
title: DROP NETWORK POLICY
description: Reference and syntax for the DROP NETWORK POLICY command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Access control
---

# DROP NETWORK POLICY
Deletes a network policy.

For more information, see [Network policies](../../../Guides/managing-your-organization/network-policies.md).

## Syntax

```DROP NETWORK POLICY <network_policy_name> [ RESTRICT | CASCADE ]```


| Parameter  | Description |
| :--------- | :---------- |
| `<network_policy_name>`  | The name of the network policy to delete. |   
| `RESTRICT` or `CASCADE` | An optional parameter to specify deletion mode.<br>RESTRICT mode prevents dropping the network policy if there is any login, service account or organization linked. RESTRICT mode is used by default.<br>CASCADE mode automatically drops the network policy and all its links to other objects.              

## Example

The following command will delete "my_network_policy".

```DROP NETWORK POLICY my_network_policy [ RESTRICT | CASCADE ]```
