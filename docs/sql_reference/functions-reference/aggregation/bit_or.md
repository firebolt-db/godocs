---
layout: default
title: BIT_OR
description: Reference material for BIT_OR
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Aggregation functions
---

# BIT_OR

Performs a bitwise `OR` operation on an integer expression, ignoring null input values. The numbers are represented in 2’s complement, meaning that the leftmost bit indicates the sign of the number. If the leftmost bit is 0, then the number is positive. If the leftmost bit is 1, the number is negative.

## Syntax

{: .no_toc}

```sql
BIT_OR
([ DISTINCT ] <expression>)
```
Note: `DISTINCT` does not have any effect on the result of the function.

## Parameters

{: .no_toc}

| Parameter      | Description                                  | Supported input types |
|:---------------|:---------------------------------------------|:----------------------|
| `<expression>` | The expression used to calculate the result. | `INT`, `BIGINT`       |

## Return Types

`INT` or `BIGINT` corresponding to the input type.

## Examples

{: .no_toc}

```sql
SELECT BIT_OR(a)
FROM generate_series(1, 10) as a;
```

**Returns**: `15`. Explanation: The query performs a bitwise `OR` operation on all integers randing from `1` to `10`. The query returns `15` because the bitwise `OR` across these numbers yields a binary value of `1111`, which is `15` in decimal.

```sql
SELECT BIT_OR(a)
FROM generate_series(-1, 1000) as a;
```

**Returns**: `-1`. Explanation: The query performs a bitwise `OR` operation on all integers ranging from `-1` to `1000`. Because `-1`, is represented as all 1s in 2's complement, the bitwise `OR` returns all 1s, which corresponds to `-1`, in 2's complement.

