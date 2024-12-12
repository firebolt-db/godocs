---
layout: default
title: Aggregating Index
description: Aggregating index overview
parent: Using indexes
nav_order: 1
---

# Aggregating Index

Firebolt's aggregating index is a powerful tool for improving performance in large-scale analytics, similar to a materialized view. It precomputes and stores the results of aggregate functions, allowing queries to access data directly from the index instead of scanning the entire table. This approach greatly reduces compute overhead and speeds up query times, making it especially useful for repetitive tasks like generating dashboards and reports.

These indexes are automatically updated in real-time whenever new data is added or when changes, such as `DELETE` or `UPDATE` operations, are made to the base table. Firebolt also enhances performance by dividing aggregating indexes into smaller segments that are spread across multiple engine nodes. This allows queries to run in parallel across these nodes, improving both scalability and efficiency while ensuring that the data remains consistent and accurate.

## Key features

1. **Automatic synchronization**:
   - The aggregating index is automatically updated in real time to reflect changes in the base table after each transaction including any **DELETE** or **UPDATE** operations.

2. **Automatic `COUNT(*)` Aggregation**:
   - A `COUNT(*)` aggregation is automatically added to every aggregating index. Maintaining a count helps to maintain data integrity by reflecting changes from `DELETE` operations, and thus preventing discrepancies in aggregate results.

6. **Primary Index Deduction**:
   The primary index for a Firebolt table is established based on the order of the **GROUP BY** keys specified during the creation of an aggregating index. Firebolt physically organizes the data according to these keys, which aligns with how queries will group and aggregate the data. Then, queries can more efficiently retrieve data through effective data pruning and reduced scan times.

## Syntax


```sql
CREATE AGGREGATING INDEX index_name
ON table_name(<grouping_element>, <aggregation_element>);
```

### Parameters:
- **`index_name`**: The name of the aggregating index.
- **`table_name`**: The name of the table on which the index is created.
- **`<grouping_element>`**: Expressions used as grouping keys or dimensions.
- **`<aggregation_element>`**: Aggregation functions applied to a specific expression.

## Example

The following example creates an aggregating index on the `sales` table:

```sql
CREATE AGGREGATING INDEX sales_agg_index
ON sales(product_id, region, SUM(sales_amount), COUNT(DISTINCT order_id));
```

In the previous code example, `product_id` and `region` are keys that are grouped together as a `grouping_element`. The code example precomputes two aggregations: the `SUM` of `sales_amount` and the `COUNT DISTINCT` of `order_id`. Subsequent queries on these aggregations will use the precomputed values instead of scanning the data and calculating them again.



## Considerations

- **Ingestion Overhead**:
  - Maintaining an aggregating index introduces additional overhead time to load data into the base table, which can slow down insert operations on the base table.

- **Vacuuming**:
  - You should periodically **vacuum** the aggregating index to ensure optimal query performance. VACUUM helps to:
  - Defragment the data in the aggregating index table.
  - Remove deleted items from disk if `DELETE` operations were applied to the base table.

  Regular vacuuming can improve query performance, especially in the following scenarios:
  
  1. **Batch Inserts**: Frequent batch inserts can lead to fragmented data in the Aggregating Index table.
  2. **Mutations on the base Table**: Operations like `DELETE` or `UPDATE` on the base table can also fragment the Aggregating Index table.

By leveraging Firebolt Aggregating Indexes, organizations can significantly improve the efficiency and performance of their data analytics workflows.
