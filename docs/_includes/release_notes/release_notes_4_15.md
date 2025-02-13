## Firebolt Release Notes - Version 4.15

### New Features

### Behavior Changes

<!-- Auto Generated Markdown for FIR-43042 - Owned by Immanuel Haffner -->
**Improved `EXPLAIN(STATISTICS)` to include estimated row counts and column distinct counts when available  **
The `EXPLAIN(STATISTICS)` function now provides estimated row counts and column distinct counts when available. This enhancement helps in analyzing query performance by offering more detailed insights.


<!-- Auto Generated Markdown for FIR-43103 - Owned by Michael Freitag -->
**Fixed a bug in the shuffle elimination logic for distributed `GROUP BY` operators that improved query performance and result accuracy

**
Resolved a bug in the shuffle elimination logic for distributed `GROUP BY` operators. This bug sometimes led to missed optimization opportunities and, in rare cases, incorrect results. Addressing this issue improves query performance and result accuracy, enhancing overall data processing efficiency.


<!-- Markdown for FIR-42197 - Owned by Tal Zelig -->
**Use NULL instead of empty strings for passing unset TVF parameters**

NULL must be used instead of empty strings ('') to pass unset TVF parameters.


### Performance Improvements

<!-- Auto Generated Markdown for FIR-42755 - Owned by Andres Senac -->
**Optimized conversion of outer joins to inner joins with null-rejecting filters for improved query performance**
Optimized the system to convert outer joins on the non-preserving side of another outer join into inner joins when a null-rejecting filter is present. This change improves query performance by reducing unnecessary outer join operations.


<!-- Auto Generated Markdown for FIR-42992 - Owned by Tobias Humig -->
**Improved performance by allowing multiple `INSERT INTO <tbl> VALUES ...` statements to be combined in a single request

**
Multiple `INSERT INTO <tbl> VALUES ...` statements can now be combined in a single request if they insert into the same table. These statements are merged and processed together on the server. This improvement reduces network overhead and enhances performance for batch data insertion.


<!-- Auto Generated Markdown for FIR-42537 - Owned by Pascal Schulze -->
**Updated `duration_us` in `information_schema.engine_running_queries` and `information_schema.engine_query_history` to include total query time across Firebolt infrastructure including retries and gateway services

**
The `duration_us` value in the system tables `information_schema.engine_running_queries` and `information_schema.engine_query_history` now reflects the complete time a query spends in the Firebolt infrastructure. Previously, it included only the time on the engine and did not consider retries. The duration now also accounts for time spent in gateway services and retries. For example, if a query activates a stopped engine, the start-up time is included in the query's duration. This change provides a more accurate measurement of query duration, allowing users to better understand and optimize performance.


### Bug Fixes

<!-- Auto Generated Markdown for FIR-42032 - Owned by Amit Schreiber -->
**Fixed an issue with `information_schema.tables` not filtering views by permissions

**
Resolved an issue where `information_schema.tables` did not filter views based on permissions. This ensures that users now see only the views they have permission to access, improving data security and access management.


<!-- Auto Generated Markdown for FIR-43280 - Owned by Lorenz Hübschle -->
**Fixed a bug in the shuffle elimination logic for distributed outer join operators, ensuring query accuracy and reliability

**
A bug in the shuffle elimination logic for distributed outer join operators was fixed. This fix ensures correct results in queries using these operators, enhancing data accuracy and reliability.


<!-- Auto Generated Markdown for FIR-43315 - Owned by Andres Senac -->
**Fixed a bug with correlated `EXISTS` subqueries that caused duplicated outer tuples in query results**
Resolved a bug where a correlated `EXISTS` subquery with both correlated and non-correlated filters duplicated the outer tuples in the query result. Users benefit from more accurate query results.
