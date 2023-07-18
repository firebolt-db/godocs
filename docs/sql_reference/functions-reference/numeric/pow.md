---
layout: default
title: POW, POWER
description: Reference material for POW, POWER functions
grand_parent: SQL functions
parent: Numeric functions
great_grand_parent: SQL reference
---

# POW, POWER

Returns a number `<value>` raised to the specified power `<value>`.

## Syntax
{: .no_toc}

```sql
POW(<value>, <value>);
POWER(<value>, <value>);
```
## Parameters 
{: .no_toc}

| Parameter | Description                                                                                                         | Supported input types |
| :--------- | :------------------------------------------------------------------------------------------------------------------- |:------|
| `<value>`   | The base value of the exponent |`DOUBLE PRECISION` |
| `<value>`   | The power value of the exponent                                                                          | `DOUBLE PRECISION` |

## Return Types
`DOUBLE PRECISION`

## Example
{: .no_toc}
The following example calculates `2` to the power of `5`:
```sql
SELECT
    POW(2, 5);
```

**Returns**: `32`
