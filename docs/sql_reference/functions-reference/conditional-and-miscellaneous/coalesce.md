---
layout: default
title: COALESCE
description: Reference material for COALESCE function
grand_parent: SQL functions
parent: Conditional and miscellaneous functions
great_grand_parent: SQL reference
---

# COALESCE

Checks from left to right for the first non-NULL argument found for each entry parameter pair. 

## Syntax
{: .no_toc}

```sql
COALESCE(<expression> [,...])
```

## Parameters 
{: .no_toc}


| Parameter | Description        |Supported input types | 
| :--------- | :---------------------------------------------------|:------------|
| `<expression>` | The expression(s) to coalesce. | A column name,  a function applied on a column (or on another function), or a literal (constant value) |

## Return Types
Same as input type

## Example
{: .no_toc}
The following example returns the first non-NULL value provided, which is the username `esimpson`:

```sql
SELECT COALESCE(NULL, 'esimpson','sabrina21') AS nicknames;
```

**Returns:** `esimpson`
