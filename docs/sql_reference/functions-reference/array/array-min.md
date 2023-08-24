---
layout: default
title: ARRAY_MIN
description: Reference material for ARRAY_MIN function
grand_parent: SQL functions
parent: Array functions
great_grand_parent: SQL reference
---

# ARRAY\_MIN

Returns the minimum element in `<arr>`.

## Syntax
{: .no_toc}

```sql
ARRAY_MIN(<arr>)
```
## Parameters 
| Parameter | Description                                  | Supported input types | 
| :--------- | :-------------------------------------------- | :----------|
| `<array>`   | The array or array-type column to be checked | `<array>` | 

## Parameters
{: .no_toc}

| Parameter | Description                         |Supported input types |
| :--------- | :----------------------------------- | :---------------------|
| `<array>`   | The array or array-type column to be checked | `<array>` | 

## Return Types
`NUMERIC` 

## Example
{: .no_toc}

The following examples calculates the maximum number in the `levels` array: 
```sql
SELECT
	ARRAY_MIN([ 1, 2, 3, 4 ]) AS levels;
```

**Returns**: `1`
