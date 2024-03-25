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

Support has been added to allow the [ANY_MATCH](../sql-reference/functions-reference/any-match.md) lambda function to work with nullable arrays.

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

The columns `spilled_bytes_uncompressed` and `spilled_bytes_compressed` of `information_schema.query_history` have been replaced by a single column `spilled_bytes`(../sql_reference/information-schema/query-history-view.md). It contains the amount of data that was spilled to disk temporarily while executing the query.

<!--- FIR-29536 --->**Aggregating index placement**

Aggregating index is now placed in the same namespace as tables and views.

<!--- FIR-29225 --->**Syntax and planner support for LATERAL scoping**

LATERAL is now a reserved keyword (../Reference/reserved-words.md). It must now be used within double-quotes when using it as an object identifier.

### Resolved issues

<!--- FIR-21152 --->Changed return for division by 0 from null to fail.

<!--- FIR-18709 --->Updated error log for upload failure for clarity.

<!--- FIR-29147 --->Fixed a bug in 'unnest' table function that occurred when not all of the 'unnest' columns were projected.

<!--- FIR-28187 --->Changed the behavior of `split_part`(../sql_reference/functions-reference/string/split-part.md) when an empty string is used as delimiter.

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
