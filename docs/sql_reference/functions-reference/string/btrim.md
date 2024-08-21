---
layout: default
title: BTRIM
description: Reference material for BTRIM function.
parent: String functions
---

# BTRIM

Removes the longest string containing only characters in `<trim_characters>` from both sides of the source string `<expression>`. If no `<trim_characters>` parameter is specified, the longest string containing only whitespace characters (ASCII Decimal 32) is removed from both sides of the specified source string `<expression>`.

## Syntax
{: .no_toc}

```sql
BTRIM(<expression>[, <trim_characters>])
```

## Parameters
{: .no_toc}

| Parameter        | Description                | Supported input types | 
| :--------------- | :------------------------- | :----------|
| `<expression>`  | An expression that returns the string to be trimmed. | `TEXT` | 
| `<trim_characters>` | Optional. An expression that returns characters to trim from both sides of the `<expression>` string. If omitted, whitespace (ASCII Decimal 32) is trimmed. | `TEXT` | 

## Return Type
`TEXT`

## Examples
{: .no_toc}

The following example trims the character `x` from both sides of a string:

```sql
SELECT
  BTRIM('xxThe Acceleration Cupxxx', 'x') 
```

**Returns**:

```sql
'The Acceleration Cup'
```

The following example trims the characters `x` and `y` from both sides of a string. Note that the ordering of characters in `<trim_characters>` is irrelevant:

```sql
SELECT
  BTRIM('xyxyThe Acceleration Cupyyxx', 'xy');
```

**Returns**:

```sql
'The Acceleration Cup'
```

The following example omits the `<trim_characters>` parameter, and thus trims whitespace from both sides of a string: 

```sql
SELECT
  BTRIM('   The Acceleration Cup     ');
```

**Returns**:

```sql
'The Acceleration Cup'
```
