---
layout: default
title: ARRAYS_OVERLAP
description: Reference material for ARRAYS_OVERLAP function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Array functions
---

# ARRAYS\_OVERLAP

Returns whether all input arrays have at least one common, non-`NULL` element.

Note that if the input arrays have only a `NULL` element in common, `ARRAYS_OVERLAP` returns `FALSE`.

Returns `NULL` if any of the inputs is `NULL`.

## Syntax
{: .no_toc}

```sql
ARRAYS_OVERLAP(<array_1>, <array_2>, [, ...n])
```

## Parameters 
{: .no_toc} 

| Parameter        | Description                                                                            | Supported input types |
| :---------------- | :-------------------------------------------------------------------------------------- | :----------|
| `<array_1>, <array_2> [, ...n]` | Two or more arrays to be tested for common elements. | `ARRAY`  |


## Return Type
`BOOLEAN`

## Examples
{: .no_toc}

{% include sql_examples/arrays_overlap.md %}
