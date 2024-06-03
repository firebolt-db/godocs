---
layout: default
title: Release notes archive
description: Release notes archive for the Firebolt data warehouse.
grand_parent: General reference
parent: Release notes
nav_order: 2
has_toc: false
has_children: false
---

# Release notes archive
{: .no_toc}

We provide an archive of release notes for your historical reference.

* Topic ToC
{:toc}

## DB version 3.33
**April 2024**

* [Enhancements, changes, and new integrations](#enhancements-changes-and-new-integrations)
* [Resolved issues](#resolved-issues)

### Enhancements, changes and new integrations

<!--- FIR-32055 --->**Removed 'element_at' Function**

The `element_at` function for arrays has been removed and replaced with the `[]` operator. 

<!--- FIR-31458 --->**Change of return type from BIGINT to INTEGER**

The `index_of`/`array_position` function now returns INTEGER instead of BIGINT. 

<!--- FIR-31280 --->**Removed LIMIT DISTINCT syntax**

The `LIMIT_DISTINCT` syntax is no longer supported by Firebolt.

  {: .note}
  New breaking change.

<!--- FIR-32252 --->**Updated CAST function behavior**

We have moved all cast logic to runtime in Firebolt. The `castColumn` function is now replaced by `fbCastColumn`, ensuring consistent casting behavior and resolving issues with the `COPY FROM` operation and other cast calls. Uses of implicit/explicit `CAST` may result in errors due to this fix.

### Resolved issues

<!--- FIR-31069 --->
* Fixed a bug in `array_position` where searching for `NULL` in an array with non-null elements incorrectly returned a match in some cases. 


## DB version 3.32
**April 2024**

* [New features](#new-features)
* [Enhancements, changes, and new integrations](#enhancements-changes-and-new-integrations)
* [Resolved issues](#resolved-issues)

### New features

<!--- FIR-4082 --->**Expose and document 'typeof' as a toTypeName function**

The `typeof` function has been added, which returns the data type of a SQL expression as a string.

### Enhancements, changes and new integrations

<!--- FIR-25079 --->**Spilling Aggregations**

Firebolt can now process most aggregations that exceed the available main memory of the engine by spilling to the SSD cache when needed. This happens transparently to the user. A query that made use of this capability will populate the `spilled_bytes` column in `information_schema.query_history`. Spilling does not support aggregations where a single group exceeds the available memory (e.g., `select count(distinct high_cardinality_column) from huge_table`) and may not yet work reliably for all aggregate functions or engine specs. We will continue improving the feature in upcoming releases.

<!--- FIR-25892 ---> **No overflow detected in cast from FLOAT to DECIMAL**

Fix results of casting from `float32` to decimals with precision > 18.
In addition to the correct results breaking change, there are certain queries that was working before that now will fail involving overflow. 

Example query: 
* `SELECT` 17014118346046923173168730371588410572::REAL::DECIMAL(37,0). 

Previously, this was working and returned a wrong result, but now it will fail with an overflow error.

<!--- FIR-29174 --->**ARRAY_COUNT returns 0 instead of NULL**

`ARRAY_COUNT` on `NULL` array now returns `0` instead of `NULL`.

<!--- FIR-29639 --->**No overflow check in arithmetic operations**

Arithmetic operators (i.e. multiplication, addition, subtraction, and division) now perform correct overflow checking. This means that queries that used to return wrong results in the past now throw runtime errors.

Example queries: 
* `SELECT` 4294967296 * 4294967296 -> now throws an error, before it would return 0

* `SELECT` 9223372036854775807 + 9223372036854775807 -> now throws an error, before it would return -2

* `SELECT` (a + b) * c -> this might throw runtime errors if there are large values in the column, but this is highly data dependent.

<!--- FIR-29747 --->**Implement bool_or/bool_and aggregation functions**

New aggregate functions bool_or and bool_and have been added. 

<!--- FIR-29729 --->**Remove old deprecate REGENERATE AGGREGATING INDEX**

'REGENERATE AGGREGATING INDEX' syntax has now been removed.  

<!--- FIR-30398 --->**Align the syntax of our "escape" string literals with PostgreSQL**

Escape [string literals](../../sql_reference/data-types.md) now support octal and Unicode escape sequences. As a result, escape string literals now behave exactly like PostgreSQL. Example: `SELECT E'\U0001F525b\x6F\154t';` returns `🔥bolt`. If the setting `standard_conforming_strings` is not enabled for you, regular string literals (e.g., `SELECT 'foo';`) will also recognize the new escape sequences. However, we recommend exclusively using escape string literals for using escape sequences. Please be aware that you will get different results if you previously used (escape) string literals containing the syntax we now use for Unicode and octal escape sequences.

<!--- FIR-30789 --->**Change return value of length and octet_length to INT**

Length and array_length now return INTEGER instead of BIGINT.

<!--- FIR-30393 --->**Subqueries in the GROUP BY/HAVING/ORDER BY clauses change**

Subqueries in `GROUP BY/HAVING/ORDER BY` can no longer references columns from the selection list of the outer query via their aliases as per PG compliance.  `select 1 + 1 as a order by (select a);` used to work, but now fails with `unresolved name a` error.

<!--- FIR-31163 --->**Bytea serialization to CSV fix**

Changed Bytea to CSV export: from escaped to non escaped. 

Example: 
* `COPY` (select 'a'::bytea) to 's3...'; the results will now be "\x61" instead of "\\x61".

### Resolved issues

<!--- FIR-25890 --->
* Fixed results of casting literal float to numeric. In the past the float literal was casted to float first then to numeric, this caused us to lose precision.

Examples:
* `SELECT` 5000000000000000000000000000000000000.0::DECIMAL(38,1); -> 5000000000000000000000000000000000000.0
* `SELECT` (5000000000000000000000000000000000000.0::DECIMAL(38,1)+5000000000000000000000000000000000000.0::DECIMAL(38 1)); -> ERROR: overflow.

Note that before, it was not an error and resulted in: 9999999999999999775261218463046128332.8.

<!--- FIR-26910 --->
* Fixed a longstanding bug with >= comparison on external table source_file_name. Whereas this would previously have scraped fewer files than expected off the remote S3 bucket, you will now get all files properly (lexicographically) compared against the input predicate. 

<!--- FIR-30107 --->
* Fixed a bug when `USAGE ANY ENGINE` (and similar) privileges were shown for * account. Now it is being show for current account.

<!--- FIR-30490 --->
* Fixed a bug involving ['btrim'](../../sql_reference/functions-reference/string/btrim.md) string characters, where invoking `btrim`, `ltrim`, `rtrim`, or `trim` with a literal string but non-literal trim characters could result in an error.

## DB version 3.31
**March 2024**

* [New features](#new-features)
* [Enhancements, changes, and new integrations](#enhancements-changes-and-new-integrations)
* [Resolved issues](#resolved-issues)

### New features

<!--- FIR-22307 --->**PG compliant division**

LQP2 has a new division operator that is PG compliant, by default.

<!--- FIR-29179 --->**Prevents usage of new line delimeter for schema inference**

An error will now occur if schema inference is used with the option “delimiter” set to something other than the default. 

### Enhancements, changes and new integrations

<!--- FIR-27548 --->**Simplified table protobuf representation**

Unique constraints in tables will be blocked for new accounts.

<!--- FIR-27355 ---> **Support for nullable arrays**

Support has been added to allow the [ANY_MATCH](../../sql-reference/functions-reference/any-match.md) lambda function to work with nullable arrays.

<!--- FIR-27799 --->**Updated AWS billing error message**

The error message for an AWS billing issue on Engine Start was on Engine Start was changed to add more information and clarity.  

<!--- FIR-28276 --->**New requirements updated for EXPLAIN**

For `EXPLAIN` queries, we now allow only one of the following options at the same time: `ALL`, `LOGICAL`, `PHYSICAL`, `ANALYZE`.`EXPLAIN (ALL)` now returns the plans in multiple rows instead of multiple columns.

<!--- FIR-29747 --->**Disabled Unix Time Functions**

The following functions are not supported anymore:
'from_unixtime'
'to_unix_timestamp'
'to_unix_time'

<!--- FIR-29729 --->**Renamed spilled metrics columns**

The columns `spilled_bytes_uncompressed` and `spilled_bytes_compressed` of `information_schema.query_history` have been replaced by a single column `spilled_bytes`. It contains the amount of data that was spilled to disk temporarily while executing the query.

<!--- FIR-29536 --->**Aggregating index placement**

Aggregating index is now placed in the same namespace as tables and views.

<!--- FIR-29225 --->**Syntax and planner support for LATERAL scoping**

[LATERAL](../../Reference/reserved-words.md) is now a reserved keyword. It must now be used within double-quotes when using it as an object identifier.

### Resolved issues

<!--- FIR-21152 --->Changed return for division by 0 from null to fail.

<!--- FIR-18709 --->Updated error log for upload failure for clarity.

<!--- FIR-29147 --->Fixed a bug in 'unnest' table function that occurred when not all of the 'unnest' columns were projected.

<!--- FIR-28187 --->Changed the behavior of [`split_part`](../../sql_reference/functions-reference/string/split-part.mdmd) when an empty string is used as delimiter.

<!--- FIR-28623 --->Fixed a bug where floating point values `-0.0` and `+0.0`, as well as `-nan` and `+nan` were not considered equal in distributed queries.

<!--- FIR-29759 --->TRY_CAST from TEXT to NUMERIC now works as expected: if the value cannot be parsed as NUMERIC it produces null.

## DB version 3.30
**November 2023**

* [New features](#new-features)
* [Enhancements, changes, and new integrations](#enhancements-changes-and-new-integrations)
* [Resolved issues](#resolved-issues)

### New features
{: .no_toc}

<!--- FIR-27590 ---> **New comparison operators**

[New comparison operators](../general-reference/operators.md) `IS DISTINCT FROM` and `IS NOT DISTINCT FROM` have been added.

### Enhancements, changes and new integrations
{: .no_toc}

<!--- FIR-27355 ---> **Support for nullable arrays**

Support has been added to allow the [ANY_MATCH](../sql-reference/functions-reference/any-match.md) lambda function to work with nullable arrays

### Resolved issues
{: .no_toc}

* Indirectly granted privileges have been removed from the `information_schema.object_privileges` view. 

* Fixed an issue where `ARRAY_FIRST` and `ARRAY_FIRST_INDEX` returned an error if the given input was nullable.

## DB version 3.29
**October 2023**

* [New features](#new-features)
* [Enhancements, changes, and new integrations](#enhancements-changes-and-new-integrations)

### New features
{: .no_toc}

<!--- FIR-25082 ---> **EXPLAIN ANALYZE now available for detailed query metrics**

You can now use the [EXPLAIN command](../../sql_reference/commands/queries/explain.md) to execute `EXPLAIN (ANALYZE) <select statement>` and get detailed metrics about how much time is spent on each operator in the query plan, and how much data is processed. The query plan shown there is the physical query plan, which you can inspect using `EXPLAIN (PHYSICAL) <select statement>` without executing the query. It shows how query processing is distributed over the nodes of an engine.


### Enhancements, changes and new integrations
{: .no_toc}

<!--- FIR-25636 ---> **PERCENTILE_CONT and PERCENTILE_DISC now return PostgreSQL-compliant results**

[PERCENTILE_CONT](../../sql_reference/functions-reference/window/percentile-cont-window.md) for decimal input now returns DOUBLE PRECISION instead of NUMERIC data type. 

<!--- FIR-24362 ---> **Virtual column 'source_file_timestamp' uses new data type**

The virtual column `source_file_timestamp` has been migrated from the data type `TIMESTAMP` (legacy timestamp type without time zone) to the type `TIMESTAMPTZ` (new timestamp type with time zone).

Despite the increased resolution, the data is still in second precision as AWS S3 provides them only as unix seconds.

Use `source_file_timestamp - NOW()` instead of `DATE_DIFF('second', source_file_timestamp, NOW())`

<!--- FIR-10514 ---> **New function added**

A new alias `ARRAY_TO_STRING` has been added to function [ARRAY_JOIN](../../sql_reference/functions-reference/array/array-join.md).


## DB version 3.28
**September 2023**

* [Resolved issues](#resolved-issues)


### Resolved issues
{: .no_toc}

* <!--- FIR-17240 ---> `IN` expressions with scalar arguments now return Postgres-compliant results if there are `NULL`s in the `IN` list. 

* <!--- FIR-26293 ---> information_schema.running_queries returns ID of a user that issued the running query, not the current user.

* <!--- FIR-26187 ---> Update error message to explain upper case behavior 
