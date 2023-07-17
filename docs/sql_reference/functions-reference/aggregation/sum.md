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
## Parameters 
{: .no_toc} 

| Parameter | Description                                     | Supported input types|
| :--------- | :----------------------------------------------|:-----------------------|
| `<expression>`   | The expression used to calculate the sum | `<column>` names or `<expression>`s that evaluate to numeric values |
| `DISTINCT` | When specified, removes duplicate values from `<expresssion>` before calculating the sum | `<column>` |

## Return Types
`NUMERIC` 

## Example

For this example, see the following table `tournaments`: 

| name                          | totalprizedollars |
| :-----------------------------| :-----------------| 
| The Drifting Thunderdome      | 24,768             |
| The Lost Track Showdown       | 5,336              |
| The Acceleration Championship | 19,274             |
| The Winter Wilderness Rally   | 21,560             |
| The Circuit Championship      | 9,739              |
| The Singapore Grand Prix      | 19,274             |

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

**Returns**: `99,951`

```
SELECT
	SUM (DISTINCT totalprizedollars)
FROM
	tournaments
```

For this calculation, since both the Singapore Grand Prix and The Acceleration Championship both had the same total prize dollars of `19,274`, only one of these values in this sum in included. 

**Returns**: `80,677`
