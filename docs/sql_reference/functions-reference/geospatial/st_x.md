---
layout: default
title: ST_X
description: Reference material for ST_X function
parent: Geospatial functions
published: true
---

# ST_X

Extracts the longitude coordinate of a `GEOGRAPHY` Point. Returns `NULL` for empty geography objects. Returns an error if the input is not a single Point (and not an empty `GEOGRAPHY` object).

## Syntax
{: .no_toc}

```sql
ST_X(<object>)
```

## Parameters 
{: .no_toc}

| Parameter | Description                                                                                                         | Supported input types |
| :--------- | :------------------------------------------------------------------------------------------------------------------- | :-------------------|
| `<object>`   | The `GEOGRAPHY` Point to extract the longitude of. | `GEOGRAPHY` |

## Return Type
`ST_X` returns a value of type `DOUBLE PRECISION`.

## Example
{: .no_toc}

{% include sql_examples/st_x.md %}
