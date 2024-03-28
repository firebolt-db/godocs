---
layout: default
title: APPROX_PERCENTILE
description: Reference material for APPROX_PERCENTILE
grand_parent: SQL functions
parent: Aggregation functions
great_grand_parent: SQL reference
published: false
---

# APPROX\_PERCENTILE

Returns an approximate value for the specified percentile based on the range of numbers returned by the input expression.

For example, if you run `APPROX_PERCENTILE` with a specified `<value>` of .75 on a column with 2,000 numbers, and the function returned `655`, then this would indicate that 75% of the 2,000 numbers in the column are less than 655.

The number returned is not necessarily in the original range of numbers.

## Syntax
{: .no_toc}

```sql
APPROX_PERCENTILE(<expression>,<value>)
```

## Parameters 
{: .no_toc}

| Parameter   | Description                                   | Supported input types | 
| :----------- | :---------------------------------------------------- | :-----------| 
| `<expression>`    | A valid expression, such as a column name, that evaluates to numeric values | `<column>` name that evaluates to numeric values | 
| `<value>` | The percentage value for the function | A constant real number greater than or equal to 0.0 and less than 1 | 

## Return Type
`DOUBLE PRECISION`

## Example
{: .no_toc}

The following example accesses the `currentscore` column of videogame players from the `playstats` table. This code displays `APPROX_PERCENTILE` of 50% of the number range in `playstats`: &#x20;

```sql
SELECT
	APPROX_PERCENTILE(currentscore, 0.5) 
FROM
    playstats;
```

**Returns**: `276,644.5`

