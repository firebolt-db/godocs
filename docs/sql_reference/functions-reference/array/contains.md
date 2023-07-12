---
layout: default
title: CONTAINS
description: Reference material for CONTAINS function
grand_parent: SQL functions
parent: Array functions
---

# CONTAINS

Returns `1` if a specified argument is present in the array, or `0` otherwise.

## Syntax
{: .no_toc}

```sql
CONTAINS(<arr>, <arg>)
```

| Parameter | Description                                      |
| :--------- | :------------------------------------------------ |
| `<arr>`   | The array to be checked for the given element.   |
| `<arg>`   | The element to be searched for within the array. |

## Return Types
The function includes returned `NUMERIC` types. 

## Example
{: .no_toc}

```sql
SELECT
	CONTAINS([ 'sabrina21', 'rileyjon', 'ywilson', 'danielle53'], 'danielle53') AS players;
```

**Returns**: `1`
`1` is returned as "danielle53" is part of the `players` array.

`CONTAINS` returns a `0` result when single character or substring matches only part of a longer string.

```
SELECT
	CONTAINS([ 'sabrina21', 'rileyjon', 'ywilson'] , 'danielle53') AS players;
```

**Returns**: `0`

`0` is returned as "danielle53" is not part of the `players` array.
