---
layout: default
title: DataSketches functions
description: Reference for datasketches functions
nav_order: 7
parent: SQL functions
has_children: true
---

## Apache DataSketches functions

[Apache DataSketches](https://datasketches.apache.org/) is a robust library that provides a collection of advanced algorithms for data analysis.
These algorithms are designed to work efficiently with large datasets and provide accurate results for various data analysis tasks.
The following functions are part of the Apache Datasketches library and can be used in SQL queries to perform advanced data analysis tasks.

### Distinct Counting with HyperLogLog Sketches
HyperLogLog (HLL) Sketches are a highly efficient probabilistic data structure used for cardinality estimation,
which means they can quickly and accurately count the number of distinct elements in large datasets.
The following functions are used to work with HLL sketches in SQL queries:
[APACHE_DATASKETCHES_HLL_BUILD](apache-datasketches-hll-build.md), [APACHE_DATASKETCHES_HLL_MERGE](apache-datasketches-hll-merge.md), [APACHE_DATASKETCHES_HLL_ESTIMATE](apache-datasketches-hll-estimate.md).
