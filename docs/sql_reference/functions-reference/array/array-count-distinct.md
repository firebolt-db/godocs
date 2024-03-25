---
layout: default
title: ARRAY_COUNT_DISTINCT
description: Reference material for ARRAY_COUNT_DISTINCT function
grand_parent: SQL functions
parent: Array functions
great_grand_parent: SQL reference
---

# ARRAY\_COUNT\_DISTINCT

Returns the number of distinct (unique) elements in the array. As with `COUNT` and `COUNT(DISTINCT ...) aggregations, `NULL` is not counted as a value if it occurs.

## Syntax
{: .no_toc}

```sql
ARRAY_UNIQ(<array>)
```
## Parameters
{: .no_toc}

| Parameter | Description                                        | Supported input types
| :-------- | :------------------------------------------------- | :-------|
| `<array>` | The array of which to count the distinct elements. | Any `ARRAY` type |

## Return Type
`INTEGER`

## Example
{: .no_toc}

```sql
SELECT ARRAY_UNIQ([ 1, 2, 4, 5, 2, NULL, 5, 1 ]) AS res;
```

**Returns**: `4`
