---
layout: default
title: COT
description: Reference material for COT function
grand_parent: SQL functions
parent: Numeric functions
great_grand_parent: SQL reference
---

# COT

Calculates the cotangent.

## Syntax
{: .no_toc}

```sql
COT(<exp>)
```

| Parameter | Description                                           |
| :--------- | :----------------------------------------------------- |
| `<exp>`   | Any expression that evaluates to a numeric data type. |

## Example
{: .no_toc}

```sql
SELECT
    COT(180);
```

**Returns**: `0.7469988144140444`
