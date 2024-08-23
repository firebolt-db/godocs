---
layout: default
title: POSITION
description: Reference material for POSITION function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: String functions
published: true
---

# POSITION

Returns the position of the substring found in the string, starting from 1. The returned value is for the first matching value, and not for any subsequent valid matches.
In case the substring does not exist, functions will return 0.

## Syntax
{: .no_toc}

```sql
POSITION(<substring> IN <string>)
```

## Parameters 
{: .no_toc}

| Parameter       | Description                      | Supported input types    | 
| :---------------| :--------------------------------|:-------------------------|
| `<substring>` | The substring to search for.        | `TEXT` |
| `<string>`    | The string that will be searched. | `TEXT` |

## Return Type
`INTEGER`

## Example
{: .no_toc}

```sql
SELECT
	POSITION('hello' IN 'hello world') AS res;
```

**Returns**: `1`

```sql
SELECT
	POSITION('world' IN 'hello world') AS res;
```

**Returns**: `7`

```sql
SELECT
	POSITION('work' IN 'hello world') AS res;
```

**Returns**: `0`
