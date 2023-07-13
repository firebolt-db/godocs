---
layout: default
title: ARRAY_REVERSE
description: Reference material for ARRAY_REVERSE function
grand_parent: SQL functions
parent: Array functions
---

# ARRAY\_REVERSE

Returns an array of the same size as the original array, with the elements in reverse order.

## Syntax
{: .no_toc}

```sql
ARRAY_REVERSE(<arr>)
```
## Return Types
`ARRAY`

## Parameters 
| Parameter | Description               | Supported input types |
| :--------- | :------------------------- | :--------| 
| `<array>`   | The array to be reversed | `<array>` |

## Example
{: .no_toc}
The following examples calculates the reverse of the `levels` array: 

```sql
SELECT
	ARRAY_REVERSE([ 1, 2, 3, 6 ]) AS levels;
```

**Returns**: `[6,3,2,1]`
