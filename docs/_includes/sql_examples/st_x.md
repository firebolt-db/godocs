The following code example constructs a Point in the `GEOGRAPHY` data type from longitude and latitude coordinates and extracts its longitude coordinate:

``` sql
SELECT ST_X(ST_GEOGPOINT(-73.98551041593687, 40.75793403395676)) AS result
```

**Returns**

| result (DOUBLE PRECISION) |
| :--- |
| -73.98551041593687 |