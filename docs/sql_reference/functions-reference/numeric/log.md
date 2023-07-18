---
layout: default
title: LOG
description: Reference material for LOG function
grand_parent: SQL functions
parent: Numeric functions
---

# LOG

Returns the common (base 10) logarithm of a numerical expression, or the logarithm to an arbitrary base if specified as the first argument.

## Syntax
{: .no_toc}

```sql
LOG([<value>,] <value>);
```
## Parameters 
{: .no_toc}
| Parameter   | Description                                                                                                         | Supported input types |
| :----------- | :------------------------------------------------------------------------------------------------------------------- |:--------------------|
| `<value>`    | Optional. The base for the logarithm. The default base is 10.                                                       |  `DOUBLE PRECISION`
| `<value>` | The exponent for the logarithm. | `DOUBLE PRECISION` |

## Return Types
`DOUBLE PRECISION`

## Example
{: .no_toc}

This example below returns the logarithm of 64.0 to base 2:

```sql
SELECT
    LOG(2, 64.0);
```

**Returns**: `6`

This example below returns the logarithm of 100.0 to the default base 10:

```sql
SELECT
    LOG(100.0);
```

**Returns**: `2`
