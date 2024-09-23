---
layout: default
title: VECTOR_COSINE_SIMILARITY
description: Reference material for VECTOR_COSINE_SIMILARITY function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Array functions
---

## VECTOR_COSINE_SIMILARITY

Returns the cosine similarity between two vectors, calculated based on the angle (θ) between them. Vector cosine similarity measures how closely two vectors point in the same direction, and is calculated as `cos(θ)`. `VECTOR_COSINE_SIMILARITY` returns a value in the range `[-1, 1]`. A vector cosine similarity of `1` means that the vectors are identical in direction. A similarity of `0` means that they are orthogonal and have no correlation. A similarity of `-1` means that they point in opposite directions.

## Syntax
{: .no_toc}

```sql
VECTOR_COSINE_SIMILARITY(<array>, <array>)
```
## Parameters 
{: .no_toc}

| Parameter | Description                                              | Supported input types      |
|:----------|:---------------------------------------------------------|:---------------------------|
| `<array>` | The first array used in the similarity calculation  | Any array of [numeric data types](https://docs.firebolt.io/sql_reference/data-types.html#numeric). |
| `<array>` | The second array used in the similarity calculation. | Any array of [numeric data types](https://docs.firebolt.io/sql_reference/data-types.html#numeric). |

## Notes
Both input `array` arguments must have the same number of elements.

## Return Type
`DOUBLE`

## Examples
{: .no_toc}

{% include sql_examples/vector_cosine_similarity.md %}
