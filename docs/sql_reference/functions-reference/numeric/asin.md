---
layout: default
title: ASIN
description: Reference material for ASIN function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Numeric functions
published: true
---

# ASIN

Calculates the arcsine of a value in radians.

## Syntax
{: .no_toc}

```sql
ASIN(<value>)
```

## Parameters
{: .no_toc}

| Parameter | Description                                                                                                         | Supported input type |
| :--------- | :------------------------------------------------------------------------------------------------------------------- | :-----------|
| `<value>`   | The number that the arcsine function is applied to. | `DOUBLE_PRECISION` |

## Return Type
`ASIN` returns a value of type `DOUBLE_PRECISION`.

## Example
{: .no_toc}

{% include sql_examples/asin_executable.md %}
