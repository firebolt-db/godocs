---
layout: default
title: ST_Y
description: Reference material for ST_Y function
parent: Geospatial functions
published: true
---

# ST_Y

Extracts the latitude coordinate of a `GEOGRAPHY` Point. Returns `NULL` for empty geography objects. Returns an error if the input is not a single Point (and not an empty `GEOGRAPHY` object).

## Syntax
{: .no_toc}

```sql
ST_Y(<object>)
```

## Parameters 
{: .no_toc}

| Parameter | Description                                                                                                         | Supported input types |
| :--------- | :------------------------------------------------------------------------------------------------------------------- | :-------------------|
| `<object>`   | The `GEOGRAPHY` Point to extract the latitude of. | `GEOGRAPHY` |

## Return Type
`ST_Y` returns a value of type `DOUBLE PRECISION`.

## Example
{: .no_toc}

{% include sql_examples/st_y.md %}
