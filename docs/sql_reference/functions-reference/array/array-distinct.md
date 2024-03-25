---
layout: default
title: ARRAY_DISTINCT
description: Reference material for ARRAY_DISTINCT function
grand_parent: SQL functions
parent: Array functions
great_grand_parent: SQL reference
---

# ARRAY\_DISTINCT

Returns an array containing only the _unique_ elements of the given array. If the given array contains multiple identical members, the returned array will include only a single member of that value. NULL is considered a value like any other, meaning that if the array contains one or more NULLs, the returned array will contain NULL.

## Syntax
{: .no_toc}

```sql
ARRAY_DISTINCT(<array>)
```
## Parameters
{: .no_toc}

| Parameter  | Description                  | Supported input types
| :--------- | :--------------------------- | :----------|
| `<array>`  | The array to be deduplicated | `ARRAY` |

## Return Type
`ARRAY` of the same type as the input array

## Example
{: .no_toc}
In the following example, the unique levels of the game are returned in an array called `levels`:

```sql
SELECT
	ARRAY_DISTINCT([ 1, 1, 2, 2, 3, 4, 1, NULL, 2, NULL ]) AS levels;
```

**Returns**: `[1,2,3,4,NULL]`
