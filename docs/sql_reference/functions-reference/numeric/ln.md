---
layout: default
title: LN
description: Reference material for LN function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Numeric functions
published: true
---

# LN

Returns natural (base e) logarithm of a numerical expression.
The value for which `ln` is computed needs to be larger than 0, otherwise an error is returned.
You can use the function [LOG](log.md) if you want to provide a different base.

## Syntax
{: .no_toc}

```sql
LN(<value>);
```
## Parameters 
{: .no_toc}

| Parameter   | Description                                                                                                         | Supported input types |
| :----------- | :------------------------------------------------------------------------------------------------------------------- |:--------------------|
| `<value>` | The value for which to compute the natural logarithm. | `DOUBLE PRECISION` |

## Return Type
`DOUBLE PRECISION`

## Examples
{: .no_toc}

{% include sql_examples/ln_executable.md %}
