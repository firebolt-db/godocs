---
layout: default
title: ANY_MATCH
description: Reference material for ANY_MATCH function
grand_parent: SQL functions
parent: Lambda functions
great_grand_parent: SQL reference
---


# ANY\_MATCH

Returns `1` if at least one of the elements of an array matches the results of the function provided in the `<func>` parameter. Otherwise returns `0`.

## Syntax
{: .no_toc}

```sql
ANY_MATCH(<function>, <array>)
```
## Parameters
{: .no_toc} 

| Parameter | Description              | Supported input types | 
| :--------- | :------------------------| :----------- | 
| `<function>`  | A [Lambda function](../../working-with-semi-structured-data/working-with-arrays.md#manipulating-arrays-with-lambda-functions) used to check elements in the array. | Any Lambda function | 
| `<array>`   | The array to be matched with the function. The array cannot be empty  | Any array |                                                                                                          |

## Return Types
* Returns `1` if the specifications are true
* Returns `0` if the specifications are false

## Example
{: .no_toc}

Because there are values in the `levels` greater than `3`, the function returns `1`. 
```sql
SELECT
	ANY_MATCH(x -> x > 3, [ 1, 2, 3, 9 ]) AS levels;
```

**Returns**: `1`

As there is no level `10` in the array, the function returns `0`. 
```
SELECT
	ANY_MATCH(x -> x = 10, [ 1, 2, 3, 9 ]) AS levels;
```

**Returns**: `0`
