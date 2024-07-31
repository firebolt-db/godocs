---
layout: default
title: DATE_TRUNC
description: Reference material for the DATE_TRUNC function
grand_parent: SQL functions
parent: Date and time functions
---

# DATE_TRUNC

Truncates a value (`<expression>`) of type `DATE`, `TIMESTAMP`, or `TIMESTAMPTZ` to the selected precision (`<time_unit>`).

## Syntax
{: .no_toc}

```sql
DATE_TRUNC(<time_unit>, <expression> [, <time_zone> ])
```

## Parameters
{: .no_toc}

| Parameter      | Description                                                                                                                                                                                                          |
| :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<time_unit>`  | A TEXT literal with the time unit precision to truncate to. Must be one of `microsecond`, `millisecond`, `second`, `minute`, `hour`, `day`, `week`, `month`, `quarter`, `year`, `decade`, `century` or `millennium`. |
| `<expression>` | A value expression evaluating to the DATE, TIMESTAMP, or TIMESTAMPTZ value that should be truncated.                                                                                                                 |
| `<time_zone>`  | An optional TEXT literal giving a time zone name.                                                                                                                                                                    |

## Return Type

DATE if `<expression>` has type DATE, TIMESTAMP if `<expression>` has type TIMESTAMP, TIMESTAMPTZ if `<expression>` has type TIMESTAMPTZ.

## Remarks
{: .no_toc}

Truncation of TIMESTAMPTZ values is performed after conversion to local time in a particular time zone.
For instance, truncation to 'day' produces a TIMESTAMPTZ that is midnight in that time zone.
By default, the function uses the time zone specified in the session's `time_zone` setting.
Alternatively, if the optional `<time_zone>` argument is provided, the function uses that time zone.

Firebolt raises an error if the optional `<time_zone>` argument is provided for an `<expression>` evaluating to DATE or TIMESTAMP.
Firebolt also raises an error if one attempts to truncate a value expression of type DATE to `microsecond`, `millisecond`, `second`, `minute`, or `hour`.

The `DATE_TRUNC` function can be used in the `PARTITION BY` clause of `CREATE TABLE` commands.

```sql
CREATE DIMENSION TABLE test (
  d DATE,
  t TIMESTAMP
)
PARTITION BY DATE_TRUNC('month', d), DATE_TRUNC('hour', t);
```

## Example
{: .no_toc}

```sql
SELECT DATE_TRUNC('century', DATE '1996-09-03');  --> 1901-01-01
SELECT DATE_TRUNC('hour', TIMESTAMP '1996-09-03 11:19:42.123');  --> 1996-09-03 11:00:00

SET time_zone = 'US/Pacific';
SELECT DATE_TRUNC('week', TIMESTAMPTZ '1996-09-03 11:19:42.123 Europe/Berlin');  --> 1996-09-02 00:00:00-07
SELECT DATE_TRUNC('week', TIMESTAMPTZ '1996-09-03 11:19:42.123 Europe/Berlin', 'Europe/Berlin');  --> 1996-09-01 15:00:00-07
```
