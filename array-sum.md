---
layout: default
title: ARRAY_SUM
description: Reference material for ARRAY_SUM function
parent: Array functions
---

# ARRAY\_SUM

Returns the sum of elements of `<array>`.

## Syntax
{: .no_toc}

```sql
ARRAY_SUM(<array>)
```
## Parameters
{: .no_toc} 

| Parameter | Description | Supported input types | 
| :--------- | :-------------------------------- |
| `<array>`   | The array to be used to calculate the function.     | Any array of numeric types | 

## Return Type 
The return type is `BIGINT` if the element type of `<array>` is `INT` and `DOUBLE PRECISION` if the element type is `REAL`. Otherwise, it matches the element type.

## Example
{: .no_toc}

```sql
SELECT
	ARRAY_SUM([ 4, 1, 3, 2 ]) AS levels;
```

**Returns**: `10`