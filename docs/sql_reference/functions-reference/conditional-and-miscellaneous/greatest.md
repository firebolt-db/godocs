---
layout: default
title: GREATEST
description: Reference material for GREATEST function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Conditional and miscellaneous functions
---

# GREATEST

The GREATEST function selects the largest value from a list of any number of expressions.
The expressions must all be convertible to a common data type, which will be the type of the result.
NULL values in the argument list are ignored. The result will be NULL only if all the expressions evaluate to NULL.

## Syntax
{: .no_toc}

```sql
GREATEST(<expression> [,...])
```

## Parameters
{: .no_toc}

| Parameter | Description                                 |Supported input types | 
| :--------- |:--------------------------------------------|:------------|
| `<expression>` | The expression(s) to select greatest value. | Any |

## Return Types
Same as input type

## Example
{: .no_toc}


```sql
SELECT GREATEST(NULL, 2^3, 3^2)
```

**Returns:** `9`
