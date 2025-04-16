---
redirect_from:
  - /sql-reference/functions-reference/split.html
layout: default
title: STRING_TO_ARRAY
description: Reference material for STRING_TO_ARRAY function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: String functions
published: true
---

# STRING_TO_ARRAY

Splits a string into an array of strings based on a specified delimiter, with the following behaviors:

* If the delimiter is an empty string `''`, the result is an array containing the entire original input string as a single element.
* If the delimiter is `NULL`, the string is split into individual characters, with one character per array element.

## Syntax
{: .no_toc}

```sql
STRING_TO_ARRAY(<string>, <delimiter>)
```
## Parameters 
{: .no_toc}

| Parameter     | Description                           |
| :------------- | :------------------------------------- |
| `<string>`    | The string to split.                  |
| `<delimiter>` | The separator to split the string by. |

## Return Types
`ARRAY(TEXT)`

## Examples
{: .no_toc}

{% include sql_examples/string_to_array.md %}
