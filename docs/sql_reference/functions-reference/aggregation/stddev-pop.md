---
layout: default
title: STDDEV_POP
description: Reference material for STDDEV_POP
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Aggregation functions
published: true
---

# STDDEV\_POP

Computes the population standard deviation of all non-`NULL` numeric values produced by an expression. The population standard deviation shows how spread out the values in a population are, by measuring the average distance of each value from the population's mean.
For information about the sample standard deviation, which estimates the spread of values across sample rather than the full population, see [STDDEV_SAMP](stddev-samp.md).

## Syntax
{: .no_toc}

```sql
STDDEV_POP([ DISTINCT ] <expression>)
```
## Parameters 
{: .no_toc}

| Parameter | Description               | Supported input types |
| :--------- | :----------------------------------- | :--------|
| `<expression>`  | An expression producing numeric values for which to calculate the population standard deviation. | `REAL`, `DOUBLE PRECISION` <!-- Any numeric type-->|

## Return Type
`DOUBLE PRECISION` <!--for `REAL` and `DOUBLE PRECISION` input types.-->
<!-- `NUMERIC` for serial and `NUMERIC` input types (not yet supported)-->

### Special cases
- If there are no non-`NULL` input values, the result is `NULL`.
- If the input contains an `Inf` or `NaN` value, the result will be `NaN`.

## Example
{: .no_toc}

{% include sql_examples/stddev_pop.md %}

