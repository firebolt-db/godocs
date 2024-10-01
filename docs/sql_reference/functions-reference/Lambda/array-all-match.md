---
layout: default
title: ARRAY_ALL_MATCH
description: Reference material for ARRAY_ALL_MATCH function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Lambda functions
published: true
---

# ARRAY_ALL_MATCH

- Returns `TRUE` if all elements in the array are `TRUE` or if the array is empty.
- Returns `FALSE` if any element in the array is `FALSE`.
- Returns `NULL` if any element is `NULL` and no element is `FALSE`.


When an optional lambda function is provided, `ARRAY_ALL_MATCH` applies the function to each element and then evaluates the resulting array.

**Alias:** `ALL_MATCH`


## Syntax
{: .no_toc}

```sql
{ ALL_MATCH | ARRAY_ALL_MATCH }([<expression> -> <condition>], <array> [, <array2>, ...])
```

## Parameters
{: .no_toc}

| Parameter      | Description                                   | Supported input types | 
| :------------- |:--------------------------------------------- | :-----------| 
| `<expression>`  | A lambda function applied to each element of the input arrays, returning a `BOOLEAN`. If no lambda function is provided, the function can only evaluate a single `BOOLEAN` array. For more information, see [Manipulating arrays with Lambda functions](../../../Guides/working-with-semi-structured-data/working-with-arrays.md#manipulating-arrays-with-lambda-functions). | Same as the element data types of the input arrays. |
| `<condition>` | A `BOOLEAN` expression that evaluates each array value using a comparison operator. | See [Comparison operators](../../operators.md#comparison). |
| `<array>` | The array to evaluate. | `ARRAY` |

## Return Type
The `ARRAY_ALL_MATCH` function returns a result of type `BOOLEAN`.

## Examples
{: .no_toc}

{% include sql_examples/array-all-match.md %}
