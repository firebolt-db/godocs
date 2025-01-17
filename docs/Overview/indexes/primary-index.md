---
layout: default
title: Primary indexes
description: Primary index overview
parent: Data modeling
nav_order: 1
---

# Primary index

The Firebolt primary index is a core optimization tool designed to organize and streamline retrieval of data based on specific column values, enabling efficient data pruning and high-performance querying for large-scale analytics workloads. By leveraging high selectivity, the primary index ensures that queries target only the most relevant portions of the data, significantly reducing the volume of unnecessary scans. This selectivity is especially powerful when the indexed columns align closely with query patterns, allowing the database to quickly locate and retrieve the required data. As a result, query performance is not only optimized but also remains consistent even as data volumes grow.

For more information, see [How primary indexes work]({% link Guides/working-with-indexes/using-primary-indexes.md %}#how-primary-indexes-work).

Topics:
* [Key features](#key-features)
* [Syntax](#syntax)
* [Parameters](#parameters)
* [Example](#example)
* [Considerations](#considerations)

## Key Features

- **Customizable indexing**:  
  - Unlike traditional databases, Firebolt allows primary indexes to be created on any columns, providing you with flexibility to align with query patterns.  
  - Primary key constraints are not enforced, allowing for greater customization.

- **Tablet-based data organization**:  
  - Data is divided into tablets, which are self-contained, fixed-size data chunks approximately 3GB each, sorted by primary index keys for efficient querying.  
  - Within each tablet, your data is further segmented into intra-tablet ranges, approximately 8,000 rows each, for faster access.

- **Support for compound indexes**:  
  - Multiple columns can be included in the primary index, optimizing complex query patterns by allowing efficient pruning and retrieval for queries that filter or group data based on combinations of these columns, such as filtering by both a date range and a category or joining fact and dimension tables on multiple keys.

- **Sparse indexing**:  
  - Firebolt employs a sparse indexing approach, storing only the first row of each tablet range. This approach allows target reads and parallel processing, significantly reducing index size while increasing query performance.

- **Automatic metadata updates**:  
  - The primary index is automatically maintained during data inserts, deletions, and updates ensuring optimal performance. 

- **Handling low-cardinality clauses**:  
  - Starting the primary index with low-cardinality columns can enhance pruning efficiency by creating long ordered runs of data. Low-cardinality columns are those with a limited number of unique values such as months, regions, or statuses, which group similar rows together. This reduces the number of tablet ranges Firebolt needs to scan, enabling faster query execution and better data pruning.

- **Inclusion of join key columns**:  
  - In star schema designs, including join key columns, or foreign keys, in the primary index of fact tables can accelerate queries by facilitating efficient data retrieval.

- **Leverage indexed columns directly**:  
  - Design queries to use indexed columns directly in WHERE clauses without transformations, ensuring that the primary index can be utilized to its full potential for faster data pruning and query execution.

## Syntax

To define a primary index, use the following syntax within a `CREATE TABLE` statement:

```sql
CREATE TABLE <table_name> (
   <column1> <data_type>,
   [<column2> <data_type>,
   ...]
   PRIMARY INDEX(<column_name1>[, <column_name2>, ...])
);
```

## Parameters

| Parameter           | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `table_name`        | The name of the table where the primary index is applied.                  |
| `column_name1, ...` | The columns chosen to be included in the primary index.                    |

## Example

The following example creates a table with a primary index optimized for query performance by filtering for `SubmitDate` and `EngineName`:

``` sql
CREATE [FACT|DIMENSION] TABLE QueryHistory (
  QueryID TEXT,
  QueryText TEXT,
  SubmitDate DATE,
  EngineName TEXT,
  SubmitTime DATE,
  Latency INT
)
PRIMARY INDEX (SubmitDate, EngineName);
```

## Considerations

* **Non-enforced primary key constraint**:  
  Firebolt does not enforce primary key constraints, so users must manage data integrity externally.

* **Managing fragmentation**:  
  Fragmentation can occur as you insert, delete, or update data in a table, which impacts storage efficiency and potentially affects your query performance. Firebolt provides tools to help mitigate this effect:  
  - **Efficient deletion management**:  
    Instead of immediately removing rows from the table, Firebolt uses a deletion mask vector to flag rows as deleted. This vector acts as a lightweight overlay that marks rows for exclusion during queries while keeping the underlying data intact until cleanup is performed.  
    This approach ensures consistency and avoids disrupting the primary index during updates or deletions.  
  - **fragmentation metric**:  
    Use the `information_schema.tables` to access the fragmentation metric to assess fragmentation levels and determine whether maintenance actions are needed.  
  - **[VACUUM]({% link sql_reference/commands/data-management/vacuum.md %}) command**:  
    You can use the `VACUUM` command to clean up rows flagged for deletion and reorganize fragmented data. It is particularly useful when large numbers of rows have been deleted or updates have introduced significant fragmentation.

* **Query Performance Overhead**:  
  While sparse indexes enable targeted reads and parallel processing to improve query performance, they may still require scanning one tablet range from multiple tablets, even for highly selective filters. This can result in more data being scanned compared to a globally sorted index, potentially affecting performance in certain scenarios.

* **Column Selection**:  
  Choose columns with high selectivity and relevance to query patterns for optimal performance. **Selectivity** refers to the ability of a column to significantly narrow down the dataset when filtered, typically measured by the proportion of unique values in the column. Columns with higher selectivity, such as IDs or timestamps, help reduce the number of rows scanned, leading to faster query execution and better resource efficiency.

By leveraging Firebolt’s primary index, your organization can enhance its query performance, optimize data management, and scale efficiently for modern analytics workloads.

