---
layout: default
title: ARRAY_ANY_MATCH
description: Reference material for ARRAY_ANY_MATCH function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Lambda functions
---


# ARRAY\_ANY\_MATCH

- Returns `TRUE` if any element in the array is `TRUE`.
- Returns `FALSE` if all elements in the array are `FALSE` or if the array is empty.
- Returns `NULL` if any element is `NULL` and no element is `TRUE`.


When an optional lambda function is provided, `ARRAY_ANY_MATCH` applies the function to each element and then evaluates the resulting arrayt.


**Alias:** `ANY_MATCH`


## Syntax
{: .no_toc}

```sql
{ ANY_MATCH | ARRAY_ANY_MATCH }([<expression> -> <condition>], <array> [, <array2>, ...])
```
## Parameters
{: .no_toc} 

 Parameter      | Description                                   | Supported input types | 
| :------------- |:--------------------------------------------- | :-----------| 
| `<expression>`  | A lambda function applied to each element of the input arrays, returning a `BOOLEAN`. If no lambda function is provided, the function can only evaluate a single `BOOLEAN` array. For more information, see [Manipulating arrays with Lambda functions](../../../Guides/working-with-semi-structured-data/working-with-arrays.md#manipulating-arrays-with-lambda-functions). | Same as the element data types of the input arrays. |
| `<condition>` | A `BOOLEAN` expression that evaluates each array value using a comparison operator. | See [Comparison operators](../../operators.md#comparison). |
| `<array>` | The array to evaluate. | `ARRAY` |

## Return Types
The `ARRAY_ANY_MATCH` function returns a result of type `BOOLEAN`.

## Examples
{: .no_toc}

{% include sql_examples/array-any-match.md %}

