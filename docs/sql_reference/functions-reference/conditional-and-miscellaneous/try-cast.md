---
layout: default
title: TRY_CAST
description: Reference material for TRY_CAST function
grand_parent: SQL functions
parent: Conditional and miscellaneous functions
great_grand_parent: SQL reference
---

# TRY_CAST

Converts data types into other data types based on the specified parameters. If the conversion cannot be performed, `TRY_CAST` returns a `NULL`. To return an error message instead, use [`CAST`](./cast.md).

## Syntax
{: .no_toc}

```sql
TRY_CAST(<value> AS <type>)
```

## Parameters 
{: .no_toc}

| Parameter | Description                   |Supported input types | 
| :--------- | :-------------------|:-------------|
| `<value>` | The value to convert or an expression that results in a value to convert | Any | 
| `<type>`  | The target [data type](../../data-types.md) (case-insensitive) | Any | 

## Return Type
Returns `NULL` if the conversion cannot be performed. Otherwise, returns the data type of `<type>`. 

## Example
{: .no_toc}

The following example attempts to cast the level input as an integer: 

```sql
SELECT TRY_CAST('1' AS INTEGER) as level, TRY_CAST('level 2' AS INTEGER) as current_level;
```

**Returns**: `1, null`
