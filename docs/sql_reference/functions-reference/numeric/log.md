---
layout: default
title: LOG
description: Reference material for LOG function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Numeric functions
published: true
---

# LOG

Returns the common (base 10) logarithm of a numerical expression, or the logarithm to an arbitrary base if specified as the first argument.
The value for which `log` is computed needs to be larger than 0, otherwise an error is returned.
If a base is provided, it also needs to be larger than 0 and not equal to 1.
You can use the function [LN](ln.md) to compute the natural logarithm (base e).

**Alias:** `LOG10` (does not support a custom `base` argument)

## Syntax
{: .no_toc}

```sql
LOG([<base>,] <value>);
```
## Parameters 
{: .no_toc}

| Parameter   | Description                                                                                                         | Supported input types |
| :----------- | :------------------------------------------------------------------------------------------------------------------- |:--------------------|
| `<base>`    | Optional. The base for the logarithm. The default base is 10.                                                       |  `DOUBLE PRECISION`
| `<value>` | The value for which to compute the logarithm. | `DOUBLE PRECISION` |

## Return Type
`DOUBLE PRECISION`

## Example
{: .no_toc}

{% include sql_examples/log_executable.md %}
