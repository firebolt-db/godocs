---
layout: default
title: RANK OVER
description: Reference material for RANK function
grand_parent: SQL functions
parent: Window functions
great_grand_parent: SQL reference
---

# RANK

Rank the current row within the requested window with gaps.

For more information on usage, please refer to [Window Functions](./index.md).

## Syntax
{: .no_toc}

```sql
RANK() OVER ([PARTITION BY <partition_by>] ORDER BY <order_by> [ASC|DESC] )
```

## Parameters 
{: .no_toc}

| Parameter | Description                                      |Supported input types | 
| :--------- | :------------------------------------------------ | :------------| 
| `<partition_by>`   | The expression used for the `PARTITION BY` clause.                                                 | Any |
| `<order_by>`   | The expression used in the `ORDER BY` clause. This parameter determines what value will be ranked. | Any |

## Return Type
`INTEGER`

## Example
{: .no_toc}

In this example below, players are ranked based on their test scores for their game level.

```sql
SELECT
	nickname,
	level,
	current_score,
	RANK() OVER (PARTITION BY level ORDER BY current_score DESC ) AS rank_in_level
FROM
	players;
```

**Returns**:

| first_name | level | current_score | rank_in_level |
|:-----------|:------------|:-----------|:--------------|
| kennethpark      |           9 |         76 |             4 |
| burchdenise      |          12 |         89 |             2 |
| ymatthews       |          9 |         76 |             4 |
| sabrina21    |          10 |         78 |             3 |

