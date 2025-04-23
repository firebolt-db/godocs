---
layout: default
title: ST_GEOGFROMTEXT
description: Reference material for ST_GEOGFROMTEXT function
parent: Geospatial functions
published: true
---

# ST_GEOGFROMTEXT

Constructs a `GEOGRAPHY` object from a [Well-Known Text (WKT)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) string. The [extended WKT format](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry#Format_variations) is supported only for Spatial Reference Identifier (SRID) 4326, which corresponds to the [WGS84](https://en.wikipedia.org/wiki/World_Geodetic_System#WGS_84) coordinate system.

[Normalization]({% link sql_reference/geography-data-type.md %}#normalization) and [invalid input handling]({% link sql_reference/geography-data-type.md %}#invalid-inputs) are applied as descibed in the [GEOGRAPHY type documentation]({% link sql_reference/geography-data-type.md %}).

## Syntax
{: .no_toc}

```sql
ST_GEOGFROMTEXT(<WKT>)
```

## Parameters 
{: .no_toc}

| Parameter | Description                                                                                                         | Supported input types |
| :--------- | :------------------------------------------------------------------------------------------------------------------- | :-------------------|
| `<WKT>`   | A WKT string to convert to a `GEOGRAPHY` object. | `TEXT` |

## Return Type
`ST_GEOGFROMTEXT` returns a value of type `GEOGRAPHY`.

## Example
{: .no_toc}

{% include sql_examples/st_geogfromtext.md %}
