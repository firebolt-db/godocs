---
layout: default
title: TRY_CAST
description: Reference material for TRY_CAST function
grand_parent: SQL functions
parent: Conditional and miscellaneous functions
great_grand_parent: SQL reference
---

# TRY_CAST

Similar to `CAST`, `TRY_CAST` converts data types into other data types based on the specified parameters. If the conversion cannot be performed, `TRY_CAST` returns a `NULL`. To return an error message instead, use `CAST`.

## Syntax
{: .no_toc}

```sql
TRY_CAST(<value> AS <type>)
```

| Parameter | Description                   | Supported input types | 
| :--------- | :-------------------|:-------------|
| `<value>` | The value to convert or an expression that results in a value to convert | A column name,  a function applied to a column or another function, or a literal value | 
| `<type>`  | The target [data type](../../general-reference/data-types.md) (case-insensitive) | Any |                                                                                          |

## Return Types 
Same as input type

## Example
{: .no_toc}

The following example casts the level inputted as an integer: 

```sql
SELECT TRY_CAST('1' AS INTEGER) as level, TRY_CAST('level 2' AS INTEGER) as current_level;
```

**Returns**: `1,null`
