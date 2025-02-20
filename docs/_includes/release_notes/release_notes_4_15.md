## Firebolt Release Notes - Version 4.15

### New Features

<!-- Auto Generated Markdown for FIR-43042 - Owned by Immanuel Haffner -->
**Improved `EXPLAIN(STATISTICS)` to include estimated row counts and column distinct counts when available**    
The `EXPLAIN(STATISTICS)` function now provides estimated row counts and column distinct counts, when available. This enhancement offers more detailed insights for analyzing query performance.

**Added a Tableau connector for the current version of Firebolt**

Tableau is a visual analytics platform that empowers users to explore, analyze, and present data through interactive visualizations. The current Firebolt connector in Tableau Exchange supports only an older version of Firebolt. You can now download the latest connector directly from Firebolt and integrate it with Tableau Desktop or Tableau Server. Follow the installation instructions in [Integrate with Tableau]({% link Guides/integrations/tableau.md %}) to set up the updated connector.

**Added a DBeaver connector for the current version of Firebolt**

DBeaver is a free, open-source database administration tool that supports multiple database types, provides a graphical interface for managing databases, running queries, and analyzing data. You can now connect to DBeaver using the [Firebolt JDBC driver](https://docs.firebolt.io/Guides/developing-with-firebolt/connecting-with-jdbc.html). Follow the instructions in [Integrate with DBeaver]({% link Guides/integrations/dbeaver.md %}) to set up a connection to DBeaver.

**Added the Firebolt Resource Center to the Firebolt Workspace**

The Firebolt Resource Center is now accessible from the **Firebolt Workspace**. Select the Firebolt icon in the bottom-right corner to access links to the Get Started guide, Knowledge Center, documentation, release notes, announcements, and a unified search tool covering all Firebolt resources.
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
Workloads that send multiple consecutive `INSERT INTO <tbl> VALUES ...` statements into the same table can now run much faster by sending all statements in a single request separated by semicolons. These statements are now automatically merged and processed together on the server within a single transaction, which means that either all of them succeed or fail. This improvement reduces network overhead and enhances performance for batch data insertion.

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
Fixed a bug with non-trivial correlated `EXISTS` subquery whereby the rows from the outer relation were duplicated in the query result. In the following example,
```sql
create table t1(x int null)

create table t2(x int null, y int null)

insert into t1 values (1), (2)

insert into t2 values (1, 2), (1, 3)

select *,
  exists(select 1 from t2 where coalesce(t2.x, t2.y) = t1.x)
from t1
--
x INTEGER,?column? BOOLEAN
1,t
1,t
2,f
```

The matching rows from t1 are repeated in the query output as many times as the number of distinct values of `(x, y)` tuples in t2.
