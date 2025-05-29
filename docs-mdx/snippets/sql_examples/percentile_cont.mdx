**Example**

The following code example calculates the 20th percentile of values from a generated series ranging from `0` to `5`, and returns it as `result`:

``` sql
SELECT PERCENTILE_CONT(0.2) WITHIN GROUP (ORDER BY x) as result FROM GENERATE_SERIES(0, 5) as x;
```

**Returns**

| result (DOUBLE PRECISION) |
| :--- |
| 1 |

The previous code example calculates the 20th percentile from a series that contains the following six values: `0`, `1`, `2`, `3`, `4`, and `5`. The position for the 20th percentile is calculated as follows: `RN = 1 + 0.2 * (6 - 1) = 2`. Since the row number is a whole number, it corresponds directly to the value at position `2`, which is `EXP_RN = 1`, using one-based indexing. 

**Example**

The following code example calculates the 20th percentile of values from a generated series ranging from `0` to `6`, interpolates the position, and returns it as `result`:

``` sql
SELECT PERCENTILE_CONT(0.2) WITHIN GROUP (ORDER BY x) as result FROM GENERATE_SERIES(0, 6) as x;
```

**Returns**

| result (DOUBLE PRECISION) |
| :--- |
| 1.2000000000000002 |

The previous code example calculates the 20th percentile from a series that contains the following seven values: `0`, `1`, `2`, `3`, `4`, `5`, and `6`. The position for the 20th percentile is calculated as follows: `RN = 1 + 0.2 * (7 - 1) = 2.2`. Since `2.2` is not a whole number, `PERCENTILE_CONT` interpolates the position as follows:

* The `CRN` is `CEILING(2.2) = 3`.
* The `FRN` is `FLOOR(2.2) = 2`.
* The `EXP_CRN` is the value at position `3` of the ordered set which is `2` using one-based indexing.
* The `EXP_FRN` is the value at position `2` of the ordered set which is `1` using one-based indexing.
* The result is `(CRN - RN) * EXP_FRN + (RN - FRN) * EXP_CRN` which is `(3 − 2.2) × 1 + (2.2 − 2) × 2 = 0.8 + 0.4 = 1.2`.