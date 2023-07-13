---
layout: default
title: ARRAY_CONCAT
description: Reference material for ARRAY_CONCAT function
grand_parent: SQL functions
parent: Array functions
---

# ARRAY\_CONCAT

Combines one or more arrays that are passed as arguments.

## Syntax
{: .no_toc}

```sql
ARRAY_CONCAT(<arr1> [, ...n])
```

## Parameters 
{: .no_toc} 

| Parameter        | Description                                                                            | Supported input types |
| :---------------- | :-------------------------------------------------------------------------------------- | :----------|
| `<array> [, ...n]` | The arrays to be combined. If only one array is given, an identical array is returned. | `<array>`

## Return Types
`ARRAY`

## Example
{: .no_toc}

In the following example, two arrays are combined to show all of the levels in a particular video game: 

```sql
SELECT
    ARRAY_CONCAT([ 1, 2, 3, 4 ], [ 5, 6, 7, 8, 9, 10 ]) AS levels;
```

**Returns**: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
