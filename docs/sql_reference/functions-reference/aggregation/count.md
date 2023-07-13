---
layout: default
title: COUNT (aggregation function)
description: Reference material for COUNT
grand_parent: SQL functions
parent: Aggregation functions
---


# COUNT

Counts the number of rows or not NULL values.

## Syntax
{: .no_toc}

```sql
COUNT([ DISTINCT ] <expr>)
```
## Parameters 
{: .no_toc}
| Parameter       | Description                   | Supported input types |
| :---------      | :-----------------------------| :---------------------|
| `<expression>`  | Rows that will be counted by the function | `<column>` names or `<function>`s that return a column name | 

{: .note}
> By default, `COUNT(DISTINCT)` returns approximate results. If you require a precise result (with a performance penalty), please contact Firebolt Support through the Help menu support form. 

## Return Types
`NUMERIC`

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

Doing a regular `COUNT` returns the total number of rows in the column. As the `tournaments` table contains 6 rows, this should be the returned value. 

```sql
SELECT
	COUNT(name)
FROM
	tournaments;
```

**Returns**: `6`

A `COUNT(DISTINCT)` function on the same column returns the number of unique rows. When applied to the `totalprizedollars` column, the value returned is `5`, as there is a repeated number in the column. 

```sql
SELECT
	COUNT(DISTINCT totalprizedollars)
FROM
	tournaments;
```

**Returns**: `5`

<!-- To understand the difference between `COUNT(DISTINCT pk)` with exact precision enabled and using default approximation, consider a table, `count_test` with 8,388,608 unique `pk` values. The `APPROX_COUNT_DISTINCT` function returns the same approximate results as the `COUNT(DISTINCT)` function with exact precision disabled, so we can see the difference between these methods with the following example. 

```sql
SELECT
	COUNT(DISTINCT pk) as count_distinct,
	APPROX_COUNT_DISTINCT(pk) as approx_count
FROM
	count_test;
```

**Returns**: 

Assuming 8,388,608 unique pk values, we will see results like: 


```sql
' +----------------+--------------+
' | count_distinct | approx_count |
' +----------------+--------------+
' |      8,388,608 |    8,427,387 |
' +----------------+--------------+
``` -->
