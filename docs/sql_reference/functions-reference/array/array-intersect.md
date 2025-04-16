---
layout: default
title: ARRAY_INTERSECT
description: Reference material for ARRAY_INTERSECT function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Array functions
---

# ARRAY\_INTERSECT

Finds the intersection of the provided argument arrays. Used for finding the common elements between arrays. 

Returns an array containing all the elements that are present in every argument array. It uses set semantics, which means the result cannot contain multiple copies of the same value. The order of elements in the result may be different than in the original arrays; use [ARRAY_SORT](../array/array-sort.md) to stipulate a specific order on the results.

This function is NULL-safe, because it treats `NULL` values _within_ arrays as known values, as shown in the following examples.

If any of the input argument arrays are themselves `NULL`, the function returns `NULL`.

## Syntax
{: .no_toc}

```sql
ARRAY_INTERSECT(<array> [, ...n])
```

## Parameters 
{: .no_toc} 

| Parameter        | Description                                                                            | Supported input types |
| :---------------- | :-------------------------------------------------------------------------------------- | :----------|
| `<array> [, ...n]` | The argument arrays whose intersection is to be computed. | `ARRAY`  |

## Return Type
`ARRAY` of the common type of all input arrays.

The common type is the supertype of the provided array types. For example, the supertype between `Array(Int)` and `Array(BigInt)` is `Array(BigInt)`.

## Examples
{: .no_toc}

{% include sql_examples/array_intersect.md %}
