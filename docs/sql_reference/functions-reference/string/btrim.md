---
layout: default
title: BTRIM
description: Reference material for BTRIM function.
grand_parent: SQL functions
parent: String functions
great_grand_parent: SQL reference
---

# BTRIM

Removes all occurrences of optionally specified characters, `<trimchars_expr>`, from both sides of a source string `<srcstr_expr>`. If no `<trimchars_expr>` are specified, removes all occurrences of common whitespace (ASCII Decimal 32) characters from both sides of the specified source string.

## Syntax
{: .no_toc}

```sql
BTRIM(<expression1>[, <expression2>])
```

| Parameter        | Description                | Supported input types | 
| :--------------- | :------------------------- | :----------|
| `<expression1>`  | An expression that returns the string to be trimmed. The string can be any of the [string data types](../../general-reference/data-types.md#string).| `TEXT` | 
| `<expression2>` | Optional. An expression that returns characters to trim from both sides of the `<expression1>` string. If omitted, whitespace (ASCII Decimal 32) is assumed. | `TEXT` | 

## Return Types
`TEXT`

## Examples
{: .no_toc}

The following example returns a trimmed string with the default amount of whitespace applied: 

```sql
SELECT
  BTRIM('  The Acceleration Cup     ');
```
**Returns**:

The Acceleration Cup

This example returns the string without any `x`: 
```sql
SELECT
  BTRIM('xxThe Acceleration Cupxxx', 'x') 
```

**Returns**:

The Acceleration Cup

This example completes a multiple character trim, with all specified characters removed, regardless of ordering:

```sql
SELECT
  BTRIM('xyxyThe Acceleration Cupyyxx', 'xy') AS trmdstrng;
```

**Returns**:

The Acceleration Cups