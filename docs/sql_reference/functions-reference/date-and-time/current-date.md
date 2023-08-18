---
layout: default
title: CURRENT_DATE
description: Reference material for CURRENT_DATE function
grand_parent: SQL functions
parent: Date and time functions
great_grand_parent: SQL reference
---

# CURRENT_DATE

Returns the current (local) date in the time zone specified in the [session's `time_zone` setting](../../general-reference/system-settings.md#set-time-zone).

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

The function takes the current Unix timestamp (in the UTC time zone), converts it to the time zone specified in the `time_zone` setting, extracts the date part, and returns it as a `DATE` value.
Two simultaneous calls of the function can return different dates, due to time zone conversion.

## Example
{: .no_toc}

The following example assumes that the current Unix timestamp is `2023-03-03 23:59:00 UTC`.
This example displays the current date in the set time zone of `Europe/Berlin`: 

```sql
SET time_zone = 'Europe/Berlin';
SELECT CURRENT_DATE;  
```

These functions return the current date in each of the timezones.  

**Returns:**
`2023-03-03`


