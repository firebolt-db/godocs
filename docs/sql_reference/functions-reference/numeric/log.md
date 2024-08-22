---
layout: default
title: LOG
description: Reference material for LOG function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Numeric functions
published: true
---

# LOG

Returns the common (base 10) logarithm of a numerical expression, or the logarithm to an arbitrary base if specified as the first argument.
The value for which `log` is computed needs to be larger than 0, otherwise an error is returned.
If a base is provided, it also needs to be larger than 0 and not equal to 1.
You can use the function [`LN`](ln.md) to compute the natural logarithm (base e).

**Alias:** `LOG10` (does not support a custom `base` argument)

## Syntax
{: .no_toc}

```sql
LOG([<base>,] <value>);
```
## Parameters 
{: .no_toc}

| Parameter   | Description                                                                                                         | Supported input types |
| :----------- | :------------------------------------------------------------------------------------------------------------------- |:--------------------|
| `<base>`    | Optional. The base for the logarithm. The default base is 10.                                                       |  `DOUBLE PRECISION`
| `<value>` | The value for which to compute the logarithm. | `DOUBLE PRECISION` |

## Return Type
`DOUBLE PRECISION`

## Example
{: .no_toc}

This example below returns the logarithm of 64.0 to base 2:

```sql
SELECT LOG(2, 64.0);
```

**Returns**: `6`

This example below returns the logarithm of 100.0 to the default base 10:

```sql
SELECT LOG(100.0), LOG10(100.0);
```

**Returns**: `2`, `2`

The logarithm can only be computed for values that are larger than 0. All of the functions below return an error:

```sql
SELECT LOG(0.0);
SELECT LOG(-1.0);
SELECT LOG('-Inf');
```

When a base is provided, it needs to be positive and not equal to zero. All of the functions below return an error:

```sql
SELECT LOG(0.0, 10.0);
SELECT LOG(-1.0, 10.0);
SELECT LOG(1.0, 10.0);
SELECT LOG('-Inf', 10.0);
```
