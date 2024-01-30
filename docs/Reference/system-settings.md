---
layout: default
title: System settings
description: Lists Firebolt system settings that you can configure using SQL.
nav_order: 4
parent: General reference
---

# Firebolt system settings
{: .no_toc}

You can use a SET statement in a SQL script to configure aspects of Firebolt system behavior. Each statement is a query in its own right and must be terminated with a semi-colon (;). The SET statement cannot be included in other queries. This topic provides a list of available settings by function.

## Set time zone

Use this setting to specify the session time zone. Time zone names are from the [tz database](http://www.iana.org/time-zones) (see the [list of tz database time zones](http://en.wikipedia.org/wiki/List_of_tz_database_time_zones)). The default value of the `time_zone` setting is UTC. For times in the future, the latest known rule for the given time zone is applied. Firebolt does not support time zone abbreviations, as they cannot account for daylight savings time transitions, and some time zone abbreviations meant different UTC offsets at different times.


### Syntax  
{: .no_toc}

```sql
SET time_zone = '<time_zone>'
```

### Example
{: .no_toc}

```sql
SET time_zone = 'UTC';
SELECT TIMESTAMPTZ '1996-09-03 11:19:33.123456 Europe/Berlin';  --> 1996-09-03 09:19:33.123456+00
SELECT TIMESTAMPTZ '2023-1-29 6:3:42.7-3:30';  --> 2023-01-29 09:33:42.7+00

SET time_zone = 'Israel';
SELECT TIMESTAMPTZ '2023-1-29 12:21:49';  --> 2023-01-29 12:21:49+02
SELECT TIMESTAMPTZ '2023-1-29Z';  --> 2023-01-29 02:00:00+02
```

## Enable parsing for literal strings

When set to `true`, strings are parsed without escaping, treating backslashes literally. By default, this setting is enabled. 

### Syntax  
{: .no_toc}

```sql
SET standard_conforming_strings = [true|false]
```

### Example
{: .no_toc}

```sql
SET standard_conforming_strings = false;
SELECT '\x3132'; -> 132 

SET standard_conforming_strings = true;
SELECT '\x3132'; -> \x3132
```

## Limit the number of result rows

When set to a value greater than zero, this setting limits the number of rows returned by `SELECT` statements. The query is executed as if an additional `LIMIT` clause is added to the SQL query. The default value is zero.

### Syntax

{: .no_toc}

```sql
SET max_result_rows = <integer>;
```

### Example

```sql
SET max_result_rows = 10000;
SELECT * FROM table;
```

is equivalent to

```sql
SELECT * FROM table LIMIT 10000;
```
