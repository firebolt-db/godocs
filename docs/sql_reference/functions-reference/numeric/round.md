---
layout: default
title: ROUND
description: Reference material for ROUND function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Numeric functions
---

# ROUND

Rounds a value to a specified number of decimal places.

## Syntax
{: .no_toc}

```sql
ROUND(<value> [, <decimal>])
```
## Parameters
{: .no_toc}

| Parameter | Description                                                                                                                   | Supported input types | 
| :--------- | :----------------------------------------------------------------------------------------------------------------------------- |:------| 
| `<value>`   | The value to be rounded       |
| `<decimal>`   | Optional. An `INTEGER` constant that defines the decimal range of the returned value. By default, `ROUND` returns whole numbers. | `INTEGER` | 

## Return Types
`DOUBLE PRECISION`

## Example
{: .no_toc}

{% include sql_examples/round_executable.md %}
