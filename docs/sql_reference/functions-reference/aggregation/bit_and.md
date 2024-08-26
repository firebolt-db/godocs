---
layout: default
title: BIT_AND
description: Reference material for BIT_AND
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Aggregation functions
---

# BIT_AND

Performs a bitwise AND operation on an integer expression.
Ignore null input values. Numbers represented in 2’s complement.

## Syntax

{: .no_toc}

```sql
BIT_AND
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
SELECT BIT_AND(a)
FROM generate_series(1, 10) as a;
```

**Returns**: `0`

```sql
SELECT BIT_AND(a)
FROM UNNEST([-1,3]) as a;
```

**Returns**: `3`

