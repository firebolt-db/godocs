---
redirect_from:
  - /sql-reference/functions-reference/acos.html
layout: default
title: ACOS
description: Reference material for ACOS function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Numeric functions
published: true
---

# ACOS

Calculates the arccosine of a value in radians.

## Syntax
{: .no_toc}

```sql
ACOS(<value>)
```

## Parameters 
{: .no_toc}

| Parameter | Description                                                                                                         | Supported input types |
| :--------- | :------------------------------------------------------------------------------------------------------------------- | :-------------------|
| `<value>`   | The number that the arccosine function is applied to. | `DOUBLE PRECISION` |

## Return Type
`ACOS` returns a value of type `DOUBLE PRECISION`.

## Example
{: .no_toc}

{% include sql_examples/acos_executable.md %}
