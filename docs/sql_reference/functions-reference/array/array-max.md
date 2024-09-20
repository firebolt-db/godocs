---
layout: default
title: ARRAY_MAX
description: Reference material for ARRAY_MAX function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Array functions
---

# ARRAY\_MAX

Returns the maximum element in an array. If the input array is empty or contains only `NULL` values, `ARRAY_MAX` will return `NULL`.


## Syntax
{: .no_toc}

```sql
ARRAY_MAX(<array>)
```

## Parameters
{: .no_toc}

| Parameter | Description                         |Supported input types |
| :--------- | :----------------------------------- | :---------------------|
| `<array>`   | The array or array-type column to evaluate, containing comparable elements. | Any type of [ARRAY](https://docs.firebolt.io/sql_reference/data-types.html#array). | 

## Return Type

Returns an element of the same data type as the input array, or `NULL` if the array is empty or contains only `NULL` values.

## Examples
{: .no_toc}

{% include sql_examples/array_max.md %}

