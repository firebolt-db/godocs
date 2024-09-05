---
layout: default
title: MOD
description: Reference material for MOD function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Numeric functions
---

# MOD

Calculates the remainder after dividing two values, `<value_n>` / `<value_d>.`

## Syntax
{: .no_toc}

```sql
MOD(<value_n>,<value_d>)
```
## Parameters 
{: .no_toc}

| Parameter   | Description                              | Supported input types |
| :---------- | :--------------------------------------- | :-------------------- |
| `<value_n>` | The numerator of the division equation   | `INT`, `BIGINT`       |
| `<value_d>` | The denominator of the division equation | `INT`, `BIGINT`       |

## Return Type
`BIGINT` if one of the inputs is `BIGINT`. `INT`, otherwise.

## Example
{: .no_toc}

The following example returns the remainder of `45` and `7`: 

```sql
SELECT
    MOD(45, 7);
```

**Returns**: `3`
