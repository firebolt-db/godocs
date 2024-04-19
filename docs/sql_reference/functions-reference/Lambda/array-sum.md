---
layout: default
title: ARRAY_SUM
description: Reference material for ARRAY_SUM function
grand_parent: SQL functions
parent: Lambda functions
great_grand_parent: SQL reference
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
Element type of `<array>` (but `BIGINT` if the input is `INT`, and `DOUBLE` if the input is `REAL`)

## Example
{: .no_toc}

```sql
SELECT
	ARRAY_SUM([ 4, 1, 3, 2 ]) AS levels;
```

**Returns**: `10`