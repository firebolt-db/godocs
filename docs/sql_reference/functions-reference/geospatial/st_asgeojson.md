---
layout: default
title: ST_ASGEOJSON
description: Reference material for ST_ASGEOJSON function
parent: Geospatial functions
published: true
---

# ST_ASGEOJSON

Converts shapes of the `GEOGRAPHY` data type to the [GeoJSON](https://datatracker.ietf.org/doc/html/rfc7946) format. 

The [GeoJSON standard](https://datatracker.ietf.org/doc/html/rfc7946) specifies that GeoJSON points are WGS 84 coordinates, and GeoJSON line segments are planar edges, meaning straight cartesian lines. However, contrary to that, in Firebolt, the line segments are interpreted as geodesic arcs.


The following image shows an extreme case of the difference between these.
Both lines show the LineString from the GeoJSON string `{"coordinates": [[-0.12457505963581639,51.5006710219584],[-74.04448100812115,40.68923977267272]],"type": "LineString"}` that connect the Statue of Liberty in New York City and Big Ben in London. The gray line represents the LineString as a straight Cartesian line, following the GeoJSON standard. In contrast, the red line interprets the LineString as a geodesic arc, consistent with Firebolt's approach.

<img src="../../../assets/images/geography/geojson_difference.png" alt="An example showing the interpretation of a GeoJSON string according to the GeoJSON standard and in Firebolt." width="600"/>

## Syntax
{: .no_toc}

```sql
ST_ASGEOJSON(<object>)
```

## Parameters 
{: .no_toc}

| Parameter | Description                                                                                                         | Supported input types |
| :--------- | :------------------------------------------------------------------------------------------------------------------- | :-------------------|
| `<object>`   | The `GEOGRAPHY` object to convert to GeoJSON format. | `GEOGRAPHY` |

## Return Type
`ST_ASGEOJSON` returns a value of type `TEXT`.

## Example
{: .no_toc}

{% include sql_examples/st_asgeojson.md %}
