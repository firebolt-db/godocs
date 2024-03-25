---
layout: default
title: ASIN
description: Reference material for ASIN function
grand_parent: SQL functions
parent: Numeric functions
great_grand_parent: SQL reference
---

# ASIN

Calculates the arcsine. `ASIN` returns `NULL` if `<value>` is higher than 1.

## Syntax
{: .no_toc}

```sql
ASIN(<value>)
```

## Parameters 
{: .no_toc}

| Parameter | Description                                                                                                         | Supported input type | 
| :--------- | :------------------------------------------------------------------------------------------------------------------- | :-----------| 
<<<<<<< HEAD:docs/sql_reference/functions-reference/numeric/asin.md
| `<value>`   | The value which the `ASIN` function is applied to | `DOUBLE PRECISION` |

## Return Type 
`DOUBLE PRECISION`
=======
| `<value>`   | The value which the `ASIN` function is applied to | `DOUBLE_PRECISION` |

## Return Type 
`DOUBLE_PRECISION`
>>>>>>> rn/gh-pages:docs/sql-reference/functions-reference/asin.md

## Example
{: .no_toc}

The following example calculates the arc sine of `1.0`:
```sql
SELECT
    ASIN(1.0);
```

**Returns**: `1.5707963267948966`
