---
redirect_from:
  - /sql-reference/functions-reference/array-enumerate.html
layout: default
title: ARRAY_ENUMERATE
description: Reference material for ARRAY_ENUMERATE function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Numeric functions
---

# ARRAY\_ENUMERATE

This function takes an array of arbitrary type as input, and produces an integer array of the same length containing increasing numbers.
The returned array starts with value one. Every successive element is incremented by one, it holds that `array[i] = array[i - 1] + 1`.

`NULLs` contained in the parameter array are treated like any other value, and result in a non-null element in the returned array.

If the parameter array is `NULL`, then the function also returns `NULL`.


## Syntax
{: .no_toc}

```sql
ARRAY_ENUMERATE(<array>)
```

## Parameters
{: .no_toc}

| Parameter | Description       | Supported input types | 
| :--------- | :------------------------ | :---------| 
| `<array>`  | The array to be enumerated. The length of the returned array is the same as the length of the parameter array. | Any array type. | 

## Return Type
{: .no_toc}

`ARRAY(INT)`

## Example 
{: .no_toc}

{% include sql_examples/array_enumerate_executable.md %}
