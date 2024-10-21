---
layout: default
title: IS_FINITE
description: Reference material for the IS_FINITE function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Numeric functions
published: true
---

# IS_FINITE

Returns `TRUE` if the argument is finite, and `FALSE` otherwise. Only `REAL` and `DOUBLE PRECISION` types can represent infinity in Firebolt, meaning that `IS_FINITE` will always return `TRUE` for `NUMERIC` inputs.

## Syntax

{: .no_toc}

```sql
IS_FINITE(<value>);
```

## Parameters

{: .no_toc}

| Parameter | Description                                    | Supported input types                 |
| :-------- | :--------------------------------------------- | :------------------------------------ |
| `<value>` | The input that will be checked to determine if it is a finite number. | `NUMERIC`, `DOUBLE PRECISION`, `REAL` |

## Return Type

`IS_FINITE` returns a value of type `BOOLEAN`.

## Examples

{: .no_toc}

**Example**

The following code example checks whether the value `inf`, after being cast to a `DOUBLE PRECISION` data type, is a finite number:

```sql
SELECT
    IS_FINITE('inf'::DOUBLE PRECISION);
```

**Returns**

The previous code example returns `FALSE` because infinity is an infinite value.

**Example**

The following code example checks whether the value `10`, after being cast to a `REAL` data type, is an infinite number:

```sql
SELECT
    IS_FINITE(10::REAL);
```

**Returns**

The previous code example returns `TRUE` because `10` is a finite value.
