---
layout: default
title: ROW_NUMBER OVER
description: Reference material for ROW_NUMBER function
grand_parent: SQL functions
parent: Window functions
great_grand_parent: SQL reference
published: false
---

# ROW\_NUMBER

Returns a unique row number for each row within the requested window.

For more information on usage, please refer to [Window Functions](./index.md).

## Syntax
{: .no_toc}

```sql
ROW_NUMBER() OVER ([PARTITION BY <partition_by>] ORDER BY <order_by> [ASC|DESC] )
```

## Parameters 
{: .no_toc}

| Parameter | Description                                      |Supported input types | 
| :--------- | :------------------------------------------------ | :------------| 
| `<partition_by>`   | The expression used for the `PARTITION BY` clause.                                                                | Any |
| `<order_by>`   | The expression used in the `ORDER BY` clause. This parameter determines what value will be used for `ROW_NUMBER`. | Any |

## Return Type
`INTEGER`

## Example
{: .no_toc}

In this example below, players in each game level are assigned a player ID.

```sql
SELECT
	nickname,
	level,
	ROW_NUMBER() OVER (PARTITION BY level ORDER BY level ASC ) AS player_id
FROM
	players;
```

**Returns**:

| nickname | level | player_id |
|:-----------|:------------|:-----------|
| ymatthews      |           9 |          1 |
| rileyjon  |          12 |          2 |
| sabrina21      |          11 |          3 |
| burchdenise      |          10 |          4 |

