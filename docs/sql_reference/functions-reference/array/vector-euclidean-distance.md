---
layout: default
title: VECTOR_EUCLIDEAN_DISTANCE
description: Reference material for VECTOR_EUCLIDEAN_DISTANCE function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Array functions
published: true
---

## VECTOR_EUCLIDEAN_DISTANCE

Returns the Euclidean distance, or L2 distance, between two vectors. The Euclidean distance measures the shortest distance between two points in space along a straight line. It is calculated by summing the squared distances of a pair of vector elements, and then taking the square root.

## Syntax
{: .no_toc}

```sql
VECTOR_EUCLIDEAN_DISTANCE(<array>, <array>)
```
## Parameters 
{: .no_toc}

| Parameter | Description                                              | Supported input types      |
|:----------|:---------------------------------------------------------|:---------------------------|
| `<array>` | The first array used in the distance calculation.  | Any array of [numeric data types](../../data-types.md#numeric). |
| `<array>` | The second array used in the distance calculation. | Any array of [numeric data types](../../data-types.md#numeric). |

## Notes
Both input `array` arguments must have the same number of elements.

## Return Type
`DOUBLE`

## Examples
{: .no_toc}

{% include sql_examples/vector_euclidean_distance.md %}