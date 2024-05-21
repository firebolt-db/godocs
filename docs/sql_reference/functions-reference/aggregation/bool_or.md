---
layout: default
title: BOOL_OR
description: Reference material for BOOL_OR
grand_parent: SQL functions
parent: Aggregation functions
great_grand_parent: SQL reference
---


# BOOL_OR

Returns true if any non NULL input value is true, otherwise false. If all input values are NULL values, returns NULL.

## Syntax
{: .no_toc}

```sql
BOOL_OR(<expression>)
```

## Parameters
{: .no_toc}

| Parameter | Description                                         | Supported input types |
| :--------- |:----------------------------------------------------|:----------------------|
| `<expression>`  | The boolean expression used to calculate the result | `BOOLEAN`              |

## Return Types

`BOOLEAN`

## Example
{: .no_toc}


| name                          | totalprizedollars |
| :-----------------------------| :-----------------| 
| The Drift Championship        | 22,048             |
| The Lost Track Showdown       | 5,336              |
| The Acceleration Championship | 19,274             |
| The French Grand Prix         | 237               |
| The Circuit Championship      | 9,739              |

We want to see if any of the tournaments have prize value more than 20,000

```sql
SELECT
	BOOL_OR(totalprizeddollars > 20000) as has_big_prize
FROM
	tournaments;
```

**Returns**: `true`
