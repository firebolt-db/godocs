---
layout: default
title: ARRAY_REVERSE_SORT
description: Reference material for ARRAY_REVERSE_SORT function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Array functions
---

# ARRAY\_REVERSE\_SORT

Returns the elements of the input array sorted in descending order.

If a `<function>` is provided, the elements are sorted based on the results of applying the `<function>` to each element.

## Syntax
{: .no_toc}

```sql
ARRAY_REVERSE_SORT([<function>], <array>)
```
## Parameters
{: .no_toc} 

| Parameter | Description                                                  | Supported input type | 
| :--------- | :------------------------------------------------------------ |:------|
| `<function>`  | (Optional) A function used to determine the sorting order. It must return a value that can be used for sorting.| Any Lambda function that accepts the elements of `<array>` as input. | 
| `<array>`   | The array to be sorted.                                      | Any type of [ARRAY](https://docs.firebolt.io/sql_reference/data-types.html#array). | 

## Return Type 
Returns an `ARRAY` of the same type as the input array.


## Examples
{: .no_toc}

{% include sql_examples/array_reverse_sort.md %}

