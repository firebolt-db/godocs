---
layout: default
title: Aggregating Index
description: Aggregating index overview
parent: Overview
nav_order: 6
---

# Aggregating Index

The Firebolt **Aggregating Index** is a powerful optimization tool that enhances query performance by precomputing and storing aggregation results. It is particularly effective for analytical workloads that frequently perform similar aggregations on large datasets.

## Key Features

1. **Similar to Materialized Views**:
   - The Aggregating Index is conceptually similar to a materialized view as it materializes a single table aggregation.
   - This means it stores the results of precomputed aggregations for faster query performance.

2. **Automatic Synchronization**:
   - The Aggregating Index is automatically updated in real time to reflect changes in the base table after each transaction.

3. **Handles DELETE/UPDATE Operations**:
   - Any **DELETE** or **UPDATE** operation on the base table automatically updates the corresponding aggregating index to ensure consistency.

4. **Automatic `COUNT(*)` Aggregation**:
   - A `COUNT(*)` aggregation is automatically added to every Aggregating Index if it is not explicitly specified by the user.
   - This ensures proper support for `DELETE` operations on the base table.

5. **Impact on Ingest Performance**:
   - While beneficial for query performance, the Aggregating Index introduces additional overhead during data ingestion. This can slow down insert operations on the base table.

6. **Primary Index Deduction**:
   - The underlying table's **Primary Index** is determined by the order of the **GROUP BY** keys specified during the Aggregating Index creation.

## Maintenance

### Vacuuming the Aggregating Index

- It is recommended to periodically **vacuum** the Aggregating Index to:
  - Defragment the data in the Aggregating Index table.
  - Remove deleted items from disk (if `DELETE` operations were applied to the base table).
- Regular vacuuming can improve query performance, especially in the following scenarios:
  1. **Batch Inserts**: Frequent batch inserts can lead to fragmented data in the Aggregating Index table.
  2. **Mutations on the base Table**: Operations like `DELETE` or `UPDATE` on the base table can also fragment the Aggregating Index table.

## Syntax

Here is the syntax to create an Aggregating Index:

```sql
CREATE AGGREGATING INDEX index_name
ON table_name(<grouping_element>, <aggregation_element>);
```

### Parameters:
- **`index_name`**: The name of the aggregating index.
- **`table_name`**: The name of the table on which the index is created.
- **`<grouping_element>`**: Expressions used as grouping keys (dimensions).
- **`<aggregation_element>`**: Aggregation functions applied to a specific expressions.

## Example

The following example creates an Aggregating Index on the `sales` table:

```sql
CREATE AGGREGATING INDEX sales_agg_index
ON sales(product_id, region, SUM(sales_amount), COUNT(DISTINCT order_id));
```

- **Grouping Keys**: `product_id`, `region`
- **Aggregations**: Precomputes the `SUM` of `sales_amount` and the `COUNT DISTINCT` of `order_id`.

## Benefits

1. **Faster Query Performance**:
   - Queries leveraging the Aggregating Index can avoid scanning raw data, reducing execution time significantly.

2. **Reduced Compute Costs**:
   - By storing pre-aggregated results, it minimizes the resources needed for on-the-fly calculations.

3. **Optimized for Dashboards and Reports**:
   - Ideal for repeated analytical queries that focus on the same aggregation patterns.

## Considerations

- **Ingestion Overhead**:
  - Maintaining the Aggregating Index increases the ingestion time into the base table due to the need to update the pre-aggregated data.

- **Vacuuming**:
  - Regularly vacuuming the Aggregating Index is critical to ensure optimal query performance by defragmenting the data and removing stale or deleted items.


By leveraging Firebolt Aggregating Indexes, organizations can significantly improve the efficiency and performance of their data analytics workflows.
