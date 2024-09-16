---
layout: default
title: ARRAY_REVERSE
description: Reference material for ARRAY_REVERSE function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Array functions
---

# ARRAY\_REVERSE

Returns an array of the same size and type as the original array, with the elements in reverse order. Nulls are retained.

## Syntax
{: .no_toc}

```sql
ARRAY_REVERSE(<array>)
```

## Parameters
{: .no_toc}

| Parameter | Description                         |Supported input types |
| :--------- | :----------------------------------- | :---------------------|
| `<array>`   | The array to be reversed | `ARRAY` of any type |

## Return Type
`ARRAY` of the same type as the input array

## Example
{: .no_toc}

{% include sql_examples/array_reverse.md %}

