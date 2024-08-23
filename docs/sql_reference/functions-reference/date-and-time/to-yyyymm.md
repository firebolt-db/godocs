---
layout: default
title: TO_YYYYMM
description: Reference material for the TO_YYYYMM function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Date and time functions
---

# TO_YYYYMM

Extracts the year and month from a `DATE`, `TIMESTAMP`, or `TIMESTAMPTZ` value and combines them into an integer beginning with the four-digit year followed by the two-digit month.
`TO_YYYYMM(<expression>)` is equivalent to `EXTRACT(YEAR FROM <expression>) * 100 + EXTRACT(MONTH FROM <expression>);`

## Syntax
{: .no_toc}

```sql
TO_YYYYMM(<expression>)
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

The `TO_YYYYMM` function can be used in the `PARTITION BY` clause of `CREATE TABLE` commands.

```sql
CREATE TABLE test (
  t TIMESTAMP
)
PARTITION BY TO_YYYYMM(t);
```
