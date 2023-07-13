---
layout: default
title: MIN (aggregation function)
description: Reference material for MIN
grand_parent: SQL functions
parent: Aggregation functions
---


# MIN

Calculates the minimum value of an expression across all input values.

## Syntax
{: .no_toc}

```sql
MIN(<expression>)
```

| Parameter | Description                                               |Supported input types                                        |
| :--------- | :--------------------------------------------------------|:------------------------------------------------------------|
| `<expression>`  | The expression used to calculate the minimum values | `<column>` names, or a `<function>` that returns a column name | 

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

When used on the `totalprizedollars` column, `MIN` will return the smallest value.

```sql
SELECT
	MIN(totalprizedollars)
FROM
	tournaments;
```

**Returns**: `237`

`MIN` can also work on text columns by returning the text row with the characters that are first in the lexicographic order. In this example, the function assesses the `name` column in the `tournaments` table.

```sql
SELECT
	MIN(name)
FROM
	tournaments;
```

**Returns**: `The Acceleration Tournament`

<!-- SELECT min(name) FROM tournaments;
-- -- SELECT min(totalprizedollars) FROM tournaments; -->
