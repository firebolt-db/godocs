---
layout: default
title: VECTOR_MANHATTAN_DISTANCE
description: Reference material for VECTOR_MANHATTAN_DISTANCE function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Array functions
published: true
---

## VECTOR_MANHATTAN_DISTANCE

Returns the Manhattan, or L1 distance, between two vectors. The Manhattan distance measures the total distance by moving strictly along orthogonal axes, similar to navigating streets in a city grid. It is calculated as the sum of absolute differences between corresponding elements of two vectors.

## Syntax
{: .no_toc}

```sql
VECTOR_MANHATTAN_DISTANCE(<array>, <array>)
```
## Parameters 
{: .no_toc}

| Parameter | Description                                              | Supported input types      |
|:----------|:---------------------------------------------------------|:---------------------------|
| `<array>` | The first array used in the distance calculation.  | Any array of [numeric data types](https://docs.firebolt.io/sql_reference/data-types.html#numeric). |
| `<array>` | The second array used in the distance calculation. | Any array of [numeric data types](https://docs.firebolt.io/sql_reference/data-types.html#numeric). |

## Notes
Both input `array` arguments must have the same number of elements.

## Return Type
`DOUBLE`

## Examples
{: .no_toc}

{% include sql_examples/vector_manhattan_distance.md %}