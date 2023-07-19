---
layout: default
title: SIGN
description: Reference material for SIGN function
grand_parent: SQL functions
parent: Numeric functions
great_grand_parent: SQL reference
---

# SIGN

Returns the sign of a number according to the table below.

## Syntax

```sql
SIGN(<value>)
```


## Parameters
{: .no_toc}

| Parameter | Description                         |Supported input types |
| :--------- | :----------------------------------- | :---------------------|
| `value` | Any expression that evaluates to a numeric data type. | `DOUBLE PRECISION` |

## Return Types
`DOUBLE PRECISION` 

## Examples

The following examples highlight what can be returned with the `SIGN` function: 
| If               | Returns |
| :--              | :------ |
| `<value>` \< `0` | `-1`   |
| `<value>` = `0`  | `0`    |
| `<value>` \> `0` | `1`    |

```sql
SIGN(5)
```

**Returns**: `1`

```sql
SIGN(-1.35E-10)
```

**Returns**: `-1`

```sql
SIGN(0)
```

**Returns**: `0`
