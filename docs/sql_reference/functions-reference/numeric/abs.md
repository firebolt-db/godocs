---
layout: default
title: ABS
description: Reference material for ABS function
grand_parent: SQL functions
parent: Numeric functions
---

# ABS

Calculates the absolute value of a number `<value>`. This means displaying the number's distance from `0`. 

## Syntax
{: .no_toc}

```sql
ABS(<value>)
```
## Parameters 
| Parameter | Description                                                                                                         | Supported input types |
| :--------- | :------------------------------------------------------------------------------------------------------------------- | :-------------------|
| `<value>`   | The number that the absolute value function is applied to | Column names, functions that return a column with numeric values, and constant numeric values |

## Return Types 
Same as input type

## Example
{: .no_toc}
The following example returns the absolute value of `-200.5`:
```sql
SELECT
    ABS(-200.50);
```

**Returns**: `200.5`
