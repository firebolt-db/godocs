## Firebolt Release Notes - Version 4.15

### New Features

### Behavior Changes

<!-- Auto Generated Markdown for FIR-43042 - Owned by Immanuel Haffner -->
**Improved `EXPLAIN(STATISTICS)` to include estimated row counts and column distinct counts when available  **
The `EXPLAIN(STATISTICS)` function now provides estimated row counts and column distinct counts, when available. This enhancement offers more detailed insights for analyzing query performance.
### Behavior Changes


<!-- Markdown for FIR-42197 - Owned by Tal Zelig -->
**Use NULL instead of empty strings for passing unset TVF parameters**

NULL must be used instead of empty strings ('') to pass unset TVF parameters.


### Performance Improvements

<!-- Auto Generated Markdown for FIR-42755 - Owned by Andres Senac -->
**Improved outer join conversion to inner joins for better query performance**

Firebolt now automatically converts outer joins on the non-preserving side of another outer join to inner joins when a null-rejecting filter is present. The non-preserving side can exclude rows without matching values, while a null-rejecting filter excludes rows with NULL values. This optimization improves query performance by reducing unnecessary outer join operations.


<!-- Auto Generated Markdown for FIR-42992 - Owned by Tobias Humig -->
**Improved performance by allowing multiple `INSERT INTO <tbl> VALUES ...` statements to be combined in a single request

**
Workloads that send multiple consecutive `INSERT INTO <tbl> VALUES ...` statements into the same table can now run much faster by combining these statements into a single request. These statements are now automatically merged and processed together on the server within a single transaction, which means that either all of them succeed or fail. This improvement reduces network overhead and enhances performance for batch data insertion.


<!-- Auto Generated Markdown for FIR-42537 - Owned by Pascal Schulze -->
**Updated `duration_us` in `information_schema.engine_running_queries` and `information_schema.engine_query_history` to include total query time across Firebolt infrastructure including retries and gateway services

**
The `duration_us` value in the system tables `information_schema.engine_running_queries` and `information_schema.engine_query_history` now reflects the complete time a query spends in the Firebolt infrastructure. Previously, it included only the time on the engine and did not consider retries. The duration now also accounts for time spent in gateway services and retries. For example, if a query activates a stopped engine, the start-up time is included in the query's duration. This change provides a more accurate measurement of query duration, allowing users to better understand and optimize performance.


### Bug Fixes

<!-- Auto Generated Markdown for FIR-43280 - Owned by Lorenz Hübschle -->
**Fixed a bug in the logic for distributed outer join operators

**
A bug in the shuffle elimination logic for distributed outer join operators was fixed. This fix ensures correct results in queries using these operators, enhancing data accuracy and reliability.


<!-- Auto Generated Markdown for FIR-43315 - Owned by Andres Senac -->
**Fixed a bug with correlated `EXISTS` subqueries that caused duplicated outer tuples in query results**
Resolved a bug where a correlated `EXISTS` subquery with both correlated and non-correlated filters duplicated the outer tuples in the query result. Users benefit from more accurate query results.
