The following code example constructs a Point in the `GEOGRAPHY` data type from longitude and latitude coordinates and extracts its latitude coordinate:

``` sql
SELECT ST_Y(ST_GEOGPOINT(-73.98551041593687, 40.75793403395676)) AS result
```

**Returns**

| result (DOUBLE PRECISION) |
| :--- |
| 40.75793403395676 |