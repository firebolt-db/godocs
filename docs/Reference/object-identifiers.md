---
layout: default
title: Object identifers
description: Provides requirements and guidance for using SQL identifiers with Firebolt.
nav_order: 5
parent: General reference
---

# Object identifers

Firebolt identifiers can refer to the following items:

* Columns
* Tables
* Indexes
* Databases
* Views
* Engines

## Syntax

Identifiers must contain at least one character, and no more than 255.

Unquoted Identifiers must adhere to the following syntax:

2. The first character must be a letter (a-z), underscore (_).
3. After the first character, subsequent characters can be letters, underscores, digits (0-9).
4. columns can also contain dollar signs ($)

Qouted identifiers can contain any UTF-8 letter 

## Unquoted identifiers

Firebolt evaluates unquoted identifiers such as table and column names entirely in lowercase. The following queries:

```
SELECT my_column FROM my_table
SELECT MY_COLUMN FROM MY_TABLE
SELECT mY_cOlUmn FROM mY_tAbLe
```

are all equivalent to:

```
SELECT my_column FROM my_table
```

{: .note}
Unquoted identifiers in some early Firebolt accounts may be case sensitive.


You can keep uppercase identifiers by enclosing them in double-quotes. For example, the following identifiers are unique:

```
"COLUMN_NAME"
"column_name"
"CoLuMn_NaMe"
```
