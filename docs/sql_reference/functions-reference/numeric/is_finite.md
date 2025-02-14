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

{% include sql_examples/is_finite_executable.md %}
