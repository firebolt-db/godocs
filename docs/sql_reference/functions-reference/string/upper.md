---
layout: default
title: UPPER
description: Reference material for UPPER function
grand_parent: SQL functions
parent: String functions
---

# UPPER

Converts the string to uppercase format.

## Syntax
{: .no_toc}

```sql
UPPER(<string>)
```

| Parameter  | Description                                             |
| :---------- | :------------------------------------------------------- |
| `<string>` | The string to be converted to all uppercase characters. |

## Return Type
The return type for this function includes `CHAR`. 

## Example
{: .no_toc}

The following example converts a video game player's username from lower case syntax to all uppercase syntax:

```sql
SELECT
	UPPER('esimpson')
```

**Returns**: `ESIMPSON`
