---
layout: default
title: TO_YYYYMMDD
description: Reference material for the TO_YYYYMMDD function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Date and time functions
---

# TO_YYYYMMDD

Extracts year, month and day from a `DATE`, `TIMESTAMP`, or `TIMESTAMPTZ` value and combines them into an integer beginning with the four-digit year followed by the two-digit month followed by the two-digit day.
`TO_YYYYMMDD(<expression>)` is equivalent to `EXTRACT(YEAR FROM <expression>) * 10000 + EXTRACT(MONTH FROM <expression>) * 100 + EXTRACT(DAY FROM <expression>);`

## Syntax
{: .no_toc}

```sql
TO_YYYYMMDD(<expression>)
```

## Parameters
{: .no_toc}

| Parameter      | Description                                             | Supported input types              |
| :------------- | :------------------------------------------------------ | :--------------------------------- |
| `<expression>` | The expression from which the time units are extracted. | `DATE`, `TIMESTAMP`, `TIMESTAMPTZ` |

`TIMESTAMPTZ` values are converted to local time according to the session's `time_zone` setting before extracting the time units.

## Return Types

`INT`

## Remarks
{: .no_toc}

The `TO_YYYYMMDD` function can be used in the `PARTITION BY` clause of `CREATE TABLE` commands.

```sql
CREATE TABLE test (
  t TIMESTAMP
)
PARTITION BY TO_YYYYMMDD(t);
```
