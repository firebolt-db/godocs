---
layout: default
title: STDDEV_SAMP
description: Reference material for STDDEV_SAMP
parent: Aggregation functions
published: false
---

# STDDEV\_SAMP

Computes the standard deviation of a sample consisting of a numeric expression.

## Syntax
{: .no_toc}

```sql
STDDEV_SAMP(<expression>)
```
## Parameters 
{: .no_toc}

| Parameter | Description               | Supported input types |
| :--------- | :----------------------------------- | :--------|
| `<expression>`  | The expression for calculating the standard deviation. | Any numeric type | 

## Return Type
`DOUBLE PRECISION`

## Example
{: .no_toc}

Consider the following table `tournament_information`, which contains the name of the tournament and the total prize dollars for the tournament: 

| name | prizedollars | 
|:-------| :--------|
| The Snow Park Grand Prix | 20903	| 
| The Acceleration Championship | 19274	|
The Acceleration Trials | 13877 | 


`STDDEV_SAMP` returns the standard deviation for the values as a `DOUBLE PRECISION`.

```sql
SELECT
	STDDEV_SAMP(prizedollars)
FROM
	tournament_information;
```

**Returns**: `3,677.5427937686873`
