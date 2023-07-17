---
layout: default
title: ATAN
description: Reference material for ATAN function
grand_parent: SQL functions
parent: Numeric functions
---

# ATAN

Calculates the arc tangent of the real number returned by the specified expression `<expr>`.

## Syntax
{: .no_toc}

```sql
ATAN(<expression>)
```
## Parameters 
| Parameter | Description | Supported input types | 
| :-------- | :-----------| :------|
| `<expression>`  | The expression that the `ATAN` function is applied to | Any expression that evaluates to a real number |

## Return Types 
`DOUBLE PRECISION` 

## Example
{: .no_toc}

The following example returns the arc tangent of the specified literal value `90`:

```sql
SELECT
    ATAN(90);
```

**Returns**: `1.5596856728972892`
