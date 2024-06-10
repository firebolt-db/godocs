---
layout: default
title: HLL_COUNT_BUILD
description: Reference material for HLL_COUNT_BUILD
parent: SQL functions
published: true
---

# HLL_COUNT_BUILD

Counts the approximate number of unique not NULL values, aggregating the values to HLL++ sketches represented as
the [BYTEA data type](../general-reference/bytea-data-type.md).
Multiple sketches can be merged to a single sketch using the aggregate function [`HLL_COUNT_MERGE`](hll-count-merge.md).
To estimate the final distinct count value, the scalar function [`HLL_COUNT_ESTIMATE`](hll-count-estimate.md) can be
used.
`HLL_COUNT_BUILD` uses the HLL++ algorithm and allows you to control the set sketch size precision, similar
to [`HLL_COUNT_DISTINCT`](hll-count-distinct.md).

`HLL_COUNT_BUILD` requires less memory than exact count distinct aggregation, but also introduces statistical uncertainty.
The default precision is 12, with a maximum of 20 set optionally.

{: .note}
> Higher precision comes at a memory and performance cost.

## Syntax

{: .no_toc}

```sql
HLL_COUNT_BUILD
( <expression> [, <precision> ] )
```

## Parameters

{: .no_toc}

| Parameter      | Description                                                                                                            | Supported input types |
|:---------------|:-----------------------------------------------------------------------------------------------------------------------|:----------------------|
| `<expression>` | Any column name or function that return a column name.                                                                 | Any type              |
| `<precision>`  | Optional literal integer value to set precision. If not included, the default precision is 12. Precision range: 12-20. | `INTEGER`, `BIGINT `  |

## Return Type

`BYTEA`

## Example

{: .no_toc}

```sql
CREATE TABLE data_to_count AS
SELECT *
FROM generate_series(0, 10000000, 3) a;

SELECT count(distinct a) AS accurate_count
FROM data_to_count;
```

| accurate_count (BIGINT) |
|:------------------------|
| 3333334                 |

```sql
CREATE TABLE data_to_count2 AS
SELECT *
FROM generate_series(0, 10000000, 2) a;

SELECT count(distinct a) AS accurate_count
FROM data_to_count2;
```

| accurate_count (BIGINT) |
|:------------------------|
| 5000001                 |

```sql
CREATE TABLE sketch_of_data_to_count AS
SELECT hll_count_build(a) a
FROM data_to_count;

INSERT INTO sketch_of_data_to_count
SELECT hll_count_build(a)
FROM data_to_count2;

SELECT hll_count_estimate(a) AS hll_estimate, a AS sketch
FROM sketch_of_data_to_count
ORDER BY 1;
```

| hll_estimate (BIGINT) | sketch (BYTEA)               |
|:----------------------|:-----------------------------|
| 3291008               | \x2f41676772656761746546.... |
| 4948957               | \x2f41676772656761746546.... |

```sql
SELECT hll_count_estimate(hll_count_merge(a)) AS hll_estimate
FROM sketch_of_data_to_count;
```

| hll_estimate (BIGINT) |
|:----------------------|
| 6606880               |