---
layout: default
title: ARRAY_TO_STRING
description: Reference material for ARRAY_TO_STRING function
grand_parent: SQL functions
parent: Array functions
great_grand_parent: SQL reference
---

# ARRAY\_TO\_STRING

Converts each array element to its text representation, and concatenates those using an optional delimiter. If no delimiter is provided, an empty string is used instead. `NULL` array elements are omitted.

## Syntax
{: .no_toc}

```sql
ARRAY_TO_STRING(<array>[, <delimiter>])
```

## Parameters 
{: .no_toc} 

| Parameter     | Description                            | Supported input types | 
| :------------- | :------------------------------------ |:---------|
| `<array>`       | An array to be concatenated | `ARRAY` |
| `<delimiter>` | The delimiter used for concatenating the array elements | `TEXT` | 

## Return Type
`TEXT`

## Example
{: .no_toc}

In the example below, the three elements are concatenated with no delimiter.

```sql
SELECT
	ARRAY_TO_STRING([ '1', '2', '3' ]) AS levels;
```

**Returns**: `123`

In this example below, the levels are concatenated separated by a comma. 

```sql
SELECT
	ARRAY_TO_STRING([ '1', '2', '3' ], ',') AS levels;
```

**Returns**: `1,2,3`

In this example below, the elements of a nested array containing a `NULL` are concatenated. 

```sql
SELECT
	ARRAY_TO_STRING([ [ 1, 2 ], [3, 4], [NULL, 5] ], ',') AS levels;
```

**Returns**: `1,2,3,4,5`
