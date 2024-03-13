---
layout: default
title: LOWER
description: Reference material for LOWER function
grand_parent: SQL functions
parent: String functions
great_grand_parent: SQL reference
---

# LOWER

Converts the input string to lowercase characters. Note that Firebolt uses the `ucs_basic` collation, therefore `lower` only converts ASCII characters to lowercase. Non-ASCII characters remain unchanged.

## Syntax
{: .no_toc}

```sql
LOWER(<expression>)
```
## Parameters
{: .no_toc}

| Parameter  | Description                 |Supported input types |
| :---------- | :--------------------------- | :-----------------|
| `<expression>` | The string to be converted to lowercase characters. | `TEXT` |

## Return Type
`TEXT`

## Example
{: .no_toc}

The following example converts a game player's username from uppercase to lowercase characters:

```sql
SELECT
	LOWER('ESIMPSON') as username
```

**Returns**: `esimpson`

Because Firebolt uses the `ucs_basic` collation, non-ASCII characters are not lowercased:
```sql
SELECT LOWER('MÜNCHEN')
```

**Returns**: `mÜnchen`
