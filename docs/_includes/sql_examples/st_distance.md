The following code example constructs two Points from their WKT representations: One at the Statue of Liberty in New York City, and one at the Big Ben in London. It then returns the shortest distance between them, as measured as a geodesic arc, in meters:

``` sql
SELECT ST_DISTANCE(
ST_GEOGFROMTEXT('POINT(-74.04447010745835 40.68924450077543)'),
ST_GEOGFROMTEXT('POINT(-0.12418551935155021 51.50086274661804)')
) AS result
```

**Returns**

| result (DOUBLE PRECISION) |
| :--- |
| 5574863.932096738 |