---
layout: default
title: LPAD
description: Reference material for LPAD function
grand_parent: SQL functions
parent: String functions
great_grand_parent: SQL reference
---

# LPAD

Adds a specified pad string to the end of the string repetitively up until the length of the resulting string is equivalent to an indicated length.

The similar function to pad the end of a string is [`RPAD`](./rpad.md).

## Syntax
{: .no_toc}

```sql
LPAD(<expression1>, <value>[, <expression2>])
```

| Parameter  | Description                                      | Supported input types | 
| :---------- | :---------------------------------------------- | :------------|
| `<expression1>`    | The original string. If the length of the original string is larger than the length parameter, this function removes the overflowing characters from the string. | Any string or name of a column | 
| `<value>` | The length of the string as an integer after it has been left-padded.  | `INTEGER` |                                                                                                         |
| `<expression2>`    | The string to add to the start of the primary string `<expression1>`. If left blank, `<expression2>` defaults to whitespace characters.         | Any string |                                                                                            |

## Return Types
`TEXT`

## Example
{: .no_toc}

The following statement adds the string "ABC" in front of the username string "esimpson" repetitively until the resulting string is equivalent to 17 characters in length.

```sql
SELECT
	LPAD('esimpson', 17, 'UserName:');
```

**Returns**:

```
UserName:esimpson
```
