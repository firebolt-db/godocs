---
redirect_from:
  - /sql-reference/functions-reference/array-to-string.html
layout: default
title: ARRAY_TO_STRING
description: Reference material for ARRAY_TO_STRING function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Array functions
---

# ARRAY\_TO\_STRING

Converts the elements of an array to text and joins them into a single string, separated by an optional delimiter. If no delimiter is provided, the elements are concatenated without spaces. `NULL` elements are skipped during concatenation, and do not appear in the result.

**Alias:** `ARRAY_JOIN`

## Syntax
{: .no_toc}

```sql
ARRAY_TO_STRING(<array>, [<delimiter>])
```

## Parameters 
{: .no_toc} 

| Parameter     | Description                            | Supported input types | 
| :------------- | :------------------------------------ |:---------|
| `<array>`       | The array whose elements will be converted to text and concatenated. | Any type of [ARRAY](https://docs.firebolt.io/sql_reference/data-types.html#array) that contains elements that can be converted to text. |
| `<delimiter>` | The delimiter used to concatenate the elements of `<array>`. | `TEXT` | 

## Return Type
Returns `TEXT` that contains the concatenated elements of the array.

## Example
{: .no_toc}

{% include sql_examples/array_to_string.md %}
