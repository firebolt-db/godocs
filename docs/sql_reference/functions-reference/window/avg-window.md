---
layout: default
title: AVG OVER
description: Reference material for AVG function
grand_parent: SQL functions
parent: Window functions
great_grand_parent: SQL reference
---

# AVG

Returns the average value within the requested window.

For more information on usage, please refer to [Window Functions](./window-functions.md).

## Syntax
{: .no_toc}

```sql
AVG( <value> ) OVER ( [ PARTITION BY <partition_by> ] )
```

## Parameters
{: .no_toc}

| Parameter | Description |Supported input types | 
| :--------- | :----------------------------------------------- | :----------|
| `<value>`   | A value used for the `AVG()` function    | Any numeric type  | 
| `<partition_by`  | An expression used for the `PARTITION BY` clause | Any | 

## Return Types
* `NUMERIC` if the input is type `INTEGER`, `BIGINT` or `NUMERIC`
* `DOUBLE PRECISION` if the input is type `REAL` or `DOUBLE PRECISION`

## Example
{: .no_toc}

The example below is querying test scores for students in various grade levels. Unlike a regular `AVG()` aggregation, the window function allows us to see how each student individually compares to the average test score for their grade level.

```sql
SELECT
	first_name,
	grade_level,
	test_score,
	AVG(test_score) OVER (PARTITION BY grade_level) AS average_for_grade
FROM
	class_test;
```

**Returns**:

```
' +------------+-------------+------------+-------------------------+
' | first_name | grade_level | test_score |    average_for_grade    |
' +------------+-------------+------------+-------------------------+
' | Frank      |           9 |         76 | 81.33333333333333       |
' | Humphrey   |           9 |         90 | 81.33333333333333       |
' | Iris       |           9 |         79 | 81.33333333333333       |
' | Sammy      |           9 |         85 | 81.33333333333333       |
' | Peter      |           9 |         80 | 81.33333333333333       |
' | Jojo       |           9 |         78 | 81.33333333333333       |
' | Brunhilda  |          12 |         92 | 89                      |
' | Franco     |          12 |         94 | 89                      |
' | Thomas     |          12 |         66 | 89                      |
' | Gary       |          12 |        100 | 89                      |
' | Charles    |          12 |         93 | 89                      |
' | Jesse      |          12 |         89 | 89                      |
' | Roseanna   |          11 |         94 | 73                      |
' | Carol      |          11 |         52 | 73                      |
' | Wanda      |          11 |         73 | 73                      |
' | Shangxiu   |          11 |         76 | 73                      |
' | Larry      |          11 |         68 | 73                      |
' | Otis       |          11 |         75 | 73                      |
' | Deborah    |          10 |         78 | 68.2                    |
' | Yolinda    |          10 |         30 | 68.2                    |
' | Albert     |          10 |         59 | 68.2                    |
' | Mary       |          10 |         85 | 68.2                    |
' | Shawn      |          10 |         89 | 68.2                    |
' +------------+-------------+------------+-------------------------+
```
