---
layout: default
title: ARRAY_FIRST_INDEX
description: Reference material for ARRAY_FIRST_INDEX function
grand_parent: SQL functions
parent: Lambda functions
great_grand_parent: SQL reference
---

# ARRAY\_FIRST\_INDEX

Returns the index of the first element in the indicated array for which the given `<function>` function returns something other than `0`. Index counting starts at 1.

The `<function>` argument must be included.

## Syntax
{: .no_toc}

```sql
ARRAY_FIRST_INDEX(<function>, <array>)
```
## Parameters 
{: .no_toc}

| Parameter | Description                          | Supported input types | 
| :--------- | :------------------------ | :---------| 
| `<function>`  | A [Lambda function](../../working-with-semi-structured-data/working-with-arrays.md#manipulating-arrays-with-lambda-functions) used to check elements in the array | Any Lambda function | 
| `<array>`   | The array evaluated by the function     | Any array | 

## Return Types
Same input type as the input type of the `ARRAY` 

## Example
{: .no_toc}
The following example returns the first value in the `levels` array that is greater than `2`: 

```sql
SELECT
	ARRAY_FIRST_INDEX(x -> x > 2, [ 1, 2, 3, 9 ]) AS levels;
```

**Returns**: `3`
