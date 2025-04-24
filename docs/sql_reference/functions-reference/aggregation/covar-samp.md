---
layout: default
title: COVAR_SAMP
description: Reference material for COVAR_SAMP
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Aggregation functions
published: true
---

# COVAR\_SAMP

Computes the sample covariance between two numeric expressions. If either one of expressions is `NULL` - that input row is ignored.
Use this when analyzing a sample rather than an entire population. For covariance of population see [COVAR_POP](covar-pop.md).

## Covariance vs Correlation

**Covariance** and **correlation** both describe how two variables change together, but they do so in different ways:

- **Covariance** measures the **direction** of the relationship between two variables:
  - Positive covariance: variables tend to increase together.
  - Negative covariance: one increases as the other decreases.
  - Its value is **unbounded** and depends on the units of the variables, making it hard to interpret on its own.

- **Correlation**, specifically **Pearson correlation**, standardizes the relationship:
  - It is the **normalized version of covariance**, giving a unitless measure between **-1 and 1**.
  - This makes it easier to compare the strength of relationships between different pairs of variables.

For information on correlation see [CORR](corr.md)

## Syntax
{: .no_toc}

```sql
COVAR_SAMP(<expr1>, <expr2>)
```
## Parameters 
{: .no_toc}

| Parameter | Description               | Supported input types |
| :--------- | :----------------------------------- | :--------|
| `<expr1>`  | First numeric expression to use for covariance computation. | `DOUBLE PRECISION`
| `<expr2>`  | Second numeric expression to use for covariance computation. | `DOUBLE PRECISION`

## Return Type
`COVAR_SAMP` returns a result of type `DOUBLE PRECISION`.


## Example
{: .no_toc}

## Examples

The code examples use `PlayStats` table from the sample `UltraFast` database.

**Example**

The `CurrentLevel` and `CurrentScore` variables are highly correlated

```sql
SELECT COVAR_SAMP(CurrentScore, CurrentLevel) FROM PlayStats
```

**Returns**

`473291.6614849927`

**Example**

But `CurrentLevel` and `CurrentScore` variables are not correlated at all

```sql
SELECT COVAR_SAMP(CurrentLevel, CurrentSpeed) FROM PlayStats
```

**Returns**

`0.040317002824098884`

