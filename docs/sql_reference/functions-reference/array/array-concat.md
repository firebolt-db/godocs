---
redirect_from:
  - /sql-reference/functions-reference/concat.html
  - /sql-reference/functions-reference/array-join.html
  - /sql-reference/functions-reference/array-concat.html
layout: default
title: ARRAY_CONCAT
description: Reference material for ARRAY_CONCAT function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Array functions
---

# ARRAY\_CONCAT
**Alias:** `ARRAY_CAT`

Combines one or more arrays that are passed as arguments into a single array.

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
| `<array> [, ...n]` | The arrays to combine. If only one array is specified, it is returned unchanged. | `ARRAY`  |


### The concatenation operator `||`

| Parameter | Description                         |Supported input types |
| :--------- | :----------------------------------- | :---------------------|
| `<expression>` | The expressions to be concatenated. | Either `TEXT` or `ARRAY`, but at least one operand must be an `ARRAY`. |


To enable array concatenation, one operand of the `||` operator must be of type `ARRAY`. The other operand can either be a string that can be converted to the array's element type, or another array of the same type. 

* If one operand to the `||` operator is `NULL`, the result will be the non-null operand. If both operands are `NULL`, the result will also be `NULL`.

* The concatenation operator `||` can also be used for [string concatenation](../string/concat.md).


## Return Type
Returns an `ARRAY` of the same type as the input arrays. 

## Examples
{: .no_toc}

{% include sql_examples/array_concat.md %}
