---
layout: default
title: ARRAY_LENGTH
description: Reference material for ARRAY_LENGTH function
parent: Array functions
---

# ARRAY_LENGTH

Returns the length of the given array, i.e., how many elements it contains. Produces `NULL` for `NULL` arrays.

**Alias:** [LENGTH](../string/length.md) (when used with an array argument)

## Syntax
{: .no_toc}

```sql
ARRAY_LENGTH(<array>)
```

## Parameters
{: .no_toc}

| Parameter  | Description                                 | Supported input types |
| :--------- | :------------------------------------------ | :----------|
| `<array>`  | The array whose length should be calculated | `ARRAY` |

## Return Type
`INTEGER`

## Example
{: .no_toc}

```sql
SELECT
	ARRAY_LENGTH([ 1, 2, 3, 4 ]) AS levels;
```

**Returns**: `4`


```sql
SELECT
	ARRAY_LENGTH([ [ 1, 2, 3 ], [ 4, 5, 6, 7 ]) AS levels;
```

**Returns**: `2`
