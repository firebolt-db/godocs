---
layout: default
title: ASIN
description: Reference material for ASIN function
grand_parent: SQL functions
parent: Numeric functions
great_grand_parent: SQL reference
---

# ASIN

Calculates the arc sinus. `ASIN` returns `NULL` if `<value>` is higher than 1.

## Syntax
{: .no_toc}

```sql
ASIN(<value>)
```

| Parameter | Description                                                                                                         | Supported input type | 
| :--------- | :------------------------------------------------------------------------------------------------------------------- | :-----------| 
| `<value>`   | The value which the `ASIN` function is applied to | `DOUBLE_PRECISION` |

## Return Types 
`DOUBLE_PRECISION`

## Example
{: .no_toc}
The following example calculates the arc sine of `1.0`:
```sql
SELECT
    ASIN(1.0);
```

**Returns**: `1.5707963267948966`
