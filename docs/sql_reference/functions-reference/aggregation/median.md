---
layout: default
title: MEDIAN
description: Reference material for MEDIAN
grand_parent: SQL functions
parent: Aggregation functions
great_grand_parent: SQL reference
---

# MEDIAN

Calculates an approximate median for a given column.

## Syntax
{: .no_toc}

```sql
MEDIAN(<value>)
```

## Parameters
{: .no_toc}

| Parameter | Description                         |Supported input types |
| :--------- | :----------------------------------- | :---------------------|
| `<value>`   | The expression used to calculate the median value | Any numeric type |


## Return Type
`DOUBLE PRECISION`

## Example
{: .no_toc}
For this example,  see the following table, `tournaments`:

| name                          | totalprizedollars  |
| :-----------------------------| :------------------| 
| The Drift Championship        | 22,048             |
| The Lost Track Showdown       | 5336               |
| The Acceleration Championship | 19,274             |
| The French Grand Prix         | 237                |
| The Circuit Championship      | 9,739              |

`MEDIAN` returns the approximate middle value between the lower and higher halves of the values.

```sql
SELECT
	MEDIAN(totalprizedollars)
FROM
	tournaments;
```

**Returns**: `9,739`
