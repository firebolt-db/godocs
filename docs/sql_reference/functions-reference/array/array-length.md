---
redirect_from:
  - /sql-reference/functions-reference/length.html
layout: default
title: ARRAY_LENGTH
description: Reference material for ARRAY_LENGTH function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Array functions
---

# ARRAY_LENGTH

Returns the number of elements in the specified array. If the array is `NULL`, `ARRAY_LENGTH` returns `NULL`. For nested arrays, `ARRAY_LENGTH` only counts the elements in the outermost array.

**Alias:** [LENGTH](../string/length.md) (when used with an array argument)

## Syntax
{: .no_toc}

```sql
ARRAY_LENGTH(<array>)
```

## Parameters
{: .no_toc}

| Parameter  | Description                                 | Supported input types |
| :--------- | :------------------------------------------ | :----------|
| `<array>`  | The array for which to calculate the length. | Any type of [ARRAY](https://docs.firebolt.io/sql_reference/data-types.html#array). |

## Return Type
Returns an `INTEGER` value.

## Examples
{: .no_toc}

{% include sql_examples/array_length.md %}
