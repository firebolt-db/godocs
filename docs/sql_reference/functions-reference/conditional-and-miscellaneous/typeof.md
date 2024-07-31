---
layout: default
title: TYPEOF
description: Reference material for TYPEOF function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Conditional and miscellaneous functions
---

# TYPEOF

Returns the type of a given expression.

## Syntax
{: .no_toc}

```sql
TYPEOF(<expression>)
```

## Parameters 
{: .no_toc}

| Parameter | Description        |Supported input types | 
| :--------- | :---------------------------------------------------|:------------|
| `<expression>` | The expression to typeof. | Any |

## Return Types
A text of the given expression data type.

## Example
{: .no_toc}
The following example returns the type of PI() function:

```sql
SELECT TYPEOF(RANDOM()) AS random_data_type;
```

**Returns:** `double precision`
