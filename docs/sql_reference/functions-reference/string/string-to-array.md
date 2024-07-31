---
layout: default
title: STRING_TO_ARRAY
description: Reference material for STRING_TO_ARRAY function
grand_parent: SQL functions
parent: String functions
published: true
---

# STRING_TO_ARRAY

This function splits a given string by a given separator and returns the result in an array of strings.

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

## Example
{: .no_toc}

The following example splits the nicknames of players into separate items in an array: 
```sql
SELECT
	STRING_TO_ARRAY('stephen70|esimpson|ruthgill|', '|') AS nicknames;
```

**Returns**: `["stephen70","esimpson","ruthgill",""]`
