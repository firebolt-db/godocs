---
layout: default
title: STRPOS
description: Reference material for STRPOSR function
grand_parent: SQL functions
parent: String functions
great_grand_parent: SQL reference
---

# STRPOS

Returns the position (in bytes) of the substring found in the string, starting from 1. The returned value is for the first matching value, and not for any subsequent valid matches.
In case the substring does not exist, functions will return 0.

## Syntax
{: .no_toc}

```sql
STRPOS(<string>, <substring>)
```

## Parameters 
{: .no_toc}

| Parameter       | Description                      | Supported input types    | 
| :---------------| :--------------------------------|:-------------------------|
| `<string>`    | The string that will be searched. | `TEXT` |
| `<substring>` | The substring to search for.        | `TEXT` |

## Return Type
`INTEGER`

## Example
{: .no_toc}

```sql
SELECT
	STRPOS('hello world','hello') AS res;
```

**Returns**: `1`

```sql
SELECT
	STRPOS('hello world','world') AS res;
```

**Returns**: `7`

```sql
SELECT
	STRPOS('hello world','work') AS res;
```

**Returns**: `0`
