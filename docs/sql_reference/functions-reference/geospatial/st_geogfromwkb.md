---
layout: default
title: ST_GEOGFROMWKB
description: Reference material for ST_GEOGFROMWKB function
parent: Geospatial functions
published: true
---

# ST_GEOGFROMWKB

Constructs a `GEOGRAPHY` object from a [Well-Known Binary](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry#Well-known_binary) (WKB) byte string. The [extended WKB](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry#Format_variations) format is supported only for Spatial Reference Identifier (SRID) 4326, which corresponds to the [WGS84](https://en.wikipedia.org/wiki/World_Geodetic_System#WGS_84) coordinate system.

[Normalization]({% link sql_reference/geography-data-type.md %}#normalization) and [invalid input handling]({% link sql_reference/geography-data-type.md %}#invalid-inputs) are applied as descibed in the [GEOGRAPHY type documentation]({% link sql_reference/geography-data-type.md %}).

## Syntax
{: .no_toc}

```sql
ST_GEOGFROMWKB(<WKB>)
```

## Parameters 
{: .no_toc}

| Parameter | Description                                                                                                         | Supported input types |
| :--------- | :------------------------------------------------------------------------------------------------------------------- | :-------------------|
| `<WKB>`   | WKB representation of the `GEOGRAPHY` object. | `BYTEA` |

## Return Type
`ST_GEOGFROMWKB` returns a value of type `GEOGRAPHY`.

## Example
{: .no_toc}

{% include sql_examples/st_geogfromwkb.md %}
