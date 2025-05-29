The following example illustrates the difference between `ST_CONTAINS` and `ST_COVERS`. The Polygon `POLYGON((0 0, 0 1, 1 1, 1 0, 0 0))` covers, but does not contain the LineString `LINESTRING(0 0, 0 0.5)` because it only lies on the Polygon's boundary and does not intersect the interior of the Polygon. The LineString `LINESTRING(0 0, 0 0.5, 0.5 0.5)` only partially lies on the Polygon's boundary but also intersects its interior, so it is covered and contained.
``` sql
SELECT 
    polygon, 
    linestring, 
    ST_CONTAINS(
        ST_GEOGFROMTEXT(polygon),
        ST_GEOGFROMTEXT(linestring)
    ) AS contains,
    ST_COVERS(
        ST_GEOGFROMTEXT(polygon),
        ST_GEOGFROMTEXT(linestring)
    ) AS covers
    FROM UNNEST (
        ['POLYGON((0 0, 0 1, 1 1, 1 0, 0 0))','POLYGON((0 0, 0 1, 1 1, 1 0, 0 0))'], 
        ['LINESTRING(0 0, 0 0.5)','LINESTRING(0 0, 0 0.5, 0.5 0.5)']
    ) AS shapes(polygon, linestring)
```

**Returns**

| polygon (TEXT) | linestring (TEXT) | contains (BOOLEAN) | covers (BOOLEAN) |
| :--- | :--- | :--- | :--- |
| 'POLYGON((0 0, 0 1, 1 1, 1 0, 0 0))' | 'LINESTRING(0 0, 0 0.5)' | f | t |
| 'POLYGON((0 0, 0 1, 1 1, 1 0, 0 0))' | 'LINESTRING(0 0, 0 0.5, 0.5 0.5)' | t | t |