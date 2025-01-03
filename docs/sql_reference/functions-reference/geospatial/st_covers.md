---
layout: default
title: ST_COVERS
description: Reference material for ST_COVERS function
parent: Geospatial functions
published: true
---

# ST_COVERS

The `ST_COVERS` function determines if one `GEOGRAPHY` object fully encompasses another. Specifically, it checks whether every point in the second `GEOGRAPHY` object (`geo2`) lies within or on the boundary of the first `GEOGRAPHY` object (`geo1`). If `geo1` covers `geo2`, the function returns `TRUE`; otherwise, it returns `FALSE`. This function is commonly used to assess spatial relationships, such as whether a larger geographic area completely includes a smaller one.

If either `geo1` or `geo2` is empty, `ST_COVERS` will return `FALSE`.

Before performing the coverage check, `geo1` and `geo2` are aligned through a snapping process, ensuring precise calculation. For more details on snapping, refer to the [snapping documentation](../../geography-data-type.md#snapping).

## Comparison with [ST_CONTAINS](st_contains.md)
`ST_COVERS` is similar to `ST_CONTAINS`, but there is a key distinction: `ST_CONTAINS` returns `FALSE` if all points in `geo2` lie exactly on the boundary of `geo1`, while `ST_COVERS` will return `TRUE` in this case. If this distinction is not important, use `ST_COVERS`, which is more efficient to compute in Firebolt.



## Syntax
{: .no_toc}

```sql
ST_COVERS(<geo1>, <geo2>)
```

## Parameters 
{: .no_toc}

| Parameter | Description                                                                                                         | Supported input types |
| :--------- | :------------------------------------------------------------------------------------------------------------------- | :-------------------|
| `<geo1>`   | The object being checked to see if it fully covers the second object. | `GEOGRAPHY` |
| `<geo2>`   | The object being checked to see if it fully covers the first object. | `GEOGRAPHY` |

## Return Type
`ST_COVERS` returns a value of type `BOOLEAN`.

## Example
{: .no_toc}

{% include sql_examples/st_covers.md %}

## Example
{: .no_toc}

{% include sql_examples/st_covers_contains_comparison.md %}
