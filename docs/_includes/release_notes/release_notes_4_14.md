## Firebolt Release Notes - Version 4.14

### New Features


<!-- Auto Generated Markdown for FIR-42324 - Owned by David Boublil -->
**Enabled support for nested arrays of arrays in Parquet files

**
Added support for arrays of arrays with any level of nesting in Parquet. This enhancement facilitates more complex data structures, making it easier to store and query nested data within Parquet files.


<!-- Auto Generated Markdown for FIR-42537 - Owned by Pascal Schulze -->
**Updated `DURATION_US` to include total query time in Firebolt infrastructure for enhanced performance monitoring and optimization.**
The `DURATION_US` in the system tables `INFORMATION_SCHEMA.ENGINE_RUNNING_QUERIES` and `INFORMATION_SCHEMA.ENGINE_QUERY_HISTORY` now includes the total time a query has spent in the Firebolt infrastructure. Previously, it only tracked time on the engine without considering retries. Now, it also counts time spent in gateway services and on retries. For example, if a query activates a stopped engine, the engine's start-up time is included in the query's duration. This update provides a more accurate representation of query execution time, aiding users in performance monitoring and optimization.


### Behavior Changes

<!-- Auto Generated Markdown for FIR-34196 - Owned by Pascal Schulze -->
**Removed support for legacy HTTP ClickHouse headers `X-ClickHouse`**
The system no longer accepts or returns legacy HTTP ClickHouse headers of the format `X-ClickHouse`. This helps to maintain compatibility and standardization across API interactions.


### Performance Improvements

<!-- Auto Generated Markdown for FIR-42903 - Owned by Demian Hespe -->
**Enhanced data ingestion performance for `GEOGRAPHY` objects of type `POINT`

**
Enhanced the performance of data ingestion for `GEOGRAPHY` objects of type `POINT`. This improvement speeds up the process of loading geographical point data, allowing for quicker data integration and analysis.


<!-- Auto Generated Markdown for FIR-42803 - Owned by Asya Shneerson -->
**Optimized performance of `SELECT` queries on External Tables with URLs to multi-file directories

**
Improved the performance of `SELECT` queries on External Tables when URLs point to folders containing many files across different directories. This update speeds up data access and processing.


<!-- Auto Generated Markdown for FIR-42519 - Owned by Demian Hespe -->
**Added support for queries with cross joins and complex joins to the result cache to enhance performance by reducing repeated calculations**
The result cache now supports queries using cross joins or complex joins with OR conditions and inequalities. This change improves query performance by reducing the need for repeated calculations.


### Bug Fixes

<!-- Auto Generated Markdown for FIR-42330 - Owned by Gil Cizer -->
**Required `USAGE` permissions for accessing `INFORMATION_SCHEMA`**
Accessing `INFORMATION_SCHEMA` now requires `USAGE` permissions on the database. Queries to the `INFORMATION_SCHEMA` will fail if the database lacks these permissions, ensuring consistent behavior with other permission-restricted queries. Users should ensure their databases have the correct permissions to avoid access issues.


<!-- Auto Generated Markdown for FIR-42393 - Owned by Judson Wilson -->
**Certainly! Please provide the content you would like summarized, and I'll be happy to help you create a title for the release note.**
It seems that the content for the release note is missing. Please provide the text that needs editing, and I will assist you in rewriting it based on your specifications.


<!-- Auto Generated Markdown for FIR-42767 - Owned by Demian Hespe -->
**Updated the `EXPLAIN` command to display accurate default values for `DATE`, `TIMESTAMP`, and `TIMESTAMPTZ` columns.  
**
The `EXPLAIN` command now displays default values for columns of type `DATE`, `TIMESTAMP`, and `TIMESTAMPTZ`. A bug was fixed that previously caused these default values to be shown inaccurately. This update assists users in verifying and understanding query plans more clearly and accurately.


<!-- Auto Generated Markdown for FIR-32711 - Owned by Pascal Schulze -->
**Enabled manual cancellation for ongoing DML queries after connection drops**
Query Cancellation on Connection Drop

When the network connection between a client and Firebolt is lost, DML queries like `INSERT`, `UPDATE`, and `DELETE` keep running in the background. This change allows users to maintain ongoing operations despite connection interruptions, such as when closing the Firebolt UI tab or experiencing network issues. Users can monitor the progress of these queries in `information_schema.engine_running_queries` or cancel them manually using the `CANCEL QUERY` statement. Meanwhile, DQL queries such as `SELECT` are still automatically canceled when a connection drops.


<!-- Auto Generated Markdown for FIR-42032 - Owned by Amit Schreiber -->
**Resolved filtering issue for views in `information_schema.tables` ensuring visibility based on user permissions

**
Fixed an issue in `information_schema.tables` where filtering for views did not function correctly. It now filters views based on permissions. This ensures users only see views they are authorized to access, improving data security.
