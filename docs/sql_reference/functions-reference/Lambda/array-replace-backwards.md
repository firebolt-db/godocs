---
layout: default
title: ARRAY_REPLACE_BACKWARDS
description: Reference material for ARRAY_REPLACE_BACKWARDS function
grand_parent: SQL functions
parent: Lambda functions
great_grand_parent: SQL reference
---

# ARRAY\_REPLACE\_BACKWARDS

Scans an array `<array>` from the last to the first element and replaces each of the elements in that array with `array[i + 1]` if the `<function>` returns `0`. The last element of `<array>` is not replaced.

The `<function>` argument must be included.

## Syntax
{: .no_toc}

```sql
ARRAY_REPLACE_BACKWARDS(<func>, <arr>)
```
## Parameters
{: .no_toc} 

| Parameter | Description                        | Supported input types | 
| :--------- | :-------------------------------------- |:-------|
| `<function>`  | A [Lambda function](../../working-with-semi-structured-data/working-with-arrays.md#manipulating-arrays-with-lambda-functions) used to check elements in the array. | Any lambda function | 
| `<array>`   | The array to be evaluated by the function.        | Any array | 

## Return Types 
`ARRAY` of elements with the same input type 

## Example
{: .no_toc}
The following example replaces elements of the array with the conditions `x > 2`:

```sql
SELECT
	ARRAY_REPLACE_BACKWARDS(x -> x > 2, [ 1, 2, 3, 9 ]) AS levels;
```

**Returns**: `3,3,3,9`
