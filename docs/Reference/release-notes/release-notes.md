---
layout: default
title: Release notes
description: Latest release notes for the Firebolt data warehouse.
parent: General reference
nav_order: 1
has_toc: false
has_children: false
---

# Release notes

Firebolt continuously releases updates so that you have access to the latest and most stable product. While these updates might occur daily, but we consolidate release notes over a longer time period for your convenience. The following are the release notes from the latest version.

- See the [Release notes archive](../release-notes/release-notes-archive.md) for release notes from earlier versions.

{: .note}
Firebolt may deploy releases in phases, meaning that new features and changes may not be immediately available to all accounts on the specified release date. 

* Topic ToC
{:toc}

## DB version 4.3
**August 2024**

### Breaking Changes

<!-- Owned by Vitaliy Lyudvichenko (for FIR-35188) --> **Temporarily restricted column DEFAULT expressions in CREATE TABLE statements**
{: style="color:red;"}

Column DEFAULT expressions in CREATE TABLE statements have been temporarily restricted, they can only consist of literals and the following functions: `CURRENT_DATE()`, `LOCALTIMESTAMP()`, `CURRENT_TIMESTAMP()`, `NOW()`. Existing tables with column DEFAULT expressions are not affected.

<!-- Auto Generated Markdown for FIR-24961 - Owned by Kfir Yehuda --> **Underflow detection while casting from TEXT to floating point data types**
{: style="color:red;"}

Firebolt now detects underflow, a condition where a numeric value becomes smaller than the minimum limit that a data type can represent, when casting from TEXT to floating point data types. For example, the query `select '10e-70'::float4;` now returns an error, while it previously returned `0.0`.

<!-- Auto Generated Markdown for FIR-33925 - Owned by Tobias Humig --> **Returning query execution errors in JSON format through the HTTP API**
{: style="color:red;"}

Firebolt's HTTP API now returns query execution errors in JSON format, allowing for future enhancements like including metadata such as error codes, or the location of a failing expression within the SQL script.

<!-- Auto Generated Markdown for FIR-35022 - Owned by David Boublil -->**Changed default of case_sensitive_column_mapping parameter in COPY FROM**
{: style="color:red;"}

The default value for the `CASE_SENSITIVE_COLUMN_MAPPING` parameter in `COPY FROM` is now `FALSE`, meaning that if a target table contains column names in uppercase and the source file to ingest has the same columns in lowercase, the ingestion will consider them the same column and ingest the data.

<!-- Auto Generated Markdown for FIR-34581 - Owned by Kfir Yehuda -->**`extract` function returns Numeric(38,9) for Epoch, second, and millisecond extraction**
{: style="color:red;"}

The result data type of the `extract` function for epoch, second, and millisecond was changed to return the type Numeric(38,9) instead of a narrower Numeric type. For example, `select extract(second from '2024-04-22 07:10:20'::timestamp);` now returns Numeric(38,9) instead of Numeric(8,6).

### New Features

<!-- Auto Generated Markdown for FIR-32335 - Owned by Krishna Thotapalli -->**Role-based permissions for COPY FROM and External Table processes**

Enabled role-based permissions for COPY FROM and External Table processes.

<!-- Auto Generated Markdown for FIR-34932 - Owned by Kfir Yehuda -->**HLL-based count distinct functions compatible with the Apache DataSketches library**

Firebolt now supports count-distinct functions using the HLL (HyperLogLog) algorithm, compatible with the Apache DataSketches library.
For details and examples, see documentation on the functions 
[APACHE_DATASKETCHES_HLL_BUILD](../../sql_reference/functions-reference/datasketches/apache-datasketches-hll-build.md),
[APACHE_DATASKETCHES_HLL_MERGE](../../sql_reference/functions-reference/datasketches/apache-datasketches-hll-merge.md),
and [APACHE_DATASKETCHES_HLL_ESTIMATE](../../sql_reference/functions-reference/datasketches/apache-datasketches-hll-estimate.md).

<!-- Auto Generated Markdown for FIR-33707 - Owned by Zhen Li -->**Supported additional join conditions and removed the restriction on the number of inequality predicates**

Firebolt has added enhanced support for more join conditions. As long as there is one equality predicate comparing a left column to a right column of the join, which is not part of a disjunctive (OR) expression, the remaining join condition can be arbitrary. The previous limitation on the number of inequality predicates has been removed.

### Performance Improvements

<!-- FIR-32882 - Owned by Michael Freitag -->**Multi-node query performance**

Firebolt has improved the performance of data transfer between nodes, resulting in faster overall query execution times.

<!-- Auto Generated Markdown for FIR-24598 - Owned by Leonard von Merzljak -->**Enhanced Interval Arithmetic Support**

Firebolt has enhanced support for interval arithmetic. You can now use expressions of the form `date_time + INTERVAL * d`, where `date_time` is a expression of type Date, Timestamp, TimestampTz, and `d` is an expression of type DOUBLE PRECISION. The interval is now scaled by `d` before being added to `date_time`. For example, writing `INTERVAL '1 day' * 3` is equivalent to writing `INTERVAL '3 days'`.

<!-- Auto Generated Markdown for FIR-33723 - Owned by Lorenz Hübschle -->**Optimized selective inner and right joins on primary index and partition by columns to reduce rows scanned**

Selective inner and right joins on primary index and partition by columns now can now benefit from pruning. This reduces the number of rows scanned by filtering out rows that are not part of the join result early in the process. This optimization works best when joining on the first primary index column or a partition by column. The optimization is applied automatically when applicable, and no action is required. Queries that used this optimization will display "Prune:" labels on the table scan in the EXPLAIN (PHYSICAL) or EXPLAIN (ANALYZE) output.

### Bug Fixes

<!-- Auto Generated Markdown for FIR-34721 - Owned by Demian Hespe -->**Fixed a bug in the combination of cross join and the `index_of` function**

Resolved an issue where the `index_of` function would fail when applied to the result of a cross join that produced a single row.

