---
layout: default
title: COS
description: Reference material for COS function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Numeric functions
published: true
---

# COS

Trigonometric function that calculates the cosine of a specific value in radians.

## Syntax
{: .no_toc}

```sql
COS(<value>)
```
## Parameters 
{: .no_toc}

| Parameter | Description                                           | Supported input types | 
| :--------- | :----------------------------------------------------- | :--------| 
| `<value>`   | The value that determines the returned cosine in radians. | `DOUBLE PRECISION` |

## Return Type 
`COS` returns a value of type `DOUBLE PRECISION`.

## Example
{: .no_toc}

{% include sql_examples/cos_executable.md %}
