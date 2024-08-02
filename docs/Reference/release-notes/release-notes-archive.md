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

## DB version 4.1
**June 2024**

* [Resolved issues](#resolved-issues)

### Resolved issues

<!--- FIR-32985--->
* Fixed an issue causing errors when using `WHERE column IN (...)` filters on external table scans.
  
## DB version 4.0
**June 2024**

* [Breaking Changes](#breaking-changes)
* [Enhancements, changes, and new integrations](#enhancements-changes-and-new-integrations)

### Breaking Changes 
{: style="color:red;"}

<!--- FIR-33028 --->**Array Casting Nullability Update**
{: style="color:red;"}

Cast to array will no longer support specifying nullability of the inner type. 
Example: 

```sql
a::array(int null)
``` 
or 
```sql
cast(a as array(int not null)) 
```
will now fail, and need to be rewritten as: 
```sql
a::array(int) 
``` 
or 
```sql
cast(a as array(int)). 
```


<!--- FIR-32252 --->**Postgres-compliant Cast**
{: style="color:red;"}

Casts now behave the same across the product and adhere to the list of supported casts. Some usages of casts (explicit, implicit, or assignment cast) that were previously allowed are no longer supported and now result in errors. For more details on list of supported casts, see the documentation [here](https://docs.firebolt.io/godocs/sql_reference/data-types.html#type-conversion).

### Enhancements, changes and new integrations
{: style="color:black;"}

<!--- FIR-32711 --->**Query Cancelation on HTTP Connection Drop**

Going forward, when the network connection between the client and Firebolt is dropped (for example because the Firebolt UI tab was closed or due to network issues), DML queries (INSERT, UPDATE, DELETE, etc) are no longer canceled automatically, but will keep running in the background. You can continue to monitor their progress in `information_schema.engine_running_queries` or cancel them manually using the `cancel query` statement if desired. DQL queries (SELECT) are still canceled automatically on connection drop. 

<!--- FIR-31795 --->**New Aggregate Functions: `CHECKSUM` and `hash_agg`**

`CHECKSUM` and `hash_agg` functions are now supported for aggregating indexes. Note that when the `hash_agg` function doesn't receive rows, the result is 0.


## DB version 3.34
**May 2024**

* [Enhancements, changes, and new integrations](#enhancements-changes-and-new-integrations)
* [Resolved issues](#resolved-issues)

### Enhancements, changes and new integrations

<!--- FIR-32710 --->**Removed `MATCH` function**

The `match` function has been removed and replaced with [`regexp_like`](../../sql_reference/functions-reference/string/regexp-like.md). 

<!--- FIR-32693 --->**Producing an error for array function failure instead of NULL**

Array function queries that accept two or more array arguments now produce an error. If you call an array function such as `array_transform(..)` or `array_sort(..)` with multiple array arguments, the arrays must have the same size. 
For example: 

```sql
array_transform(x, y -> x + y, arr1, arr2)
```

This raises an error if `array_length(arr1) != array_length(arr2)`. We now also perform this check for NULL literals. If you previously used `array_transform(x, y -> x + y, NULL::INT[], Array[5, 6])`, you got back `NULL`. Now, the query using that expression will raise an error.

<!--- FIR-32652 --->**Added ARRAY_FIRST function**

The [`array_first`](../../sql_reference/functions-reference/Lambda/array-first.html) function has been added. It returns the first element in the given array for which the given function returns `true`.

<!--- FIR-32597 --->**New name for `any_match`**

A new name for `any_match` has been added: [`array_any_match`](../../sql_reference/functions-reference/Lambda/array-any-match.md). `any_match` will be kept as an alias. 

<!--- FIR-32566 --->**Updated ARRAY_SUM return types**

The `array_sum` function of `bigint[]` now returns a numeric value and `array_sum` of `real[]` returns a real value. 

<!--- FIR-32491 --->**Precedence of operators**

Breaking change in operator precedence between comparison operators such as `=`, `<`, `>`, and `IS` operator. New behavior is compatible with Postgres. 

Examples of query that changed behavior:

```sql
select 1 is null = 2 is null
```
This used to be `true`, because it was interpreted as `select (1 is null) = (2 is null)`. It now becomes an error of incompatible types in `=`

```sql
select false = false is not null
```
The result used to be `false` - `select false = (false is not null)`, but now is `true` - `select (false = false) is not null`.

<!--- FIR-32451 --->**Dropping the role**

Role cannot be dropped if there are permissions granted to the role. The error message will be displayed if you need to manually drop permissions associated to the role.

<!--- FIR-32163 --->**Coalesce Short-Circuiting**

`COALESCE` now supports short-circuiting in Firebolt. Queries such as `COALESCE(a, 1 / 0) FROM t` could fail before, even when there were no NULLs in t. Only `CASE WHEN` supported short circuiting. Firebolt is now aligned with PostgreSQL and supports short circuiting in `COALESCE` as well.

<!--- FIR-31821 --->**Create table under I_S schema**

You can now execute `CREATE TABLE`/`VIEW`/`AGGREGATING INDEX` only under the public schema. 

<!--- FIR-31680 --->**Improved error message for JSON `PARSE_AS_TEXT` format**

The error message for external tables created with JSON `PARSE_AS_TEXT` format has been revised. This format reads specifically into a *single* column of type either TEXT or `TEXT NOT NULL`. (Note there may be external table partition columns defined after the single TEXT column, and they are okay). Now, only the error message regarding the `CREATE EXTERNAL TABLE` statement on a user's first attempt to use `SELECT` will be seen. Support for reading format JSON `PARSE_AS_TEXT=TRUE` into a `TEXT NOT NULL` column has been added.

<!--- FIR-29793 --->**Implemented column_mismatch**

Support for `ALLOW_COLUMN_MISMATCH` in `COPY INTO` has been added. 

<!--- FIR-296907 --->**Corrected NULL behavior of `STRING_TO_ARRAY`**

The behavior of `string_to_array` now matches its behavior in PostgreSQL. The change affects NULL delimiters where the string is split into individual characters, as well as empty strings and where the output is now an empty array. 

<!--- FIR-27311 --->**Changed city_hash behavior for nullable inputs**

The behavior for `city_hash` has changed for nullable inputs. 
For example:
```sql
SELECT CITY_HASH([null]) = CITY_HASH([''])
```
This is now false. 

<!--- FIR-16217 --->**Function `ARRAY_AGG` now preserves NULLS**

The `array_agg` function has been changed to return PostgreSQL-compliant results:
  * `array_agg` now preserves `NULL` values in its input, e.g. `select array_agg(x) from unnest(array [1,NULL,2] x)` returns `{1,NULL,2}`
  * `array_agg` now returns `NULL` instead of an empty array if there are no input values

<!--- FIR-8970 --->**Lambda parameters are no longer supported by `array_sum`**

Array aggregate functions no longer support lambda parameters. To get the old behavior for conditional lambda functions, use transform instead. 
For example:

```sql
array_sum(transform(...))
```

**Explicit Parquet conversion from DATE to INT is now needed**

A breaking change has been implemented in raising an error on reading a Parquet/ORC `DATE`/`TIMESTAMP` column if the `EXTERNAL TABLE` expects the column to have type `INT`/`BIGINT`. `DATE`/`TIMESTAMP` cannot be cast to `INT`/`BIGINT`, and external table scans will no longer allow this cast either. You need to explicitly transform the Parquet/ORC `DATE`/`TIMESTAMP` column with `EXTRACT`(`EPOCH FROM` col) to insert it into an `INT`/`BIGINT` column.

### Resolved issues

<!--- FIR-32432 --->
* Fixed a bug where negation did not check for overflows correctly.

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

<!--- FIR-32252 --->**Updated CAST function behavior**

All cast logic has been moved to runtime in Firebolt. The `castColumn` function is now replaced by `fbCastColumn`, ensuring consistent casting behavior and resolving issues with the `COPY FROM` operation and other cast calls. Uses of implicit/explicit `CAST` may result in errors due to this fix.

  {: .note}
  New breaking change.

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

Support has been added to allow the [ARRAY_ANY_MATCH](../../sql_reference/functions-reference/Lambda/array-any-match.md) lambda function to work with nullable arrays.

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

<!--- FIR-28187 --->Changed the behavior of [`split_part`](../../sql_reference/functions-reference/string/split-part.md) when an empty string is used as delimiter.

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

[New comparison operators](../../sql_reference/operators.md) `IS DISTINCT FROM` and `IS NOT DISTINCT FROM` have been added.

### Enhancements, changes and new integrations
{: .no_toc}

<!--- FIR-27355 ---> **Support for nullable arrays**

Support has been added to allow the ANY_MATCH lambda function to work with nullable arrays

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

A new alias [`ARRAY_TO_STRING`](../../sql_reference/functions-reference/array/array-to-string.md) has been added to function `ARRAY_JOIN`.

## DB version 3.28
**September 2023**

* [Resolved issues](#resolved-issues)


### Resolved issues
{: .no_toc}

* <!--- FIR-17240 ---> `IN` expressions with scalar arguments now return Postgres-compliant results if there are `NULL`s in the `IN` list. 

* <!--- FIR-26293 ---> information_schema.running_queries returns ID of a user that issued the running query, not the current user.

* <!--- FIR-26187 ---> Update error message to explain upper case behavior 
