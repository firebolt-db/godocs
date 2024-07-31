---
layout: default
title: ARRAY_AGG
description: Reference material for ARRAY_AGG function
parent: Aggregation functions
grand_parent:  SQL functions

---

# ARRAY_AGG

Concatenates input values, including `NULL` values, into an array.


## Syntax
{: .no_toc}

```sql
ARRAY_AGG(<expression>)
```

## Parameters 
{: .no_toc}

| Parameter | Description                                         | Supported input type |
| :--------- | :--------------------------------------------------|:-----|
| `<expression>`   | Expression of any type to be accumulated into an array. | Any |

## Return Type
{: .no_toc}

`ARRAY` of the same type as the input data. If there is no input data, `ARRAY_AGG` returns `NULL`.

## Example
{: .no_toc}

For the following example, see the `player_information` table:

| nickname   | playerid |
| :------ | :----- |
| stephen70  | 1    |
| burchdenise | 7   |
| sabrina21   | NULL    |

This example code selects the columns in the `player_information` table and returns the values in two arrays, `nicknames` and `playerids`. 

```sql
SELECT
  ARRAY_AGG(nickname) AS nicknames,
  ARRAY_AGG(playerid) AS playerids
FROM
	price_list;
```

**Returns**: `{'stephen70', 'burchdenise', 'sabrina21'}, {1, 7, NULL}`

If a filter is added to the query which rejects all rows, `ARRAY_AGG` will return `NULL`.

```sql
SELECT
  ARRAY_AGG(nickname) AS nicknames,
  ARRAY_AGG(playerid) AS playerids
FROM
	price_list
WHERE
  playerid = 42;
```

**Returns**: `NULL, NULL`
