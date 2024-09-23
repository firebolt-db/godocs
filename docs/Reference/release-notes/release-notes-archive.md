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

{% include release_notes/release_notes_4_5.md %}

{% include release_notes/release_notes_4_4_0.md %}

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


## DB version 4.2
**July 2024**

### New features

<!--- FIR-32118---> **New `ntile` window function**

Firebolt now supports the `ntile` window function. Refer to our [NTILE](../sql_reference/../../sql_reference/functions-reference/window/ntile.md) documentation for examples and usage. 

### Breaking Changes 

<!--- FIR-33028 --->**Improved rounding precision for floating point to integer casting**
{: style="color:red;"}

Casting from floating point to integers now uses Banker's Rounding, matching PostgreSQL's behavior. This means that numbers that are equidistant from the two nearest integers are rounded to the nearest even integer:  

Examples:
```sql
SELECT 0.5::real::int
``` 
This returns 0. 

```sql
SELECT 1.5::real::int
``` 
This returns 2. 

 Rounding behavior has not changed for numbers that are strictly closer to one integer than to all others.
 
<!--- FIR-33869---> **JSON functions update**
{: style="color:red;"}

Removed support for `json_extract_raw`, `json_extract_array_raw`, `json_extract_values`, and `json_extract_keys`. Updated `json_extract` function: the third argument is now `path_syntax`, which is a JSON pointer expression. See [JSON_EXTRACT](../sql_reference/../../sql_reference/functions-reference/JSON/json-extract.md) for examples and usage. 

<!--- FIR-32486---> **Cluster ordinal update**
{: style="color:red;"}

Replaced `engine_cluster` with [`cluster_ordinal`](../sql_reference/../../sql_reference/information-schema/engine-metrics-history.md) in `information_schema.engine_metrics_history`. The new column is an integer representing the cluster number.

<!--- FIR-34090 ---> **Configurable cancellation behavior on connection drop**
{: style="color:red;"}

Introduced the `cancel_query_on_connection_drop` setting, allowing clients to control query cancellation on HTTP connection drop. Options include `NONE`, `ALL`, and `TYPE_DEPENDENT`. Refer to [system settings](../system-settings.md#query-cancellation-mode-on-connection-drop) for examples and usage. 

<!--- FIR-33925 ---> **JSON format as default for error output**
{: style="color:red;"}

The HTTP API now returns query execution errors in JSON format by default. This change allows for the inclusion of meta information such as error codes and the location of failing expressions in SQL scripts.

<!--- FIR-33925 ---> **STOP ENGINE will drain currently running queries first**
{: style="color:red;"}

`STOP ENGINE` command now supports graceful drain, meaning any currently running queries will be run to completion. Once all the queries are completed, the engine will be fully stopped and terminated. If you want to stop the engine immediately, you can issue a STOP ENGINE command use the TERMINATE option. For example, to immediately stop an engine, my_engine, you can use:

```sql
 STOP ENGINE myEngine WITH TERMINATE = TRUE
```

<!--- FIR-33925 ---> **Scaling engines will not terminate currently running queries**
{: style="color:red;"}

`ALTER ENGINE` command now supports graceful drain, meaning when you scale an engine (vertically or horizontally), any currently running queries will not be terminated. New queries after the scaling operation will be directed to a new cluster, while queries running on the old cluster will be run to completion.

<!--- FIR-33857---> **Updated RBAC ownership management**
{: style="color:red;"}

We have introduced several updates to role and privilege management: 
  * The `security_admin` role will be removed temporarily and re-introduced in a later release.
  * `Information_object_privileges` includes more privileges. Switching to to a specific user database (e.g by executing `use database db`) will only show privileges relevant for that database. Account-level privileges no longer show up when attached to a specific database. 
  * Every newly created user is granted with a `public` role. This grant can be revoked.

### Enhancements, changes and new integrations

<!--- FIR-33699---> **Improved query performance**

Queries with "`SELECT [project_list] FROM [table] LIMIT [limit]`" on large tables are now significantly faster.

<!--- FIR-33857---> **Updated table level RBAC**

Table level RBAC is now supported by Firebolt. This means that RBAC checks also cover schemas, tables, views and aggregating indexes. Refer to our [RBAC](./../../Guides/security/rbac.md) docs for a detailed overview of this new feature. The new Firebolt version inhibits the following change:
   * System built-in roles are promoted to contain table level RBAC information. This means that new privileges are added to `account_admin`, `system_admin` and `public` roles. The effect is transparent— any user assigned with those roles will not be affected.

<!--- FIR-33857---> **Removal of Deprecated Columns from `INFORMATION_SCHEMA.ENGINES`**

We removed the following columns from `INFORMATION_SCHEMA.ENGINES` that were only for FB 1.0 compatibility: `region`, `spec`, `scale`, `warmup`, and `attached_to`. These columns were always empty. (These columns are hidden and do not appear in `SELECT *` queries, but they will still work if referenced explicitly.)


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

Casts now behave the same across the product and adhere to the list of supported casts. Some usages of casts (explicit, implicit, or assignment cast) that were previously allowed are no longer supported and now result in errors. For more details on list of supported casts, see the documentation [here](https://docs.firebolt.io/sql_reference/data-types.html#type-conversion).

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
