---
layout: default
title: SIN
description: Reference material for SIN function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Numeric functions
published: true
---

# SIN

Trigonometric function that calculates the sine of a provided value.

## Syntax
{: .no_toc}

```sql
SIN(<value>)
```
## Parameters
{: .no_toc}

| Parameter | Description     | Supported input types | 
| :--------- | :---------------------- | :----|
| `<value>`   | The value that determines the returned sine in radians. | `DOUBLE PRECISION` | 

## Return Type
`DOUBLE PRECISION` 

## Example
{: .no_toc}

{% include sql_examples/sin.md %}
