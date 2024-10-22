---
layout: default
title: Object identifers
description: Provides requirements and guidance for using SQL identifiers with Firebolt.
nav_order: 5
parent: General reference
---

# Object identifers

Firebolt object identifiers are used to refer to database items as columns, tables, indexes, views, and engines.

## Syntax

Identifiers must contain at least one character, and no more than `255` characters total.

## Unquoted identifiers

Unquoted identifiers must adhere to the following syntax:

1. The **first character** must be a letter (a-z), or an underscore (`_`).
2. After the first character, **subsequent characters** can include letters, underscores, or digits (0-9).

Firebolt evaluates unquoted identifiers such as table and column names **entirely in lowercase**. The following queries:

```
SELECT my_column FROM my_table
SELECT MY_COLUMN FROM MY_TABLE
SELECT mY_cOlUmn FROM mY_tAbLe
```

are all equivalent to:

```
SELECT my_column FROM my_table
```

You can keep uppercase identifiers by enclosing them in double-quotes. For example, the following identifiers are unique:

```
"COLUMN_NAME"
"column_name"
"CoLuMn_NaMe"
```

## Quoted identifiers

Quoted identifiers can contain any UTF-8 characters of the following [Unicode general category values](https://www.unicode.org/reports/tr44/#General_Category_Values):

1. Any letter in any language, as represented by the Unicode general category value for **Letter**.
2. Any numeric character in any language as represented by the Unicode general category value for **Number**.
3. Special characters beyond standard alphanumeric characters. Examples include `@`, `#`, `-`, `$`, `%`, `?`, and others. Any object identifier that contains special characters, spaces, or are case-sensitive must be enclosed in double quotes (`"`) as follows: `"my-column"` or `"User@Name"`. 
4. Underscores, as represented by the Unicode general category value for **Connector_Punctuation**.

