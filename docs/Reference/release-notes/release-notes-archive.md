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
## DB version 3.30
**November 2023**

* [New features](#new-features)
* [Enhancements, changes, and new integrations](#enhancements-changes-and-new-integrations)
* [Resolved issues](#resolved-issues)

### New features
{: .no_toc}

<!--- FIR-27590 ---> **New comparison operators**

[New comparison operators](../../sql_reference/operators.md) `IS DISTINCT FROM` and `IS NOT DISTINCT FROM` have been added.

### Enhancements, changes and new integrations
{: .no_toc}

<!--- FIR-27355 ---> **Support for nullable arrays**

Support has been added to allow the [ANY_MATCH](../../sql_reference/functions-reference/Lambda/any-match.md) lambda function to work with nullable arrays

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
