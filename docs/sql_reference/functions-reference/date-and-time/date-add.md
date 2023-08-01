---
layout: default
title: DATE_ADD
description: Reference material for DATE_ADD function
grand_parent: SQL functions
parent: Date and time functions
great_grand_parent: SQL reference
---

# DATE\_ADD

Calculates a new `DATE `or `TIMESTAMP` by adding or subtracting a specified number of time units from an indicated expression.

## Syntax
{: .no_toc}

```sql
DATE_ADD('<unit>', <value>, <expression>)
```
## Parameters 
{: .no_toc}

| Parameter     | Description       | Supported input types | 
| :------------- | :---------------------- | :---------|
| `<datepart>`      | A unit of time | `SECOND`, `MINUTE`, `HOUR`, `DAY`, `WEEK`, `MONTH`, `QUARTER`, or `YEAR`  |                                                              |
| `<value>`  | The number of times to increase the `<datepart>` by the time unit specified by `<unit>` | Positive or negative number | 
| `<expression>` | A date expression  | Any expression that evaluates to a `DATE` or `TIMESTAMP` value |                                                            |

## Return Types 
`DATE` or `TIMESTAMP`

## Example
{: .no_toc}

The example below uses a table `player_registry` with the columns and values below.

| player | registeredon |
| :-------- | :---------- |
| steven70        | 2012-05-01 |
| burchdenise       | 2021-08-30 |
| stephanie86        | 1999-12-31 |

This example below adds 15 weeks to the `registeredon` column.

```sql
SELECT
	category,
	DATE_ADD('WEEK', 15, registeredon)
FROM
	player_registry;
```

**Returns**:

| player | registerdon | 
|:---------------|:-------|
| steven70 | 2012-08-14 |
| burchdenise | 2021-12-13 |
| stephanie86 | 2000-04-14 |



This example below subtracts 6 months from a given start date string. This string representation of a date first needs to be transformed to `DATE `type using the `CAST `function.

```
SELECT
    DATE_ADD('MONTH', -6, CAST ('2021-11-04' AS DATE));
```

**Returns**: `2021-05-04`
