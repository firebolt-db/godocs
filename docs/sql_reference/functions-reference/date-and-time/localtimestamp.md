---
layout: default
title: LOCALTIMESTAMP
description: Reference material for LOCALTIMESTAMP function
parent: SQL functions
great_grand_parent: SQL reference
---

# LOCALTIMESTAMP

Returns the current local timestamp in the time zone specified in the session's [`time_zone` setting](../../general-reference/system-settings.md#set-time-zone).

## Syntax
{: .no_toc}

The function can be called with or without parentheses:

```sql
LOCALTIMESTAMP
LOCALTIMESTAMP()
```

## Return Type
`TIMESTAMP`

## Remarks
{: .no_toc}

The function takes the current Unix timestamp (in the UTC time zone), converts it to the time zone specified in the `time_zone` setting, and returns it as a `TIMESTAMP` value.
Two simultaneous calls of the function can return different timestamps, due to time zone conversion.

## Example
{: .no_toc}

The following example assumes that the current timestamp is `2023-03-03 14:42:31.123456 UTC`.
Observe how we return different `TIMESTAMP` values with different time zone settings:

```sql
SET time_zone = 'Europe/Berlin';
SELECT LOCALTIMESTAMP;  --> 2023-03-03 15:42:31.123456

SET time_zone = 'America/New_York';
SELECT LOCALTIMESTAMP;  --> 2023-03-03 09:42:31.123456
```
