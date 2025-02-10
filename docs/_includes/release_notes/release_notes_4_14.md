## Firebolt Release Notes - Version 4.14

### New Features


<!-- Auto Generated Markdown for FIR-42537 - Owned by Pascal Schulze -->
**Added `E2E_DURATION_US` to include total query time in Firebolt infrastructure for enhanced performance monitoring and optimization**

Added a new column `E2E_DURATION_US` in the system tables `INFORMATION_SCHEMA.ENGINE_RUNNING_QUERIES`, `INFORMATION_SCHEMA.ENGINE_QUERY_HISTORY`, and `INFORMATION_SCHEMA.ENGINE_USER_QUERY_HISTORY` which shows the total time a query has spent within the Firebolt infrastructure. In contrast, `DURATION_US` measures only the time spent using the engine without considering retries or routing. The `E2E_DURATION_US` metric measures the total time a query takes from initiation to final result delivery, and includes all sub-components of latency such as routing, preparation, queuing, compilation, retries, and runtimes. For example, if a query starts a stopped engine, the engine's startup time is included in the query's end-to-end duration. This update provides a more accurate representation of total query latency, for performance monitoring and optimization.

**Unhid `scanned_storage_bytes` and `scanned_cache_bytes` from information schema views**

Unhid `scanned_storage_bytes` and `scanned_cache_bytes` columns from `information_schema.engine_query_history` and `information_schema.engine_user_query_history` views. These columns were previously accessible when explicitly used in a `SELECT` clause, but will now appear by default when you use `SELECT *`.

### Performance Improvements

<!-- Auto Generated Markdown for FIR-42903 - Owned by Demian Hespe -->
**Enhanced data ingestion performance for `GEOGRAPHY` objects of type `POINT`**

Improved data loading performance for `GEOGRAPHY` objects of type `POINT`, enabling up to four times faster loading of geographical point data for more efficient data integration and analysis.


<!-- Auto Generated Markdown for FIR-42803 - Owned by Asya Shneerson -->
**Improved file listing times for large external scans**

In operations that read data from Amazon S3 buckets such as external table scans or `COPY FROM` queries, Firebolt lists files in a URL to an Amazon S3 bucket. This process is constrained by the AWS API, which limits file listing to 1,000 files per request. Firebolt has increased the number of concurrent operations so that listing a large number of files is up to 3.5 times faster.

<!-- Auto Generated Markdown for FIR-42519 - Owned by Demian Hespe -->
**Added result cache support for cross and complex joins for improved performance**

The [query result cache]({% link Reference/system-settings.md %}#result-cache) now supports queries using cross joins or complex joins with `OR` conditions and inequalities. This change reduces redundant calculations, improving query performance.


### Bug Fixes

<!-- Auto Generated Markdown for FIR-42330 - Owned by Gil Cizer -->
**`USAGE` permissions are now required to access `INFORMATION_SCHEMA` views**

Accessing `INFORMATION_SCHEMA` views now requires `USAGE` permissions on the database. Queries to `INFORMATION_SCHEMA` will fail if these permissions are missing, ensuring consistent enforcement across permission-restricted queries. Ensure that your database has the necessary permissions to prevent access issues.


<!-- Auto Generated Markdown for FIR-42767 - Owned by Demian Hespe -->
**Improved `EXPLAIN` command accuracy for default values of `DATE`, `TIMESTAMP`, and `TIMESTAMPTZ` columns**

The `EXPLAIN` command now displays default values for columns of type `DATE`, `TIMESTAMP`, and `TIMESTAMPTZ` columns. This update fixes a bug that previously caused default values to be shown incompletely, improving clarity and accuracy in query plan analysis.

<!-- Auto Generated Markdown for FIR-42032 - Owned by Amit Schreiber -->
**Resolved filtering issue for views in `information_schema.tables` to enforce user permissions**

Fixed a bug in `information_schema.tables` which previously listed views that users were not authorized to access. Even though querying these views would fail, users could still see that they existed. Now `information_schema.tables` only lists views that users are allowed to access. 
