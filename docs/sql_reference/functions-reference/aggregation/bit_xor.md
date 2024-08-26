---
layout: default
title: BIT_XOR
description: Reference material for BIT_XOR
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Aggregation functions
---

# BIT_XOR

Performs a bitwise XOR operation on an integer expression.
Ignore null input values. Numbers represented in 2’s complement.

## Syntax

{: .no_toc}

```sql
BIT_XOR
([ DISTINCT ] <expression>)
```
Note: `DISTINCT` effect on the results of the function.

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
SELECT BIT_XOR(a)
FROM UNNEST([1,2,1]) as a;
```

**Returns**: `1`

```sql
SELECT BIT_XOR(distinct a)
FROM UNNEST([1,2,1]) as a;
```

**Returns**: `3`

```sql
SELECT BIT_XOR(a)
FROM generate_series(1, 10) as a;
```

**Returns**: `11`

```sql
SELECT BIT_XOR(a)
FROM generate_series(-1, 1000) as a;
```

**Returns**: `-1001`

