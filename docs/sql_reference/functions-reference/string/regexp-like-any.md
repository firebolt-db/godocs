---
layout: default
title: REGEXP_LIKE_ANY
description: Reference material for REGEXP_LIKE_ANY function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: String functions
---

# REGEXP_LIKE_ANY

Checks whether a given string matches any regular expression pattern from a specified list of patterns. Returns `FALSE` if it doesn’t match, or `TRUE` if it matches.

## Syntax
{: .no_toc}

```sql
REGEXP_LIKE_ANY(<expression>, ['<pattern1>', '<pattern2>', ...])
```
## Parameters 
{: .no_toc}

| Parameter      | Description    |Supported input types         |
| :------------- | -------------- | :--------------------------- |
| `<expression>` | The input string or column to be evaluated against the regular expression patterns.  | `TEXT`  |
| `<pattern>`    | A list of regular expression patterns to match against the expression.  | ARRAY[`TEXT`] where each element complies to the [RE2 regular expression](https://github.com/google/re2/wiki/Syntax) syntax |

## Return Type
`BOOLEAN` 

## Examples

The following code example checks whether the string `123` matches either the `[a-z]` expression, which specifies any lowercase letter, or the `[1-9]+` expression, which specifies one or more digits:

```sql
SELECT
    REGEXP_LIKE_ANY('123',['[a-z]','[1-9]+']);
```
 
**Returns**: The function returns `TRUE` because the string `'123'` matches the second pattern.

The following code example checks whether the string `!@#$%^&*()` matches either the `\d+` expression, which specifies one or more digits, or the `[a-z|A-Z]+` expression, which specifies one or more lowercase or uppercase characters:

```sql
SELECT 
    REGEXP_LIKE_ANY('!@#$%^&*()', [ '\d+', '[a-z|A-Z]+' ]);
```

**Returns**: The function returns `FALSE` because the string does not match any of the regular expressions in the array.

The following code example checks if the string `a` matches either the `[1-9]+` expression, which specifies one or more digits, or a `NULL` value:

```sql
SELECT 
    REGEXP_LIKE_ANY('a', ['[1-9]+', NULL]);
```

The following code example checks whether the string `123` matches either the `[1-9]+` expression, which specifies one or more digits, or the `NULL` value, in the array.  


```sql
SELECT 
    REGEXP_LIKE_ANY('123', ['[1-9]+', NULL]);
```

**Returns**: The function returns `TRUE` because the string matches the first regular expression. The `NULL` element does not affect the result as long as a match is found. If a match is not found, the function returns `FALSE`, even if there is a `NULL` element in the array.

