---
layout: default
title: ATAN2
description: Reference material for ATAN2 function
grand_parent: SQL functions
parent: Numeric functions
great_grand_parent: SQL reference
---

# ATAN2

Two-argument arc tangent function. Calculates the angle, in radians, between the specified positive x-axis value and the ray from the origin to the point `(y,x)`.

## Syntax
{: .no_toc}

```sql
ATAN2(<value>,<value>)
```
## Parameters
{: .no_toc}

| Parameter   | Description | Supported input types | 
| :---------- | :-----------| :-------| 
| `<value>`  | The `y value` in the arc tangent calculation | `DOUBLE PRECISION` |
| `<value>`  | The `x value` in the arc tangent calculation | `DOUBLE PRECISION` |

## Return Types
`DOUBLE PRECISION`

## Example
{: .no_toc}

The following example returns the arc tangent with the values `(11, 3)`:
```sql
SELECT ATAN2(11,3);
```

**Returns:**
`1.3045442776439713`
