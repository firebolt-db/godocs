---
redirect_from:
  - /sql-reference/functions-reference/flatten.html
layout: default
title: ARRAY_FLATTEN
description: Reference material for ARRAY_FLATTEN function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Array functions
---

# ARRAY_FLATTEN

Converts an array of arrays into a flat array, meaning it eliminates any nested or multi-dimensional structures. For each array element, `ARRAY_FLATTEN` extracts its individual elements and combines them into a single flattened array that contains all the elements from the source arrays.

The following apply:

* `ARRAY_FLATTEN` flattens only one level of nested arrays.
* `ARRAY_FLATTEN` cannot be applied to arrays that are already flat.

## Syntax
{: .no_toc}

```sql
ARRAY_FLATTEN(<array>)
```

## Parameters
{: .no_toc}

| Parameter | Description                         |Supported input types |
| :--------- | :----------------------------------- | :---------------------|
| `<array>` | The array of arrays to be flattened. | Any type of [ARRAY](https://docs.firebolt.io/sql_reference/data-types.html#array). | 

## Return Type
Returns an `ARRAY` of the same type as the input array.

## Examples
{: .no_toc}

{% include sql_examples/array_flatten.md %}

