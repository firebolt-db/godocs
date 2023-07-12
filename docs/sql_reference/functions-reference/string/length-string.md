---
layout: default
title: LENGTH (string function)
description: Reference material for LENGTH function
grand_parent: SQL functions
parent: String functions
---

# LENGTH

Calculates the string length.

## Syntax
{: .no_toc}

```sql
LENGTH(<string>)
```

| Parameter  | Description                                |
| :---------- | :------------------------------------------ |
| `<string>` | The string for which to return the length. |

## Return Types
This function returns `NUMERIC` types. 

## Example
{: .no_toc}
The following example returns the length of a string, which is a name of a particular tournament: 
```sql
SELECT LENGTH('The Accelerator Cup')
```
As this string includes spaces, these spaces are calculated in the total length. 

**Returns**: `19`

