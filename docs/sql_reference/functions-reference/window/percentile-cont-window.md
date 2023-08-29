---
layout: default
title: PERCENTILE_CONT OVER
description: Reference material for PERCENTILE_CONT window function
grand_parent: SQL functions
parent: Window functions
great_grand_parent: SQL reference
---

# PERCENTILE_CONT

Calculates a percentile over a partition, assuming a continuous distribution of values of <expr0> defined. Results are interpolated, rather than matching any of the specific column values. 

PERCENTILE\_CONT is available as an [aggregation function](../aggregation/index.md).
See also [PERCENTILE\_DISC](./percentile-disc-window.md), which returns a percentile over a partition equal to a specific column value. For more information on usage, please refer to [Window Functions](./window-functions.md).

## Syntax
{: .no_toc}

```sql
PERCENTILE_CONT( <value> ) WITHIN GROUP ( ORDER BY <order_by> [ { ASC | DESC } ] ) [ OVER ( PARTITION BY <partition_by> ) ]
```

## Parameters 
{: .no_toc}

| Parameter | Description                                      |Supported input types | 
| :--------- | :------------------------------------------------ | :------------| 
| `<value>`   | A value between 0.0 and 1.0.  | `DOUBLE PRECISION`, `REAL` |
| `<order_by>` | An expression used for the order by clause. | Any numeric type |
| `<partition_by>` | An expression used for the partition by clause. | Any |

## Return Types
Same as input type. 

## Example
{: .no_toc}

The example below calculates the max percentile value based on continuous distribution of students, partitioned by grade level. 

```sql
SELECT
	first_name,
	PERCENTILE_CONT(1.0) WITHIN GROUP (ORDER BY test_score) OVER (PARTITION BY grade_level) AS percentile
FROM
	class_test;
```

**Returns**:

```sql
' +-------------+------------+
' | grade_level | percentile | 
' +-------------+------------+
' |       Frank |         90 |
' |       Peter |         90 |
' |        Iris |         90 |
' |    Humphrey |         90 |
' |        Jojo |         90 |
' |       Sammy |         90 |
' |      Albert |         89 |
' |     Deborah |         89 |
' |     Yolinda |         89 |
' |        Mary |         89 |
' |       Shawn |         89 |
' |        Otis |         94 |
' |       Larry |         94 |
' |       Carol |         94 |
' |       Wanda |         94 |
' |    Roseanna |         94 |
' |    Shangxiu |         94 |
' |      Franco |        100 |
' |     Charles |        100 |
' |   Brunhilda |        100 |
' |        Gary |        100 |
' |      Thomas |        100 |
' |       Jesse |        100 |
' +-------------+------------+
```
