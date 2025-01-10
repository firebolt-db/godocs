---
layout: default
title: ST_DISTANCE
description: Reference material for ST_DISTANCE function
parent: Geospatial functions
published: true
---

# ST_DISTANCE

The `ST_DISTANCE` function calculates the shortest distance, measured as a geodesic arc between two `GEOGRAPHY` objects, measured in meters. It models the earth as a perfect sphere with a fixed radius of 6,371,008 meters.


If either input is empty, `ST_DISTANCE` will return `NULL`.

## Syntax
{: .no_toc}

```sql
ST_DISTANCE(<geo1>, <geo2>)
```

## Parameters 
{: .no_toc}

| Parameter | Description                                                                                                         | Supported input types |
| :--------- | :------------------------------------------------------------------------------------------------------------------- | :-------------------|
| `<geo1>`   | The first `GEOGRAPHY` object to calculate the distance between. | `GEOGRAPHY` |
| `<geo2>`   | The second `GEOGRAPHY` object to calculate the distance between. | `GEOGRAPHY` |

## Return Type
`ST_DISTANCE` returns a value of type `DOUBLE PRECISION`.

## Example
{: .no_toc}

{% include sql_examples/st_distance.md %}
