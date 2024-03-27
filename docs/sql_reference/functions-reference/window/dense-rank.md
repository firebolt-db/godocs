---
layout: default
title: DENSE_RANK OVER
description: Reference material for DENSE_RANK function
grand_parent: SQL functions
parent: Window functions
great_grand_parent: SQL reference
published: false
---

# DENSE\_RANK

Rank the current row within the requested window.

For more information on usage, please refer to [Window Functions](./index.md).

## Syntax
{: .no_toc}

```sql
DENSE_RANK() OVER ([PARTITION BY <partition_by>] ORDER BY <order_by> [ASC|DESC] )
```

## Parameters 
{: .no_toc}

| Parameter | Description                                      | Supported input types | 
| :--------- | :------------------------------------------------ | :------------| 
| `<partition_by>`   | The expression used for the `PARTITION BY` clause.                                                | Any |
| `<order_by>`    | The expression used in the `ORDER BY` clause. This parameter determines what value will be ranked.  | Any | 

## Return Types 
Same as input type 

## Example
{: .no_toc}

In this example below, players are ranked based on their high scores for their game level.

```sql
SELECT
	nickname,
	level,
	highscore,
	DENSE_RANK() OVER (PARTITION BY level ORDER BY highscore DESC ) AS game_rank
FROM
	players;
```

**Returns**:

| nickname | level | highscore | game_rank |
|:-------|:------|:------|:------|
| kennethpark      |           9 |         76 |             6 |
| sabrina21    |          10 |         78 |             3 |
| rileyjon   |          11 |         94 |             1 |
| ymatthews  |          12 |         92 |             4 |


