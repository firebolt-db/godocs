---
layout: default
title: MAX
description: Reference material for MAX
parent: Aggregation functions
---


# MAX

Returns the maximum value in its argument. NULL values are ignored. If all inputs are NULL, `MAX` returns NULL.

## Syntax
{: .no_toc}

```sql
MAX(<expression>)
```

## Parameters
{: .no_toc}

| Parameter | Description                                               |Supported input types                                        |
| :--------- | :--------------------------------------------------------|:------------------------------------------------------------|
| `<expression>`  | The expression whose maximum to determine | Any type |

## Return Types
Same as input type

## Example
{: .no_toc}
For this example, see the following table, `tournaments`:

| name                          | totalprizedollars |
| :-----------------------------| :-----------------|
| The Drifting Thunderdome      | 24,768             |
| The Lost Track Showdown       | 5,336              |
| The Acceleration Championship | 19,274             |
| The Winter Wilderness Rally   | 21,560             |
| The Circuit Championship      | 9,739              |

When used on the `totalprizedollars` column, `MAX` will return the highest value.

```sql
SELECT
	MAX(totalprizedollars) as maxprize
FROM
	tournaments;
```

**Returns**: `24,768`


`MAX` can also work on text or array columns, in which case it returns the lexicographically largest value. In this example, the function assesses the `name` column in the `tournaments` table.

```sql
SELECT
	MAX(name) as maxtournament
FROM
	tournaments;
```

**Returns**: `The Winter Wilderness Rally`
