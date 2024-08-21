---
layout: default
title: LOCALTIMESTAMP
description: Reference material for LOCALTIMESTAMP function
parent: Date and time functions
---

# LOCALTIMESTAMP

Returns the current local timestamp in the time zone specified in the session's [`time_zone` setting](../../../Reference/system-settings.md#set-time-zone).

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

The function gets the current timestamp from the system, converts it to the time zone specified in the `time_zone` setting, and returns it as a `TIMESTAMP` value.

## Example
{: .no_toc}

The following example assumes that the current timestamp is `2023-03-03 14:42:31.123456 UTC`.
Observe how it returns different `TIMESTAMP` values for different time zone settings:

```sql
SET time_zone = 'Europe/Berlin';
SELECT LOCALTIMESTAMP;  --> 2023-03-03 15:42:31.123456

SET time_zone = 'America/New_York';
SELECT LOCALTIMESTAMP;  --> 2023-03-03 09:42:31.123456
```
