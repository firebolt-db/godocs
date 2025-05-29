The following code example constructs a dataset containing three `GEOGRAPHY` objects: a valid Point, an empty Point, and a LineString. The code example computes their S2 cell IDs at cell levels 30 and 10, returning results only for the valid Point:

``` sql
WITH data AS (
  SELECT 1 AS id, ST_GEOGFROMTEXT('POINT(-122 47)') AS geo
  UNION ALL
  SELECT 2 AS id, ST_GEOGFROMTEXT('POINT EMPTY') AS geo
  UNION ALL
  SELECT 3 AS id, ST_GEOGFROMTEXT('LINESTRING(1 2, 3 4)') AS geo
)
SELECT id,
       ST_S2CELLIDFROMPOINT(geo) cell30,
       ST_S2CELLIDFROMPOINT(geo, 10) cell10
FROM data;
```

**Returns**

| id (INTEGER) | cell30 (BIGINT) | cell10 (BIGINT) |
| :--- | :--- | :--- |
| 1 | 6093613931972369317 | 6093613287902019584 |
| 2 | NULL | NULL |
| 3 | NULL | NULL |

The previous code example returns the S2 cell ID for the first input at the default, finest resolution of 30. The function returns `NULL` for the second input because it is empty and contains no geographic data, and for the third input because LineString is not a supported `GEOGRAPHY` type.