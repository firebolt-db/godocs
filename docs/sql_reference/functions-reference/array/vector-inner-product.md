---
layout: default
title: VECTOR_INNER_PRODUCT
description: Reference material for VECTOR_INNER_PRODUCT function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Array functions
published: true
---

## VECTOR_INNER_PRODUCT

Returns the inner product, also known as the dot or scalar product, between two vectors. The inner product measures how closely two vectors align with each other, both in magnitude and the cosine of the angle between them. It is calculated by multiplying the corresponding elements of the vectors and then summing the results. 

If the vectors have similar directions and large magnitudes, the inner product has a large positive value. If they are orthogonal, the inner product is zero, regardless of magnitude. If they point in roughly opposite directions, and at least one has a small magnitude, the inner product is small and negative.

## Syntax
{: .no_toc}

```sql
VECTOR_INNER_PRODUCT(<array>, <array>)
```
## Parameters 
{: .no_toc}

| Parameter | Description                                           | Supported input types      |
|:----------|:------------------------------------------------------|:---------------------------|
| `<array>` | The first array used in the inner product calculation.  | Any array of [numeric data types](https://docs.firebolt.io/sql_reference/data-types.html#numeric). |
| `<array>` | The second array used in the inner product calculation. | Any array of [numeric data types](https://docs.firebolt.io/sql_reference/data-types.html#numeric). |

## Notes
Both input `array` arguments must have the same number of elements.

## Return Type
`DOUBLE`

## Examples
{: .no_toc}

{% include sql_examples/vector_inner_product.md %}