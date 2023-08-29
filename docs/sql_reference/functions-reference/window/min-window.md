---
layout: default
title: MIN OVER
description: Reference material for MIN function
grand_parent: SQL functions
parent: Window functions
great_grand_parent: SQL reference
---

# MIN

Returns the minimum value within the requested window.

For more information on usage, please refer to [Window Functions](./window-functions.md).

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

The example below queries test scores for students in various grade levels. Unlike a regular `MIN()` aggregation, the window function allows us to see how each student individually compares to the lowest test score for their grade level.

```sql
SELECT
	first_name,
	grade_level,
	test_score,
	MIN(test_score) OVER (PARTITION BY grade_level) AS lowest_score
FROM
	class_test;
```

**Returns**:

```
+------------+-------------+------------+--------------+
| first_name | grade_level | test_score | lowest_score |
+------------+-------------+------------+--------------+
| Frank      |           9 |         76 |           76 |
| Humphrey   |           9 |         90 |           76 |
| Iris       |           9 |         79 |           76 |
| Sammy      |           9 |         85 |           76 |
| Peter      |           9 |         80 |           76 |
| Jojo       |           9 |         78 |           76 |
| Brunhilda  |          12 |         92 |           66 |
| Franco     |          12 |         94 |           66 |
| Thomas     |          12 |         66 |           66 |
| Gary       |          12 |        100 |           66 |
| Charles    |          12 |         93 |           66 |
| Jesse      |          12 |         89 |           66 |
| Roseanna   |          11 |         94 |           52 |
| Carol      |          11 |         52 |           52 |
| Wanda      |          11 |         73 |           52 |
| Shangxiu   |          11 |         76 |           52 |
| Larry      |          11 |         68 |           52 |
| Otis       |          11 |         75 |           52 |
| Deborah    |          10 |         78 |           30 |
| Yolinda    |          10 |         30 |           30 |
| Albert     |          10 |         59 |           30 |
| Mary       |          10 |         85 |           30 |
| Shawn      |          10 |         89 |           30 |
+------------+-------------+------------+--------------+
```
