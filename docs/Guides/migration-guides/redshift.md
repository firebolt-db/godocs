---
layout: default
title: Migrate from Amazon Redshift 
description: Learn how to migrate your workflow from Redshift
nav_order: 1 
parent: Migrate to Firebolt
has_toc: true
has_children: false
---

# Migrate from Amazon Redshift to Firebolt

Migrating from Amazon Redshift to Firebolt unlocks significant improvements in performance, scalability, and cost efficiency for analytics workloads. Firebolt’s modern, decoupled architecture eliminates many of the constraints of Redshift’s monolithic cluster approach, enabling faster query performance, elastic compute scaling, and optimized workload management.

This guide provides a step-by-step approach to migrating from Redshift to Firebolt, covering:

* **Schema transformation** &ndash; Adapting Redshift’s `SORT` and `DIST` keys to Firebolt’s indexing model.
* **Data migration** &ndash; Exporting Redshift data and loading it efficiently into Firebolt.
* **Query adaptation** &ndash; Translating Redshift SQL to Firebolt for improved performance.
* **Performance optimization** &ndash; Using Firebolt’s indexing and compute elasticity to maximize speed.

### Key considerations

Migrating from Redshift to Firebolt is more than just moving data. It requires rethinking how workloads are managed and optimized. Unlike Redshift’s single-cluster model, Firebolt allows for independent compute engines, for workload isolation and cost efficiency. A simple one-to-one migration may not fully use Firebolt’s capabilities, so careful planning is required.

The following sections will guide you through understanding Firebolt’s architecture, selecting the right compute engines, transforming your schema, and optimizing query performance to ensure a seamless and efficient migration.

Overview:
* [Architectural differences](#architectural-differences) &ndash; Firebolt separates compute from storage, enabling independent scaling, workload isolation, and cost efficiency.
* [Schema differences](#schema-differences) &ndash; Firebolt replaces Redshift’s manual distribution keys and rigid schemas with dynamic indexing, denormalization, and flexible JSON handling for faster, simpler queries.

Steps:
* [Export data from Redshift](#export-data-from-redshift) &ndash; Export Redshift data to Amazon S3 in CSV or Parquet format, prepared for efficient loading into Firebolt.
* [Load data into Firebolt](#load-data-into-firebolt) &ndash; 
* [Translate queries](#translate-queries)
* [Performance testing and optimization](#performance-testing-and-optimization)
* [Automated migration](#automated-migration)
* [Post-migration validation and maintenance](#post-migration-validation-and-maintenance)


## Architectural differences

Migrating from Amazon Redshift to Firebolt requires adapting to a different architecture. Redshift’s monolithic cluster model, where compute and storage are tightly integrated, limits flexibility and forces full-cluster scaling. In contrast, Firebolt separates compute engines from storage, enabling elastic scaling, workload isolation, and advanced indexing for faster performance, as summarized in the following table:

| **Feature**               | **Redshift**                                        | **Firebolt**                                          | **Impact on Data Modeling** |
|---------------------------|-----------------------------------------------------|------------------------------------------------------|-----------------------------|
| **Architecture**          | Monolithic cluster, compute-storage tightly coupled. | Virtualized engines, compute-storage decoupled. | Distribute workloads across multiple engines instead of a single cluster. |
| **Scalability and Elasticity** | Resizing requires downtime, limited concurrency scaling. | Highly elastic, auto-scaling, independent compute and storage. | Assign separate engines for ingestion, analytics, and ETL to optimize resources. |
| **Workload Isolation**    | Shared cluster, resource contention. | Multiple engines, fully isolated workloads. | Use dedicated engines to prevent query interference. |
| **Data Storage**          | Requires manual tuning of `SORT` and `DIST` keys. | Index-based optimization (primary, aggregating, join indexes). | Replace `SORT` and `DIST` keys with indexing for faster queries. |
| **Cost Model**            | Charged for cluster uptime, additional cost for concurrency scaling. | Pay-as-you-go, billed per engine runtime. | Pause idle engines and use right-sized compute to reduce costs. |

This section outlines key differences in compute and storage, scalability, workload isolation, indexing, and cost model, helping you optimize Firebolt for speed and efficiency.

### Architectural compute and storage differences

One of the biggest advantages of migrating to Firebolt is its engine-based architecture, which allows you to tailor your compute resources to specific workloads. Amazon Redshift **combines compute and storage into a single cluster**, meaning all workloads share the same resources, and scaling requires resizing the entire cluster, even if only compute or storage needs adjustment. In contrast, **Firebolt separates compute engines from storage**, allowing workloads to run on independent engines that can be resized, paused, or restarted without affecting storage. This prevents resource contention, improves query performance, and enables cost-efficient scaling.  

Since Firebolt allows dedicated compute engines for different workloads, selecting the right engine type is critical to optimizing performance and cost efficiency. Unlike Redshift, where all workloads run on the same cluster, Firebolt lets you assign separate engines for ingestion, analytics, and transformation tasks. To maximize efficiency, engines should be right-sized based on workload needs, scaled independently of storage, and paused when not in use to reduce costs.

#### Best practices for architectural differences

| **Best practices for architectural differences** | **Impact**                                      | **How to implement**  |
|------------------------------------------------|------------------------------------------------|----------------------|
| [1. Use separate Firebolt engines for different workloads](#1-use-separate-firebolt-engines-for-different-workloads) | Prevents resource contention and improves workload isolation. | Assign dedicated engines for ingestion, analytics, and transformations to avoid competition for resources. |
| [2. Scale compute and storage independently](#2-scale-compute-and-storage-independently) | Allows flexible resource allocation without overprovisioning. | Increase compute resources for analytics without expanding storage, and scale engines independently based on workload needs. |
| [3. Pause idle engines to reduce costs](#3-pause-idle-engines-to-reduce-costs) | Lowers operational costs while keeping data accessible. | Use auto-stop settings to pause unused engines and restart them on demand. |
| [4. Optimize queries with indexing](#4-optimize-queries-with-indexing) | Speeds up query processing and reduces scan times. | Use primary indexes for efficient filtering and aggregating indexes for precomputed aggregations. |
 

##### 1. Use separate Firebolt engines for different workloads

Unlike Redshift, where all queries run in a shared cluster, Firebolt enables workload isolation by assigning dedicated compute engines for different tasks. This ensures that data loading processes no longer compete with analytical queries, maintaining consistent performance. Allocate dedicated engines for critical workloads such as real-time dashboards or high-volume data transformation pipelines to maximize efficiency. 

Some key differences include:

* Firebolt engines support both read and write operations on shared data while maintaining strong consistency across engines, eliminating the need for manual synchronization.  
* Firebolt optimizes workload execution dynamically based on configuration, resource utilization, and query history. This helps balance latency and throughput, ensuring that resources are used efficiently.  

The following table outlines the recommended Firebolt engine configurations for different workloads, ensuring optimal performance, scalability, and cost efficiency:

| **Workload type**          | **Recommended engine configuration** |
|---------------------------|--------------------------------------|
| **High-concurrency business intelligence (BI)**    | Use medium to large engines with high parallelism for supporting many concurrent queries efficiently. |
| **ETL and transformations** | Use small to medium engines with moderate concurrency, optimized for data ingestion and transformations. |
| **Data science**           | Use small engines for iterative, ad-hoc queries or training datasets. |
| **Data-intensive applications** | Use dedicated small engines with consistent SLA for low-latency queries. |
| **Ad-hoc analytics**       | Use on-demand engines that start quickly and scale based on query complexity. |

The following table provides recommended Firebolt engine configurations for different workloads, ensuring optimal performance, scalability, and cost efficiency:

| **Workload**                 | **Engine name**        | **Configuration**          | **Purpose** |
|------------------------------|------------------------|----------------------------|-------------|
| **Data ingestion**           | `ingestion_engine`     | `TYPE = S, NODES = 1`      | Continuous data loading. |
| **High-concurrency queries** | `analytics_engine`     | `TYPE = M, NODES = 6`      | Supports many concurrent queries. |
| **Real-time dashboards**     | `dashboard_engine`     | `TYPE = M, NODES = 2`      | Low-latency SLA-sensitive queries. |
| **Ad-hoc analytics**         | `ad_hoc_engine`        | `TYPE = S, NODES = 2, AUTO_STOP` | Cost-efficient for intermittent use. |

The following code example shows how to create different engines with different sizes to separate data loading and analytics workloads:
 
```sql
CREATE ENGINE "ingestion_engine" WITH
TYPE = "M"
NODES = 2;

CREATE ENGINE "analytics_engine" WITH
TYPE = "L"
NODES = 8;
```
##### 2. Scale compute and storage independently

Firebolt allows scaling compute without affecting storage, unlike Redshift, where storage grows with compute. You can allocate more compute resources for analytics while keeping storage unchanged. Use smaller engines for intermittent workloads.

The following code example shows how to scale an engine for high-currency analytics:
```sql
ALTER ENGINE "analytics_engine" SET NODES = 10;
```
##### 3. Pause idle engines to reduce costs

Firebolt engines consume credits only when engines are running, so pausing unused engines can significantly reduce costs. In Redshift, charges are based on cluster uptime, even if it is idle. In Firebolt, you can pause an engine without losing access to stored data.

The following code example creates an engine that automatically pauses after 30 minutes of inactivity:

```sql
CREATE ENGINE "adaptive_engine" WITH
TYPE = "L"
AUTO_STOP = 30
AUTO_START = TRUE;
```

##### 4. Optimize queries with indexing

Firebolt eliminates the need for `SORT` and `DIST` keys by using indexing for faster query performance. You can filter by a primary index to reduce scan times and use an aggregating index for precomputed aggregations.

The following code example creates a [primary index]({% link Overview/indexes/primary-index.md %}), which is a sparse index, to filter on `GameID` or `PlayerID` so that the query scans over only this index:

```sql
CREATE FACT TABLE playstats (
    GameID INT,
    PlayerID INT,
    CurrentScore BIGINT,
    PlayTime INT
) 
PRIMARY INDEX (GameID, PlayerID);
```

The following code example uses an [aggregating index]({% link Overview/indexes/aggregating-index.md %}) to return results instead of processing calculations at runtime:

```sql
CREATE AGGREGATING INDEX playtime_agg_idx 
ON PlayStats (
    GameID,
    SUM(CurrentPlayTime)
);
```

## Schema differences

Migrating from Amazon Redshift to Firebolt requires adapting your schema to leverage Firebolt’s indexing model, denormalization benefits, and optimized query execution. Unlike Redshift, which relies on `SORT` and `DIST` keys for performance tuning, Firebolt automatically optimizes queries using primary, aggregating, and join indexes. This eliminates the need for manual data distribution and sorting, reducing complexity while improving performance.  

Additionally, semi-structured data handling differs. Redshift’s `SUPER` type allows nested JSON storage, while Firebolt stores JSON as `TEXT`, enabling flexible querying with JSON functions like `JSON_VALUE` and `JSON_EXTRACT`. Firebolt’s schema design also favors denormalization, reducing the need for complex joins and improving analytical query speed.  

The following table outlines key schema differences between Redshift and Firebolt, highlighting the mechanisms Firebolt uses to optimize data modeling and query performance:


| **Schema feature**           | Redshift                                         | Firebolt                                        | Key mechanism and explanation |
|-----------------------------|-------------------------------------------------|-----------------------------------------------|-----------------------------------|
| **Column data types**        | Supports a broad range, including `SUPER` for semi-structured data. | Uses similar types but stores JSON as `TEXT` with functions for querying. | Firebolt requires converting JSON data to `TEXT` and using JSON functions (`JSON_VALUE`, `JSON_EXTRACT`) to query nested fields. |
| **Data distribution, sorting, and indexing** | Uses `SORTKEY` and `DISTKEY` for query performance tuning, requiring manual optimization. | Uses primary, aggregating, and join indexes instead. | Firebolt eliminates manual tuning by using indexes to optimize queries and automatically scan relevant data. |
| **Schema design approach**   | Often normalized to improve joins and reduce redundancy. | Encourages denormalization for faster performance. | Firebolt's indexing structure allows fewer joins, improving query speed and reducing complexity. |
| **Semi-structured data (JSON)** | Supports `SUPER` type for nested JSON storage. | Stores JSON as `TEXT`, with JSON parsing functions. | Firebolt enables dynamic JSON parsing instead of requiring pre-defined structures. |
| **Fact and dimension table design** | Requires explicit distribution styles for performance tuning. | Uses fact and dimension tables with indexing for optimized access. | Firebolt’s fact and dimension tables are designed to work with indexes, ensuring fast analytical queries. |

The following sections explain key schema differences and best practices for adapting your Redshift schema to Firebolt.

#### Best practices for migrating schema

| **Best practices for migrating schema** | **Impact**                                          | **How to implement**  |
|--------------------------------------|--------------------------------------------------|----------------------|
| [1. Replace SORTKEY and DISTKEY with indexes](#replace-sortkey-and-distkey-with-indexes) | Reduces manual optimization, improves query efficiency | Use primary, aggregating, and join indexes instead of `SORTKEY` and `DISTKEY`. |
| [2. Optimize schema for columnar storage](#optimize-schema-for-columnar-storage)  | Improves data pruning, query performance, and reduces joins | Use fact tables for large datasets, primary indexes for filtering, aggregating indexes for precomputed calculations, and denormalize frequently joined tables. |
| [3. Convert JSON SUPER columns to TEXT](#convert-json-super-columns-to-text)    | Enables flexible querying of semi-structured data | Store JSON as `TEXT`, extract values with `JSON_VALUE` and `JSON_EXTRACT`. |
| [4. Validate schema changes before migration](#validate-schema-changes-before-migration) | Ensures data consistency and query optimization   | Compare row counts, query execution times, and indexing efficiency between Redshift and Firebolt. |


#### 1. Replace `SORTKEY` and `DISTKEY` with indexes

Amazon Redshift relies on `SORTKEY` and `DISTKEY` to optimize data distribution and query performance. `SORTKEY` determines the order in which data is physically stored, improving range queries and filtering, while `DISTKEY` controls how data is distributed across cluster nodes to balance query performance. These keys require manual selection and tuning based on query patterns, making performance optimization a complex and ongoing task. Additionally, these keys must be set at table creation and cannot be changed without recreating the table and reloading data, making schema adjustments rigid and time-consuming.

In Redshift, data is partitioned across nodes based on the `DISTKEY`. Selecting a poor distribution key can lead to data skew, where some nodes store significantly more data than others, causing uneven workloads and performance bottlenecks.

One major limitation of Redshift’s approach is that scaling a cluster involves redistributing data across nodes, which can lead to performance degradation and downtime. When the cluster size changes, Redshift must redistribute data based on the defined `DISTKEY`, potentially causing imbalanced workloads and requiring manual re-optimization of data distribution.

Firebolt eliminates the need for manual data distribution and sorting by using indexes to optimize query processing automatically. Unlike Redshift’s fixed distribution and sorting keys, Firebolt’s indexes can be dynamically modified based on changing workloads or replaced without reloading data. [Primary indexes]({% link Overview/indexes/primary-index.md %}) improve scan efficiency by physically storing data in an ordered structure, [aggregating indexes]({% link Overview/indexes/aggregating-index.md %}) precompute results during loading time for faster aggregations, and join indexes optimize joins between large tables. 

Firebolt’s indexing strategy, combined with tablet-based storage, ensures faster query performance with minimal manual tuning, reducing the need for manual `VACUUM` and `ANALYZE` operations required in Redshift to maintain query efficiency. Firebolt’s decoupled architecture makes node-level data distribution unnecessary. Indexes enable the engine to dynamically access only the relevant data. Understanding how indexes and tablet-based storage replace distribution and sort keys is critical. Firebolt stores data in tablets and uses indexing to prune unnecessary data, allowing faster queries without manual tuning.

To migrate Redshift keys to Firebolt indexes, do the following:
* Use a primary index instead of a `SORTKEY` to efficiently filter and scan only relevant data during query runtime.
* Replace `DISTKEY` with an aggregating index when optimizing aggregations, avoiding the need for manual data distribution.
* Use join indexes instead of explicit distribution keys to improve query speed without pre-sorting tables.

The following code example shows a Redshift schema that creates a `sales` table that distributes data by `customer_id (DISTKEY)` for optimized joins, sorts rows by `sale_date (SORTKEY)` for faster range queries, and defines a `customers` table with `customer_id` as the primary key for relational integrity. In Redshift, the primary key is informational only and not enforced at the database level:

```sql
CREATE TABLE sales (
    sale_id INT,
    customer_id INT,
    product_id INT,
    sale_date DATE,
    total_amount DECIMAL(10,2)
) 
DISTSTYLE KEY 
DISTKEY (customer_id) 
SORTKEY (sale_date);

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name TEXT
);
```

The following code example shows the Firebolt equivalent schema using primary, aggregating, and join indexes:
```sql
CREATE FACT TABLE sales (
    sale_id INT,
    customer_id INT,
    product_id INT,
    sale_date DATE,
    total_amount DECIMAL(10,2)
) 
PRIMARY INDEX (sale_date);

CREATE AGGREGATING INDEX sales_summary 
ON sales (
    customer_id,
    SUM(total_amount)
);

CREATE DIMENSION TABLE customers (
    customer_id INT,
    customer_name TEXT
) 
PRIMARY INDEX (customer_id);

CREATE JOIN INDEX customer_lookup 
ON sales (customer_id) 
REFERENCING customers (customer_id);
```

In the previous code example, the following apply:
* `DISTKEY(customer_id)` is replaced with the aggregating index `(customer_id, SUM(total_amount))`. This aggregation runs faster than Redshift because `SUM(total_amount)` is precomputed in the aggregating index.
* `SORTKEY(sale_date)` is replaced with the primary index `(sale_date)`.
* The join index on `customer_id` replaces an explicit join optimization in Redshift, ensuring faster lookups between `sales` and `customers`.

 In the following example, the `DISTKEY` in Redshift partitions data across nodes by `game_id`. Firebolt’s primary index on `GameID` and `PlayerID` allows the engine to quickly prune data during query processing, achieving similar optimization without manual distribution.

In Redshift, the following schema uses `DISTKEY` and `SORTKEY` for the `playstats` table:

```sql
CREATE TABLE playstats (
    game_id INT,
    player_id INT,
    score BIGINT,
    play_time INT
)
DISTSTYLE KEY
DISTKEY (game_id)
SORTKEY (game_id, player_id);
```
In Firebolt, the equivalent schema uses a primary index on `GameID` and `PlayerID`:
```sql
CREATE FACT TABLE playstats ( 
    GameID INT, 
    PlayerID INT, 
    CurrentScore BIGINT, 
    CurrentPlayTime INT 
) 
PRIMARY INDEX (GameID, PlayerID);
```

#### 2. Optimize schema for columnar storage

Firebolt’s columnar storage model organizes data in tablets, allowing queries to scan only the necessary portions of a dataset. Unlike row-based storage, columnar storage reduces I/O overhead and improves query performance by efficiently storing, filtering, and aggregating data.

In Redshift, schemas are often highly normalized to reduce redundancy and optimize joins. However, in Firebolt, denormalization improves performance by reducing the need for complex joins and allowing queries to retrieve data more efficiently. Since Firebolt’s indexing model automatically optimizes filtering and aggregations, denormalized schemas can perform better without increasing redundancy-related costs.

To optimize schema for Firebolt’s columnar storage, do the following:

* Store frequently queried large datasets in fact tables.
* Use dimension tables for reference data and optimize joins with join indexes.
* Denormalize frequently joined tables to minimize query complexity.

The following code example shows a normalized Redshift schema using separate tables for orders and customers:

```sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2)
);

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name TEXT
);
```

In Redshift, retrieving an order with its customer name requires a join as follows:
```sql
SELECT o.order_id, o.order_date, o.total_amount, c.customer_name
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE o.order_date >= '2024-01-01';
```

In Firebolt, denormalization removes the need for this join by storing the `customer_name` directly in the `orders` table:

```sql
CREATE FACT TABLE orders (
    order_id INT,
    customer_id INT,
    customer_name TEXT,
    order_date DATE,
    total_amount DECIMAL(10,2)
);
```
Now, the same query does not require a join, making it simpler and faster:
```sql
SELECT order_id, order_date, total_amount, customer_name
FROM orders
WHERE order_date >= '2024-01-01';
```

In the previous code example, the following apply:

* Denormalization: The `customer_name` column is stored directly in the `orders` table, eliminating the need for a join and reducing query complexity.
* Optimized columnar storage: Firebolt efficiently scans only the required columns, improving read performance for analytical workloads.

By optimizing schema for Firebolt’s columnar storage, you can reduce query complexity, improve filtering efficiency, and accelerate data retrieval without relying on traditional row-based storage and extensive joins.

#### 3. Convert JSON `SUPER` columns to `TEXT` 

Firebolt improves the handling of JSON data by storing it as `TEXT`, allowing dynamic field extraction without predefined schemas. Firebolt includes specialized JSON functions to extract, convert, and manipulate JSON data stored in `TEXT` columns, enabling flexible and efficient querying without predefined structures. Unlike Redshift’s `SUPER` type, which requires fixed structures and functions like `JSON_EXTRACT_PATH_TEXT`, Firebolt enables flexible querying with [JSON_VALUE]({% link sql_reference/functions-reference/JSON/json-value.md %}), [JSON_EXTRACT]({% link sql_reference/functions-reference/JSON/json-extract.md %}), and [JSON_POINTER_EXTRACT_TEXT]({% link sql_reference/functions-reference/JSON/json-pointer-extract-text.md %}). These functions allow queries to retrieve only the necessary JSON fields, reducing scan time and improving performance.

Firebolt’s approach removes the need for manual schema updates, simplifies query logic, and supports dynamic key lookups without restructuring the data model. Queries are easier to write and maintain because Firebolt avoids the nested function calls required in Redshift. By replacing `SUPER` with `TEXT`, users gain a more efficient and flexible way to query JSON data.

In Redshift, tables may store JSON data using the `SUPER` type as follows:  

```sql
CREATE TABLE events (
    event_id INT PRIMARY KEY,
    event_data SUPER
);
```

When migrating to Firebolt, export the JSON data from Redshift as `TEXT`, for example, by unloading to S3 in JSON or CSV format. Then, define the column in Firebolt as `TEXT` as follows:

```sql
CREATE FACT TABLE events (
    event_id INT,
    event_data TEXT
);
```
The previous code example allows you to load JSON content into Firebolt as plain text and query it using Firebolt’s JSON functions.

**Extracting JSON in Redshift versus Firebolt**

In Redshift, extracting a JSON field requires fixed paths and multiple function calls for nested structures as follows:  

```sql
SELECT JSON_EXTRACT_PATH_TEXT(event_data, 'user_id') AS user_id
FROM events;
```
For nested JSON fields, Redshift queries become more complex as shown in the following code example:

```sql
SELECT JSON_EXTRACT_PATH_TEXT(JSON_EXTRACT_PATH_TEXT(event_data, 'metadata'), 'user_id') AS user_id
FROM events;
```
Firebolt simplifies this by allowing direct field extraction with `JSON_VALUE` as follows:

```sql
SELECT JSON_VALUE(event_data, 'user_id') AS user_id
FROM events;
```

For nested fields, Firebolt uses a single function call as follows:

```sql
SELECT JSON_VALUE(JSON_POINTER_EXTRACT_TEXT(event_data, '/metadata/user/id')) AS user_id
FROM events;
```
JSON pointer expressions are used to navigate JSON documents, enabling precise access to nested elements and arrays by specifying the path to the desired value.

Firebolt also supports dynamic key lookups without predefined paths. The following example shows dynamic path construction with `CONCAT`:

```sql
SELECT JSON_VALUE(JSON_POINTER_EXTRACT_TEXT(event_data, CONCAT('/users/', user_index, '/id'))) AS dynamic_user_id
FROM events;
```
#### 4. Validate schema changes before migration  

Before migrating from Redshift to Firebolt, validate your schema changes to ensure data consistency and optimized query performance. Differences in data types, indexing, and table design require careful verification to avoid mismatches and unexpected results after migration.

The following table shows common Redshift data types and their Firebolt equivalents to help you adjust column definitions during schema migration:

| Redshift type          | Firebolt equivalent  | Notes                                                      |
|------------------------|----------------------|------------------------------------------------------------|
| SMALLINT               | SMALLINT             | Identical.                                                 |
| INTEGER                | INT or INTEGER       | Firebolt uses INT for integer types.                       |
| BIGINT                 | BIGINT               | Identical.                                                 |
| REAL                   | FLOAT4               | Alias mapping for single-precision floats.                 |
| DOUBLE PRECISION       | DOUBLE               | Use DOUBLE for double-precision floats.                    |
| NUMERIC(p, s)          | DECIMAL(p, s)        | Equivalent; Firebolt uses DECIMAL.                         |
| BOOLEAN                | BOOLEAN              | Identical.                                                 |
| CHAR(n) or VARCHAR(n)  | TEXT                 | Firebolt uses TEXT with no length restrictions.            |
| DATE                   | DATE                 | Identical.                                                 |
| TIMESTAMP              | TIMESTAMP            | Firebolt supports TIMESTAMP without time zone.             |
| JSON                   | TEXT                 | JSON is stored as TEXT and queried using JSON functions.   |
| ARRAY                  | ARRAY(TEXT)          | Firebolt arrays require explicit type definitions.         |

**Example schema conversion**  

The following example shows how to convert a Redshift table to a Firebolt dimension table with type adjustments and a primary index:  

In Redshift, the following code example creates a `players` table with columns for `player_id`, `nickname`, registration date, and `score` using specified data types:

```sql
CREATE TABLE players (
    player_id INTEGER,
    nickname VARCHAR(50),
    registered_on DATE,
    score NUMERIC(10, 2)
);
```

In Firebolt, the following code example creates a `players` dimension table with columns for `PlayerID`, `Nickname`, registration date, and `Score`, and defines a primary index on `PlayerID` to optimize filtering and lookups.:

```sql
CREATE DIMENSION TABLE players (
    PlayerID INT,
    Nickname TEXT,
    RegisteredOn DATE,
    Score DECIMAL(10, 2)
) PRIMARY INDEX PlayerID;
```

Although Firebolt’s indexing and denormalization reduce the need for manual tuning, you should still validate that queries and aggregations behave as expected. Data integrity checks help ensure that row counts and aggregated results in Firebolt match those in Redshift. Performance tests verify that indexing strategies deliver the intended improvements.

**Validate row counts and aggregate metrics**  

Run queries in both Redshift and Firebolt to compare row counts and sum totals.  

In Redshift, the following code example counts the total number of rows in the `playstats` table and calculates the sum of the `currentscore` column:

```sql
SELECT COUNT(*) FROM playstats;
SELECT SUM(currentscore) AS total_score FROM playstats;
```

In Firebolt, the following code performs the equivalent check:

```sql
SELECT COUNT(*) FROM playstats;
SELECT SUM(currentscore) AS total_score FROM playstats;
```
Ensure that counts and aggregates are identical between both systems.

**Validate indexing efficiency with EXPLAIN**

Review query plans to identify sequential scans and costly joins. 

The following code example displays the query plan for grouping `playstats` by `gameid` and summing `currentscore` showing how Redshift's database will process the query:

```sql
EXPLAIN 
SELECT gameid, SUM(currentscore)
FROM playstats
GROUP BY gameid;
```

In Firebolt, use [EXPLAIN (ANALYZE)]({% link sql_reference/commands/queries/explain.md %}#example-with-analyze) to view actual data scanned and confirm that indexes are applied. This example runs the same query and returns runtime metrics, showing row counts and processing times for each step:

```sql
EXPLAIN (ANALYZE)
SELECT gameid, SUM(currentscore)
FROM playstats
GROUP BY gameid;
```
The output from the previous code example shows row counts and processing times for each step, confirming that indexes are reducing scanned data.

**Validate consistency using checksums**

Firebolt’s [HASH_AGG]({% link sql_reference/functions-reference/aggregation/hash-agg.md %}) function provides a checksum of table contents to compare against Redshift results.

In Redshift, the following code example generates a checksum value by concatenating all `gameid`, `playerid`, and `currentscore` values from the `playstats` table, aggregating them into a single string, and applying the MD5 hash to verify data consistency:

```sql
SELECT MD5(STRING_AGG(CONCAT(gameid, ',', playerid, ',', currentscore), '')) AS table_checksum
FROM playstats;
```

In Firebolt, use HASH_AGG to generate a checksum across all rows and columns as follows:

```sql
SELECT HASH_AGG(*) AS table_checksum
FROM playstats;
```
Matching checksums confirm that all data has been migrated accurately.

By validating row counts, aggregates, query plans, and checksums before final migration, you ensure that schema changes deliver consistent, reliable, and optimized results in Firebolt.

## Export data from Redshift

Before migrating to Firebolt, export your Redshift data to Amazon S3. Redshift supports efficient parallel unloading of data in various formats such as CSV or Parquet, which Firebolt can load directly.

Follow these steps to export data:

1. Use Redshift’s `UNLOAD` command to export tables or query results to Amazon S3.

    The following code example unloads the sales table data in CSV format to the specified Amazon S3 bucket:
    
    ```sql
    UNLOAD ('SELECT * FROM sales')
    TO 's3://your-redshift-data/sales/'
    CREDENTIALS 'aws_access_key_id=your-access-key;aws_secret_access_key=your-secret-key'
    PARALLEL OFF
    ALLOWOVERWRITE
    DELIMITER ',';
    ```

2. Format data for Firebolt as follows:

    * Ensure that exported data is in CSV or Parquet format.  
    * Include headers in CSV files to simplify mapping during loading.  
    * Use Parquet for efficient compression and faster loading.  
    * Compress CSV files with gzip to reduce storage and speed up transfer.  
    * Use consistent delimiters and avoid special characters that may cause parsing errors.  
    * Validate that exported data types match the expected Firebolt schema.  
    * Disable schema evolution in Parquet exports to avoid mismatches during loading.

3. Organize files in Amazon S3 for parallel loading.

    * Store exported files in Amazon S3 folders using clear prefixes, for example: `s3://your-redshift-data/sales/2024/01/`.  
    * Use multiple small-to-medium sized files of 100 MB to 1 GB each to maximize parallel loading in Firebolt.  
    * Follow consistent naming conventions including table names, export dates, or partitions.  
    * Clean up any incomplete or partial exports to avoid loading invalid data.

## Load data into Firebolt

Firebolt uses `COPY` 
## Translate queries

## Performance testing and optimization

## Automated migration

## Post-migration validation and maintenance

## Best practices