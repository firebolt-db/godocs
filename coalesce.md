---
layout: default
title: COALESCE
description: Reference material for COALESCE function
parent: Conditional and miscellaneous functions
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
| `<expression>` | The expression(s) to coalesce. | Any |

## Return Types
Same as input type

## Example
{: .no_toc}
The following example returns the first non-NULL value provided, which is the username `esimpson`:

```sql
SELECT COALESCE(NULL, 'esimpson','sabrina21') AS nicknames;
```

**Returns:** `esimpson`
