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

Computes the sample standard deviation of all non-NULL numeric values produced by an expression.\\
For the population standard deviation, see [STDDEV_POP](stddev-pop.md).

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
| `<expression>`  | An expression producing numeric values for which to calculate the standard sample deviation. | `REAL`, `DOUBLE PRECISION` <!-- Any numeric type-->|

## Return Type
`DOUBLE PRECISION` <!--for `REAL` and `DOUBLE PRECISION` input types.-->
<!-- `NUMERIC` for serial and `NUMERIC` input types (not yet supported)-->

### Special cases
- If there is at most one non-`NULL` input value, the result is `NULL`.
- If the input has more than one non-`NULL` input value and the input contains `Inf` and/or `NaN`, the results is `NaN`.

## Example
{: .no_toc}

Given the table `exams` that has the column `grade`:
{% include sql_examples/stddev_samp.md %}

