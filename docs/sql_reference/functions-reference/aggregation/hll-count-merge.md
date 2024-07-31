---
layout: default
title: HLL_COUNT_MERGE
description: Reference material for HLL_COUNT_MERGE
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Aggregation functions
published: true
---

# HLL_COUNT_MERGE

Merges one or more HLL++ sketches that were previously built using the aggregate
function [`HLL_COUNT_BUILD`](hll-count-build.md) into a new sketch.

Each sketch must be built on the same type and the same precision.
Attempts to merge sketches for different types or precisions results in an error.
For example, you cannot merge a sketch built from `INTEGER` data with one built from `TEXT` data,
or a sketch built with precision 13 and a sketch built with precision 14.

## Syntax

{: .no_toc}

```sql
HLL_COUNT_MERGE(<expression>)
```

## Parameters

{: .no_toc}

| Parameter      | Description                                                                                              | Supported input types |
|:---------------|:---------------------------------------------------------------------------------------------------------|:----------------------|
| `<expression>` | HLL++ sketch in a valid format, e.g. the output of the [`HLL_COUNT_BUILD`](hll-count-build.md) function. | `BYTEA`               |

## Return Type

`BYTEA`

## Example

{: .no_toc}

Following the [example](hll-count-build.md#example) in [`HLL_COUNT_BUILD`](hll-count-build.md):

```sql
SELECT hll_count_estimate(hll_count_merge(a)) AS hll_estimate, hll_count_merge(a) AS merged_sketch
FROM sketch_of_data_to_count;
```

| hll_estimate BIGINT | merged_sketch BYTEA            |
|:--------------------|:-------------------------------|
| 6606880             | \x2f4167677265676174654675.... |
