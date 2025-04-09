---
redirect_from:
  - /sql-reference/functions-reference/array-uniq.html
  - /sql-reference/functions-reference/array-distinct.html
layout: default
title: ARRAY_DISTINCT
description: Reference material for ARRAY_DISTINCT function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Array functions
---

# ARRAY\_DISTINCT

Returns an array containing only the _unique_ elements of the given array. If the given array contains duplicate values, the result will include just one instance of each. `NULL` is treated as a regular value, meaning that if the array contains one or more `NULL` values, the result will include a single `NULL` value.

## Syntax
{: .no_toc}

```sql
ARRAY_DISTINCT(<array>)
```
## Parameters
{: .no_toc}

| Parameter  | Description                  | Supported input types
| :--------- | :--------------------------- | :----------|
| `<array>`  | The array from which duplicate elements are removed. | Any type of [ARRAY](https://docs.firebolt.io/sql_reference/data-types.html#array). |

## Return Type
Returns an `ARRAY` of the same type as the input array.

## Examples
{: .no_toc}

{% include sql_examples/array_distinct.md %}

