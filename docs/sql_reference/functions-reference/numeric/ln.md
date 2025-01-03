---
layout: default
title: LN
description: Reference material for LN function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Numeric functions
published: true
---

# LN

Returns natural (base e) logarithm of a numerical expression.
The value for which `ln` is computed needs to be larger than 0, otherwise an error is returned.
You can use the function [LOG](log.md) if you want to provide a different base.

## Syntax
{: .no_toc}

```sql
LN(<value>);
```
## Parameters 
{: .no_toc}

| Parameter   | Description                                                                                                         | Supported input types |
| :----------- | :------------------------------------------------------------------------------------------------------------------- |:--------------------|
| `<value>` | The value for which to compute the natural logarithm. | `DOUBLE PRECISION` |

## Return Type
`DOUBLE PRECISION`

## Examples
{: .no_toc}

**Example**

The following code example  computes the natural logarithm of 1.0:

```sql
SELECT LN(1.0);
```

**Returns**

`0.0`

**Example**

The following code example returns the natural logarithm close to e:

```sql
SELECT LN(2.7182818284590452353);
```

**Returns**

`1.0`

**Example**

The natural logarithm can only be computed for values that are larger than 0. All the following functions return an error:

```sql
SELECT LN(0.0);
SELECT LN(-1.0);
SELECT LN('-Inf');
```

