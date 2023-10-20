---
layout: default
title: PERCENTILE_CONT OVER
description: Reference material for PERCENTILE_CONT window function
grand_parent: SQL functions
parent: Window functions
great_grand_parent: SQL reference
---

# PERCENTILE_CONT

Calculates a percentile over a partition, assuming a continuous distribution of values defined. Results are interpolated, rather than matching any of the specific column values. 

PERCENTILE\_CONT is available as an Window function. See also [PERCENTILE\_DISC](../window/percentile-disc-window.md), which returns a percentile over a partition equal to a specific column value. For more information on usage, please refer to [Window Functions](../window/index.md).

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
`DOUBLE PRECISION`

## Example
{: .no_toc}

The example below calculates the max percentile value based on continuous distribution of players, partitioned by game level. 

```sql
SELECT
	nickname,
	PERCENTILE_CONT(1.0) WITHIN GROUP (ORDER BY current_score) OVER (PARTITION BY leve;) AS percentile
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

