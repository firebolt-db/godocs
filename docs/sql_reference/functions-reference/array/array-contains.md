---
redirect_from:
  - /sql-reference/functions-reference/contains.html
layout: default
title: ARRAY_CONTAINS
description: Reference material for ARRAY_CONTAINS function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Array functions
---

# ARRAY_CONTAINS

Returns `TRUE` if a specified argument is present in the array, or `FALSE` otherwise. `ARRAY_CONTAINS` uses `IS NOT DISTINCT FROM` semantics. This means that it treats `NULL` as a valid value, meaning that `NULL` is equal to `NULL`, so `NULL = NULL` returns `TRUE`.

**Alias:** `CONTAINS`

## Syntax
{: .no_toc}

```sql
ARRAY_CONTAINS(<array>, <value>)
```

## Parameters 
{: .no_toc}

| Parameter | Description                                      | Supported input types | 
| :--------- | :------------------------------------------------ | :--------|
| `<array>`   | The array to check for the specified `value`.   | `ARRAY` | 
| `<value>`   | The element to be searched for within the array. | Any type that can be converted to the array's element type. | 

## Return Type

The `BOOLEAN` value `TRUE` if the element to be searched is present in the array, or `FALSE` otherwise.

## Examples
{: .no_toc}

{% include sql_examples/array_contains.md %}
