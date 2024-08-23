---
layout: default
title: ARRAY_FIRST
description: Reference material for ARRAY_FIRST function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Lambda functions
published: true
---

# ARRAY\_FIRST

Returns the first element in the given array for which the given function returns `true`. The `<function>` parameter must be included.

## Syntax
{: .no_toc}

```sql
ARRAY_FIRST(<function>, <array>)
```
## Parameters 
{: .no_toc}

| Parameter | Description                  | Supported input types | 
| :--------- | :--------------------------- | :-------- | 
| `<function>`  | A [Lambda function](../../../Guides/working-with-semi-structured-data/working-with-arrays.md#manipulating-arrays-with-lambda-functions) used to check elements in the array | A Lambda function returning `BOOLEAN` |
| `<array>`   | The array evaluated by the function  | Any array | 

## Return Type
The element type of `<array>` 

## Examples
{: .no_toc}

The following example returns the first value in the `levels` array greater than 2: 

```sql
SELECT
	ARRAY_FIRST(x -> x > 2, [ 1, 2, 4, 9 ]) AS levels;
```

**Returns**: `4`
