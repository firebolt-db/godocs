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

Computes the sample variance of all non-NULL numeric values produced by an expression.\\
For the population variance, see [VAR_POP](variance-pop.md).

**Alias**: `VARIANCE`

## Syntax
{: .no_toc}

```sql
{ VARIANCE | VAR_SAMP }([ DISTINCT ] <expression>)
```
## Parameters 
{: .no_toc}

| Parameter | Description               | Supported input types |
| :--------- | :----------------------------------- | :--------|
| `<expression>`  | An expression producing numeric values for which to calculate the standard sample deviation. | `REAL`, `DOUBLE PRECISION` <!-- Any numeric type-->|

## Return Type
`DOUBLE PRECISION` <!--for `REAL` and `DOUBLE PRECISION` input types.-->
<!-- `NUMERIC` for serial and `NUMERIC` input types (not yet supported)-->

### Special cases
- If there is at most one non-`NULL` input value, the result is `NULL`.
- If the input has more than one non-`NULL` input value and the input contains `Inf` and/or `NaN`, the results is `NaN`.

## Example
{: .no_toc}

For this example, we create a new table `exams` and calculate the sample variance of the grades:
{% include sql_examples/var_samp.md %}

{: .note}
> This function uses a numerically unstable algorithm.

