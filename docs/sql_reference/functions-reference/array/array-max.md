---
layout: default
title: ARRAY_MAX
description: Reference material for ARRAY_MAX function
grand_parent: SQL functions
parent: Array functions
great_grand_parent: SQL reference
---

# ARRAY\_MAX

<<<<<<< HEAD
Returns the maximum element in an array `<array>`.
=======
Returns the maximum element in an array.
>>>>>>> 07662ff7863c7e2b479373c46e9f4a07e6bcfc78

## Syntax
{: .no_toc}

```sql
ARRAY_MAX(<array>)
```

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
	ARRAY_MAX([ 1, 2, 3, 4 ]) AS levels;
```

**Returns**: `4`
