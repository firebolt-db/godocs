---
layout: default
title: CBRT
description: Reference material for CBRT function
grand_parent: SQL functions
parent: Numeric functions
---

# CBRT

Returns the cubic-root of a non-negative numeric expression.

## Syntax
{: .no_toc}

```sql
CBRT(<val>);
```

| Parameter | Description                                                                                                         |
| :--------- | :------------------------------------------------------------------------------------------------------------------- |
| `<val>`   | Valid values include column names, functions that return a column with numeric values, and constant numeric values. |

## Example
{: .no_toc}

```sql
SELECT
    CBRT(8);
```

**Returns**: `2`
