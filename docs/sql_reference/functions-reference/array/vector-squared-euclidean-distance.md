---
layout: default
title: VECTOR_SQUARED_EUCLIDEAN_DISTANCE
description: Reference material for VECTOR_SQUARED_EUCLIDEAN_DISTANCE function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Array functions
published: true
---

## VECTOR_SQUARED_EUCLIDEAN_DISTANCE

Returns the squared [Euclidean distance](./vector-euclidean-distance.md), or squared [L2 distance](./vector-euclidean-distance.md) between two vectors. The squared Euclidean distance measures how far apart two vectors based on the size of their differences, without considering direction. By squaring the difference, it emphasizes larger differences, which can help in finding outliers or large deviations.

## Syntax
{: .no_toc}

```sql
VECTOR_SQUARED_EUCLIDEAN_DISTANCE(<array>, <array>)
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

{% include sql_examples/vector_squared_euclidean_distance.md %}
