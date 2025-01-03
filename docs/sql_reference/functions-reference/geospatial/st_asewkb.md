---
layout: default
title: ST_ASEWKB
description: Reference material for ST_ASEWKB function
parent: Geospatial functions
published: true
---

# ST_ASEWKB

Converts shapes of the `GEOGRAPHY` data type to the [extended Well-Known Binary (EWKB)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry#Format_variations) format using Spatial Reference Identifier (SRID) 4326, which corresponds to the [WGS84](https://en.wikipedia.org/wiki/World_Geodetic_System#WGS_84) coordinate system.

## Syntax
{: .no_toc}

```sql
ST_ASEWKB(<object>)
```

## Parameters 
{: .no_toc}

| Parameter | Description                                                                                                         | Supported input types |
| :--------- | :------------------------------------------------------------------------------------------------------------------- | :-------------------|
| `<object>`   | The `GEOGRAPHY` object to convert to EWKB format. | `GEOGRAPHY` |

## Return Type
`ST_ASEWKB` returns a value of type `BYTEA`.

## Example
{: .no_toc}

{% include sql_examples/st_asewkb.md %}
