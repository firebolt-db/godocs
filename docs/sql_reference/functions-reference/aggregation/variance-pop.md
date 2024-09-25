---
layout: default
title: VAR_POP
description: Reference material for VAR_POP
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Aggregation functions
published: true
---

# VAR\_POP

Computes the population standard deviation of all non-NULL numeric values produced by an expression.\\
For the sample variance, see [VAR_SAMP](variance-samp.md).


## Syntax
{: .no_toc}

```sql
VAR_POP([ DISTINCT ] <expression>)
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
- If there are no non-`NULL` input value, the result is `NULL`.
- If the input contains one `Inf` and/or `NaN` value, the result is `NaN`.

## Example
{: .no_toc}

Given the table `exams`, `var_pop` calculates the population variance of the grades:
{% include sql_examples/var_pop.md %}

{: .note}
> This function uses a numerically unstable algorithm.

