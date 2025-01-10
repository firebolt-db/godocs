---
layout: default
title: PERCENTILE_CONT
description: Reference material for PERCENTILE_CONT aggregate function
parent: Aggregation functions
published: true
---

# PERCENTILE_CONT

Returns the value at the position in an ordered list where a specified percentage falls. If the percentile value does not correspond to an exact data point in the dataset, `PERCENTILE_CONT` interpolates between the two closest values surrounding the specified percentile to estimate the result. The interpolation is based on the dataset's ascending or descending order. 

For example, if you want to find the `40%` percentile on the ordered list `[10,20,30]`, position `1` corresponds to the value `10`, and position `2` corresponds to the value `20`. The position that corresponds to the specified percentile is calculated as `1` plus the percentile multiplied by (`n-1`), where `n` is the number of data points in the set. Then, the `40th` percentile corresponds to `1 + 0.40 * (3 - 1) = 1.8`, which falls between position `1` and `2`, or the values `10` and `20`. Because the desired percentile does not correspond to an exact data point, `PERCENTILE_CONT` interpolates an estimated value using the following formula:

**Formula to interpolate values**
```text
RN = 1 + <percentile> * (<number_of_values> - 1)
CRN = CEILING(RN)
FRN = FLOOR(RN)
EXP_CRN = <sorted_expression>[CRN]
EXP_FRN = <sorted_expression>[FRN]
If RN is a whole number, RESULT = <ordered_set>[RN].
If RN is not a whole number, RESULT = (CRN - RN) * EXP_FRN + (RN - FRN) * EXP_CRN.
```

**Formula definitions**
In the previous formula for interpolation, the following apply:

- `RN`: The row number of the exact position of a value within an ordered dataset.
- `CRN`: The ceiling row number, which determines the upper row position for interpolation.
- `FRN`: The floor row number, which determines the lower row position for interpolation.
- `EXP_CRN`: The value from the sorted dataset that corresponds to the `CRN`, used as the **upper** bound in percentile calculations when interpolation is required.
- `EXP_FRN`: The value from the sorted dataset that corresponds to the FRN, used as the **lower** bound in percentile calculations when interpolation is required.
- `<sorted_expression>`: The ordered list of values derived from the input expression, arranged in ascending or descending order, used as the basis for percentile calculations.
- `<number_of_values>`: The total count of values within the input expression, used to calculate the exact position of a specified percentile by multiplying the percentile (as a decimal) by (`number_of_values` − 1). This calculated position then identifies the two values in the sorted dataset used for interpolation.

In the previous example, `PERCENTILE_CONT` estimates the value between `10` and `20` in the ordered list `[10,20,30]` to find the 40th percentile as follows:

`result = (CRN - RN) * (EXP_FRN) + (RN - FRN) * EXP_CRN = (2 - 1.8) * 10 + (1.8 - 1) * 20 = 18`.

In the previous example, the set `[10,20,30]` is in ascending order. If the set were in descending order as `[30,20,10]`, the `40th` percentile would correspond to:

`result = (CRN - RN) * (EXP_FRN) + (RN - FRN) * EXP_CRN = (2 - 1.8) * 30 + (1.8 - 1) * 20 = 22`.

## Syntax

{: .no_toc}

```sql
PERCENTILE_CONT
( <percentile> ) WITHIN GROUP ( ORDER BY <expression> [ { ASC | DESC } ] )
```

## Parameters

{: .no_toc}

| Parameter      | Description                                                                              | Supported input types                                  | 
|:---------------|:-----------------------------------------------------------------------------------------|:-------------------------------------------------------|
| `<percentile>` | The desired percentile position within the ordered dataset.                                                        | `DOUBLE PRECISION`, `REAL` literal between 0.0 and 1.0 |
| `<sorted_expression>` | The expression used to calculate the percentile, which is sorted in ascending or descending order prior to calculation. | `DOUBLE PRECISION`, `REAL`, `BIGINT`, `INT`            | 

## Return Types

`PERCENTILE_CONT` returns a value of type `DOUBLE PRECISION`.
- This function ignores `NULL` values.
- This function returns `NULL` if the input is either empty or contains only `NULL` values.

## Examples

{: .no_toc}

These calculations use 1-based indexing, where the first element is at position `1`.

{% include sql_examples/percentile_cont.md %}