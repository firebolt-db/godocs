---
layout: default
title: BTRIM
description: Reference material for BTRIM function.
great_grand_parent: SQL reference
grand_parent: SQL functions
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

{% include sql_examples/btrim.md %}

