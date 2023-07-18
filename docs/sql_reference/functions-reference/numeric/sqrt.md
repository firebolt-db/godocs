---
layout: default
title: SQRT
description: Reference material for SQRT function
grand_parent: SQL functions
parent: Numeric functions
great_grand_parent: SQL reference
---

# SQRT

Returns the square root of a non-negative numeric expression.

## Syntax
{: .no_toc}

```sql
SQRT(<val>);
```

| Parameter | Description                                                                                                                                                       |
| :--------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<val>`   | Valid values include column names, functions that return a column with numeric values, and constant numeric values. Returns `NULL `if a negative value is given.  |

## Example
{: .no_toc}

```sql
SELECT
    SQRT(64);
```

**Returns**: `8`
