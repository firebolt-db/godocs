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

Firebolt continuously releases updates so that you can benefit from the latest and most stable service. These updates might happen daily, but we aggregate release notes to cover a longer time period for easier reference. The most recent release notes from the latest version are below. 

- See the [Release notes archive](../release-notes/release-notes-archive.md) for earlier-version release notes.

{: .note}
Firebolt might roll out releases in phases. New features and changes may not yet be available to all accounts on the release date shown.

## DB version 3.31
**February 2024**

* [New features](#new-features)
* [Enhancements, changes, and new integrations](#enhancements-changes-and-new-integrations)
* [Resolved issues](#resolved-issues)

### New features

<!--- FIR-22307 --->**PG compliant division**

LQP2 has a new division operator that is PG compliant, by default.

<!--- FIR-29179 --->**Prevents usage of new line delimeter for schema inference**

An error will now occur if schema inference is used with the option “delimiter” set to something other than the default. 

### Enhancements, changes and new integrations

<!--- FIR-29747 --->**Disabled Unix Time Functions**

The following functions are not supported anymore:
'from_unixtime'
'to_unix_timestamp'
'to_unix_time'

<!--- FIR-27548 --->**Simplified table protobuf representation**

Unique constraints in tables will be blocked for new accounts.

<!--- FIR-29729 --->**Renamed spilled metrics columns**

The columns `spilled_bytes_uncompressed` and `spilled_bytes_compressed` of `information_schema.query_history` have been replaced by a single column [`spilled_bytes`](../../sql_reference/information-schema/query-history-view.md). It contains the amount of data that was spilled to disk temporarily while executing the query.

<!--- FIR-27799 --->**Updated AWS billing error message**

The error message for an AWS billing issue on Engine Start was on Engine Start was changed to add more information and clarity.  

<!--- FIR-28276 --->**New requirements updated for EXPLAIN**

For [`EXPLAIN`](../../sql_reference/commands/queries/explain.md) queries, we now allow only one of the following options at the same time: `ALL`, `LOGICAL`, `PHYSICAL`, `ANALYZE`.`EXPLAIN (ALL)` now returns the plans in multiple rows instead of multiple columns.

<!--- FIR-29536 --->**Aggregating index placement**

Aggregating index is now placed in the same namespace as tables and views.

<!--- FIR-29225 --->**Syntax and planner support for LATERAL scoping**

[LATERAL](../reserved-words.md) is now a reserved keyword. It must now be used within double-quotes when using it as an object identifier

### Resolved issues

<!--- FIR-21152 --->
* Changed return for division by 0 from null to fail.

<!--- FIR-18709 --->
* Updated error log for upload failure for clarity.

<!--- FIR-29147 --->
* Fixed a bug in 'unnest' table function that occurred when not all of the 'unnest' columns were projected.

<!--- FIR-28187 --->
* Changed the behavior of [`split_part'](../../sql_reference/functions-reference/string/split-part.md) when an empty string is used as delimiter.

<!--- FIR-28623 --->
* Fixed a bug where floating point values `-0.0` and `+0.0`, as well as `-nan` and `+nan` were not considered equal in distributed queries.

<!--- FIR-29759 --->
* 'TRY_CAST' from 'TEXT' to 'NUMERIC' now works as expected: if the value cannot be parsed as 'NUMERIC' it produces null.