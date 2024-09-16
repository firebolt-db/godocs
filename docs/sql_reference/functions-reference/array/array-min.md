---
layout: default
title: ARRAY_MIN
description: Reference material for ARRAY_MIN function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Array functions
---

# ARRAY\_MIN

Returns the minimum element in an array.

## Syntax
{: .no_toc}

```sql
ARRAY_MIN(<array>)
```

## Parameters 
{: .no_toc}

| Parameter | Description                                  | Supported input types | 
| :--------- | :-------------------------------------------- | :----------|
| `<array>`   | The array or array-type column to be checked | `ARRAY` | 


## Return Type

Same as the element type of the array.

## Example
{: .no_toc}

{% include sql_examples/array_min.md %}

