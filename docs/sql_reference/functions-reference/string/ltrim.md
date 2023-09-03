---
layout: default
title: LTRIM
description: Reference material for LTRIM function
grand_parent: SQL functions
parent: String functions
great_grand_parent: SQL reference
---

# LTRIM

Removes all occurrences of optionally specified characters, `<trim>`, from the left side of a source string `<expression>`. If no `<trim>` characters are specified, removes all occurrences of common whitespace (ASCII Decimal 32) characters from the left side of the specified source string.

## Syntax
{: .no_toc}

```sql
LTRIM(<expression>[, <trim>])
```
## Parameters 
{: .no_toc}

| Parameter        | Description                | Supported input types | 
| :--------------- | :------------------------- | :----------|
| `<expression>`  | An expression that returns the string to be trimmed. | `TEXT`|
| `<trim>` | Optional. An expression that returns characters to trim from the left side of the `<expression>` string. If omitted, whitespace (ASCII Decimal 32) is assumed. | `TEXT` | 

## Return Type 
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
