---
layout: default
title: ARRAY_ANY_MATCH
description: Reference material for ARRAY_ANY_MATCH function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Lambda functions
---


# ARRAY\_ANY\_MATCH

Returns `TRUE` if at least one of the elements in a `BOOLEAN` array is `TRUE` when no function is provided, and returns `FALSE` otherwise. When an optional function parameter is provided, the result is `TRUE` if the function evaluates to `TRUE` for at least one element in the array, and `FALSE` otherwise.

**Alias:** `ANY_MATCH`


## Syntax
{: .no_toc}

```sql
ARRAY_ANY_MATCH([<function>], <array>)
```
## Parameters
{: .no_toc} 

| Parameter | Description              | Supported input types | 
| :--------- | :------------------------| :----------- | 
| `<function>`  | A [lambda function](../../../Guides/working-with-semi-structured-data/working-with-arrays.md#manipulating-arrays-with-lambda-functions) used to check elements in the array. | Any lambda function that returns a `BOOLEAN` value. | 
| `<array>`   | The array to evaluate with the function.  | Can be any array, but must be of type `BOOLEAN` if no `<function>` is provided.|       

## Return Type
The `ARRAY_ANY_MATCH` function returns a result of type `BOOLEAN`.

## Example
{: .no_toc}

The following code example checks if any element in an array is greater than `3`:

```sql
SELECT
	ARRAY_ANY_MATCH(x -> x > 3, [ 1, 2, 3, 9 ]);
```

**Returns**
The query returns `TRUE` because `9` is greater than `3`.


**Example**

The following code example checks if any element in the array equals `10`:

```sql
SELECT
	ARRAY_ANY_MATCH(x -> x = 10, [ 1, 2, 3, 9 ]);
```

**Returns**
The previous code returns `FALSE` because there is no value `10` in the array.
