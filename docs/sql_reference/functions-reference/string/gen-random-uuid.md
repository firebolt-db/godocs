---
layout: default
title: GEN_RANDOM_UUID
description: Reference material for GEN_RANDOM_UUID function
grand_parent: SQL functions
parent: String functions
great_grand_parent: SQL reference
published: false
---

# GEN\_RANDOM\_UUID

Returns a version 4 universally unique identifier (UUID) according to [RFC-4122](https://tools.ietf.org/html/rfc4122#section-4.4). This function accepts no arguments.

## Syntax
{: .no_toc}

```sql
GEN_RANDOM_UUID()
```
## Return Type
`TEXT`

## Example
{: .no_toc}

The example below outputs the result of `GEN_RANDOM_UUID` as `player_id`.

```sql
SELECT
	GEN_RANDOM_UUID() AS player_id;
```

**Returns**:

|              session_id              |
|:-------------------------------------|
| 08a95d43-2f01-4227-a111-de4f8ad205a0 |

