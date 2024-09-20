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

Returns an approximate count, or cardinality, from a single HyperLogLog++ (HLL++) sketch, created with the [`HLL_COUNT_BUILD`](../aggregation/hll-count-build.md) aggregate
function.

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

Returns a count of type `BIGINT`.

## Examples

{: .no_toc}

**Example**

Following the [example](../aggregation/hll-count-build.md#example) in [`HLL_COUNT_BUILD`](../aggregation/hll-count-build.md), the code retrieves an approximate count of unique elements from an HLL++ sketch:

```sql
SELECT HLL_COUNT_ESTIMATE(a) AS hll_estimate
FROM sketch_of_data_to_count
ORDER BY 1;
```

**Returns**

| hll_estimate (BIGINT) |
|:----------------------|
| 3,291,008               |
| 4,948,957               |


**Example**
The following example merges multiple HLL++ sketches from the `a` column using `hll_count_merge` and retrieves an approximate count of unique elements:

```sql
SELECT HLL_COUNT_ESTIMATE(hll_count_merge(a)) AS hll_estimate
FROM sketch_of_data_to_count;
```

**Returns**

| hll_estimate (BIGINT) |
|:----------------------|
| 6,606,880               |

The previous code example uses `HLL_COUNT_ESTIMATE` to estimate the total number of unique elements across merged HLL++ sketches.