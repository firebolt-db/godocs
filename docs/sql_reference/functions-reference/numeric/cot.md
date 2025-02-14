---
layout: default
title: COT
description: Reference material for COT function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Numeric functions
published: true
---

# COT

Trigonometric function that calculates the cotangent of a specific value in radians.

## Syntax
{: .no_toc}

```sql
COT(<value>)
```
## Parameters 
{: .no_toc}

| Parameter | Description                                           | Supported input types | 
| :--------- | :----------------------------------------------------- | :----------| 
| `<value>`   | The value which the `COT` function will be applied to in radians. | `DOUBLE PRECISION` | 

## Return Types 
{: .no_toc}

`COT` returns a value of type `DOUBLE PRECISION`.

## Example
{: .no_toc}

{% include sql_examples/cot_executable.md %}
