---
layout: default
title: MIN OVER
description: Reference material for MIN function
grand_parent: SQL functions
parent: Window functions
---

# MIN

Returns the minimum value within the requested window.

For more information on usage, please refer to [Window Functions](./index.md).

## Syntax
{: .no_toc}

```sql
MIN( <expression> ) OVER ( [ PARTITION BY <partition_by> ] )
```

## Parameters 
{: .no_toc}

| Parameter | Description                                      | Supported input types | 
| :--------- | :------------------------------------------------ | :------------| 
| `<expression>`   | A value used for the `MIN` function       | Any |
| `<partition_by>`   | An expression used for the `PARTITION BY` clause. | Any |

## Example
{: .no_toc}

The example below queries test scores for players in various grade levels. Unlike a regular `MIN()` aggregation, the window function highlights how each player individually compares to the lowest game score for their level.

```sql
SELECT
	nickname,
	level,
	current_score,
	MIN(current_score) OVER (PARTITION BY level) AS lowest_score
FROM
	players;
```

**Returns**:

 | nickname | level | current_score |    lowest_score    |
 |:------------|:-------------|:------------|:-------------------------|
 | kennethpark      |           9 |         76 | 2      |
 | sabrina21   |           7 |         90 | 15      |
 | burchdenise       |           5 |         79 | 4      |
 | ymatthews      |           6 |         85 | 9       |
| rileyjon      |           8 |         80 | 20     |

