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

Computes the population variance of all non-`NULL` numeric values produced by an expression. The population variance measures the average of the squared differences from the population mean, indicating how spread out the values are within the entire population. For information about the sample variance, which measures how spread out the values are within a sample, see [VAR_SAMP](variance-samp.md).


## Syntax
{: .no_toc}

```sql
VAR_POP(<expression>)
```
## Parameters 
{: .no_toc}

| Parameter | Description               | Supported input types |
| :--------- | :----------------------------------- | :--------|
| `<expression>`  | An expression producing numeric values for which to calculate the population variance. | `REAL`, `DOUBLE PRECISION` <!-- Any numeric type-->|

## Return Type
`VAR_POP` returns a result of type `DOUBLE PRECISION`. <!--for `REAL` and `DOUBLE PRECISION` input types.-->
<!-- `NUMERIC` for serial and `NUMERIC` input types (not yet supported)-->

### Special cases
- If there are no non-`NULL` input values, the result is `NULL`.
- If the input contains an `Inf` or `NaN` value, the result will be `NaN`.

## Example
{: .no_toc}

{% include sql_examples/var_pop.md %}

