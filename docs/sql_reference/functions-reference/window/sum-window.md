---
layout: default
title: SUM OVER
description: Reference material for SUM function
grand_parent: SQL functions
parent: Window functions
great_grand_parent: SQL reference
---

# SUM 

Calculate the sum of the values within the requested window.

The SUM function works with numeric values and ignores `NULL` values.

For more information on usage, please refer to [Window Functions](./window-functions.md).

## Syntax
{: .no_toc}

```sql
SUM([ DISTINCT ] <value> ) OVER ( [ PARTITION BY <partition_by> ] )
```

## Parameters 
{: .no_toc}

| Parameter | Description                                      |Supported input types | 
| :--------- | :------------------------------------------------ | :------------| 
| `<value>`   | The expression used for the `SUM` function       | Any numeric type |
| `<partition_by>`  | An expression used for the `PARTITION BY` clause | Any |

## Return Types
`NUMERIC` 

When `DISTINCT` is specified, duplicate values from `<expression>` are removed before calculating the sum.

## Example
{: .no_toc}

The example below shows how many players registered on a specific date: 

```sql
SELECT
	first_name,
	SUM(vaccinated) OVER (PARTITION BY grade_level ) AS vaccinated_students
FROM
	class_test;
```

**Returns**:

```
+------------+---------------------+
| first_name | vaccinated_students |
+------------+---------------------+
| Frank      |                   5 |
| Humphrey   |                   5 |
| Iris       |                   5 |
| Sammy      |                   5 |
| Peter      |                   5 |
| Jojo       |                   5 |
| Brunhilda  |                   5 |
| Franco     |                   5 |
| Thomas     |                   5 |
| Gary       |                   5 |
| Charles    |                   5 |
| Jesse      |                   5 |
| Roseanna   |                   4 |
| Carol      |                   4 |
| Wanda      |                   4 |
| Shangxiu   |                   4 |
| Larry      |                   4 |
| Otis       |                   4 |
| Deborah    |                   4 |
| Yolinda    |                   4 |
| Albert     |                   4 |
| Mary       |                   4 |
| Shawn      |                   4 |
+------------+---------------------+
```
