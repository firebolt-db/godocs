---
redirect_from:
  - /sql-reference/functions-reference/array-reverse.html
layout: default
title: ARRAY_REVERSE
description: Reference material for ARRAY_REVERSE function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Array functions
---

# ARRAY\_REVERSE

Returns an array of the same size and type as the original input array, with its elements reversed, and `NULL` values remain in their original positions.

## Syntax
{: .no_toc}

```sql
ARRAY_REVERSE(<array>)
```

## Parameters
{: .no_toc}

| Parameter | Description                         |Supported input types |
| :--------- | :----------------------------------- | :---------------------|
| `<array>`   | Any type of [ARRAY](https://docs.firebolt.io/sql_reference/data-types.html#array). |

## Return Type
Returns an `ARRAY` of the same type as the input array.

## Examples
{: .no_toc}

{% include sql_examples/array_reverse.md %}

