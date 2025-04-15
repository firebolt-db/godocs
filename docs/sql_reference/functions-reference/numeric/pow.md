---
redirect_from:
  - /sql-reference/functions-reference/exp.html
layout: default
title: POW
description: Reference material for POW, POWER functions
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Numeric functions
---

# POW
Returns a number `<value>` raised to the specified power `<value>`.

**Alias:** `POWER`

## Syntax
{: .no_toc}

```sql
POW(<value>, <exponent>);
```
## Parameters 
{: .no_toc}

| Parameter | Description                                                                                                         | Supported input types |
| :--------- | :------------------------------------------------------------------------------------------------------------------- |:------|
| `<value>`   | The base value of the exponent |`DOUBLE PRECISION` |
| `<exponent>`   | The power value of the exponent | `DOUBLE PRECISION` |

## Return Type
`DOUBLE PRECISION`

## Example
{: .no_toc}

{% include sql_examples/pow_executable.md %}
