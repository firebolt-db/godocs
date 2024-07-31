---
layout: default
title: ARRAY_REVERSE
description: Reference material for ARRAY_REVERSE function
grand_parent: SQL functions
parent: Array functions
---

# ARRAY\_REVERSE

Returns an array of the same size and type as the original array, with the elements in reverse order. Nulls are retained.

## Syntax
{: .no_toc}

```sql
ARRAY_REVERSE(<array>)
```

## Parameters
{: .no_toc}

| Parameter | Description                         |Supported input types |
| :--------- | :----------------------------------- | :---------------------|
| `<array>`   | The array to be reversed | `ARRAY` of any type |

## Return Type
`ARRAY` of the same type as the input array

## Example
{: .no_toc}

The following example returns the reverse of the input array:

```sql
SELECT
	ARRAY_REVERSE([ 1, 2, 3, 6 ]);
```

**Returns**: `[6,3,2,1]`

Only the outermost array is reversed for nested arrays:
```sql
SELECT
	ARRAY_REVERSE([[1,2,3], [4,5], NULL, [7], [8,9]]);
```

**Returns**: `[[8,9], [7], NULL, [4,5], [1,2,3]]`
