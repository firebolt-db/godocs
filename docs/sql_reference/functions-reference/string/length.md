---
layout: default
title: LENGTH
description: Reference material for LENGTH function
grand_parent: SQL functions
parent: String functions
great_grand_parent: SQL reference
---

# LENGTH

Calculates the length of the input string.

When used with an array argument, `LENGTH` is a synonym for [ARRAY_LENGTH](../array/array-length.md)

## Syntax
{: .no_toc}

```sql
LENGTH(<expression>)
```
## Parameters
{: .no_toc}

| Parameter      | Description                                  |Supported input types |
| :--------------| :--------------------------------------------|:----------------------|
| `<expression>` | The string or binary data for which to return the length.   | `TEXT`, `BYTEA`. For `ARRAY`, see [ARRAY_LENGTH](../array/array-length.md) |

## Return Type
`INTEGER`

## Example
{: .no_toc}

Use the `LENGTH` to find the length of any string, such as:

```sql
SELECT LENGTH('The Accelerator Cup')
```
Spaces are included in the calculation of the total length of the string.

**Returns**: `19`
