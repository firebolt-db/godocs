The following example illustrates the difference between `ST_CONTAINS` and `ST_COVERS`. The Polygon `POLYGON((0 0, 0 1, 1 1, 1 0, 0 0))` covers, but does not contain the LineString `LINESTRING(0 0, 0 0.5)` because it only lies on the Polygon's boundary and does not intersect the interior of the Polygon. The LineString `LINESTRING(0 0, 0 0.5, 0.5 0.5)` only partially lies on the Polygon's boundary but also intersects its interior, so it is covered and contained.

{% include query-window.html sql_file="sql_examples/st_covers_contains_comparison_example_0.sql" %}

**Returns**

