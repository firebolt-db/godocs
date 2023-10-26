---
layout: default
title: RECOMMEND DDL
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Queries
---

# RECOMMEND DDL
`CALL recommend_ddl` can help you to optimize schema configuration to enhance query performance. The statement finds primary index and partition by recommendations for a specified table tailored to a workload.

## Syntax

```sql
CALL recommend_ddl(<table_name>, (<select_statement>))
```

## Parameters
{: .no_toc}

| Parameter              | Description |
| :--------------------- | :---------- |
| `<table_name>`  | The name of the table for which primary index and partition key recommendations should be found. |
| `<select_statement>`    | [SELECT](./select.md) statement that returns the workload that the DDL recommendation is based on. The `<select_statement>` must return exactly one column of type `TEXT`. |

## Example
The example below demonstrates retrieving schema recommendation using the `CALL recommend_ddl` statement for a table named `lineitem` tailored to the workload in the query history of the past week.

```sql
CALL recommend_ddl(lineitem, (SELECT query_text FROM information_schema.query_history WHERE query_start_ts > NOW() - INTERVAL '1 week'))
```
The `<select_statement>` returns exactly one column of type `TEXT` containing the SQL statements that the `CALL recommend_ddl` command should analyze.

**Returns:**

| recommended_partition_key | recommended_primary_index | scan_savings | analyzed_queries |
| :--- | :--- | :--- | :--- |
| DATE_TRUNC('month', l_orderdate) | l_shipmode, l_returnflag, l_shipinstruct | 0.12 | 420 |

The `CALL recommend_ddl` results indicate that the amount of bytes scanned can be decreased by up to 21% by configuring `"l_shipmode, l_returnflag, l_shipinstruct"` as a primary index and `"DATE_TRUNC('month', l_orderdate)"` as the partition by expression.
The statement analyzed 420 queries returned by the <select_statement> that scanned the `lineitem` table and applied filters to any of the `lineitem` columns.

## Under The Hood

Primary index and partition key configurations are chosen to maximize pruning potential and thus reduce query runtime time. Columns with selective filters and low cardinality are suggested as primary index and partition key columns. Recommendations can be run on empty tables as well as on tables with production data. The more queries executed on a populated table, the better the recommendations become. If additionally the workload of a table changes over time, it can be beneficial to run the `CALL recommend_ddl` command periodically to check for better table configurations.
