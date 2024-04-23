---
layout: default
title: ANY_MATCH
description: Reference material for ANY_MATCH function
grand_parent: SQL functions
parent: Lambda functions
great_grand_parent: SQL reference
---


# ANY\_MATCH

Returns `true` if at least one of the elements of a `BOOLEAN` array is `true`.  Otherwise returns `false`.

If an optional function parameter is provided, returns `true` if the function returns `true` for at least one of the elements in the array. Otherwise returns `false`.

## Syntax
{: .no_toc}

```sql
ANY_MATCH([<function>], <array>)
```
## Parameters
{: .no_toc} 

| Parameter | Description              | Supported input types | 
| :--------- | :------------------------| :----------- | 
| `<function>`  | A [Lambda function](../../../Guides/working-with-semi-structured-data/working-with-arrays.md#manipulating-arrays-with-lambda-functions) used to check elements in the array. | Any Lambda function returning `BOOLEAN` | 
| `<array>`   | The array to be matched with the function.  | Any array (must be of type `BOOLEAN` if `<function>` is not provided)|       

## Return Types
Returns `BOOLEAN`

## Example
{: .no_toc}

Because there are values in the array greater than `3`, the function returns `true`. 
```sql
SELECT
	ANY_MATCH(x -> x > 3, [ 1, 2, 3, 9 ]);
```

**Returns**: `true`

As there is no value `10` in the array, the function returns `false`. 
```sql
SELECT
	ANY_MATCH(x -> x = 10, [ 1, 2, 3, 9 ]);
```

**Returns**: `false`
