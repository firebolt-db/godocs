The following code example creates a `GEOGRAPHY` object from the WKT representation of a Point at specified longitude and latitude coordinates and converts it to EWKB format:

``` sql
SELECT ST_ASEWKB(ST_GEOGFROMTEXT('POINT(-73.98551041593687 40.75793403395676)')) AS result
```

**Returns**

| result (BYTEA) |
| :--- |
| '\x0101000020e61000003d94479a127f52c0502f80fb03614440' |