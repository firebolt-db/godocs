---
layout: default
title: CONVERT_FROM
description: Reference material for CONVERT_FROM function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Binary functions
published: true
---

# CONVERT_FROM

Converts a binary string from a specified encoding to a sql `TEXT` type, using the database's encoding.

## Syntax

{: .no_toc}

```sql
CONVERT_FROM
(<bytes>, <src_encoding>)
```

## Parameters

{: .no_toc}

| Parameter        | Description                                                                                                                                                                          | Supported input types |
|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| `<bytes>`        | A sequence of bytes representing text in `<src_encoding>`.                                                                                                                             | `BYTEA`               |
| `<src_encoding>` | The encoding from which the src `<bytes>` are derived, must be constant. The supported source encoding aligns with those supported in the [ICU library](https://icu.unicode.org/). | `TEXT`                |  

## Return Type

`TEXT`

## Errors

If `<src_encoding>` is invalid, an error is thrown.
If `<bytes>` are malformed according to `<src_encoding>`, the behavior is undefined. For example, in UTF-8, malformed bytes are converted to � character.

## Examples

{: .no_toc}

The following examples use databases encoded UTF-8 and convert the given bytes to `TEXT`. All results are displayed in UTF-8):

```sql
SELECT CONVERT_FROM('\x1212003100'::BYTEA, 'utf16');
```

**Returns**: `ሒ1�`. Explanation: `1212` corresponds to the UTF-16 representation of `ሒ`, and `0031` represents the character `1` in UTF-16. Because `00` is single byte, it is invalid in UTF-16, and produces the character `�`.

```sql
SELECT CONVERT_FROM('\x31a031ffffffff'::BYTEA, 'windows-1252');
```

**Returns**: `1 1ÿÿÿÿ`. Explanation: `31` is the windows-1252 representation of `1`, and `a0` is the windows-1252 representation of ` `, a ([non-breaking space character](https://en.wikipedia.org/wiki/Non-breaking_space)), and `ff` is the windows-1252 representation of `ÿ`.
