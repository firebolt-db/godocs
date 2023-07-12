---
layout: default
title: MIN_BY
description: Reference material for MIN_BY
grand_parent: SQL functions
parent: Aggregation functions
---


# MIN\_BY

The `MIN_BY` function returns the value of `arg` column at the row in which the `val` column is minimal.

If there is more than one minimal values in `val`, then the first will be used.

## Syntax
{: .no_toc}

```sql
MIN_BY(arg, val)
```

| Parameter | Description                                    |
| :--------- | :---------------------------------------------|
| `<arg>`   | The column from which the value is returned.   |
| `<val>`   | The column that is search for a minimum value. |

## Return Types
The return types for this function includes `CHAR`, `NUMERIC`, `REAL`, and `DOUBLE PRECISION`. 

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


In this example below, `MIN_BY` is used to find the tournament  with the lowest total prize dollars.

```sql
SELECT
	MIN_BY(name, totalprizedollars)
FROM
	tournaments
```

**Returns:** `The French Grand Prix`
