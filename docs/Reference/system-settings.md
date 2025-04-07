---
redirect_from:
  - /sql-reference/functions-reference/timezone.html
  - /general-reference/system-settings.html
layout: default
title: System settings
description: Lists Firebolt system settings that you can configure using SQL.
nav_order: 3
parent: General reference
---

# Firebolt system settings

{: .no_toc}

You can use a `SET` statement in a SQL script to configure aspects of Firebolt's system behavior. Each statement is a query in its own right and must be terminated with a semi-colon (;). The `SET` statement cannot be included in other queries. This topic provides a list of available settings by function.

## Setting the time zone

Use this setting to specify the session time zone. Time zone names are from the [Time Zone Database](http://www.iana.org/time-zones). You can see the list of tz database time zones [here](http://en.wikipedia.org/wiki/List_of_tz_database_time_zones). For times in the future, the latest known rule for the given time zone is applied. Firebolt does not support time zone abbreviations, as they cannot account for daylight savings time transitions, and some time zone abbreviations have meant different UTC offsets at different times. The default value of the `timezone` setting is UTC. 

### Syntax
{: .no_toc}

```sql
SET timezone = '<time_zone>'
```

### Example
{: .no_toc}
The following code example demonstrates how setting the timezone parameter affects the interpretation and conversion of `TIMESTAMPTZ` values:

```sql
SET timezone = 'UTC';
SELECT TIMESTAMPTZ '1996-09-03 11:19:33.123456 Europe/Berlin';  --> 1996-09-03 09:19:33.123456+00
SELECT TIMESTAMPTZ '2023-1-29 6:3:42.7-3:30';  --> 2023-01-29 09:33:42.7+00

SET timezone = 'Israel';
SELECT TIMESTAMPTZ '2023-1-29 12:21:49';  --> 2023-01-29 12:21:49+02
SELECT TIMESTAMPTZ '2023-1-29Z';  --> 2023-01-29 02:00:00+02
```

## Enable parsing for literal strings

If set to `true`, strings are parsed without escaping, treating backslashes literally. By default, this setting is enabled. 

### Syntax
{: .no_toc}

```sql
SET standard_conforming_strings = [true|false]
```

### Example
{: .no_toc}
The following code example demonstrates how setting `standard_conforming_strings` affects the interpretation of escape sequences in string literals:

```sql
SET standard_conforming_strings = false;
SELECT '\x3132'; --> 132

SET standard_conforming_strings = true;
SELECT '\x3132'; --> \x3132
```

## Statement timeout
Specifies the number of milliseconds a SQL statement is allowed to run. Any SQL statement or query exceeding the specified time is canceled. A value of zero disables the timeout by default.

### Syntax
{: .no_toc}

```sql
SET statement_timeout = <number_of_milliseconds>;
```

### Example
{: .no_toc}
The following SQL example sets the query timeout to three seconds:

```sql
SET statement_timeout = 3000;
```

## Limit the number of result rows
When set to a value greater than zero, this setting limits the number of rows returned by `SELECT` statements. The query is executed as if an additional `LIMIT` clause is added to the SQL query. A value of zero or less means that no limit is applied. By default, no limit to the number of result rows is applied.

### Syntax
{: .no_toc}

```sql
SET max_result_rows = <integer>;
```

### Example
{: .no_toc}
The following queries all return the same result. For the first query, no explicit settings are set:

```sql
SELECT * FROM table LIMIT 10000;

SET max_result_rows = 10000;
SELECT * FROM table;

SET max_result_rows = 10000;
SELECT * FROM table LIMIT 20000;
```

## Query cancellation mode on connection drop
Specify how the query should behave when the HTTP connection to Firebolt is dropped, such as when the UI window is closed. For this, you can choose between 3 different modes:
- `NONE`: The query will not be canceled on connection drop
- `ALL` : The query will be canceled on connection drop
- `TYPE_DEPENDENT`: Only queries without side effects will be canceled, such as `SELECT`. 

The default is `TYPE_DEPENDENT`.

### Syntax
```sql
SET cancel_query_on_connection_drop = <mode>
```

### Example
The following code example demonstrates how to control query cancellation behavior when a connection drops using `none`, `all`, and `type_dependent` modes for `SET cancel_query_on_connection_drop`:

```sql
SET cancel_query_on_connection_drop = none;
INSERT INTO X [...]
SELECT * FROM X; 

SET cancel_query_on_connection_drop = all;
INSERT INTO X [...]
SELECT * FROM X;  

SET cancel_query_on_connection_drop = type_dependent;
INSERT INTO X [...] 
SELECT * FROM X;  
```

## Query labeling/tagging
Use this option to label your query with a custom text. This simplifies query cancellation and retrieving the query status from system tables.

### Syntax
```sql
SET query_label = '<text>'
```

### Example
The following code example assigns a query label to a query using `SET query_label`, allowing you to track it in `information_schema`, `engine_running_queries`, and `information_schema.engine_query_history`. It then demonstrates how to retrieve the `QUERY_ID` for the labeled query and cancel it using `CANCEL QUERY`:

```sql
SET query_label = 'Hello Firebolt';
SELECT * FROM X;  

SET query_label = '';

SELECT query_id, * FROM information_schema.engine_running_queries WHERE query_label = 'Hello Firebolt'
SELECT query_id, * FROM information_schema.engine_query_history WHERE query_label = 'Hello Firebolt'

CANCEL QUERY WHERE query_id = '<retrieved query_id>'
```

## Multi-cluster engine warmup
Use this option to distribute queries across all clusters of an engine, simplifying the process of initializing cached data to a consistent state across all clusters after a `START ENGINE` or `ALTER ENGINE` operation.

Warmup queries complete after they have run on all clusters of the engine. The queries return an empty result if they succeed on all clusters. If the query fails on any cluster, it returns an error. If multiple errors occur, only one error is returned. 

### Syntax

```sql
SET warmup = true;
```

### Example 
The following code example activates the warmup mode so that the query runs on `production_table` using all clusters of an engine, and returns an empty result upon success:

```sql
USE ENGINE multi_cluster_engine;
SET warmup = true;
SELECT checksum(*) FROM production_table;
SET warmup = false;
```

## Result cache
Set `enable_result_cache` to `FALSE` to disable the use of Firebolt's [result cache]({% link Overview/queries/understand-query-performance-subresult.md %}), which is set to `TRUE` by default. Disabling result cashing can be useful for benchmarking query performance. When `enable_result_cache` is disabled, resubmitting the same query will recompute the results rather than retrieving them from cache. 

### Syntax

```sql
SET enable_result_cache = [true|false];
```

### Example
The following code example disables the result cache so that no previously cached results are used, and no new cache entries are written:

```sql
SET enable_result_cache = false;
SELECT checksum(*) FROM production_table;
```

## Subresult cache
Firebolt implements [advanced cross-query optimization]({% link Overview/queries/understand-query-performance-subresult.md %}) that allows SQL queries to reuse intermediate query execution states from previous requests.
Subresult caching operates at a semantic level, which allows Firebolt to understand and optimize queries based on the meaning and context of the data rather than solely based on their syntax or structure. This capability allows Firebolt to optimize across different query patterns for improved efficiency.

Set `enable_subresult_cache` to `FALSE` to disable Firebolt’s subresult caching, which is set to `TRUE` by default.

Disabling subresult caching is generally **not recommended**, as it can negatively impact query performance, especially for complex workloads. For most benchmarking scenarios, disable the result cache instead, as described in the previous [Result cache](#result-cache) section. This approach affects only the final result caching while preserving the benefits of subresult optimizations.

### Syntax

```sql
SET enable_subresult_cache = [true|false];
```

### Example 
The following code example disables the subresult cache so no previously cached subresult is used and no new cache entries are written by this query:

```sql
SET enable_subresult_cache = false;
SELECT count(*) FROM fact_table INNER JOIN dim_table ON (a = b);
```

Setting `enable_subresult_cache` to `FALSE` disables the use of all [cached subresults]({% link Overview/queries/understand-query-performance-subresult.md %}). In particular, it deactivates two caching mechanisms that normally speed up query runtimes: the use of the `MaybeCache` operator, which includes the full result cache, and the hash-table cache used by the `Join` operator.
