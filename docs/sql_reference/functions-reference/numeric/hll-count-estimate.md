---
layout: default
title: HLL_COUNT_ESTIMATE
description: Reference material for HLL_COUNT_ESTIMATE
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Numeric functions
published: true
---

# HLL_COUNT_ESTIMATE

Extracts a cardinality estimate of a single HLL++ sketch that was previously built using the aggregate
function [`HLL_COUNT_BUILD`](../aggregation/hll-count-build.md).

## Syntax

{: .no_toc}

```sql
HLL_COUNT_ESTIMATE(<expression>)
```

## Parameters

{: .no_toc}

| Parameter      | Description                                                                       | Supported input types |
|:---------------|:----------------------------------------------------------------------------------|:----------------------|
| `<expression>` | An HLL++ sketch produced by the [`HLL_COUNT_BUILD`](../aggregation/hll-count-build.md) function. | `BYTEA`               |

## Return Type

`BIGINT`

## Example

{: .no_toc}

Following the [example](../aggregation/hll-count-build.md#example) in [`HLL_COUNT_BUILD`](../aggregation/hll-count-build.md):

```sql
SELECT hll_count_estimate(a) AS hll_estimate
FROM sketch_of_data_to_count
ORDER BY 1;
```

| hll_estimate (BIGINT) |
|:----------------------|
| 3291008               |
| 4948957               |

```sql
SELECT hll_count_estimate(hll_count_merge(a)) AS hll_estimate
FROM sketch_of_data_to_count;
```

| hll_estimate (BIGINT) |
|:----------------------|
| 6606880               |
