---
layout: default
title: MIN_BY
description: Reference material for MIN_BY
grand_parent: SQL functions
parent: Aggregation functions
---


# MIN\_BY

The `MIN_BY` function returns the value of `expression` column at the row in which the `value` column is minimal.

If there is more than one minimal values in `val`, then the first will be used.

## Syntax
{: .no_toc}

```sql
MIN_BY(arg, val)
```

| Parameter | Description                                        | Supported input Type |
| :--------- | :-------------------------------------------------|:---------------------|
| `<expression>`   | The column from which the value is returned | `<column>`           |
| `<value>`   | The column that is search for a minimum value    | `<column>`           |

## Return Types
`CHAR`, `NUMERIC`, `REAL`, `DOUBLE PRECISION`

## Example
{: .no_toc}

For this example,  see the following table, `tournaments`:

| name                          | totalprizedollars |
| :-----------------------------| :-----------------| 
| The Drift Championship        | 22048             |
| The Lost Track Showdown       | 5336              |
| The Acceleration Championship | 19274             |
| The French Grand Prix         | 237               |
| The Circuit Championship      | 9739              |


In this example below, `MIN_BY` is used to find the tournament with the lowest total prize dollars. The function evaluates the `totalprizedollars` column for values and returns an entry from the `name` column. 

```sql
SELECT
	MIN_BY(name, totalprizedollars)
FROM
	tournaments
```

**Returns:** `The French Grand Prix`
