---
layout: default
title: Network policies
description: Use this reference to learn about the metadata available about network policies using the information schema.
parent: Information schema
grand_parent: SQL reference
---

# Information schema for network_policies

You can use the `information_schema.network_policies` view to return information about network policies.
You can use a `SELECT` query to return information about each network policy as shown in the example below.
```sql
SELECT
  *
FROM
  information_schema.network_policies;
```

Read more about network policies [here](../../../Guides/managing-your-organization/network-policies.md).

## Columns in information_schema.network_policies

Each row has the following columns with information about a network policy.

|  Column Name    | Data Type | Description                                                     |
|:----------------|:----------|:----------------------------------------------------------------|
| network_policy_name | TEXT      | The name of the network policy. |
| allowed_ips  | ARRAY(TEXT)      | List of allowed ips |
| blocked_ips     | ARRAY(TEXT)      | List of blocked ips                                        |
| is_organizational | BOOLEAN | Specifies if the network policy is active at the organization level . |
| network_policy_description | TEXT | The description of the network policy.  |
| created         | TIMESTAMPTZ | Time the service account was created.   |
| network_policy_owner      | TEXT   | The name of the login that created the network policy. If the network policy was created by a service account, the service account name appears instead. |
| last_altered    | TIMESTAMPTZ | Time the service account was last altered.   |
| last_altered_by | TEXT      | The name of the login that edited the network policy. If the network policy was edited by a service account, the service account name appears instead. |

