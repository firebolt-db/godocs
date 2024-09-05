---
layout: default
title: LTRIM
description: Reference material for LTRIM function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: String functions
---

# LTRIM

Removes the longest string containing only characters in `<trim_characters>` from the left side of the source string `<expression>`. If no `<trim_characters>` parameter is specified, the longest string containing only whitespace characters (ASCII Decimal 32) is removed from the left side of the specified source string `<expression>`.

## Syntax
{: .no_toc}

```sql
LTRIM(<expression>[, <trim_characters>])
```

## Parameters 
{: .no_toc}

| Parameter        | Description                | Supported input types | 
| :--------------- | :------------------------- | :----------|
| `<expression>`  | An expression that returns the string to be trimmed. | `TEXT` |
| `<trim_characters>` | Optional. An expression that returns characters to trim from the left side of the `<expression>` string. If omitted, whitespace (ASCII Decimal 32) is trimmed. | `TEXT` | 

## Return Type 
`TEXT`

## Examples
{: .no_toc}

The following example trims the character `x` from the left side of a string:

```sql
SELECT
  LTRIM('xxThe Acceleration Cupxxx', 'x') 
```

**Returns**:

```sql
'The Acceleration Cupxxx'
```

The following example trims the characters `x` and `y` from the left side of a string. Note that the ordering of characters in `<trim_characters>` is irrelevant:

```sql
SELECT
  LTRIM('xyxyThe Acceleration Cupyyxx', 'xy');
```

**Returns**:

```sql
'The Acceleration Cupyyxx'
```

The following example omits the `<trim_characters>` parameter, and thus trims whitespace from the left side of a string: 

```sql
SELECT
  LTRIM('   The Acceleration Cup     ');
```

**Returns**:

```sql
'The Acceleration Cup     '
```
