---
layout: default
title: LOWER
description: Reference material for LOWER function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: String functions
---

# LOWER

Converts the input string to lowercase characters. Note that Firebolt uses the `POSIX` locale, therefore `lower` only converts the ASCII characters “A” through “Z” to lowercase. Non-ASCII characters remain unchanged.

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

Because Firebolt uses the `POSIX` locale, non-ASCII characters are not lowercased:
```sql
SELECT LOWER('MÜNCHEN')
```

**Returns**: `mÜnchen`
