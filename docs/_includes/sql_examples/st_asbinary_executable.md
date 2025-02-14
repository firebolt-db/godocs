The following query uses `ST_GEOGFROMTEXT` to create a `GEOGRAPHY` object from the WKT representation of a Point at specified longitude and latitude coordinates, and then uses `ST_ASBINARY` to convert it to WKB representation:


{% include query-window.html sql_file="sql_examples/st_asbinary_example_0.sql" %}

**Returns**

