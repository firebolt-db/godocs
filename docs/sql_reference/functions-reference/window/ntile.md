---
layout: default
title: NTILE OVER
description: Reference material for NTILE function
grand_parent: SQL functions
parent: Window functions
great_grand_parent: SQL reference
---

# NTILE

Divides an ordered data set equally into the number of buckets specified by the argument value. Buckets are sequentially numbered 1 through the argument value. 

For more information on usage, please refer to [Window Functions](./window-functions.md).

## Syntax
{: .no_toc}

```sql
NTILE( <value> ) OVER ( [ PARTITION BY <partition_by> ] ORDER BY <order_by> [ { ASC | DESC } ] )
```

## Parameters 
{: .no_toc}

| Parameter | Description                                      | Supported input types | 
| :--------- | :------------------------------------------------ | :------------| 
| `<value>`   | An integer expression used for the `NTILE()` function to specify the number of buckets for division.    | `INTEGER` |
| `<partition_by>` | An expression used for the partition by clause. | Any |
| `<order_by>` | An expression used for the order by clause. | Any |

## Return Type
`INTEGER`

If there is a remainder after dividing the rows in a partition by the argument value, it will result in buckets of different sizes. For example, 
- `NTILE(2)` over 5 rows will result in 2 buckets, the first with 3 rows, the second with 2
- `NTILE(3)` over 5 rows results in 3 buckets, the first 2 with 2 rows each and the last with one. 

## Example
{: .no_toc}

The example below divides students with the same grade level into three groups. 

```sql
SELECT
	first_name,
	NTILE(3) OVER (PARTITION BY level) AS ntile_buckets
FROM
	class_test;
```

**Returns**:

```sql
' +------------+---------------+
' | first_name | ntile_buckets | 
' +------------+---------------+
' | Frank      |             1 |
' | Humphrey   |             1 |
' | Iris       |             2 |
' | Sammy      |             2 |
' | Peter      |             3 |
' | Jojo       |             3 |
' | Brunhilda  |             1 |
' | Franco     |             1 |
' | Thomas     |             2 |
' | Gary       |             2 |
' | Charles    |             3 |
' | Jesse      |             3 |
' | Roseanna   |             1 |
' | Wanda      |             1 |
' | Shangxiu   |             2 |
' | Larry      |             2 |
' | Otis       |             3 |
' | Deborah    |             1 |
' | Yolinda    |             2 |
' | Albert     |             3 | 
' +------------+---------------+
```
