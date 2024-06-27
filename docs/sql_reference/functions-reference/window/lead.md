---
layout: default
title: LEAD OVER
description: Reference material for LEAD function
grand_parent: SQL functions
parent: Window functions
great_grand_parent: SQL reference
published: true
---

# LEAD

Returns values from the row after the current row within the requested window.

For more information on usage, please refer to [Window Functions](./index.md).

## Syntax
{: .no_toc}

```sql
LEAD ( <expression> [, <offset> [, <default> ]] )
    OVER ( [ PARTITION BY <partition_by> ] ORDER BY <order_by> [ { ASC | DESC } ] )
```

## Parameters 
{: .no_toc}

| Parameter | Description                                      | Supported input types | 
| :--------- | :------------------------------------------------ | :------------| 
| `<expression>`     | Any valid expression that will be returned based on the `<offset>.`                                                    | Any |
| `<offset>`  | The number of rows forward from the current row from which to obtain a value.  |	`INTEGER` |
| `<default>` | The expression to return when the offset goes out of the bounds of the window. Must be a literal of the same type as `<expression>`. The default is `NULL`. | Any |
| `<partition_by>`    | The expression used for the `PARTITION BY` clause.                                                                           | Any |
| `<order_by>` | An expression used for the `ORDER BY` clause. | Any |


## Example
{: .no_toc}

In the example below, the `LEAD` function is being used to find the players in each level who ranked before and after a certain player. In some cases, if the player has no one ranked before or after them, the `LEAD` function returns `NULL`.

```sql
SELECT
	nickname,
	level,
	LEAD(nickname, -1) OVER (PARTITION BY level ORDER BY nickname) AS player_before,
	LEAD(nickname, 1) OVER (PARTITION BY level ORDER BY nickname) AS player_after
FROM
	players;
```

**Returns**:

| nickname | level | player_before | player_after |
|:----------|:-------------|:-------------|:--------------|
| kennethpark      |           9 | NULL        | rileyjon     |
| rileyjon   |           9 | kennethpark       | sabrina21         |
| sabrina21       |           9 | rileyjon    | ymatthews         |
| ymatthews      |           9 | sabrina21       | NULL         |
