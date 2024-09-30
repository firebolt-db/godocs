---
layout: default
title: STDDEV_SAMP
description: Reference material for STDDEV_SAMP
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Aggregation functions
published: true
---

# STDDEV\_SAMP

Computes the sample standard deviation of all non-`NULL` numeric values produced by an expression. 
The sample standard deviation measures how spread out values are in a sample by calculating the square root of the average of squared deviations from the sample mean, using a correction for sample size. For information about the population standard deviation, which estimates the spread of values in the full population, see [STDDEV_POP](stddev-pop.md).

**Alias**: `STDDEV`


## Syntax
{: .no_toc}

```sql
{ STDDEV | STDDEV_SAMP }([ DISTINCT ] <expression>)
```
## Parameters 
{: .no_toc}

| Parameter | Description               | Supported input types |
| :--------- | :----------------------------------- | :--------|
| `<expression>`  | An expression producing numeric values for which to calculate the sample standard deviation. | `REAL`, `DOUBLE PRECISION` <!-- Any numeric type-->|

## Return Type
`STDDEV_SAMP` returns a result of type `DOUBLE PRECISION`. <!--for `REAL` and `DOUBLE PRECISION` input types.-->
<!-- `NUMERIC` for serial and `NUMERIC` input types (not yet supported)-->

### Special cases
- If there is at most one non-`NULL` input value, the result is `NULL`.
- If the input contains an `Inf` or `NaN` value, the result will be `NaN`.

## Example
{: .no_toc}

{% include sql_examples/stddev_samp.md %}

