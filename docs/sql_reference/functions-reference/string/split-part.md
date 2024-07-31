---
layout: default
title: SPLIT_PART
description: Reference material for SPLIT_PART function
grand_parent: SQL functions
parent: String functions
---

# SPLIT_PART

Splits `<string>` at occurrences of `<delimiter>` and returns the `<index>`'th field, with 1 being the first index.
If `<index>` is negative, returns the `abs(<index>)`'th-from-last field.
If `<delimiter>` is empty, `<string>` is returned at `<index>` 1.
If `abs(<index>)` is larger than the number of fields, returns an empty string.
The function raises an error for `<index>` 0.

## Syntax
{: .no_toc}

```sql
SPLIT_PART(<string>, <delimiter>, <index>)
```

## Parameters 
{: .no_toc}

| Parameter     | Description                                                        | Supported input types |
| :------------ | :----------------------------------------------------------------- | :-------------------- |
| `<string>`    | A value expression evaluating to the string to be split.           | `TEXT`                |
| `<delimiter>` | A value expression evaluating to the delimiter character sequence. | `TEXT`                |
| `<index>`     | The index from which to return the substring.                      | `INTEGER`             |

## Return Type
`TEXT`

## Examples
{: .no_toc}

```sql
SELECT
	SPLIT_PART('hello#world','#',1) AS res;
```

**Returns**: `'hello'`

```sql
SELECT
	SPLIT_PART('this|is|my|test', '|', -2) AS res;
```

**Returns**: `'my'`

```sql
SELECT
	SPLIT_PART('hello world', '', 1) AS res;
```

**Returns**: `hello world`

```sql
SELECT
	SPLIT_PART('hello world', '', 7) AS res;
```

**Returns**: `''`
