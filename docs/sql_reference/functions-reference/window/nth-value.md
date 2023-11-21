---
layout: default
title: NTH_VALUE OVER
description: Reference material for NTH_VALUE function
grand_parent: SQL functions
parent: Window functions
great_grand_parent: SQL reference
---

# NTH_VALUE

Returns the value evaluated of the nth row of the specified window frame (starting at the first row). If the specified row does not exist, NTH_VALUE returns NULL.

See also [FIRST\_VALUE](./first-value.md), which returns the first value evaluated in the specified window frame. For more information on usage, please refer to [Window Functions](./index.md).

## Syntax
{: .no_toc}

```sql
NTH_VALUE( <expression>, <n> ) OVER ( [ PARTITION BY <partition_by> ] ORDER BY <order_by> [ASC|DESC] )
```

## Parameters 
{: .no_toc}

| Parameter | Description                                      | Supported input types | 
| :--------- | :------------------------------------------------ | :------------| 
| `<expression>`   | A SQL expression of any type to evaluate.                                                | Any |
| `<n>`     | A constant integer in range [1, max of datatype `INTEGER`] to indicate the row number to evaluate. | `INTEGER` |
| `<partition_by>` | An expression used for the PARTITION clause. | Any |
| `<order_by>` | An expression used for the order by clause. | Any |

## Return Types
Same as input type. 

This function respects `NULL` values, and results will be ordered with default null ordering `NULLS LAST` unless otherwise specified in the `ORDER BY` clause. If applied without an `ORDER BY` clause, the order will be undefined.

## Example
{: .no_toc}

The example below returns the student with the second highest test score for each grade level. Notice that the function returns `NULL` for the first row in each partition, unless the value of the expression for first and second rows of the partition are equal. 

```sql
SELECT
    nickname,
    level,
    current_score,
    NTH_VALUE(first_name, 2) OVER (PARTITION BY level ORDER BY current_score DESC) second_highest_score
FROM
    players;
```

**Returns**:

| nickname | level | current_score | second_highest_score |
|:------------|:-------------|:------------|:------------------|
| ymatthews      |           9 |         85 |                Sammy |
| rileyjon      |          10 |         89 |                 null |
| kennethpark   |          11 |         94 |                 null |
| sabrina21    |          12 |        100 |              burchdenise |
