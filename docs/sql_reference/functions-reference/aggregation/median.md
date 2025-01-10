---
layout: default
title: MEDIAN
description: Reference material for MEDIAN
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Aggregation functions
published: true
---

# MEDIAN

Returns the middle value in a given column. If number of values are even, `MEDIAN` returns the average of the two middle values.


## Syntax

{: .no_toc}

```sql
MEDIAN(<value>)
```

## Parameters

{: .no_toc}

| Parameter | Description                                       | Supported input types                       |
|:----------|:--------------------------------------------------|:--------------------------------------------|
| `<value>` | The expression used to calculate the median value. | `DOUBLE PRECISION`, `REAL`, `BIGINT`, `INT` |


## Return Type

`MEDIAN` returns a value of type `DOUBLE PRECISION`.


* This function ignores `NULL` values.
* If the input is empty, the function returns `NULL`.

## Examples

{: .no_toc}
{% include sql_examples/median.md %}
