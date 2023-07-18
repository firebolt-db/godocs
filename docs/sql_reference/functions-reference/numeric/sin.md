---
layout: default
title: SIN
description: Reference material for SIN function
grand_parent: SQL functions
parent: Numeric functions
great_grand_parent: SQL reference
---

# SIN

Calculates the sinus.

## Syntax
{: .no_toc}

```sql
SIN(<val>)
```

| Parameter | Description                                                                                                         |
| :--------- | :------------------------------------------------------------------------------------------------------------------- |
| `<val>`   | Valid values include column names, functions that return a column with numeric values, and constant numeric values. |

## Example
{: .no_toc}

```sql
SELECT
    SIN(90);
```

**Returns**: `0.8939966636005579`
