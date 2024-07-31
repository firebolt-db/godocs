---
layout: default
title: MIN
description: Reference material for MIN
grand_parent: SQL functions
parent: Aggregation functions
---


# MIN

Returns the minimum value in its argument. NULL values are ignored. If all inputs are NULL, `MIN` returns NULL.

## Syntax
{: .no_toc}

```sql
MIN(<expression>)
```

## Parameters
{: .no_toc}

| Parameter | Description                         |Supported input types |
| :--------- | :----------------------------------- | :---------------------|
| `<expression>`  | The expression whose minimum to determine | Any type |

## Return Types

Same as input type

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

When used on the `totalprizedollars` column, `MIN` will return the smallest value.

```sql
SELECT
	MIN(totalprizedollars) as minprize
FROM
	tournaments;
```

**Returns**: `237`

`MIN` can also work on text or array columns, in which case it returns the lexicographically smallest value. In this example, the function assesses the `name` column in the `tournaments` table.

```sql
SELECT
	MIN(name) as mintournament
FROM
	tournaments;
```

**Returns**: `The Acceleration Championship`
