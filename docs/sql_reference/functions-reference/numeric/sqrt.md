---
layout: default
title: SQRT
description: Reference material for SQRT function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Numeric functions
published: true
---

# SQRT

Returns the square root of a numeric expression.

## Syntax
{: .no_toc}

```sql
SQRT(<value>);
```
## Parameters
{: .no_toc}

| Parameter | Description  | Supported input types | 
|:----------|:-----------------------------------------------|:-----| 
| `<value>`  | Value that the `SQRT` function is applied to  | `DOUBLE PRECISION` | 

## Notes
* When input value is integer data type, it is implicitly converted to `DOUBLE PRECISION`.
* When input value is `NUMERIC`, the `SQRT` function returns an error.
* When input value is negative, the `SQRT` function returns an error.


## Return Types 
`DOUBLE PRECISION`.

## Example
{: .no_toc}

The following example returns the square root of `64`: 
```sql
SELECT
    SQRT(64);
```

**Returns**: `8`
