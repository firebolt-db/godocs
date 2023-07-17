---
layout: default
title: SLICE
description: Reference material for SLICE function
grand_parent: SQL functions
parent: Array functions
---

# SLICE

Returns a slice of the array based on the indicated offset and length.

## Syntax
{: .no_toc}

```sql
SLICE(<array>, <offset>[, <length>])
```

| Parameter  | Description                            | Supported input types | 
| :---------- | :------------------------------------ | :-------- | 
| `<array>`    | The array of data to be sliced               | `<array>`
| `<value>` | Indicates starting point of the array slice | `<value>`
| `<value>` | The length of the required slice | `<value>` | 

## Return Types
`ARRAY`

## Example
{: .no_toc}

The following example slices the `levels` array to a different length: 
```sql
SELECT
	SLICE([ 1, 2, 3, 4, 5 ], 1, 3) AS levels;
```

**Returns**: `[1, 2, 3]`
