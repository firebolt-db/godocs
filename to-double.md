---
layout: default
title: TO_DOUBLE
description: Reference material for TO_DOUBLE function
parent: String functions
published: false
---

# TO\_DOUBLE

Converts a string to a numeric `DOUBLE PRECISION` data type.

## Syntax
{: .no_toc}

```sql
TO_DOUBLE(<expression>)
```

## Parameters 
{: .no_toc}

| Parameter       | Description                      | Supported input types                                                           | 
| :---------------| :--------------------------------|:--------------------------------------------------------------------------------|
| `<expression>`  | An expression to become a double | Any numeric data type or numeric characters that resolve to a `TEXT` data type. |

## Return Type
`DOUBLE PRECISION`

## Example
{: .no_toc}
The following example takes the input of `100` and returns the value as a `DOUBLE PRECISION` type.
```sql
SELECT
	TO_DOUBLE('100');
```

**Returns**: `100`
