## Firebolt Release Notes - Version 4.11

### New Features

<!-- Auto Generated Markdown for FIR-36897 - Owned by Demian Hespe -->
**Introduced the `GEOGRAPHY` data type and functions for geospatial data handling [public preview]**

Added a new [GEOGRAPHY]({% link sql_reference/geography-data-type.md %}) data type and functions for working with geospatial data. Firebolt supports the three industry standard formats [Well-Known Text (WKT)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry), [Well-Known Binary (WKB)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry#Well-known_binary), and [GeoJSON](https://datatracker.ietf.org/doc/html/rfc7946) for geospatial data.

This public preview release includes the following functions:  
* [ST_ASBINARY]({% link sql_reference/functions-reference/geospatial/st_asbinary.md %}) &ndash; Converts shapes of the `GEOGRAPHY` data type to the [Well-Known Binary (WKB)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry#Well-known_binary) format for geographic objects.
* [ST_ASEWKB]({% link sql_reference/functions-reference/geospatial/st_asewkb.md %}) &ndash; Converts shapes of the `GEOGRAPHY` data type to the [extended Well-Known Binary (EWKB)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry#Format_variations) format using Spatial Reference Identifier (SRID) 4326, which corresponds to the [WGS84](https://en.wikipedia.org/wiki/World_Geodetic_System#WGS_84) coordinate system.
* [ST_ASGEOJSON]({% link sql_reference/functions-reference/geospatial/st_asgeojson.md %}) &ndash; Converts shapes of the `GEOGRAPHY` data type to the [GeoJSON](https://datatracker.ietf.org/doc/html/rfc7946) format.
* [ST_ASTEXT]({% link sql_reference/functions-reference/geospatial/st_astext.md %}) &ndash; Converts shapes of the `GEOGRAPHY` data type to the [Well-Known Text (WKT)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) format.
* [ST_CONTAINS]({% link sql_reference/functions-reference/geospatial/st_contains.md %}) &ndash; Determines if one `GEOGRAPHY` object fully contains another.
* [ST_COVERS]({% link sql_reference/functions-reference/geospatial/st_covers.md %}) &ndash; Determines if one `GEOGRAPHY` object fully encompasses another.
* [ST_DISTANCE]({% link sql_reference/functions-reference/geospatial/st_distance.md %}) &ndash; Calculates the shortest distance, measured as a geodesic arc between two `GEOGRAPHY` objects, measured in meters.
* [ST_GEOGFROMGEOJSON]({% link sql_reference/functions-reference/geospatial/st_geogfromgeojson.md %}) &ndash; Constructs a `GEOGRAPHY` object from a [GeoJSON](https://datatracker.ietf.org/doc/html/rfc7946) string.
* [ST_GEOGFROMTEXT]({% link sql_reference/functions-reference/geospatial/st_geogfromtext.md %}) &ndash; Constructs a `GEOGRAPHY` object from a [Well-Known Text (WKT)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) string.
* [ST_GEOGFROMWKB]({% link sql_reference/functions-reference/geospatial/st_geogfromwkb.md %}) &ndash; Constructs a `GEOGRAPHY` object from a [Well-Known Binary](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry#Well-known_binary) (WKB) byte string.
* [ST_GEOGPOINT]({% link sql_reference/functions-reference/geospatial/st_geogpoint.md %}) &ndash; Constructs a Point in the `GEOGRAPHY` data type created from specified longitude and latitude coordinates.
* [ST_INTERSECTS]({% link sql_reference/functions-reference/geospatial/st_intersects.md %}) &ndash; Determines whether two input `GEOGRAPHY` objects intersect each other.
* [ST_X]({% link sql_reference/functions-reference/geospatial/st_x.md %}) &ndash; Extracts the longitude coordinate of a `GEOGRAPHY` Point.
* [ST_Y]({% link sql_reference/functions-reference/geospatial/st_y.md %}) &ndash; Extracts the latitude coordinate of a `GEOGRAPHY` Point.

**Added keyboard shortcuts to the Firebolt Develop Space**

The user interface in the Firebolt **Develop Space** added the following [keyboard shortcuts]({% link Guides/query-data/using-the-develop-workspace.md %}#keyboard-shortcuts-for-the-develop-space):
* Cmd + Enter &ndash; Runs the current query.
* Cmd+Shift+Enter &ndash; Runs all queries in a script.

**Added the window function `FIRST_VALUE`**

Added a new [FIRST_VALUE]({% link sql_reference/functions-reference/window/first-value.md %}) window function that returns the first value evaluated in a specified window frame.