---
layout: default
title: BOOL_AND
description: Reference material for BOOL_AND
grand_parent: SQL functions
parent: Aggregation functions
---


# BOOL_OR

Returns true if all non NULL input value are true, otherwise false. If all input values are NULL values, returns NULL.

## Syntax
{: .no_toc}

```sql
BOOL_AND(<expression>)
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

We want to check if all tournaments have prize money

```sql
SELECT
	BOOL_ALL(totalprizeddollars IS NOT NULL AND totalprizeddollars > 0) as all_have_prizes 
FROM
	tournaments;
```

**Returns**: `true`
