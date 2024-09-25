---
layout: default
title: VECTOR_COSINE_DISTANCE
description: Reference material for VECTOR_COSINE_DISTANCE function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Array functions
---

## VECTOR_COSINE_DISTANCE

Returns the cosine distance between two vectors, calculated based on the angle (θ) between them. Vector cosine distance emphasizes the directional difference between the vectors, rather than magnitude. It is calculated as `1 - cos(θ)`, where `cos(θ)` is the [cosine similarity](./vector-cosine-similarity) between the vectors. `VECTOR_COSINE_DISTANCE` returns a value in the range `[0, 2]`. A vector cosine distance of `0` means that the vectors are identical in direction. A distance of `1` means that they are orthogonal and have no correlation. A distance of `2` means that they point in opposite directions.

## Syntax
{: .no_toc}

```sql
VECTOR_COSINE_DISTANCE(<array>, <array>)
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

{% include sql_examples/vector_cosine_distance.md %}
