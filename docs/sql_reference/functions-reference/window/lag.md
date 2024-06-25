---
layout: default
title: LAG OVER
description: Reference material for LAG function
grand_parent: SQL functions
parent: Window functions
great_grand_parent: SQL reference
published: true
---

# LAG

Returns the value of the input expression at the given offset before the current row within the requested window.

For more information on usage, please refer to [Window Functions](./index.md).

## Syntax
{: .no_toc}

```sql
LAG ( <expression> [, <offset> [, <default> ]] )
    OVER ( [ PARTITION BY <partition_by> ] ORDER BY <order_by> [ { ASC | DESC } ] )
```

## Parameters 
{: .no_toc}

| Parameter | Description                                      | Supported input types | 
| :--------- | :------------------------------------------------ | :------------| 
| `<value>`     | Any valid expression that will be returned based on the `<offset>.`                                                    | Any |
| `<partition_by>`    | The expression used for the `PARTITION BY` clause.                                                                           | Any |
| `<offset>`  | The number of rows backward from the current row from which to obtain a value. A negative number will act as `LEAD()`        | 	`INTEGER` |
| `<default>` | The expression to return when the offset goes out of the bounds of the window. Must be a literal `INTEGER`. The default is `NULL`. | `INTEGER` |
| `<order_by>` | An expression used for the order by clause. | Any |

## Example
{: .no_toc}

In the example below, the `LAG` function is being used to find the players in each level who ranked above and below a certain player. In some cases, if the player has no one ranked above or below them, the `LAG` function returns `NULL`.

```sql
SELECT
	nickname,
	level,
	LAG(nickname, 1) OVER (PARTITION BY level ORDER BY nickname) AS player_above,
	LAG(first_name, -1) OVER (PARTITION BY level ORDER BY first_name) AS player_below
FROM
	players;
```

**Returns**:

| nickname | level | player_above | player_below |
|:----------|:-------------|:-------------|:--------------|
| kennethpark      |           9 | NULL        | rileyjon     |
| rileyjon   |           9 | kennethpark       | sabrina21         |
| sabrina21       |           9 | rileyjon    | ymatthews         |
| ymatthews      |           9 | sabrina21       | NULL         |
