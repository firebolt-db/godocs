---
layout: default
title: CAST
description: Reference material for CAST function
grand_parent: SQL functions
parent: Conditional and miscellaneous functions
great_grand_parent: SQL reference
---


# CAST

Similar to `TRY_CAST`, `CAST` converts data types into other data types based on the specified parameters. If the conversion cannot be performed, `CAST` returns an error. To return a `NULL` value instead, use `TRY_CAST`.

## Syntax
{: .no_toc}

```sql
CAST(<value> AS <type>)
```
## Parameters 
{: .no_toc}

| Parameter | Description     | Supported input types | 
| :--------- | :-------------------- |:---------|
| `<value>` | The value to convert or an expression that results in a value to convert | column name,  a function applied to a column or another function, or a literal value | 
| `<type>`  | The target [data type](../../general-reference/data-types.md) (case-insensitive) | Any supported data type |                                                                                          |

## Return Types 
Same datatype as `<type>`

## Example
{: .no_toc}

The following example returns `1` as an integer: 

```sql
SELECT CAST('1' AS INT) as level;
```

**Returns**: `1`

`CAST` can also be done by writing the format before the object, for example - `select date '2022-01-01'` , `select timestamp '2022-01-01 01:02:03'.`

{: .note}
`CAST` can also be done by using the `::` operator. For more information, see [:: operator for CAST](../../general-reference/operators.md#-operator-for-cast).



