---
layout: default
title: Table-valued functions
description: Reference for strvectoring functions
nav_order: 15
parent: SQL functions
has_children: true
---

## Table-valued functions

A Table-Valued Function (TVF) returns a set of rows. You can use a table-valued function anywhere you can use a table. For example, the `generate_series` TVF generates a range of numbers as rows.
```sql
-- This query produces 100 rows with numbers 1 to 100. The table alias r(x) names the output column x.
SELECT x FROM generate_series(1, 100) r(x);
```

Firebolt provides TVFs that make it easy to explore data on S3. The TVF `list_objects` allows you to explore files on S3. Functions such as `read_parquet` make it easy to read data from S3.
