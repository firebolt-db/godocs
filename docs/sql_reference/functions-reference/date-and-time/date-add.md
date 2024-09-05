---
layout: default
title: DATE_ADD
description: Reference material for DATE_ADD function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Date and time functions
---

# DATE\_ADD

Computes a new TIMESTAMP or TIMESTAMPTZ value by adding or subtracting a specified number of time units from a DATE, TIMESTAMP, or TIMESTAMPTZ value.
It's similar to [arithmetic with intervals](../../../Reference/interval-arithmetic.md), but it also allows using a column reference for the `<quantity>`.

## Syntax
{: .no_toc}

```sql
DATE_ADD('<unit>', <quantity>, <expression>)
```
## Parameters 
{: .no_toc}

| Parameter      | Description                                                                                                                                                                             |
| :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<unit>`       | A TEXT literal specifying the time unit. Must be one of `microsecond`,`millisecond`,`second`,`minute`,`hour`,`day`,`week`,`month`,`quarter`,`year`,`decade`,`century`, or `millennium`. |
| `<quantity>`   | An INT or BIGINT specifying how often the time unit should be added or subtracted to <expression>.                                                                                      |
| `<expression>` | An expression evaluating to type DATE, TIMESTAMP, or TIMESTAMPTZ.                                                                                                                       |

## Return Types

TIMESTAMP if `<expression>` has type DATE or TIMESTAMP.
TIMESTAMPTZ if `<expression>` has type TIMESTAMPTZ.

## Example
{: .no_toc}

```sql
SELECT date_add('week', 4, '2024-04-15 12:13:14'::timestamp);
```

**Returns**:
`'2024-05-13 12:13:14'::timestamp`.
