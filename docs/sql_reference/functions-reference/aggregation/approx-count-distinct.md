---
layout: default
title: APPROX_COUNT_DISTINCT
description: Reference material for APPROX_COUNT_DISTINCT
grand_parent: SQL functions
parent: Aggregation functions
great_grand_parent: SQL reference
---


# APPROX_COUNT_DISTINCT

Counts the approximate number of unique or not NULL values. `APPROX_COUNT_DISTINCT` uses the HLL algorithm with the default parameter to control the sketch size set to 17. This is subject to change. 

## Syntax
{: .no_toc}

```sql
APPROX_COUNT_DISTINCT ( <expression> )
```

## Parameters
{: .no_toc}

| Parameter | Description  | Supported input types | 
| :--------- | :-----------|:----------|
| `<expression>`  | Expression that the `APPROX_COUNT_DISTANCE function` is applied to | Any `<column>` name or any function that returns a `<column>` name | 

{: .note}
> By default, `APPROX_COUNT_DISTINCT` and `COUNT(DISTINCT)` return the same, approximate results. If you require a precise result for `COUNT(DISTINCT)` (with a performance penalty), please contact Firebolt Support through the Help menu support form. 

## Return Types 
`INTEGER`

## Example
{: .no_toc}

The following example draws from the `INTEGER` column `playerid` from the `players` table. The code calculates the `COUNT` of `playerid` values as well as the `APPROX_COUNT_DISTINCT` of these two values in a labeled table: 

```sql
SELECT
	COUNT(DISTINCT playerid) as playerid_count_distinct,
	APPROX_COUNT_DISTINCT(playerid) as playerid_approx_count
FROM
	players;
```

**Returns**: 


| playerid_count_distinct | playerid_approx_count | 
|:----------------|:--------------|
| 5,420 | 5,428 | 


