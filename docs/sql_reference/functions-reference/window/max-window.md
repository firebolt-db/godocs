---
layout: default
title: MAX OVER
description: Reference material for MAX function
grand_parent: SQL functions
parent: Window functions
great_grand_parent: SQL reference
---

# MAX OVER

Returns the maximum value within the requested window.

For more information on usage, please refer to [Window Functions](./window-functions.md).

## Syntax
{: .no_toc}

```sql
MAX( <expression> ) OVER ( [ PARTITION BY <partition_by> ] )
```

## Parameters 
{: .no_toc}

| Parameter | Description                                      | Supported input types | 
| :--------- | :------------------------------------------------ | :------------| 
| `<expression>`   | A value used for the `MAX` function       | Any |
| `<partition_by>`   | An expression used for the `PARTITION BY` clause. | Any |


## Return Types
Same as input type

## Example
{: .no_toc}

The example below queries test scores for players in various grade levels. Unlike a regular `MAX()` aggregation, the window function highlights how each player individually compares to the highest game score for their level.

```sql
SELECT
	nickname,
	level,
	current_score,
	MAX(current_score) OVER (PARTITION BY level) AS highest_score
FROM
	players;
```

**Returns**:

 | nickname | level | current_score |    highest_score    |
 |:------------|:-------------|:------------|:-------------------------|
 | kennethpark      |           9 |         76 | 95      |
 | sabrina21   |           7 |         90 | 98      |
 | burchdenise       |           5 |         79 | 99      |
 | ymatthews      |           6 |         85 | 93       |
| rileyjon      |           8 |         80 | 84     |

