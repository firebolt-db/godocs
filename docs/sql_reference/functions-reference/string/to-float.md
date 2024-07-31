---
layout: default
title: TO_FLOAT
description: Reference material for TO_FLOAT function
grand_parent: SQL functions
parent: String functions
published: false
---

# TO\_FLOAT

Converts a string to a numeric `REAL` data type.

## Syntax
{: .no_toc}

```sql
TO_FLOAT(<expression>)
```
## Parameters 
{: .no_toc}

| Parameter | Description                                                                                              | Supported input types |
| :--------- | :-------------------------------------------------------------------------------------------------------- | :----------|
| `<expression>`  | An expression to become a float | Any numeric data type or numeric characters that resolve to a `TEXT` data type. |

## Return Type
`REAL` 

## Example
{: .no_toc}

The following example takes the input of `10.5` and returns the value as a `FLOAT`.

```sql
SELECT
	TO_FLOAT('10.5');
```

**Returns**: `10.5`
