---
layout: default
title: ARRAY_SUM
description: Reference material for ARRAY_SUM function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Array functions
---

# ARRAY\_SUM

Returns the sum of elements in `<array>`.

## Syntax
{: .no_toc}

```sql
ARRAY_SUM(<array>)
```
## Parameters
{: .no_toc} 

| Parameter | Description | Supported input types | 
| :--------- | :-------------------------------- |
| `<array>`   | The array to be summed.     | Any array containing elements with a [numeric](https://docs.firebolt.io/sql_reference/data-types.html#numeric) data type. | 

## Return Type 
Returns `BIGINT` if the array elements are `INTEGER`, `DOUBLE PRECISION`, if they are `REAL`, or the same type as the array elements for other numeric data types.

## Examples
{: .no_toc}

{% include sql_examples/array_sum.md %}

