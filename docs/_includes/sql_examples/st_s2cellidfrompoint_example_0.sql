WITH data AS (
  SELECT 1 AS id, ST_GEOGFROMTEXT('POINT(-122 47)') AS geo
  UNION ALL
  SELECT 2 AS id, ST_GEOGFROMTEXT('POINT EMPTY') AS geo
  UNION ALL
  SELECT 3 AS id, ST_GEOGFROMTEXT('LINESTRING(1 2, 3 4)') AS geo
)
SELECT id,
       st_s2cellidfrompoint(geo) cell30,
       st_s2cellidfrompoint(geo, 10) cell10
FROM data;