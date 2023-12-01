---
layout: default
title: NUMERIC data type
description: Describes the Firebolt implementation of the `NUMERIC` data type
nav_exclude: true
search_exclude: false
---

# NUMERIC data type
{:.no_toc}

This topic describes the Firebolt implementation of the `NUMERIC` data type.

* Topic ToC
{:toc}

## Overview

The `NUMERIC` data type is an exact numeric data type defined by its precision (total number of digits) and scale (number of digits to the right of the decimal point). 

`NUMERIC` has two optional input parameters: `NUMERIC(precision, scale)`

The maximum precision is 38. The scale value is bounded by the precision value `(scale<=precision)`. 

The precision must be positive, while the scale can be zero or positive.

The `DECIMAL` data type is a synonym to the `NUMERIC` data type.

### Default values for precision and scale

If the scale is not specified when declaring a column of `NUMERIC` data type, then it defaults to `NUMERIC(precision, min(9, precision))`

If both the precision and scale are not specified, then it defaults to `NUMERIC(38, 9)`

### Precision vs. scale

If the scale of a value to be stored is greater than the declared scale of the column, the system will round the value to the specified number of fractional digits. If the number of digits to the left of the decimal point exceeds the declared precision, minus the declared scale, an error results.

  ```sql
  SELECT CAST(100.76 AS NUMERIC(5,2)); -- 100.76
  SELECT CAST(100.76 AS NUMERIC(5,1)); -- 100.8
  SELECT(100.76 AS NUMERIC(3,1)); -- error
  ```
### Type conversion

1. **P1≠P2 or S1≠S2** (casting required)

    Any operation between two decimals with different precision and/or scale requires explicit casting of the input to the desired precision and scale. 

    ```sql
    f(NUMERIC(P1, S1), NUMERIC(P2, S2)) -> ERROR (P1≠P2 or S1≠S2) 
    ```
    where P1≠P2 or S1≠S2


2. **P1=P2 and S1=S2** (casting optional)

    If the two decimals have the same precision and scale, the result will implicitly cast to the same precision and scale. You can still explicitly cast to any other precision and scale.
  
    ```sql
    f(NUMERIC(P1, S1), NUMERIC(P1, S1)) -> NUMERIC(P1, S1))**
    ```
 
### Supported operators

**Operators:**

+<br>
-<br>
*<br>
/<br>