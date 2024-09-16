---
layout: default
title: ARRAY_CONCAT
description: Reference material for ARRAY_CONCAT function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Array functions
---

# ARRAY\_CONCAT
**Alias:** `ARRAY_CAT`

Combines one or more arrays that are passed as arguments.

## Syntax
{: .no_toc}

```sql
ARRAY_CONCAT(<array> [, ...n])
```
**OR**

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

{% include sql_examples/array_concat.md %}
