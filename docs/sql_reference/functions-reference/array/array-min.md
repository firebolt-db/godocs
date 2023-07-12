---
layout: default
title: ARRAY_MIN
description: Reference material for ARRAY_MIN function
grand_parent: SQL functions
parent: Array functions
---

# ARRAY\_MIN

Returns the minimum element in `<arr>`.

## Syntax
{: .no_toc}

```sql
ARRAY_MIN(<arr>)
```

| Parameter | Description                                  |
| :--------- | :-------------------------------------------- |
| `<arr>`   | The array or array-type column to be checked |

## Return Types
The function includes returned `NUMERIC` types.  

## Example
{: .no_toc}

The following examples calculates the maximum number in the `levels` array: 
```sql
SELECT
	ARRAY_MIN([ 1, 2, 3, 4 ]) AS levels;
```

**Returns**: `1`
