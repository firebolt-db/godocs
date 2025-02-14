---
layout: default
title: IS_INFINITE
description: Reference material for the IS_INFINITE function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Numeric functions
published: true
---

# IS_INFINITE

Returns `TRUE` if the argument is infinite, and `FALSE` otherwise. Only `REAL` and `DOUBLE PRECISION` types can represent infinity in Firebolt, meaning that `IS_INFINITE` will always return `FALSE` for `NUMERIC` inputs.


## Syntax

{: .no_toc}

```sql
IS_FINITE(<value>);
```

## Parameters

{: .no_toc}

| Parameter | Description                                      | Supported input types                 |
| :-------- | :----------------------------------------------- | :------------------------------------ |
| `<value>` | The input that will be checked to determine if it is an infinite number. | `NUMERIC`, `DOUBLE PRECISION`, `REAL` |

## Return Type

`IS_INFINITE` returns a value of type `BOOLEAN`.

## Examples

{: .no_toc}

{% include sql_examples/is_infinite_executable.md %}
