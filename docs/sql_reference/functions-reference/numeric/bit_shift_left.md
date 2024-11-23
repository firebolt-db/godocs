---
layout: default
title: BIT_SHIFT_LEFT
description: Reference material for BIT_SHIFT_LEFT
parent: Numeric functions
---

# BIT_SHIFT_LEFT

Shifts the bits in the first argument to the left by `n` bits, where `n` is the second argument. Shifting left by `n` positions is equivalent to multiplying the number by `2^n`.

## Syntax

{: .no_toc}

```sql
BIT_SHIFT_LEFT(<value>, <bits>)
```

## Parameters

{: .no_toc}

| Parameter | Description                   | Supported input types |
|:----------|:------------------------------|:----------------------|
| `<value>` | Specifies the value to shift. | `INT`, `BIGINT`       |
| `<bits>`  | The number of bits to shift.  | `INT`                 |

## Return Types

The `BIT_SHIFT_LEFT` function returns a result of either type `INT` or `BIGINT`, depending on the type of the input `<expression>`.

## Examples

{: .no_toc}

{% include sql_examples/bit_shift_left_executable.md %}
