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

Escape [string literals](../sql_reference/data-types.md) now support octal and Unicode escape sequences. As a result, escape string literals now behave exactly like PostgreSQL. Example: `SELECT E'\U0001F525b\x6F\154t';` returns `🔥bolt`. If the setting `standard_conforming_strings` is not enabled for you, regular string literals (e.g., `SELECT 'foo';`) will also recognize the new escape sequences. However, we recommend exclusively using escape string literals for using escape sequences. Please be aware that you will get different results if you previously used (escape) string literals containing the syntax we now use for Unicode and octal escape sequences.

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
* Fixed a bug involving ['btrim'](../sql_reference/functions-reference/string/btrim.md) string characters, where invoking `btrim`, `ltrim`, `rtrim`, or `trim` with a literal string but non-literal trim characters could result in an error.
