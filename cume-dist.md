---
layout: default
title: CUME_DIST OVER
description: Reference material for CUME_DIST window function
parent: Window functions
published: false
---

# CUME_DIST

Calculates the relative rank (cumulative distribution) of the current row in relation to other rows in the same partition within an ordered data set, as 
`( rank + number_of_peers - 1 ) / ( total_rows )`
where rank is the current row's rank within the partition, number_of_peers is the number of row values equal to the current row value (including the current row), and total_rows is the total number of rows in the partition.
The return value ranges from 1/(total_rows) to 1.

See also [PERCENT_RANK](./percent-rank.md), which returns the relative rank of the current row within an ordered data set. For more information on usage, please refer to [Window Functions](./index.md).

## Syntax
{: .no_toc}
```sql
CUME_DIST() OVER ( [ PARTITION BY <partition_by> ] ORDER BY <order_by> [ASC|DESC] )
```

## Parameters 
{: .no_toc}

| Parameter | Description                                      | Supported input types | 
| :--------- | :------------------------------------------------ | :------------| 
| `<partition_by>`    | The expression used for the `PARTITION BY` clause.                                                | Any |
| `<order_by>`    | The expression used in the `ORDER BY` clause. This parameter determines what value will be ranked.  | Any |

## Return Type
`DOUBLE PRECISION`

This function respects `NULL` values, and results will be ordered with default null ordering `NULLS LAST` unless otherwise specified in the `ORDER BY` clause.

## Example
{: .no_toc}

The example below returns the cumulative distribution of player IDs for people in North America: 

```sql
SELECT
	nickname, playerid,
	CUME_DIST() OVER (PARTITION BY playerid ORDER BY playerid DESC) as cume_dist
FROM
	class_test
WHERE location="North America";
```

**Returns**:

| nickname | playerid |      cume_dist      |
|:+------------+------------+---------------------+
| kennethpark   |         90 | 0.16666666666666666 |
| sabrina21      |         85 |  0.3333333333333333 |
| rileyjon      |         80 |                 0.5 |
| burchdenise       |         79 |  0.6666666666666666 |

