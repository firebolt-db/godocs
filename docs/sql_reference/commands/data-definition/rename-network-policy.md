---
layout: default
title: RENAME NETWORK POLICY
description: Reference and syntax for the RENAME NETWORK POLICY command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Data definition
---

# RENAME NETWORK POLICY
Renames the specified network policy.

For more information, see [Network policies](../../../Guides/managing-your-organization/network-policies.md).

## Syntax

```sql
ALTER NETWORK POLICY [ IF EXISTS ] <network_policy_name> 
    RENAME TO <new_network_policy_name>;
```

## Parameters
{: .no_toc}

| Parameter                                           | Description                                                                                 |
|:----------------------------------------------------|:--------------------------------------------------------------------------------------------|
| `<network_policy_name>`                             | The name of the network policy to rename.                                                   |
| `<new_network_policy_name>`                         | The new name for the network policy.                                          |                                          | 

## Example

The following command will rename 'my_network_policy' into 'my_renamed_network_policy:

```sql
RENAME NETWORK POLICY my_network_policy RENAME TO my_renamed_network_policy
```

