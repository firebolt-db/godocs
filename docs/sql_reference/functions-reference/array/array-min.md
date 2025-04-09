---
redirect_from:
  - /sql-reference/functions-reference/min.html
  - /sql-reference/functions-reference/array-min.html
layout: default
title: ARRAY_MIN
description: Reference material for ARRAY_MIN function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Array functions
---

# ARRAY\_MIN

Returns the minimum element in an array. If the input array is empty or contains only `NULL` values, `ARRAY_MIN` will return `NULL`.

## Syntax
{: .no_toc}

```sql
ARRAY_MIN(<array>)
```

## Parameters 
{: .no_toc}

| Parameter | Description                                  | Supported input types | 
| :--------- | :-------------------------------------------- | :----------|
| `<array>`   | The array or array-type column to evaluate, containing comparable elements. | Any type of [ARRAY](https://docs.firebolt.io/sql_reference/data-types.html#array). | 


## Return Type

Returns an element of the same data type as the input array, or `NULL` if the array is empty or contains only `NULL` values.

## Examples
{: .no_toc}

{% include sql_examples/array_min.md %}

