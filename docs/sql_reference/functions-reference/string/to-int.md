---
layout: default
title: TO_INT
description: Reference material for TO_INT function
grand_parent: SQL functions
parent: String functions
---

# TO\_INT

Converts a string to a numeric `INTEGER` data type.

## Syntax
{: .no_toc}

```sql
TO_INT(<expression>)
```

| Parameter | Description                                                                                              |
| :--------- | :-------------------------------------------------------------------------------------------------------- |
| `<expression>`  | A numeric data type expression that resolves to a `TEXT` data type. |

## Return Types
This function returns `NUMERIC` types. 

## Example
{: .no_toc}

The following examplesadjusts the inputted string value as the integer `10`: 
```sql
SELECT
	TO_INT('10');
```

**Returns**: `10`
