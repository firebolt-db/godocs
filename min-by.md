---
layout: default
title: MIN_BY
description: Reference material for MIN_BY
parent: Aggregation functions
---

# MIN\_BY

Returns the value of the first argument for the row that contains the minimum of the second argument. If the minimum of the second argument is not unique, an arbitrary non-NULL value of the first argument is returned from the set of rows that minimize the second argument. If the first argument is NULL for all rows minimizing the second argument, NULL is returned.

## Syntax
{: .no_toc}

```sql
MIN_BY(<result>, <value>)
```

## Parameters
{: .no_toc}

| Parameter | Description                         |Supported input types |
| :--------- | :----------------------------------- | :---------------------|
| `<result>` | The column from which the value is returned | Any type |
| `<value>`  | The column that is minimized | Any type |

## Return Types

Same as input type of <result>

## Example
{: .no_toc}

For this example, see the following table, `tournaments`:

| name                          | totalprizedollars |
| :-----------------------------| :-----------------|
| The Drift Championship        | 22,048            |
| The Lost Track Showdown       | 5,336             |
| The Acceleration Championship | 19,274            |
| The French Grand Prix         | 237               |
| The Circuit Championship      | 9,739             |


In the example below, `MIN_BY` is used to find the name of the tournament with the lowest total prize.

```sql
SELECT
	MIN_BY(name, totalprizedollars) as minprizetournament
FROM
	tournaments
```

**Returns:** `The French Grand Prix`


When multiple rows minimize the second argument, an arbitrary one is chosen, preferring non-NULL values of the first argument:
```sql
SELECT MIN_BY(key, value)
FROM UNNEST(
    ['a', NULL, 'c', 'd', 'e', NULL],
    [10,  1,    100,  1,   1,  NULL]
) t(key, value)
```
**Returns** `'d'` or `'e'`, as rows 2, 4, and 5 minimize the second argument, but the first argument is NULL for row 2. Because non-NULL values of the first argument exist for the other rows, one of those values is returned. Which of them is non-deterministic, hence this query may return either `'d'` or `'e'`.


However, if all rows minimizing the second argument are NULL in the first argument, NULL is returned:
```sql
SELECT MIN_BY(key, value)
FROM UNNEST(
    ['a', NULL, 'c', 'd', NULL, 'f'],
    [10,  1,    100,  2,   1,  NULL]
) t(key, value)
```
**Returns** `NULL`.
