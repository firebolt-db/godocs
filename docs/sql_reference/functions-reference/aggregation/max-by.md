---
layout: default
title: MAX_BY
description: Reference material for MAX_BY
grand_parent: SQL functions
parent: Aggregation functions
---


# MAX\_BY

The `MAX_BY` function returns a value for the `<arg>` column based on the max value in a separate column, specified by `<val>`.

If there is more than one max value in `<val>`, then the first will be used.

## Syntax
{: .no_toc}

```sql
MAX_BY(<arg>, <val>)
```

| Parameter | Description                                    |
| :--------- | :---------------------------------------------- |
| `<arg>`   | The column from which the value is returned.   |
| `<val>`   | The column that is search for a maximum value. |

## Return Types
The return types for this function includes `CHAR`, `NUMERIC`, `REAL`, and `DOUBLE PRECISION`. 

## Example
{: .no_toc}

For this example,  see the following table, `tournaments`:

| name                          | totalprizedollars |
| :-----------------------------| :-----------------| 
| The Drifting Thunderdome      | 24768             |
| The Lost Track Showdown       | 5336              |
| The Acceleration Championship | 19274             |
| The French Grand Prix         | 237               |
| The Circuit Championship      | 9739              |


In this example below, `MAX_BY` is used to find the tournament  with the highest total prize dollars.

```sql
SELECT
	MAX_BY(name, totalprizedollars)
FROM
	tournaments;
```

**Returns:** `The Drifting Thunderdome`
