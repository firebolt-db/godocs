## Firebolt Release Notes - Version 4.14

### New Features


<!-- Auto Generated Markdown for FIR-42537 - Owned by Pascal Schulze -->
**Updated `E2E_DURATION_US` to include total query time in Firebolt infrastructure for enhanced performance monitoring and optimization.**
Added a new column `E2E_DURATION_US` in the system tables `INFORMATION_SCHEMA.ENGINE_RUNNING_QUERIES`, `INFORMATION_SCHEMA.ENGINE_QUERY_HISTORY` and `INFORMATION_SCHEMA.ENGINE_USER_QUERY_HISTORY` which shows the total time a query has spent within the Firebolt infrastructure. In contrast, `DURATION_US`, measures only the time spent using the engine without considering retries. `E2E_DURATION_US` also counts time spent in gateway services and on retries. For example, if a query starts a stopped engine, the engine's startup time is included in the query's end-to-end duration. This update provides a more accurate representation of query runtime, for performance monitoring and optimization.


**Added support for cross-region data ingestion and export.**
You can now ingest and export data to Amazon S3 buckets located in different AWS Regions from your Firebolt engines. Previously, the engine had to be in the same region as the Amazon S3 bucket. **Cross-region transfers will incur additional AWS network fees and longer processing times**.


### Behavior Changes

<!-- Auto Generated Markdown for FIR-34196 - Owned by Pascal Schulze -->
**Removed support for legacy  `X-ClickHouse` HTTP ClickHouse headers**
The system no longer accepts or returns legacy HTTP ClickHouse headers of the format `X-ClickHouse`. This helps to maintain compatibility and standardization across API interactions.


### Performance Improvements

<!-- Auto Generated Markdown for FIR-42903 - Owned by Demian Hespe -->
**Enhanced data ingestion performance for `GEOGRAPHY` objects of type `POINT`

**
Improved data loading performance for `GEOGRAPHY` objects of type `POINT`, enabling faster loading of geographical point data for quicker data integration and analysis.


<!-- Auto Generated Markdown for FIR-42803 - Owned by Asya Shneerson -->
**Optimized performance of `SELECT` queries on External Tables with URLs to multi-file directories

**
Improved the performance of `SELECT` queries on External Tables when URLs point to folders containing many files across different directories. This update speeds up data access and processing.


<!-- Auto Generated Markdown for FIR-42519 - Owned by Demian Hespe -->
**Added result cache support for cross and complex joins for improved performance**
The result cache now supports queries using cross joins or complex joins with `OR` conditions and inequalities. This change reduces redundant calculations, improving query performance.


### Bug Fixes

<!-- Auto Generated Markdown for FIR-42330 - Owned by Gil Cizer -->
**Required `USAGE` permissions for accessing `INFORMATION_SCHEMA`**
Accessing `INFORMATION_SCHEMA` now requires `USAGE` permissions on the database. Queries to the `INFORMATION_SCHEMA` will fail if the database lacks these permissions, ensuring consistent behavior with other permission-restricted queries. Users should ensure their databases have the correct permissions to avoid access issues.


<!-- Auto Generated Markdown for FIR-42767 - Owned by Demian Hespe -->
**Updated the `EXPLAIN` command to display accurate default values for `DATE`, `TIMESTAMP`, and `TIMESTAMPTZ` columns.  
**
The `EXPLAIN` command now displays default values for columns of type `DATE`, `TIMESTAMP`, and `TIMESTAMPTZ` columns. This update fixes a bug that previously caused default values to be shown incompletely, improving clarity and accuracy in query plan analysis.



<!-- Auto Generated Markdown for FIR-42032 - Owned by Amit Schreiber -->
**Resolved filtering issue for views in `information_schema.tables` ensuring visibility based on user permissions

**
Fixed an issue in `information_schema.tables` where filtering for views did not function correctly. It now filters views based on permissions. This ensures users only see views they are authorized to access, improving data security.
