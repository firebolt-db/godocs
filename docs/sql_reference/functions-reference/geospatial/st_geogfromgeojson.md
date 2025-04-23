---
layout: default
title: ST_GEOGFROMGEOJSON
description: Reference material for ST_GEOGFROMGEOJSON function
parent: Geospatial functions
published: true
---

# ST_GEOGFROMGEOJSON

Constructs a `GEOGRAPHY` object from a [GeoJSON](https://datatracker.ietf.org/doc/html/rfc7946) string.

The [GeoJSON standard](https://datatracker.ietf.org/doc/html/rfc7946) specifies that GeoJSON points are WGS 84 coordinates, and GeoJSON line segments are planar edges, meaning straight cartesian lines. However, contrary to that, in Firebolt, the line segments are interpreted as geodesic arcs.


The following image shows an extreme case of the difference between these.
Both lines show the LineString from the GeoJSON string `{"coordinates": [[-0.12457505963581639,51.5006710219584],[-74.04448100812115,40.68923977267272]],"type": "LineString"}` that connect the Statue of Liberty in New York City and Big Ben in London. The gray line represents the LineString as a straight Cartesian line, following the GeoJSON standard. In contrast, the red line interprets the LineString as a geodesic arc, consistent with Firebolt's approach.

<img src="../../../assets/images/geography/geojson_difference.png" alt="An example showing the interpretation of a GeoJSON string according to the GeoJSON standard and in Firebolt." width="600"/>

[Normalization]({% link sql_reference/geography-data-type.md %}#normalization) and [invalid input handling]({% link sql_reference/geography-data-type.md %}#invalid-inputs) are applied as descibed in the [GEOGRAPHY type documentation]({% link sql_reference/geography-data-type.md %}).

## Syntax
{: .no_toc}

```sql
ST_GEOGFROMGEOJSON(<GeoJSON>)
```

## Parameters 
{: .no_toc}

| Parameter | Description                                                                                                         | Supported input types |
| :--------- | :------------------------------------------------------------------------------------------------------------------- | :-------------------|
| `<GeoJSON>`   | GeoJSON text representing the `GEOGRAPHY` object. | `TEXT` |

## Return Type
`ST_GEOGFROMGEOJSON` returns a value of type `GEOGRAPHY`.

## Example
{: .no_toc}

{% include sql_examples/st_geogfromgeojson.md %}
