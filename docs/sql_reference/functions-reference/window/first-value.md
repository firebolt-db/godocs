---
layout: default
title: FIRST_VALUE OVER
description: Reference material for FIRST_VALUE function
parent: Window functions
published: false
---

# FIRST_VALUE

Returns the first value evaluated in the specified window frame. If there are no rows in the window frame, returns NULL.

See also [NTH\_VALUE](./nth-value.md), which returns the value evaluated of the nth row (starting at the first row).

## Syntax
{: .no_toc}

```sql
FIRST_VALUE( <expression> ) OVER ( [ PARTITION BY <partition_by> ] ORDER BY <order_by> [ASC|DESC] )
```

## Parameters 
{: .no_toc}

| Parameter | Description                                      | Supported input types | 
| :--------- | :------------------------------------------------ | :------------| 
| `<expression>`   | A SQL expression of any type to evaluate.                                                | Any |
| `<partition_by>` | An expression used for the `PARTITION BY` clause. | Any |
| `<order_by>` | An expression used for the order by clause. | Any |

## Return Types
Same as input type. 

This function respects `NULL` values, and results will be ordered with default null ordering `NULLS LAST` unless otherwise specified in the `ORDER BY` clause. If applied without an `ORDER BY` clause, the order will be undefined.

## Example
{: .no_toc}

The example below returns the highest test score for each grade level. 

```sql
SELECT
  nickname,
  level,
  current_score,
  FIRST_VALUE(test_score) OVER (PARTITION BY level ORDER BY current_score DESC) highest_score
FROM
    players;
```

**Returns**:



| nickname | level | current_score | highest_score |
|:---------|:----------|:-----------|:----------|
| kennethpark   |           9 |         90 |            90 |  
| sabrina21      |           9 |         85 |            90 | 
| rileyjon      |           9 |         80 |            90 |
| burchdenise       |           9 |         79 |            90 |
| ymatthews       |           9 |         78 |            90 |
| sanderserin      |           9 |         76 |            90 |


Note that you will get the same results using the [NTH_VALUE](./nth-value.md) function with n=1

```sql
SELECT
    nickname,
    level,
    current_score,
    NTH_VALUE(current_score, 1) OVER (PARTITION BY level ORDER BY current_score DESC) highest_score
FROM
    players;
```
