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