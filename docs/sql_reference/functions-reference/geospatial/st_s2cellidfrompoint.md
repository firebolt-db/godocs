---
layout: default
title: ST_S2CELLIDFROMPOINT
description: Reference material for ST_S2CELLIDFROMPOINT function
parent: Geospatial functions
published: true
---

# ST_S2CELLIDFROMPOINT

Returns the [S2 cell ID](http://s2geometry.io/devguide/s2cell_hierarchy), which uniquely identifies the region on Earth that fully contains, or covers, a single Point `GEOGRAPHY` object.

`ST_S2CELLIDFROMPOINT` exclusively supports single Point `GEOGRAPHY` objects, and returns `NULL` for all other values including
MultiPoint, LineString, Polygon, and an empty `GEOGRAPHY` object.


## Syntax
{: .no_toc}

```sql
ST_S2CELLIDFROMPOINT(<geo> [, <cell_level> ])
```

## Parameters 
{: .no_toc}

| Parameter | Description                                                                                                         | Supported input types |
| :--------- | :------------------------------------------------------------------------------------------------------------------- | :-------------------|
| `<geo>`   | A single valid `GEOGRAPHY` Point for which `ST_S2CELLIDFROMPOINT` calculates and returns the S2 cell that covers it. | `GEOGRAPHY` |
| `<cell_level>`   | The resolution of the S2 cell to return. Valid levels range from 0, the coarsest level, to 30, the finest level. The default level is 30 if unspecified.  | `BIGINT` |

## Return Type
`ST_S2CELLIDFROMPOINT` returns a value of type `BIGINT`, which may include negative values.

## Example
{: .no_toc}

{% include sql_examples/st_s2cellidfrompoint.md %}