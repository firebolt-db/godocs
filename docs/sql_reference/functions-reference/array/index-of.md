---
layout: default
title: INDEX_OF
description: Reference material for INDEX_OF function
grand_parent: SQL functions
parent: Array functions
---

# INDEX\_OF

Returns the index position of the first occurrence of the element in the array (or `0` if not found).

## Syntax
{: .no_toc}

```sql
INDEX_OF(<arr>, <x>)
```

| Parameter | Description                                       |
| :--------- | :------------------------------------------------- |
| `<arr>`   | The array to be analyzed.                         |
| `<x>`     | The element from the array that is to be matched. |

## Return Types
The function includes returned `NUMERIC` types. 

## Example
{: .no_toc}
The following example highlights the index that 5 is in the `levels` array:

```sql
SELECT
	INDEX_OF([ 1, 3, 4, 5, 7 ], 5) AS levels;
```

**Returns**: `4`
