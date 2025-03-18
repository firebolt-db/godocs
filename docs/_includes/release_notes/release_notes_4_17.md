## Firebolt Release Notes - Version 4.17

### New Features

<!-- Auto Generated Markdown for FIR-44170 - Owned by Mosha Pasumansky -->
**Introduced the `IF` function to enhance query readability and simplify conditional expressions**           
The new [`IF`]({% link sql_reference/functions-reference/conditional-and-miscellaneous/if.md %}) function simplifies query writing as a more concise alternative to the `CASE WHEN` expression.                 
You can now use
`IF(<cond_expr>, <then_expr>, <else_expr>)`
as a shorter equivalent to
`CASE WHEN <cond_expr> THEN <then_expr> ELSE <else_expr> END`.

 **Added `INCREMENTAL` index optimization with `VACUUM`**             
The [`VACUUM`]({% link sql_reference/commands/data-management/vacuum.md %}) statement now supports an `INDEXES = INCREMENTAL` option, allowing incremental optimization of related indexes. This new mode uses fewer resources compared to a full reevaluation, improving index layouts. Although incremental optimization may not achieve the optimal layout of a full reevaluation, it maintains a balance between performance and resource usage. 

<!-- Auto Generated Markdown for FIR-43599 - Owned by Misha Shneerson -->
**Added `MAX_CONCURRENCY` option to `VACUUM` statement**            
The `VACUUM` command now supports the `MAX_CONCURRENCY` option, enabling you to limit concurrent processes during optimization. This allows for control of the number of concurrent processes in a `VACUUM` operation, optimizing resource usage and improving performance in multi-threaded environments.

<!-- Manually Generated Markdown for FIR-43757 - Owned by Demian Hespe -->
**Added longitude wrapping for `GEOGRAPHY` data**          
Firebolt now automatically wraps longitude values outside the range of -180 to 180 degrees when parsing `GEOGRAPHY` data from WKT, GeoJSON, WKB, or using the `ST_GeogPoint` function. For example, `POINT(180.5 1)` is now correctly interpreted as `POINT(-179.5 1)`. This improvement simplifies geographic data handling. 

<!-- Auto Generated Markdown for FIR-44120 - Owned by Mosha Pasumansky -->
**Enhanced the `EXPLAIN` function to support all SQL statements except for DDL and DCL**          
The [`EXPLAIN`]({% link sql_reference/commands/queries/explain.md %}) feature now supports analysis of all SQL statements. However, it does not provide output details for DDL (Data Definition Language) and DCL (Data Control Language) statements.

### Performance Improvements

<!-- Auto Generated Markdown for FIR-37060 - Owned by Tali Magidson -->
**Optimized `COPY FROM` filtering performance**           
Filters applied to pseudo columns, such as `$SOURCE_FILE_NAME` and `$SOURCE_FILE_TIMESTAMP`, are now pushed down to the file listing during the `COPY FROM` process when using multiple URL and pattern locations. This enhancement improves performance by reducing unnecessary data processing and speeds up data loading operations.

### Bug Fixes

<!-- Auto Generated Markdown for FIR-43757 - Owned by Demian Hespe -->
**Fixed latitude handling for `LineString` in WKT**                       
Fixed an issue where latitudes outside the valid range of -90 to 90 degrees, in `LineString` data were incorrectly accepted when parsing from WKT. For example, `LINESTRING(0.5 1, 1 90.5)` now correctly returns an error instead of being interpreted as `LINESTRING(0.5 1, -179 89.5)`. This fix enhances data integrity and prevents erroneous geographic entries.
