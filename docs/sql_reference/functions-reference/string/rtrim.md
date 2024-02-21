---
layout: default
title: RTRIM
description: Reference material for RTRIM function
grand_parent: SQL functions
parent: String functions
great_grand_parent: SQL reference
---

# RTRIM

Removes the longest string containing only characters in `<trim_characters>` from the right side of the source string `<expression>`. If no `<trim_characters>` parameter is specified, the longest string containing only whitespace characters (ASCII Decimal 32) is removed from the right side of the specified source string `<expression>`.

## Syntax
{: .no_toc}

```sql
RTRIM(<expression>[, <trim_characters>])
```

## Parameters 
{: .no_toc}

| Parameter        | Description                | Supported input types | 
| :--------------- | :------------------------- | :----------|
| `<expression>`  | An expression that returns the string to be trimmed. | `TEXT` |
| `<trim_characters>` | Optional. An expression that returns characters to trim from the right side of the `<expression>` string. If omitted, whitespace (ASCII Decimal 32) is trimmed. | `TEXT` | 

## Return Types 
`TEXT`

## Examples
{: .no_toc}

The following example trims the character `x` from the right side of a string:

```sql
SELECT
  RTRIM('xxThe Acceleration Cupxxx', 'x') 
```

**Returns**:

`'xxThe Acceleration Cup'`

The following example trims the characters `x` and `y` from the right side of a string. Note that the ordering of characters in `<trim_characters>` is irrelevant:

```sql
SELECT
  RTRIM('xyxyThe Acceleration Cupyyxx', 'xy');
```

**Returns**:

`'xyxyThe Acceleration Cup'`

The following example omits the `<trim_characters>` parameter, and thus trims whitespace from the right side of a string: 

```sql
SELECT
  RTRIM('   The Acceleration Cup     ');
```

**Returns**:

`'   The Acceleration Cup'`
