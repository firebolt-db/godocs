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
**&mdash;OR&mdash;**

```sql
<expression> || <expression>
```

## Parameters 
{: .no_toc} 

| Parameter        | Description                                                                            | Supported input types |
| :---------------- | :-------------------------------------------------------------------------------------- | :----------|
| `<array> [, ...n]` | The arrays to be combined. If only one array is given, an identical array is returned. | `ARRAY`  |


### `||` operator

| Parameter | Description                         |Supported input types |
| :--------- | :----------------------------------- | :---------------------|
| `<expression>` | The expressions to be concatenated. | `TEXT` / `ARRAY`, but at least one `ARRAY` |


To enable array concatenation, one parameter to the `||` operator must be of type `ARRAY`, while the other parameter can be a string whose value can be converted to the underlying type of the array parameter, or it can be an array of the same type. 

If one parameter to the `||` operator is `NULL`, the result will be the non-null parameter; if both parameters are `NULL`, the result will be `NULL`.

The concatenation operator `||` can also be used for [string concatenation](../string/concat.md).


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

The following example concatenates two integer arrays:

```sql
SELECT ARRAY[1,2] || ARRAY[3];
```
**Returns**: `[1, 2, 3]`

The following example concatenates a string, whose value can be converted to integer, with an integer array:

```sql
SELECT '{2}' || ARRAY[1];
```

**Returns**: `[2, 1]`