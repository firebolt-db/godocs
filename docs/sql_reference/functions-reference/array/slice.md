---
layout: default
title: SLICE
description: Reference material for SLICE function
grand_parent: SQL functions
parent: Array functions
great_grand_parent: SQL reference
---

# SLICE

Returns a slice of the array based on the indicated offset and length.

## Syntax
{: .no_toc}

```sql
SLICE(<array>, <value1>[, <value2>])
```

| Parameter  | Description                            | Supported input types | 
| :---------- | :------------------------------------ | :-------- | 
| `<array>`    | The array of data to be sliced               | `ARRAY` of any type | 
| `<value1>` | Indicates starting point of the array slice | `INTEGER` | 
| `<value2>` | The length of the required slice | `INTEGER` | 

## Return Types
`ARRAY` of the same type as inputted array 

## Example
{: .no_toc}

The following example slices the `levels` array to a different length: 
```sql
SELECT
	SLICE([ 1, 2, 3, 4, 5 ], 1, 3) AS levels;
```

**Returns**: `[1, 2, 3]`
