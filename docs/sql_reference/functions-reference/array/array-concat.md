---
layout: default
title: ARRAY_CONCAT
description: Reference material for ARRAY_CONCAT function
grand_parent: SQL functions
parent: Array functions
great_grand_parent: SQL reference
---

# ARRAY\_CONCAT
**Alias:** `ARRAY_CAT`

Combines one or more arrays that are passed as arguments.

## Syntax
{: .no_toc}

```sql
ARRAY_CONCAT(<array> [, ...n])
```

## Parameters 
{: .no_toc} 

| Parameter        | Description                                                                            | Supported input types |
| :---------------- | :-------------------------------------------------------------------------------------- | :----------|
| `<array> [, ...n]` | The arrays to be combined. If only one array is given, an identical array is returned. | `ARRAY`  |

## Return Type
`ARRAY` of the same type as the input arrays 

## Example
{: .no_toc}

In the following example, two arrays are combined to show all of the levels in a particular game: 

```sql
SELECT
    ARRAY_CONCAT([ 1, 2, 3, 4 ], [ 5, 6, 7, 8, 9, 10 ]) AS levels;
```

**Returns**: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`


```sql
<expression> || <expression>
```


### `||` operator

| Parameter | Description                         |Supported input types |
| :--------- | :----------------------------------- | :---------------------|
| `<expression>` | The expressions to be concatenated. | `TEXT` / `ARRAY` |

One parameter to the `||` operator must be of type `ARRAY` to perform array concatenation, while the other parameter can be a string whose value can be converted to the underlying type of the array parameter, or it can be an array of the same type. 

If only one parameter to the `||` operator is `NULL`, the result will be the other parameter. If both parameters are `NULL` literals, the string concatenation operator will be invoked and the result will be `NULL` of type `TEXT`.

## Return Type
`ARRAY` if at least one parameter is an array data type

## Example
{: .no_toc}

The following example concatenates a string, whose value can be converted to integer, with an integer array.

```sql
SELECT '{2}' || array[1];
```

**Returns**: `[2,1]`
