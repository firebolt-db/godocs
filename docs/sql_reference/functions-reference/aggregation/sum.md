---
layout: default
title: SUM (aggregation function)
description: Reference material for SUM
grand_parent: SQL functions
parent: Aggregation functions
---

# SUM

Calculates the sum of an expression.

## Syntax
{: .no_toc}

```sql
SUM ([DISTINCT] <expr>)
```

| Parameter | Description                                                                                                                              |
| :--------- | :---------------------------------------------------------------------------------------------------------------------------------------- |
| `<expr>`   | The expression used to calculate the sum. Valid values for `<expr>` include column names or expressions that evaluate to numeric values. |
| `DISTINCT` | When specified, removes duplicate values from `<expr>` before calculating the sum. |

## Return Types
This function returns `NUMERIC` types. 

## Example

For this example, see the following table `tournaments`: 

| name                          | totalprizedollars |
| :-----------------------------| :-----------------| 
| The Drifting Thunderdome      | 24768             |
| The Lost Track Showdown       | 5336              |
| The Acceleration Championship | 19274             |
| The Winter Wilderness Rally   | 21560             |
| The Circuit Championship      | 9739              |
| The Singapore Grand Prix      | 19274             |

<!-- | firstname | score |
|:----------|:------|
| Deborah   |    90 |
| Albert    |    50 |
| Carol     |    11 |
| Frank     |    87 |
| Thomas    |    85 |
| Peter     |    50 |
| Sammy     |    90 |
| Humphrey  |    56 | -->


```
SELECT
	SUM(totalprizedollars)
FROM
	tournaments
```

**Returns**: `99951`

```
SELECT
	SUM (DISTINCT totalprizedollars)
FROM
	tournaments
```

For this calculation, since both the Singapore Grand Prix and The Acceleration Championship both had the same total prize dollars of `19274`, only one of these values in this sum in included. 

**Returns**: `80677`
