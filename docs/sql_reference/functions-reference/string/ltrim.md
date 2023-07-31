---
layout: default
title: LTRIM
description: Reference material for LTRIM function
grand_parent: SQL functions
parent: String functions
great_grand_parent: SQL reference
---

# LTRIM

Removes all occurrences of optionally specified characters, `<trimchars_expr>`, from the left side of a source string `<srcstr_expr>`. If no `<trimchars_expr>` are specified, removes all occurrences of common whitespace (ASCII Decimal 32) characters from the left side of the specified source string.

## Syntax
{: .no_toc}

```sql
LTRIM(<expression1>[, <expression2>])
```
## Parameters 
{: .no_toc}

| Parameter        | Description                | Supported input types | 
| :--------------- | :------------------------- | :----------|
| `<expression1>`  | An expression that returns the string to be trimmed. | Any [string data types](../../general-reference/data-types.md#string).|
| `<expression2>` | Optional. An expression that returns characters to trim from the left side of the `<expression1>` string. If omitted, whitespace (ASCII Decimal 32) is assumed. | `TEXT` | 

## Return Types 
`TEXT`

## Examples
{: .no_toc}

Default whitespace trim.

The following example returns the default whitespace trim, as there is no additional parameters provided: 

```sql
SELECT
  LTRIM('  The Acceleration Cup     ');
```

**Returns**:

The Acceleration Cup     

This example displays a single character trim, with whitespace not specified and left as a remainder: 

```sql
SELECT
  LTRIM('xxx    The Acceleration Cup', 'x');
```

**Returns**:

The Acceleration Cup  

This example highlights a multiple character trim, with all specified characters removed, regardless of ordering: 

```sql
SELECT
  LTRIM('yyxxyx  The Acceleration Cup', 'xy');
```

**Returns**:

The Acceleration Cup  
