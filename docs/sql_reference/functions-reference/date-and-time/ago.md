---
layout: default
title: AGO
description: Reference material for AGO function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Date and time functions
---

# AGO

Subtracts the specified interval from the current timestamp, and returns it as a `TIMESTAMPTZ` value.
For more information, see [Arithmetic with intervals](../../../Reference/interval-arithmetic.md).


## Syntax
{: .no_toc}

```sql
AGO(<interval>)
```
## Parameters
{: .no_toc}

| Parameter           | Description                                                                                                                                                                                        |
| :------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<interval>`            | An `interval` literal representing substracted a duration. |

## Return Type

`TIMESTAMPTZ`

## Example
{: .no_toc}

The following example assumes that the current Unix timestamp is `2023-03-03 14:42:31.123456 UTC`.

```sql
SET time_zone = 'Europe/Berlin';
SELECT CURRENT_TIMESTAMP;  --> 2023-03-03 15:42:31.123456+01
SELECT AGO('1h');  --> 2023-03-03 14:42:31.123456+01
```
