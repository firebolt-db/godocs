## Firebolt Release Notes - Version 4.15

### New Features

<!-- Auto Generated Markdown for FIR-43042 - Owned by Immanuel Haffner -->
**Improved `EXPLAIN(STATISTICS)` to include estimated row counts and column distinct counts when available**    
The `EXPLAIN(STATISTICS)` function now provides estimated row counts and column distinct counts, when available. This enhancement offers more detailed insights for analyzing query performance.

### Performance Improvements

<!-- Auto Generated Markdown for FIR-42755 - Owned by Andres Senac -->
**Improved outer join conversion to inner joins for better query performance**     
A `LEFT JOIN` nested within another `LEFT JOIN` is now converted into an `INNER` join if the upper `LEFT JOIN` discards the null-padded rows introduced by the lower `LEFT JOIN`. This occurs when the upper `LEFT JOIN` filters out `NULL` values from the right-hand side of the lower `LEFT JOIN`. For example, the following query:
```sql
SELECT * 
FROM t1 
LEFT JOIN (
    SELECT t3.x 
    FROM t2 
    LEFT JOIN t3 ON t2.x = t3.x
) t4 
ON t1.x = t4.x;
```
Is now treated as:

```sql
SELECT * 
FROM t1 
LEFT JOIN (
    SELECT t3.x 
    FROM t2 
    INNER JOIN t3 ON t2.x = t3.x
) t4 
ON t1.x = t4.x;
```
This occurs because the upper `LEFT JOIN` filters out rows from `t4` where `t3.x` is `NULL`, making the lower `LEFT JOIN` redundant.

<!-- Auto Generated Markdown for FIR-42992 - Owned by Tobias Humig -->
**Improved performance by allowing multiple `INSERT INTO <tbl> VALUES ...` statements to be combined in a single request**      
Workloads that send multiple consecutive `INSERT INTO <tbl> VALUES ...` statements into the same table can now run much faster by combining these statements into a single request. These statements are now automatically merged and processed together on the server within a single transaction, which means that either all of them succeed or fail. This improvement reduces network overhead and enhances performance for batch data insertion.

<!-- Auto Generated Markdown for FIR-42537 - Owned by Pascal Schulze -->
**Updated `duration_us` in `information_schema.engine_running_queries` and `information_schema.engine_query_history` to include total query time across Firebolt infrastructure including retries and gateway services**       
The `duration_us` value in the system tables `information_schema.engine_running_queries` and `information_schema.engine_query_history` now reflects the complete time a query spends in the Firebolt infrastructure. Previously, it included only the time on the engine and did not consider retries. The duration now also accounts for time spent in gateway services and retries. For example, if a query activates a stopped engine, the start-up time is included in the query's duration. This change provides a more accurate measurement of query duration, allowing users to better understand and optimize performance.

### Behavior Changes

<!-- Markdown for FIR-42197 - Owned by Tal Zelig -->
**Use NULL instead of empty strings for passing unset TVF parameters**      
Table-valued functions (TVFs) such as `list_objects`, `read_parquet`, and `read_csv`, that accept string named parameters like `aws_access_key_id` and `aws_role_arn`, will no longer treat empty strings (`''`) as unset arguments. The empty strings will instead be forwarded to the credential provider and may return errors. If you want to pass an explicitly unset parameter, use `NULL` instead.

### Bug Fixes

<!-- Auto Generated Markdown for FIR-43280 - Owned by Lorenz Hübschle and FIR-43103 - Owned by Michael Freitag -->
**Resolved issue in distributed GROUP BY and JOIN planning**         
Resolved a bug in the optimization process for distributed `GROUP BY` and `JOIN` operators. This bug sometimes led to missed optimization opportunities and, in rare cases, incorrect results.

<!-- Auto Generated Markdown for FIR-43315 - Owned by Andres Senac -->
**Fixed a bug in correlated `EXISTS` subqueries that caused duplicated outer tuples in query results**      
Resolved a bug in correlated `EXISTS` subqueries that occurred when both correlated and non-correlated filters were applied. This bug caused the outer rows, or tuples, in the query results to duplicate. The fix ensures that only unique outer rows appear in the result, improving query accuracy and reliability.
