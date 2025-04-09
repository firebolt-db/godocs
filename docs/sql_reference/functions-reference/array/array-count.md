---
redirect_from:
  - /sql-reference/functions-reference/array-count-global.html
  - /sql-reference/functions-reference/array-count.html
layout: default
title: ARRAY_COUNT
description: Reference material for ARRAY_COUNT function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Array functions
---


# ARRAY\_COUNT
Counts the number of elements in an array where `function(array[i])` evaluates to `TRUE`, if `<function>` is provided.
If `<function>` is not provided, `ARRAY_COUNT` counts the elements that evaluate to `TRUE`, by default. This is equivalent to using a `<function>` defined as `x -> x`.

To count all elements in an array without any conditions, use [ARRAY_LENGTH](../array/array-length.md) instead.

## Syntax
{: .no_toc}

```sql
ARRAY_COUNT(<array>, <function>)
```
## Parameters
{: .no_toc}

| Parameter | Description         | Supported input types |
| :--------- | :-------------------------------------------- | :--------|
| `<function>`  | Optional. A [Lambda function]({% link Guides/loading-data/working-with-semi-structured-data/working-with-arrays.md %}#lambda-function-general-syntax) used to check elements in the array. If `<function>` is not provided, `x -> x` is used. | Any Lambda function returning `BOOLEAN` |
| `<array>`   | An array of elements | Any `ARRAY` type if `<function>` is provided, else `ARRAY(BOOLEAN)`  |

## Return Type
Returns an `INTEGER` value.

## Examples
{: .no_toc}

{% include sql_examples/array_count.md %}

