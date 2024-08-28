---
layout: default
title: CURRENT_DATE
description: Reference material for CURRENT_DATE function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Date and time functions
---

# CURRENT_DATE

Returns the current local date in the time zone specified in the [session's `time_zone` setting](../../../Reference/system-settings.md#setting-the-time-zone).

## Syntax
{: .no_toc}

The function can be called with or without parentheses:

```sql
CURRENT_DATE
CURRENT_DATE()
```

## Return Type

`DATE`

## Remarks
{: .no_toc}

The function gets the current timestamp from the system, converts it to the time zone specified in the `time_zone` setting, and truncates it to a `DATE` value.

## Example
{: .no_toc}

The following example assumes that the current timestamp is `2023-03-03 23:59:00 UTC`.
It displays the current date in the time zone `Europe/Berlin`.

```sql
SET time_zone = 'Europe/Berlin';
SELECT CURRENT_DATE();
```

**Returns:**
`2023-03-04`

Notice that the time zone conversion from `UTC` to `Europe/Berlin` causes the resulting date to be `2023-03-04` instead of `2023-03-03`.
