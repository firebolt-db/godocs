---
redirect_from:
  - /sql-reference/functions-reference/degrees.html
layout: default
title: DEGREES
description: Reference material for DEGREES function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Numeric functions
published: true
---

# DEGREES

Converts a value in radians to degrees.

## Syntax
{: .no_toc}

```sql
DEGREES(<value>)
```
## Parameters
{: .no_toc}

| Parameter | Description                                           | Supported input types | 
| :--------- | :----------------------------------------------------- | :------------|
| `<value>`   | The value to be converted to degrees from radians. | `DOUBLE PRECISION` | 

## Return Types
`DEGREES` returns a value of type `DOUBLE PRECISION`.

## Example
{: .no_toc}

{% include sql_examples/degrees_executable.md %}
