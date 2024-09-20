---
layout: default
title: ARRAY_COUNT_DISTINCT
description: Reference material for ARRAY_COUNT_DISTINCT function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Array functions
---

# ARRAY\_COUNT\_DISTINCT

Returns the number of unique elements in an array. Similar to `COUNT` and `COUNT(DISTINCT ...)` aggregations, `NULL` values are not included in the count.

## Syntax
{: .no_toc}

```sql
ARRAY_COUNT_DISTINCT(<array>)
```
## Parameters
{: .no_toc}

| Parameter | Description                                        | Supported input types
| :-------- | :------------------------------------------------- | :-------|
| `<array>` | The array from which to count the distinct elements. | Any type of [ARRAY](https://docs.firebolt.io/sql_reference/data-types.html#array). |

## Return Type
Returns an `INTEGER` value.

## Example
{: .no_toc}

{% include sql_examples/array_count_distinct.md %}

