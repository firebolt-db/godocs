---
layout: default
title: CAST
description: Reference material for CAST function
grand_parent: SQL functions
parent: Conditional and miscellaneous functions
great_grand_parent: SQL reference
---


# CAST

Converts data types into other data types based on specified parameters. If the conversion cannot be performed, `CAST` returns an error. To return a `NULL` value instead, use [`TRY_CAST`](./try-cast.md).

## Syntax
{: .no_toc}

```sql
CAST(<value> AS <type>)
```
## Parameters 
{: .no_toc}

| Parameter | Description     | Supported input types | 
| :--------- | :-------------------- |:---------|
| `<value>` | The value to convert or an expression that results in a value to convert. | Any | 
| `<type>`  | The target [data type](../../data-types.md) (case-insensitive) | Any       |

## Return Types 
Same data type as `<type>`

## Example
{: .no_toc}

The following example returns `1` as an integer: 

```sql
SELECT CAST('1' AS INTEGER) as level;
```

**Returns**: `1`

`CAST` can also be done by writing the format before the object, for example - `SELECT DATE '2022-01-01'` , `SELECT TIMESTAMP '2022-01-01 01:02:03'.`

{: .note}
`CAST` can also be done by using the `::` operator. For more information, see [:: operator for CAST](../../operators.md#-operator-for-cast).



