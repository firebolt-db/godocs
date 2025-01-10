---
layout: default
title: VAR_SAMP
description: Reference material for VAR_SAMP
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Aggregation functions
published: true
---

# VAR\_SAMP

Computes the sample variance of all non-`NULL` numeric values produced by an expression. The sample variance measures the average of the squared differences from the sample mean, indicating how spread out the values are within a sample.
For information about the population variance, which measures how spread out the values are within the full population, see [VAR_POP](variance-pop.md).

**Alias**: `VARIANCE`

## Syntax
{: .no_toc}

```sql
{ VARIANCE | VAR_SAMP }(<expression>)
```
## Parameters 
{: .no_toc}

| Parameter | Description               | Supported input types |
| :--------- | :----------------------------------- | :--------|
| `<expression>`  | An expression producing numeric values for which to calculate the sample variance. | `REAL`, `DOUBLE PRECISION` <!-- Any numeric type-->|

## Return Type
`VAR_SAMP` returns a result of type `DOUBLE PRECISION`. <!--for `REAL` and `DOUBLE PRECISION` input types.-->
<!-- `NUMERIC` for serial and `NUMERIC` input types (not yet supported)-->

### Special cases
- If there is at most one non-`NULL` input value, the result is `NULL`.
- If the input contains an `Inf` or `NaN` value, the result will be `NaN`.

## Example
{: .no_toc}

{% include sql_examples/var_samp.md %}

