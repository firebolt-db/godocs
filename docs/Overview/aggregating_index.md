
# Firebolt Aggregating Index

The Firebolt **Aggregating Index** is a powerful optimization tool that enhances query performance by precomputing and storing aggregation results. It is particularly effective for analytical workloads that frequently perform similar aggregations on large datasets.

## Key Features

1. **Similar to Materialized Views**:
   - The Aggregating Index is conceptually similar to a materialized view as it materializes a single table aggregation.
   - This means it stores the results of precomputed aggregations for faster query performance.

2. **Implemented as a Table**:
   - The Aggregating Index is implemented as a physical table that can store intermediate aggregation results.

3. **Automatic Synchronization**:
   - The Aggregating Index is automatically updated in real time to reflect changes in the origin table after each transaction.

4. **Handles DELETE/UPDATE Operations**:
   - Any **DELETE** or **UPDATE** operation on the origin table automatically updates the corresponding aggregating index to ensure consistency.

5. **Impact on Ingest Performance**:
   - While beneficial for query performance, the Aggregating Index introduces additional overhead during data ingestion. This can slightly slow down insert operations on the origin table.

6. **Primary Index Deduction**:
   - The underlying table's **Primary Index** is determined by the order of the **GROUP BY** keys specified during the Aggregating Index creation.

## Syntax

Here is the syntax to create an Aggregating Index:

```sql
CREATE AGGREGATING INDEX index_name
ON table_name(column1, column2, AGG_FUNCTION1(column3), AGG_FUNCTION2(column4), ...);
```

### Parameters:
- **`index_name`**: The name of the aggregating index.
- **`table_name`**: The name of the table on which the index is created.
- **`column1`, `column2`**: Columns used as grouping keys (dimensions).
- **`AGG_FUNCTION1(column3)`**: Aggregation function applied to a specific column.

## Example

The following example creates an Aggregating Index on the `sales` table:

```sql
CREATE AGGREGATING INDEX sales_agg_index
ON sales(product_id, region, SUM(sales_amount), COUNT(order_id));
```

- **Grouping Keys**: `product_id`, `region`
- **Aggregations**: Precomputes the `SUM` of `sales_amount` and the `COUNT` of `order_id`.

## Benefits

1. **Faster Query Performance**:
   - Queries leveraging the Aggregating Index can avoid scanning raw data, reducing execution time significantly.

2. **Reduced Compute Costs**:
   - By storing pre-aggregated results, it minimizes the resources needed for on-the-fly calculations.

3. **Optimized for Dashboards and Reports**:
   - Ideal for repeated analytical queries that focus on the same aggregation patterns.

## Considerations

- **Ingestion Overhead**:
  - Maintaining the Aggregating Index increases the ingestion time into the origin table due to the need to update the pre-aggregated data.

- **Automatic Updates**:
  - Every data change, including `INSERT`, `DELETE`, or `UPDATE`, triggers an update in the Aggregating Index, ensuring it always remains consistent.

## Behind the Scenes

- **Index Storage**:
  - The Aggregating Index is physically stored as a table in Firebolt, which facilitates faster lookups.

- **Primary Index**:
  - The order of the **GROUP BY** keys in the Aggregating Index creation determines the **Primary Index** of the underlying table.

By leveraging Firebolt Aggregating Indexes, organizations can significantly improve the efficiency and performance of their data analytics workflows.
