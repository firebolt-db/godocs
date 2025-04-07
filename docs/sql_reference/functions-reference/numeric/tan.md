---
redirect_from:
  - /sql-reference/functions-reference/tan.html
layout: default
title: TAN
description: Reference material for TAN function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Numeric functions
published: true
---

# TAN

Trigonometric function that calculates the tangent of a specific value in radians.

## Syntax
{: .no_toc}

```sql
TAN(<value>)
```
## Parameters
{: .no_toc}

| Parameter | Description     | Supported input types | 
| :--------- | :--------------------------------- | :---------|
| `<value>`   | The value that determines the returned tangent in radians. | `DOUBLE PRECISION` |

## Return Type
`TAN` returns a value of type `DOUBLE PRECISION`.

## Example
{: .no_toc}

{% include sql_examples/tan_executable.md %}
