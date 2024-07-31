---
layout: default
title: LEAST
description: Reference material for LEAST function
grand_parent: SQL functions
parent: Conditional and miscellaneous functions
---

# LEAST

The LEAST function selects the smallest value from a list of any number of expressions.
The expressions must all be convertible to a common data type, which will be the type of the result.
NULL values in the argument list are ignored. The result will be NULL only if all the expressions evaluate to NULL.

## Syntax
{: .no_toc}

```sql
LEAST(<expression> [,...])
```

## Parameters
{: .no_toc}

| Parameter | Description                                 |Supported input types | 
| :--------- |:--------------------------------------------|:------------|
| `<expression>` | The expression(s) to select smallest value. | Any |

## Return Types
Same as input type

## Example
{: .no_toc}


```sql
SELECT LEAST(NULL, 2^3, 3^2)
```

**Returns:** `8`
