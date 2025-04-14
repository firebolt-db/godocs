---
layout: default
title: GROUPING
description: Reference material for GROUPING
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Aggregation functions
published: true
---

# GROUPING
This function is particularly useful when working with
[GROUPING SETS](../../../sql_reference/commands/queries/select.html#group-by-grouping-sets),
[ROLLUP](../../../sql_reference/commands/queries/select.html#group-by-rollup) or
[CUBE](../../../sql_reference/commands/queries/select.html#group-by-cube) clauses.

`GROUPING SETS`, `ROLLUP`, and `CUBE` clauses produce aggregates that use `NULL` values to pad columns that are not part of the current grouping set. 
This may cause ambiguity if those columns also contain actual `NULL` values.
The `GROUPING` function helps resolve this ambiguity by distinguishing between columns that are excluded from a grouping set and those that genuinely contain `NULL` values.

Key points about the `GROUPING` function:
* It accepts expressions that are also used in the `GROUP BY [GROUPING SETS | ROLLUP | CUBE]` clause as arguments.
* It returns an integer where each bit represents whether the corresponding column is part of the grouping set or not.
* A bit is set to `1` if the corresponding column is **not** part of the grouping set; otherwise, it is `0`.
* The first argument corresponds to the most significant bit, with subsequent arguments following in order.

## Syntax
{: .no_toc}

```sql
GROUPING(<expression> [, ...n])
```

## Parameters
{: .no_toc}

| Parameter      | Description                                                                                                                                       | Supported input types  |
|:-------------- |:------------------------------------------------------------------------------------------------------------------------------------------------- |:---------------------- |
| `<expression>` | An expression that also appears as a `<grouping_element>` in a `GROUPING SETS`, `ROLLUP`, or `CUBE` clause. The maximum number of arguments is 31.| Any                    |

## Return Type
`GROUPING` returns a value of type `INT`. 

## Examples
{: .no_toc}

Consider this table `addresses`:

| user_id    | country | county         | city        |
|:---------- |:------- |:-------------- |:----------- |
| 3          | USA     | California     | Los Angeles |
| 34         | USA     | California     | Los Angeles |
| 15         | Canada  | NULL           | NULL        |
| 1          | Canada  | Quebec         | Montreal    |
| 45         | Canada  | Quebec         | Montreal    |
| 10         | USA     | California     | Springfield |
| 11         | USA     | Oregon         | Springfield |
| 23         | Canada  | Ontario        | London      |
| 30         | UK      | Greater London | London      |

Let's say we are interested in the number of users per region, going from the city level up to country level:

```sql
select 
    grouping(country, county, city), 
    country, 
    county, 
    city, 
    count(*)
from 
    locations
group by 
    grouping sets (
        (country, county, city),
        (country, county),
        (country)
    )
order by
    1, 2, 3, 4
```
The query returns this result:

| grouping | country | county         | city        | count |
| -------- | ------- | -------------- | ----------- | ----- |
| 0        | Canada  | Ontario        | London      | 1     |
| 0        | Canada  | Quebec         | Montreal    | 2     |
| 0        | Canada  | null           | null        | 1     |
| 0        | UK      | Greater London | London      | 1     |
| 0        | USA     | California     | Los Angeles | 2     |
| 0        | USA     | California     | Springfield | 1     |
| 0        | USA     | Oregon         | Springfield | 1     |
| 1        | Canada  | Ontario        | null        | 1     |
| 1        | Canada  | Quebec         | null        | 2     |
| 1        | Canada  | null           | null        | 1     |
| 1        | UK      | Greater London | null        | 1     |
| 1        | USA     | California     | null        | 3     |
| 1        | USA     | Oregon         | null        | 1     |
| 3        | Canada  | null           | null        | 4     |
| 3        | UK      | null           | null        | 1     |
| 3        | USA     | null           | null        | 4     |

The `GROUPING` function evaluates to three distinct values: 0, 1, and 3. Each value corresponds to a specific grouping set defined in the `GROUP BY GROUPING SETS` clause. 

* A value of `0` indicates that the row is grouped by all specified columns.
* A value of `1` (`0b001` in binary) signifies that the `city` column is excluded from the grouping.
* A value of `3` (`0b011` in binary) indicates that both the `county` and `city` columns are excluded from the grouping.

This allows us to differentiate between rows with the same grouping key values, such as `Canada, NULL, NULL`, by identifying which columns were used for aggregation in each case.
