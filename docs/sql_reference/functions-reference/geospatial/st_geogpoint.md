---
layout: default
title: ST_GEOGPOINT
description: Reference material for ST_GEOGPOINT function
parent: Geospatial functions
published: true
---

# ST_GEOGPOINT

Constructs a Point in the `GEOGRAPHY` data type created from specified longitude and latitude coordinates.

Coordinate validation and wrapping is applied as explained in the [GEOGRAPHY type documentation]({% link sql_reference/geography-data-type.md %}#normalization).

## Syntax
{: .no_toc}

```sql
ST_GEOGPOINT(<longitude>, <latitude>)
```

## Parameters 
{: .no_toc}

| Parameter | Description                                                                                                         | Supported input types |
| :--------- | :------------------------------------------------------------------------------------------------------------------- | :-------------------|
| `<langitude>`   | The longitude coordinate of the `GEOGRAPHY` Point to construct. | `DOUBLE PRECISION` |
| `<latitude>`   | The latitude of the `GEOGRAPHY` Point to construct. | `DOUBLE PRECISION` |

## Return Type
`ST_GEOGPOINT` returns a value of type `GEOGRAPHY`.

## Example
{: .no_toc}

{% include sql_examples/st_geogpoint.md %}
