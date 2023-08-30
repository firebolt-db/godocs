---
layout: default
title: RTRIM
description: Reference material for RTRIM function
grand_parent: SQL functions
parent: String functions
great_grand_parent: SQL reference
---

# RTRIM

Removes all occurrences of optionally specified characters, `<trimchars_expr>`, from the right side of a source string `<srcstr_expr>`. If no `<trimchars_expr>` are specified, removes all occurrences of common whitespace (ASCII Decimal 32) characters from the right side of the specified source string.

## Syntax
{: .no_toc}

```sql
RTRIM(<expression1>[, <expression2>])
```
## Parameters 
{: .no_toc}

| Parameter        | Description                |
| :--------------- | :------------------------- |
| `<expression1>`  | An expression that returns the string to be trimmed. The string can be any of the [string data types](../../general-reference/data-types.md#string).|
| `<expression2>` | Optional. An expression that returns characters to trim from the right side of the `<expression3>` string. If omitted, whitespace (ASCII Decimal 32) is assumed. |

## Return Types 
Same as input type 

## Examples
{: .no_toc}

The following example returns the string with the default whitespace trim: 

```sql
SELECT
  RTRIM('  Level three     ') AS currentlevel;
```

**Returns**: Level three



The following example performs a single character trim, with whitespace not specified and left as a remainder:

```sql
SELECT
  RTRIM('Level three  xxx', 'x') AS currentlevel;
```

**Returns**: Level three

This next example performs a multiple character trim, with all specified characters removed, regardless of ordering:

```sql
SELECT
  RTRIM('  Level threeyyxxy', 'xy') AS currentlevel;
```

**Returns**: Level three 