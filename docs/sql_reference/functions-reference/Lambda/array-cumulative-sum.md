---
layout: default
title: ARRAY_CUMULATIVE_SUM
description: Reference material for ARRAY_CUMULATIVE_SUM function ( cumulative )
grand_parent: SQL functions
parent: Lambda functions
great_grand_parent: SQL reference
---

# ARRAY\_CUMULATIVE\_SUM

Returns an array of partial sums of elements from the source array (a cumulative sum). If the argument `<function>` is provided, the values of the array elements are converted by this function before summing.

## Syntax
{: .no_toc}

```sql
ARRAY_CUMULATIVE_SUM( [<function>,] array)
```

| Parameter | Description                                     | Supported input types 
| :--------- | :----------------------------------------------- | :------|
| `<function>`  | The function used to convert the array members. | Any function that can convert an array |  
| `<array>`   | The array used for the sum calculations.        | Any array of numeric values

## Example
{: .no_toc}

The following example adds `1` to each level in the `levels` array: 
```sql
SELECT
	ARRAY_CUMULATIVE_SUM(x -> x + 1, [ 1, 2, 3, 9 ]) AS levels;
```

**Returns**: `2,5,9,19`

<!-- ```sql
SELECT
	ARRAY_CUMULATIVE_SUM([ 1, 2, 3, 9 ]) AS levels;
```

**Returns**: `1,3,6,15` -->
