---
layout: default
title: SLICE
description: Reference material for SLICE function
grand_parent: SQL functions
parent: Array functions
---

# SLICE

Returns a slice of the array based on the indicated offset and length.

## Syntax
{: .no_toc}

```sql
SLICE(<arr>, <offset>[, <length>])
```

| Parameter  | Description                                                                                                                                                        |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `<arr>`    | The array of data to be sliced. Array elements set to `NULL` are handled as normal values. The numbering of the array items begins with `1`.                       |
| `<offset>` | Indicates starting point of the array slice. A positive value indicates an offset on the left, and a negative value is an indent on the right.                     |
| `<length>` | The length of the required slice.<br>If you omit this value, the function returns the slice from the `<offset>` to the end of the array. |

## Return Types
The return types for this function includes `CHAR`, `NUMERIC`, `REAL`, and `DOUBLE PRECISION`. 

## Example
{: .no_toc}

The following example slices the `levels` array to a different length: 
```sql
SELECT
	SLICE([ 1, 2, 3, 4, 5 ], 1, 3) AS levels;
```

**Returns**: `[1, 2, 3]`
