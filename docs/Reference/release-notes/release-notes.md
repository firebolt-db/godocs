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

## DB version 3.34
**May 2024**

* [Enhancements, changes, and new integrations](#enhancements-changes-and-new-integrations)
* [Resolved issues](#resolved-issues)

### Enhancements, changes and new integrations

<!--- FIR-32710 --->**Removed `MATCH` function**

The `match` function has been removed and replaced with the `regexp_like`. 

<!--- FIR-32693 --->**Producing an error for array function failure instead of NULL**

Array function queries that accept two or more array arguments now produce an error. If you call an array function such as `array_transform(..)` or `array_sort(..)` with multiple array arguments, the arrays must have the same size. 
For example: 

```sql
array_transform(x, y -> x + y, arr1, arr2)
```

This raises an error if `array_length(arr1) != array_length(arr2)`. We now also perform this check for NULL literals. If you previously used `array_transform(x, y -> x + y, NULL::INT[], Array[5, 6])`, you got back `NULL`. Now, the query using that expression will raise an error.

<!--- FIR-32652 --->**Added ARRAY_FIRST function**

The `array_first` function has been added. It returns the first element in the given array for which the given function returns `true`.

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

<!--- FIR-32163 --->**Coalesce compliance**

`COALESCE` now supports short-circuiting in Firebolt. Queries such as `COALESCE(a, 1 / 0) FROM t` could fail before, even when there were no NULLs in t. Only `CASE WHEN` supported short circuiting. Firebolt is now aligned with PostgreSQL and supports short circuiting in `COALESCE` as well.

<!--- FIR-31821 --->**Create table under I_S schema**

You can now execute `CREATE TABLE`/VIEW/`AGGREGATING INDEX` only under the public schema. 

<!--- FIR-31680 --->**Improved error message for JSON `PARSE_AS_TEXT` format**

The error message for external tables created with JSON `PARSE_AS_TEXT` format has been revised. This format reads specifically into a *single* column of type either TEXT or `TEXT NOT NULL`. (Note there may be external table partition columns defined after the single TEXT column, and they are okay). Now, only the error message regarding the `CREATE EXTERNAL TABLE` statement on a user's first attempt to use `SELECT` will be seen. Support for reading format JSON `PARSE_AS_TEXT=TRUE` into a `TEXT NOT NULL` column has been added.

<!--- FIR-29793 --->**Implemented column_mismatch**

Support for `ALLOW_COLUMN_MISMATCH` in `COPY FROM` has been added. 

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

The `array_agg` function has changed to return PostgreSQL-compliant results:
  * `array_agg` now preserves `NULL` values in its input, e.g. `select array_agg(x) from unnest(array [1,NULL,2] x)` returns `{1,NULL,2}`
  * `array_agg` now returns `NULL` instead of an empty array if there are no input values

<!--- FIR-8970 --->**Lambda parameters are no longer supported by `array_sum`**

Array aggregate functions no longer support lambda parameters. To get the old behavior for conditional lambda functions, use transform instead. 
For example:

```sql
array_sum(transform(...))
```

### Resolved issues

<!--- FIR-32432 --->
* Fixed a bug where negation did not check for overflows correctly.