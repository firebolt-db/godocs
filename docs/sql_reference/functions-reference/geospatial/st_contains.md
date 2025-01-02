---
layout: default
title: ST_CONTAINS
description: Reference material for ST_CONTAINS function
parent: Geospatial functions
published: true
---

# ST_CONTAINS

The `ST_CONTAINS` function determines if one `GEOGRAPHY` object fully contains another. Specifically, it checks whether every point in the second `GEOGRAPHY` object (`geo2`) lies within or on the boundary of the first `GEOGRAPHY` object (`geo1`), and the interiors of the two input objects intersect. If `geo1` contains `geo2`, the function returns `TRUE`; otherwise, it returns `FALSE`. This function is commonly used to assess spatial relationships, such as whether a larger geographic area completely includes a smaller one.

If either `geo1` or `geo2` is empty, `ST_CONTAINS` will return `FALSE`.

Before performing the containment check, `geo1` and `geo2` are aligned through a snapping process, ensuring precise calculation. For more details on snapping, refer to the [snapping documentation](../../geography-data-type.md#snapping).

## Interior definition
A notable part of `ST_CONTAINS` is that the interiors of the inputs must intersect. The interior for the different `GEOGRAPHY` shape types is defined as follows:
- Point: The interior of a point consists only of the point itself, and is defined by its location.
- LineString: All vertices and line segments of a LineString are part of the interior, except for the first and the last vertex.
    - If the first and the last vertex are the same point after snapping, then this point is also part of the interior.

    - If the interior passes through the first and last vertex, or just one of them, then it is part of the interior.

- Polygon: Every point within the boundaries, excluding points on the boundaries themselves, is part of the interior.

- MultiPoint, MultiLineString, MultiPolygon, GeometryCollection: Any point that lies within the interior of one of the shapes in the collection is part of the collection's interior.


## Comparison with [ST_COVERS](st_covers.md)
`ST_CONTAINS` is similar to `ST_COVERS`, but there is a key distinction: `ST_CONTAINS` returns `FALSE` if all points in `geo2` lie exactly on the boundary of `geo1`, while `ST_COVERS` will return `TRUE` in this case. This behavior arises from an additional requirement in `ST_CONTAINS` that the interiors of the geometries must intersect. If this distinction is not important, use `ST_COVERS`, which is more efficient to compute in Firebolt.



## Syntax
{: .no_toc}

```sql
ST_CONTAINS(<geo1>, <geo2>)
```

## Parameters 
{: .no_toc}

| Parameter | Description                                                                                                         | Supported input types |
| :--------- | :------------------------------------------------------------------------------------------------------------------- | :-------------------|
| `<geo1>`   | The object being checked to see if it fully contains the second object. | `GEOGRAPHY` |
| `<geo2>`   | The object being checked to see if it is fully contained by the first object. | `GEOGRAPHY` |


## Return Type
`ST_CONTAINS` returns a value of type `BOOLEAN`.

## Example
{: .no_toc}

{% include sql_examples/st_contains.md %}

## Example
{: .no_toc}

{% include sql_examples/st_covers_contains_comparison.md %}
