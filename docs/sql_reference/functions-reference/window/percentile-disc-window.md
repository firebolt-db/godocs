---
layout: default
title: PERCENTILE_DISC OVER
description: Reference material for PERCENTILE_DISC window function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Window functions
published: false
---

# PERCENTILE\_DISC

Returns a percentile over a partition for an ordered data set. The result is equal to a specific column value, the smallest distributed value that is greater than or equal to the percentile specified. 

PERCENTILE\_DISC is available as a Window function. See also [PERCENTILE\_CONT](../window/percentile-cont-window.md), which calculates an interpolated result over a partition, rather than matching any of the specific column values. For more information on usage, please refer to [Window Functions](./index.md).

## Syntax
{: .no_toc}

```sql
PERCENTILE_DISC( <value> ) WITHIN GROUP ( ORDER BY <order_by> [ { ASC | DESC } ] ) [ OVER ( PARTITION BY <partition_by> ) ]
```

## Parameters 
{: .no_toc}

| Parameter | Description                                      |Supported input types | 
| :--------- | :------------------------------------------------ | :------------| 
| `<value>`   | A value between 0.0 and 1.0.  | `DOUBLE PRECISION`, `REAL` |
| `<order_by>` | An expression used for the order by clause. | Any numeric type |
| `<partition_by>` | An expression used for the partition by clause. | Any |

## Return Types
Same as the order by expression type.

This function ignores `NULL` values.


## Example
{: .no_toc}

The example below returns the 70th percentile value per student, partitioned by the game level. The percentile value returned is a value from the data set. 

```sql
SELECT
	first_name,
	PERCENTILE_DISC(0.7) WITHIN GROUP (ORDER BY current_score) OVER (PARTITION BY level) AS percentile
FROM
	players;
```

**Returns**:

| nickname | percentile | 
|:-----|:-------|
| kennethpark | 90 | 
| sabrina21 | 85 | 
| ymatthews | 80 | 
| rileyjon | 75 | 
