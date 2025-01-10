---
layout: default
title: VECTOR_ADD
description: Reference material for VECTOR_ADD function
parent: Vector functions
---

## VECTOR_ADD

Returns an array that is the sum of two input arrays.

## Syntax
{: .no_toc}

```sql
VECTOR_ADD(<array>, <array>)
```

## Parameters
{: .no_toc}

| Parameter | Description                                   | Supported input types                                           |
|:----------|:----------------------------------------------|:----------------------------------------------------------------|
| `<array>` | The first array in the addition calculation.  | Any array of [numeric data types](../../data-types.md#numeric). |
| `<array>` | The second array in the addition calculation. | Any array of [numeric data types](../../data-types.md#numeric). |

## Notes
Both input `ARRAY` arguments must have the same number of elements.

## Return Type
`VECTOR_ADD` returns a result of type `ARRAY(BIGINT)` if the elements of `<array>` are of type `INT`, and returns a result of type `ARRAY(DOUBLE PRECISION)` if the elements are of type `REAL`. For other element types, `VECTOR_ADD` returns a result that matches the original element type, or follows Firebolt's [type conversion](../../data-types.html#type-conversion) rules to convert them to compatible data types.

## Examples
{: .no_toc}

{% include sql_examples/vector_add.md %}
