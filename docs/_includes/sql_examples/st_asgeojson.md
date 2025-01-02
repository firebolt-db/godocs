The following query creates a `GEOGRAPHY` object from the WKT representation of a Point at specified longitude and latitude coordinates and converts it to GeoJSON format:

``` sql
SELECT ST_ASGEOJSON(ST_GEOGFROMTEXT('POINT(-73.98551041593687 40.75793403395676)')) AS result
```

**Returns**

| result (TEXT) |
| :--- |
| '{"type":"Point","coordinates":[-73.98551041593687,40.75793403395676]}' |