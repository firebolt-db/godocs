---
layout: default
title: ARRAY_MAX
description: Reference material for ARRAY_MAX function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Array functions
---

# ARRAY\_MAX

Returns the maximum element in an array.

## Syntax
{: .no_toc}

```sql
ARRAY_MAX(<array>)
```

## Parameters
{: .no_toc}

| Parameter | Description                         |Supported input types |
| :--------- | :----------------------------------- | :---------------------|
| `<array>`   | The array or array-type column to be checked | `ARRAY` | 

## Return Type

Same as the element type of the array.

## Example
{: .no_toc}

The following example calculates the maximum number in the `levels` array:
```sql
SELECT
	ARRAY_MAX([ 1, 2, 3, 4 ]) AS levels;
```

**Returns**: `4`
