---
redirect_from:
  - /godocs/Guides/working-with-indexes/using-aggregating-indexes.html
  - /using-indexes/using-aggregating-indexes.html
layout: default
title: Aggregating index
description: Aggregating index overview
parent: Data modeling
nav_order: 1
---

# Aggregating index

Firebolt's aggregating index is a powerful tool for improving performance in large-scale analytics. Similar to a materialized view, it precomputes and stores the results of aggregate functions, allowing queries to access data directly from the index instead of scanning the entire table. This approach greatly reduces compute overhead and speeds up query times, making it especially useful for repetitive tasks like generating dashboards and reports.

Aggregating indexes are automatically updated in real-time whenever new data is added or when changes, such as `DELETE` or `UPDATE` operations, are made to the base table. Firebolt also enhances performance by dividing aggregating indexes into smaller segments that are distributed across multiple engine nodes. This allows queries to run in parallel across these nodes, improving both scalability and efficiency while ensuring that the data remains consistent and accurate.

Topics:
- [Aggregating index](#aggregating-index)
  - [Key features](#key-features)
  - [Syntax](#syntax)
    - [Parameters](#parameters)
  - [Example](#example)
  - [Considerations](#considerations)

## Key features

* **Automatic synchronization**

   The aggregating index is automatically updated in real-time to reflect changes in the base table after each transaction including **DELETE** or **UPDATE** operations.

* **Automatic `COUNT(*)` aggregations**

   A `COUNT(*)` aggregation is automatically added to every aggregating index unless explicitly specified by the user. This ensures the index can accurately handle `DELETE` operations by tracking the number of rows affected. The aggregating index adjusts its precomputed results to remain synchronized with the base table, maintaining consistency and ensuring accurate query results.

* **Primary index deduction**

   Because an aggregating index is a unique type of table, when you create an aggregating index, the primary indexes for that created table are established based 
   on the order of the **GROUP BY** keys specified during the creation of the aggregating index. This primary index works like any other primary index: Firebolt 
   physically organizes the data according to these keys, which align with how queries group and aggregate the data. This optimization enables effective data 
   pruning and reduces scan times, making data retrieval more efficient.

## Syntax


```sql
CREATE AGGREGATING INDEX <index_name>
ON <table_name> (
   <grouping_element>
     [, ...],
     <aggregation_element>
     [, ...]
);
```

### Parameters

| Parameter             | Description                                                            |
|-----------------------|------------------------------------------------------------------------|
| `<index_name>`        | The name of the aggregating index.                                     |
| `<table_name>`        | The name of the table on which the index is created.                  |
| `<grouping_element>`  | Expressions specified as grouping keys or dimensions when creating the index.                      |
| `<aggregation_element>` | Aggregation functions applied to specific expressions.               |


## Example

The following example creates an aggregating index `sales_agg_index` on the `sales` table and precomputes the `SUM` and `COUNT` aggregations:

```sql
CREATE AGGREGATING INDEX sales_agg_index
ON sales(product_id, region, SUM(sales_amount), COUNT(DISTINCT order_id));
```

In the previous code example, `product_id` and `region` are grouping keys that are grouped together as `grouping_element`. These keys define how the data is grouped for aggregation, similar to the `GROUP BY` clause in a SQL query. Subsequent queries using these aggregations can retrieve the precomputed values directly from the index, avoiding a full table scan.

Because the code example precomputes `SUM` and `COUNT`, subsequent queries using these aggregations can retrieve the precomputed values directly from the index, avoiding a full table scan.


## Considerations

**Ingestion Overhead**
  
  Maintaining an aggregating index adds processing overhead during data loading, which can slow down Data Manipulation Language (DML) operations such as `INSERT`, `DELETE`, and `UPDATE` on the base table.

**Vacuuming**

  To ensure optimal query performance, you should periodically **vacuum** the aggregating index. [VACUUM]({% link sql_reference/commands/data-management/vacuum.md %}) helps to:

  * Defragment data in the aggregating index table.
  * Remove stale or deleted items from disk after `DELETE` operations on the base table.

  Regular vacuuming can improve query performance, especially for the following:

  * **Frequent batch inserts** &ndash; These inserts can lead to fragmented data in the aggregating index table.
  * **Base table mutations** &ndash; Operations like `DELETE` or `UPDATE` on the base table can also cause fragmentation, impacting query performance.
