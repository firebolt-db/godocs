---
layout: default
title: ARRAY_TO_STRING
description: Reference material for ARRAY_TO_STRING function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Array functions
---

# ARRAY\_TO\_STRING

Converts each array element to its text representation, and concatenates those using an optional delimiter. If no delimiter is provided, an empty string is used instead. `NULL` array elements are omitted.

**Alias:** `ARRAY_JOIN`

## Syntax
{: .no_toc}

```sql
ARRAY_TO_STRING(<array>[, <delimiter>])
```

## Parameters 
{: .no_toc} 

| Parameter     | Description                            | Supported input types | 
| :------------- | :------------------------------------ |:---------|
| `<array>`       | An array to be concatenated | `ARRAY` |
| `<delimiter>` | The delimiter used for concatenating the array elements | `TEXT` | 

## Return Type
`TEXT`

## Example
{: .no_toc}

{% include sql_examples/array_to_string.md %}
