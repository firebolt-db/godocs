---
layout: default
title: DATE_DIFF
nav_exclude: true
description: Reference material for DATE_DIFF function
parent: Date and time functions
---

# DATE_DIFF

Calculates the difference between `start_timestamp` and `end_timestamp` by the indicated unit.

## Syntax
{: .no_toc}

```sql
DATE_DIFF('<unit>', <start_timestamp>, <end_timestamp>)
```
## Parameters
{: .no_toc}

| Parameter           | Description                                                                                                                                                                                        |
| :------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<unit>`            | A TEXT literal specifying the time unit. Must be one of `microsecond`, `millisecond`, `second`, `minute`, `hour`, `day`, `week`, `month`, `quarter`, `year`, `decade`, `century`, or `millennium`. |
| `<start_timestamp>` | A value expression evaluating to a `TIMESTAMP` or `TIMESTAMPTZ` value.                                                                                                                             |
| `<end_timestamp>`   | A value expression evaluating to a `TIMESTAMP` or `TIMESTAMPTZ` value.                                                                                                                             |

## Return Type

`BIGINT`

## Example
{: .no_toc}

```sql
SELECT DATE_DIFF('day', '2024-01-01'::TIMESTAMP, '2024-04-15'::TIMESTAMP);
```

**Returns**: 105
