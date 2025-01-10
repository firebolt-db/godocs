---
layout: default
title: VECTOR_SUBTRACT
description: Reference material for VECTOR_SUBTRACT function
parent: Vector functions
---

## VECTOR_SUBTRACT

Returns an array that is the difference of two input arrays.

## Syntax
{: .no_toc}

```sql
VECTOR_SUBTRACT(<array>, <array>)
```

## Parameters
{: .no_toc}

| Parameter | Description                                        | Supported input types                                           |
|:----------|:---------------------------------------------------|:----------------------------------------------------------------|
| `<array>` | The first array in the difference calculation.  | Any array of [numeric data types](../../data-types.md#numeric). |
| `<array>` | The second array in the difference calculation. | Any array of [numeric data types](../../data-types.md#numeric). |

## Notes
Both input `array` arguments must have the same number of elements.

## Return Type
`VECTOR_SUBTRACT` returns a result of type `ARRAY(BIGINT)` if the elements of `<array>` are of type `INT`, and returns a result of type `ARRAY(DOUBLE PRECISION)` if the elements are of type `REAL`. For other element types, `VECTOR_ADD` returns a result that matches the original element type, or follows Firebolt's [type conversion](../../data-types.html#type-conversion) rules to convert them to compatible data types.

## Examples
{: .no_toc}

{% include sql_examples/vector_subtract.md %}
