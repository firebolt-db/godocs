---
layout: default
title: CONTAINS
description: Reference material for CONTAINS function
grand_parent: SQL functions
parent: Array functions
great_grand_parent: SQL reference
---

# CONTAINS

Returns `true` if a specified argument is present in the array, or `false` otherwise. Note that `CONTAINS` employs `IS NOT DISTINCT FROM` semantics when comparing values, i.e. `NULL` is considered equal to `NULL`.

## Syntax
{: .no_toc}

```sql
CONTAINS(<array>, <value>)
```

## Parameters 
{: .no_toc}

| Parameter | Description                                      | Supported input types | 
| :--------- | :------------------------------------------------ | :--------|
| `<array>`   | The array to be checked for the given element.   | `ARRAY` | 
| `<value>`   | The element to be searched for within the array | Any type that can be converted to the element type of the array | 

## Return Type

The `BOOLEAN` value `true` if the element to be searched is present in the array, or `false` otherwise.

## Example
{: .no_toc}

```sql
SELECT
	CONTAINS(['sabrina21', 'rileyjon', 'ywilson', 'danielle53', NULL], 'danielle53');
```

**Returns**: `true`, since `'danielle53'` is an element of the input array.

```sql
SELECT
	CONTAINS(['sabrina21', 'rileyjon', 'ywilson', NULL] , 'danielle53');
```

**Returns**: `false`, since `'danielle53'` is not an element of the input array.

```sql
SELECT
	CONTAINS(['sabrina21', 'rileyjon', 'ywilson', NULL] , NULL);
```

**Returns**: `true`, since `NULL` is an element of the input array.
