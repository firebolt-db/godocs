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

The following sections will guide you through an overview of Firebolt's architecture and schema differences, which will help you optimize performance, scalability, and cost efficiency by leveraging Firebolt’s engine-based architecture, workload isolation, indexing, and flexible schema design. Then, The following sections will also cover the steps for exporting data from Redshift, loading it into Firebolt, translating queries, optimizing performance, automating the migration process, and validating and maintaining data after migration to ensure a smooth and efficient transition.

Overview:
* [Architectural differences](#overview-architectural-differences) &ndash; An overview of how to adapt your Redshift workflow to Firebolt’s decoupled compute-storage model, which provides elastic scaling, workload isolation, and advanced indexing.
* [Schema differences](#overview-schema-differences) &ndash; An overview of how to adapt your schema from Redshift’s `SORT` and `DIST` keys to Firebolt’s dynamic indexing, denormalization, and flexible JSON handling, which replace manual distribution keys and rigid schemas for faster, simpler queries.

Steps:
* [Export data from Redshift](#export-data-from-redshift) &ndash; Learn how to efficiently export your Redshift data to Amazon S3 in CSV or Parquet format, format it for Firebolt, and organize it for optimal parallel loading.
* [Load data into Firebolt](#load-data-into-firebolt) &ndash; 
* [Translate queries](#translate-queries)
* [Performance testing and optimization](#performance-testing-and-optimization)
* [Automated migration](#automated-migration)
* [Post-migration validation and maintenance](#post-migration-validation-and-maintenance)


## Overview: architectural differences

Migrating from Amazon Redshift to Firebolt requires adapting to a different architecture. Redshift’s monolithic cluster model, where compute and storage are tightly integrated, limits flexibility and forces full-cluster scaling. In contrast, Firebolt separates compute engines from storage, enabling elastic scaling, workload isolation, and advanced indexing for faster performance, as summarized in the following table:

| **Feature**               | **Redshift**                                        | **Firebolt**                                          | **Impact on Data Modeling** |
|---------------------------|-----------------------------------------------------|------------------------------------------------------|-----------------------------|
| **Architecture**          | Monolithic cluster, compute-storage tightly coupled. | Virtualized engines, compute-storage decoupled. | Distribute workloads across multiple engines instead of a single cluster. |
| **Scalability and Elasticity** | Resizing requires downtime, limited concurrency scaling. | Highly elastic, auto-scaling, independent compute and storage. | Assign separate engines for ingestion, analytics, and ETL to optimize resources. |
| **Workload Isolation**    | Shared cluster, resource contention. | Multiple engines, fully isolated workloads. | Use dedicated engines to prevent query interference. |
| **Data Storage**          | Requires manual tuning of `SORT` and `DIST` keys. | Index-based optimization using primary and aggregating indexes. | Replace `SORT` and `DIST` keys with indexing for faster queries. |
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

## Overview: schema differences

Migrating from Amazon Redshift to Firebolt requires adapting your schema to leverage Firebolt’s indexing model, denormalization benefits, and optimized query execution. Unlike Redshift, which relies on `SORT` and `DIST` keys for performance tuning, Firebolt automatically optimizes queries using primary, and aggregating indexes. This eliminates the need for manual data distribution and sorting, reducing complexity while improving performance.  

Additionally, semi-structured data handling differs. Redshift’s `SUPER` type allows nested JSON storage, while Firebolt stores JSON as `TEXT`, enabling flexible querying with JSON functions like `JSON_VALUE` and `JSON_EXTRACT`. Firebolt’s schema design also favors denormalization, reducing the need for complex joins and improving analytical query speed.  

The following table outlines key schema differences between Redshift and Firebolt, highlighting the mechanisms Firebolt uses to optimize data modeling and query performance:


| **Schema feature**           | Redshift                                         | Firebolt                                        | Key mechanism and explanation |
|-----------------------------|-------------------------------------------------|-----------------------------------------------|-----------------------------------|
| **Column data types**        | Supports a broad range, including `SUPER` for semi-structured data. | Uses similar types but stores JSON as `TEXT` with functions for querying. | Firebolt requires converting JSON data to `TEXT` and using JSON functions `JSON_VALUE`, `JSON_EXTRACT_TEXT` to query nested fields. |
| **Data distribution, sorting, and indexing** | Uses `SORTKEY` and `DISTKEY` for query performance tuning, requiring manual optimization. | Uses primary and aggregating indexes instead. | Firebolt eliminates manual tuning by using indexes to optimize queries and automatically scan relevant data. |
| **Schema design approach**   | Often normalized to improve joins and reduce redundancy. | Encourages denormalization for faster performance. | Firebolt's indexing structure allows fewer joins, improving query speed and reducing complexity. |
| **Semi-structured data (JSON)** | Supports `SUPER` type for nested JSON storage. | Stores JSON as `TEXT`, with JSON parsing functions. | Firebolt enables dynamic JSON parsing instead of requiring pre-defined structures. |
| **Fact and dimension table design** | Requires explicit distribution styles for performance tuning. | Uses fact and dimension tables with indexing for optimized access. | Firebolt’s fact and dimension tables are designed to work with indexes, ensuring fast analytical queries. |

The following sections explain key schema differences and best practices for adapting your Redshift schema to Firebolt.

#### Best practices for migrating schema

| **Best practices for migrating schema** | **Impact**                                          | **How to implement**  |
|--------------------------------------|--------------------------------------------------|----------------------|
| [1. Replace SORTKEY and DISTKEY with indexes](#replace-sortkey-and-distkey-with-indexes) | Reduces manual optimization, improves query efficiency | Use primary and aggregating indexes instead of `SORTKEY` and `DISTKEY`. |
| [2. Optimize schema for columnar storage](#optimize-schema-for-columnar-storage)  | Improves data pruning, query performance, and reduces joins | Use fact tables for large datasets, primary indexes for filtering, aggregating indexes for precomputed calculations, and denormalize frequently joined tables. |
| [3. Convert JSON SUPER columns to TEXT](#convert-json-super-columns-to-text)    | Enables flexible querying of semi-structured data | Store JSON as `TEXT`, extract values with `JSON_VALUE` and `JSON_EXTRACT`. |
| [4. Validate schema changes before migration](#validate-schema-changes-before-migration) | Ensures data consistency and query optimization   | Compare row counts, query execution times, and indexing efficiency between Redshift and Firebolt. |


#### 1. Replace `SORTKEY` and `DISTKEY` with indexes

Amazon Redshift relies on `SORTKEY` and `DISTKEY` to optimize data distribution and query performance. `SORTKEY` determines the order in which data is physically stored, improving range queries and filtering, while `DISTKEY` controls how data is distributed across cluster nodes to balance query performance. These keys require manual selection and tuning based on query patterns, making performance optimization a complex and ongoing task. Additionally, these keys must be set at table creation and cannot be changed without recreating the table and reloading data, making schema adjustments rigid and time-consuming.

In Redshift, data is partitioned across nodes based on the `DISTKEY`. Selecting a poor distribution key can lead to data skew, where some nodes store significantly more data than others, causing uneven workloads and performance bottlenecks.

One major limitation of Redshift’s approach is that scaling a cluster involves redistributing data across nodes, which can lead to performance degradation and downtime. When the cluster size changes, Redshift must redistribute data based on the defined `DISTKEY`, potentially causing imbalanced workloads and requiring manual re-optimization of data distribution.

Firebolt eliminates the need for manual data distribution and sorting by using indexes to optimize query processing automatically. Unlike Redshift’s fixed distribution and sorting keys, Firebolt’s indexes can be dynamically modified based on changing workloads or replaced without reloading data. [Primary indexes]({% link Overview/indexes/primary-index.md %}) improve scan efficiency by physically storing data in an ordered structure, and [aggregating indexes]({% link Overview/indexes/aggregating-index.md %}) precompute results during loading time for faster aggregations. 

Firebolt’s indexing strategy, combined with tablet-based storage, ensures faster query performance with minimal manual tuning, reducing the need for manual `VACUUM` and `ANALYZE` operations required in Redshift to maintain query efficiency. Firebolt’s decoupled architecture makes node-level data distribution unnecessary. Indexes enable the engine to dynamically access only the relevant data. Understanding how indexes and tablet-based storage replace distribution and sort keys is critical. Firebolt stores data in tablets and uses indexing to prune unnecessary data, allowing faster queries without manual tuning.

To migrate Redshift keys to Firebolt indexes, do the following:
* Use a primary index instead of a `SORTKEY` to efficiently filter and scan only relevant data during query runtime.
* Replace `DISTKEY` with an aggregating index when optimizing aggregations, avoiding the need for manual data distribution.

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

The following code example shows the Firebolt equivalent schema using primary and aggregating indexes:
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
```

In the previous code example, the following apply:
* `DISTKEY(customer_id)` is replaced with the aggregating index `(customer_id, SUM(total_amount))`. This aggregation runs faster than Redshift because `SUM(total_amount)` is precomputed in the aggregating index.
* `SORTKEY(sale_date)` is replaced with the primary index `(sale_date)`.


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
* Use dimension tables for reference data.
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

## Steps to migrate from Redshift to Firebolt

* [Export data from Redshift](#export-data-from-redshift)
* [Load data into Firebolt](#load-data-into-firebolt)
* [Translate queries into Firebolt](#translate-queries)
* [Performance testing and optimization](#performance-testing-and-optimization)
* [Automated migration](#automated-migration)
* [Post-migration validation and maintenance](#post-migration-validation-and-maintenance)

### Export data from Redshift

Before migrating to Firebolt, export your Redshift data to Amazon S3. Redshift supports efficient parallel unloading of data in various formats such as CSV or Parquet, which Firebolt can load directly.

Follow these steps to export data:

1. Use Redshift’s `UNLOAD` command to export tables or query results to Amazon S3.

    The following code example unloads the `sales` table data in CSV format to the specified Amazon S3 bucket:
    
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
    * Include headers in CSV files for clarity during loading.  
    * Use Parquet with Snappy compression for faster loading.  
    * Compress CSV files with gzip compression to reduce storage and speed up transfer.  
    * Use consistent delimiters and avoid special characters that may cause parsing errors.  
    * Validate that exported data types match the expected Firebolt schema.  


3. Organize files in Amazon S3 for parallel loading.

    * Store exported files in Amazon S3 folders using clear prefixes, for example: `s3://your-redshift-data/sales/2024/01/`.  
    * Use multiple small-to-medium sized files of 100 MB to 1 GB each to maximize parallel loading in Firebolt.  
    * Follow consistent naming conventions including table names, export dates, or partitions.  
    * Clean up any incomplete or partial exports to avoid loading invalid data.

## Load data into Firebolt

Firebolt loads data directly from AWS S3 using the [COPY FROM]({% link sql_reference/commands/data-management/copy-from.md %}) command, supporting parallel ingestion, automatic schema discovery, metadata handling, and error management. It works with both CSV and Parquet formats, with Parquet recommended for efficient compression.

The following code example loads data from Parquet files stored in an S3 bucket into the `tournaments` table in Firebolt, mapping specific columns from the file to the table's fields and including metadata such as the source file name and timestamp:

```sql
COPY INTO tournaments (
  tournamentid $1, 
  name $2, 
  gameid $3, 
  totalprizedollars $4, 
  startdatetime $5, 
  enddatetime $6, 
  rulesdefinition $7, 
  source_file_name $SOURCE_FILE_NAME, 
  source_file_timestamp $SOURCE_FILE_TIMESTAMP)
FROM 's3://firebolt-sample-datasets-public-us-east-1/gaming/parquet/tournaments/' 
WITH PATTERN = '*' 
TYPE = PARQUET;
```
For more information, see [Load data]({% link Guides/loading-data/loading-data.md %}).

## Translate queries into Firebolt

Migrating queries from Redshift to Firebolt requires more than just adjusting syntax; it involves utilizing Firebolt's advanced query optimization features to enhance performance. While the SQL syntax in both platforms is largely similar, Firebolt's powerful indexing, advanced functions, and query execution insights require careful adaptation of Redshift queries.

This section is divided into the following:

* [Window functions](#translate-window-functions-into-firebolt) &ndash; Learn how to translate window functions from Redshift to Firebolt and optimize them using Firebolt's indexing features for improved performance.
* [Aggregation queries](#translate-aggregation-queries-into-firebolt) &ndash; Discover how to handle aggregation queries, leveraging Firebolt’s aggregating indexes to precompute results and significantly speed up query performance.
* [Handle JSON data](#handle-json-data-in-firebolt) &ndash; Understand how to work with JSON in Firebolt using its specialized functions, providing more flexibility and efficiency compared to Redshift's approach.
* [Query plan insights](#firebolts-query-plan-insights) &ndash; Gain insights into query plans and how Firebolt's [EXPLAIN (ANALYZE)]({% link sql_reference/commands/queries/explain.md %}#example-with-analyze) command helps optimize queries through runtime metrics for optimal performance.

### Translate window functions into Firebolt

Window functions in Firebolt are compatible with standard SQL, allowing users to compute values across a set of rows related to the current row. Both Redshift and Firebolt support common window functions like `ROW_NUMBER`, `RANK`, and `SUM` with the `OVER` clause, but Firebolt can enhance performance through indexing, particularly primary indexes, which minimize the data that needs to be processed.

The following example shows how to calculate a running total of player scores by game in both Redshift and Firebolt, using the `SUM` window function.

In Redshift, the query to calculate the running total of the `currentscore` for each `playerid` within each `gamid` ordered by `playerid`, using a window function:

```sql
SELECT gameid, playerid, 
SUM(currentscore) OVER (PARTITION BY gameid ORDER BY playerid) 
AS running_total 
FROM PlayStats;
```

The same query can be run in Firebolt with no changes, as Firebolt supports standard SQL window functions. However, to optimize performance, use Firebolt’s primary indexes to reduce the number of rows that need to be scanned before applying the window function.

The following code example creates a `PlayStats` table in Firebolt with columns for `gameid`, `playerid`, and `currentscore`. It defines a primary index on `gameid` and `playerid` to optimize query performance, such as the running total calculation, by efficiently retrieving the relevant rows based on these columns:

```sql
CREATE FACT TABLE PlayStats (
  gameid INT,
  playerid INT,
  currentscore BIGINT
) 
PRIMARY INDEX (gameid, playerid);
```
### Translate aggregation queries into Firebolt

Aggregation queries in Firebolt are similar to those in Redshift, but Firebolt offers better performance, especially for large datasets, by utilizing aggregating indexes. Both platforms support common aggregation functions like `SUM`, `COUNT`, and `AVG`, and the `GROUP BY` clause. Firebolt, however, enhances performance by precomputing and storing aggregated results through aggregating indexes, which reduce the need for runtime calculations.

The following example shows how to calculate the total playtime by game in both Redshift and Firebolt using the `SUM` aggregation function.

In Redshift, the following code calculates the total `currentplaytime` for each `gameid` in the `PlayStats` table by grouping the data by `gameid` and summing the `currentplaytime` for each group:

```sql
SELECT gameid, SUM(currentplaytime) 
AS total_playtime 
FROM PlayStats 
GROUP BY gameid;
```

The same query can be run in Firebolt with no changes, as Firebolt supports standard SQL aggregation functions. To optimize performance, create an aggregating index in Firebolt that precomputes the total playtime for each `gameid`, avoiding runtime aggregation.

The following code example creates an aggregating index on the `PlayStats` table, precomputing the sum of `currentplaytime` for each `gameid`, which optimizes query performance by storing the aggregated results for faster retrieval:

```sql
CREATE AGGREGATING INDEX playtime_agg_idx 
ON PlayStats (
  gameid,
  SUM(currentplaytime)
);
```
With this aggregating index, Firebolt retrieves precomputed results instead of performing the aggregation during query execution, significantly reducing query time.

### Handle JSON data in Firebolt

Firebolt provides a flexible and efficient way to handle JSON data, offering specialized functions to extract, convert, and manipulate JSON stored in `TEXT` columns. Unlike Redshift’s `SUPER` data type, which requires predefined structures, Firebolt allows users to work with raw JSON data directly, offering significant advantages in both performance and flexibility.

Firebolt’s JSON functions are divided into three main categories:

* Extract functions &ndash; Used to retrieve specific parts of a JSON document.
* Convert functions &ndash; Used to convert JSON data into SQL-compatible types like `TEXT` or `ARRAY`.
* Hybrid functions &ndash; Combine extraction and conversion in one step, especially useful for nested JSON elements.

Additionally, Firebolt handles escaped characters using specialized functions.

**Extract functions**

Extract functions in Firebolt are designed to extract specific parts of a JSON document while preserving the original data format. Commonly used extract functions include the following:

* [JSON_EXTRACT]({% link sql_reference/functions-reference/JSON/json-extract.md %}) &ndash; Extracts a part of the JSON data as raw JSON.
* [JSON_POINTER_EXTRACT_VALUES]({% link sql_reference/functions-reference/JSON/json-pointer-extract-values.md %}) &ndash; Extracts values from a JSON document using a pointer to the desired location.

```sql
SELECT JSON_EXTRACT(event_data, '$.user_id') AS user_id
FROM events;
```

**Convert functions**

Convert functions are used to convert JSON values into SQL-compatible types, such as `TEXT` or `ARRAY`. Key convert functions include the following:

* [JSON_VALUE]({% link sql_reference/functions-reference/JSON/json-value.md %}) &ndash; Extracts a JSON value and converts it to a SQL-compatible format like TEXT.
* [JSON_VALUE_ARRAY]({% link sql_reference/functions-reference/JSON/json-value-array.md %}) &ndash; Converts a JSON array into an array of SQL-compatible values.
* [JSON_POINTER_EXTRACT_KEYS]({% link sql_reference/functions-reference/JSON/json-pointer-extract-keys.md %}) &ndash; Extracts keys from a JSON document.

```sql
SELECT JSON_VALUE(event_data, 'user_id') AS user_id
FROM events;
```

**Hybrid functions**

Hybrid functions, like [JSON_POINTER_EXTRACT_TEXT]({% link sql_reference/functions-reference/JSON/json-pointer-extract-text.md %}), combine both extraction and conversion, allowing access to nested JSON values. Hybrid functions in Firebolt combine extraction and conversion in a single operation. 

The following code example extracts the raw JSON value of the `id` key from the nested metadata object in the `event_data` JSON column of the `events` table and returns it as `user_id`:

```sql
SELECT JSON_POINTER_EXTRACT_TEXT(event_data, '/metadata/user/id') AS user_id
FROM events;
```

You can also use `JSON_POINTER_EXTRACT_TEXT` to extract values from nested JSON objects using JSON pointer expressions as follows. The following code example extracts the value of the `id` key from the nested metadata object in the `event_data` JSON column of the events table and returns it as `user_id`:

```sql
SELECT JSON_VALUE(JSON_POINTER_EXTRACT_TEXT(event_data, '/metadata/user/id')) AS user_id
FROM events;
```

When dealing with JSON keys that contain special characters such as tilde ~ or forward slash /, Firebolt uses the standard JSON Pointer specification for escaping characters:

~0 represents the tilde (~).
~1 represents the forward slash (/).

The following code example extracts values from the `event_data` JSON column in the `events` table, accessing keys with the tilde and slash special characters by using escape sequences and returning them as `key_with_tilde` and `key_with_slash`:

```sql
SELECT JSON_VALUE(JSON_POINTER_EXTRACT_TEXT(event_data, '/key~0with~0tilde')) AS key_with_tilde,
       JSON_VALUE(JSON_POINTER_EXTRACT_TEXT(event_data, '/key~1with~1slash')) AS key_with_slash
FROM events;
```

### Firebolt's query plan insights

Firebolt provides advanced query plan insights that help optimize query performance. Unlike Redshift, which relies on static query plans, Firebolt offers dynamic plans with real-time runtime metrics when using the [EXPLAIN (ANALYZE)]({% link sql_reference/commands/queries/explain.md %}#example-with-analyze) command. This allows for deeper insights into how queries are run and where performance improvements can be made.

In Redshift, the `EXPLAIN` command provides a static query plan, showing the sequence of operations, estimated costs, and resource allocation. This plan lacks runtime performance metrics and detailed insights into data movement across nodes.

In Redshift, the following code example analyzes a join query:

```sql
EXPLAIN 
SELECT eventid, eventname, event.venueid, venuename
FROM event
JOIN venue ON event.venueid = venue.venueid;
```

The output from running the previous code example in Redshift highlights the sequence of operations and the relative cost estimates of the query:

``` script
XN Hash Join DS_DIST_OUTER  (cost=2.52..58653620.93 rows=8712 width=43)
Hash Cond: ("outer".venueid = "inner".venueid)
->  XN Seq Scan on event  (cost=0.00..87.98 rows=8798 width=23)
->  XN Hash  (cost=2.02..2.02 rows=202 width=22)
->  XN Seq Scan on venue  (cost=0.00..2.02 rows=202 width=22)
```

In Firebolt, the [EXPLAIN]({% link sql_reference/commands/queries/explain.md %}) command provides two key plans:
* The **logical plan** outlines the structure of the query, including projections, filters, and joins.
* The **physical plan** reveals how these operations are distributed across nodes, with details on data shuffling and execution strategies. 

When paired with the [ANALYZE]({% link sql_reference/commands/queries/explain.md %}#example-with-analyze) option, Firebolt’s `EXPLAIN` command adds runtime metrics, such as CPU time, thread time, rows processed, and runtime for each operation, allowing for detailed performance analysis.

In Firebolt, the following code example analyzes the same query and provides runtime metrics:

```sql
EXPLAIN (ANALYZE)
SELECT eventid, eventname, event.venueid, venuename
FROM event
JOIN venue ON event.venueid = venue.venueid;
```

The output from running the previous code example in Firebolt shows output cardinality, thread time, and CPU time for each step:
```script
[0] [Projection] event.eventid, event.eventname, event.venueid, venue.venuename
 |   [Execution Metrics]: output cardinality = 10000, thread time = 3ms, cpu time = 2ms
 \_[1] [HashJoin] event.venueid = venue.venueid
    |   [Execution Metrics]: output cardinality = 10000, thread time = 10ms, cpu time = 8ms
    \_[2] [StoredTable] event
    |   [Execution Metrics]: output cardinality = 5000, thread time = 5ms, cpu time = 4ms
    \_[3] [StoredTable] venue
        [Execution Metrics]: output cardinality = 5000, thread time = 5ms, cpu time = 4ms
```

## Validation, performance testing, and engine optimization

Validation and performance testing are critical steps when migrating from Redshift to Firebolt. **Validating data consistency** ensures the accuracy of the data after migration before optimizing for performance. Once data consistency is validated, **performance testing** helps identify bottlenecks, resource inefficiencies, and areas for improvement. Lastly, check performance using different engine setups to identify the most suitable configuration for your workloads to ensure that Firebolt meets or exceeds the performance of your Redshift setup.

### Validate data consistency

Before focusing on performance optimization, check that the data in Firebolt matches the data in Redshift. Compare data, checksums, and test edge cases to avoid discrepancies and data corruption during migration.

**Data comparison** &ndash; Compare row counts, aggregates, and query results between Redshift and Firebolt to ensure consistency. This includes checking for missing or extra records and validating that the sum or average values match.

The following code example checks the number of rows in the `playstats` table in both Redshift and Firebolt:

```sql
SELECT COUNT(*) FROM playstats;
```

The following code example checks the aggregate sum in both Redshift and Firebolt:

```sql
SELECT SUM(currentscore) AS total_score FROM playstats;
```

The following code example compares specific fields using `GROUP BY` in both Redshift and Firebolt:

```sql
SELECT gameid, playerid, SUM(currentscore) AS total_score 
FROM playstats
GROUP BY gameid, playerid;
```

**Checksum validation** &ndash; Use checksums to compare the integrity of data between Redshift and Firebolt. This method aggregates values and applies an MD5 hash to ensure the data is identical across both systems.

The following code example checks a hash value of all columns in Redhisft:

```sql
SELECT MD5(STRING_AGG(CONCAT(gameid, ',', playerid, ',', currentscore), '')) AS table_checksum
FROM playstats;
```

The following code example checks the equivalent has value in Firebolt:

```sql
SELECT HASH_AGG(*) AS table_checksum
FROM playstats;
```

**Edge case testing** &ndash; Test how Firebolt handles edge cases like `NULL` values, large datasets, and complex joins. This ensures that data migration doesn’t introduce errors in rare or complex scenarios.

The following code example complex joins from multiple tables in Redshift and Firebolt:

```sql
SELECT e.eventid, e.eventname, v.venuename
FROM event e
JOIN venue v ON e.venueid = v.venueid;
```

The following code example checks how `NULL` values are handled in both Redshift and Firebolt:

```sql
SELECT COUNT(*) FROM playstats WHERE currentscore IS NULL;
```

The following code example checks data types in Redshift for text and integer columns:

```sql
SELECT DISTINCT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'playstats';
```

The following code example checks data types in Firebolt:

```sql
DESCRIBE playstats;
```

### Performance testing

Once data consistency is confirmed, check query runtimes, resource utilization, and scalability to ensure optimal query performance:

**Query runtime and resource utilization** &ndash; Measure both the time it takes for queries to run and how much CPU, memory, and disk are consumed during query runtime to help identify performance bottlenecks and optimize resource usage. Test the runtime time for common queries, as well as more complex queries involving joins and aggregations.

The following code example measures the estimated runtime, memory size used, CPU utilization, and query queue time for a simple query in Redshift:

```sql
EXPLAIN
SELECT gameid, SUM(currentplaytime) AS total_playtime
FROM playstats
GROUP BY gameid;

-- Monitor resource usage during query execution
SELECT pid, user_name, start_time, query, db, state, 
       total_queue_time, total_exec_time, memory_size
FROM stv_recents
WHERE query = (SELECT max(query) FROM stv_recents);
```

The following code example measures the actual runtime, CPU time, thread time, and data processed for each operator in the same query in Firebolt:

```sql
EXPLAIN (ANALYZE)
SELECT gameid, SUM(currentplaytime) AS total_playtime
FROM playstats
GROUP BY gameid;
```

**Scalability** &ndash; Test how Firebolt handles larger datasets or higher concurrency. This includes simulating higher data volumes or increased user loads to test how well Firebolt scales under pressure.

The dataset used in this section duplicate rows to simulate large datasets to observe the impact on performance. Change the code to better emulate your actual workloads.

The following code uses `UNION ALL` to increase the size of the `playstats` table in Redshift and measures the runtime and resource usage:

```sql
EXPLAIN
SELECT gameid, SUM(currentplaytime) AS total_playtime
FROM (
    SELECT * FROM playstats
    UNION ALL
    SELECT * FROM playstats  -- Duplicate the rows to simulate a larger dataset
) AS playstats
GROUP BY gameid;
```

The following code example uses the same approach to duplicate the dataset and measures the runtime and resource utilization in Firebolt:

```sql
EXPLAIN (ANALYZE)
SELECT gameid, SUM(currentplaytime) AS total_playtime
FROM (
    SELECT * FROM playstats
    UNION ALL
    SELECT * FROM playstats  -- Duplicate the rows to simulate a larger dataset
) AS playstats
GROUP BY gameid;
```

### Engine optimization

Check how queries perform with different engine configurations to help identify the optimal engine size for your workload and ensure that Firebolt is scaled correctly for your needs. 

In Redshift, engine configurations are set at the cluster level rather than for individual queries, so changing the engine configuration requires resizing the cluster. You can benchmark queries after resizing your cluster to identify the best configuration for your workload. Use `EXPLAIN` and `STV_RECENTS` to evaluate query performance and resource consumption.

The following code example measures query runtime, resource usage, and queue time. Rerun it using different cluster sizes:

```sql
EXPLAIN
SELECT gameid, SUM(currentplaytime) AS total_playtime
FROM playstats
GROUP BY gameid;
```

In Firebolt, you can easily test different engine sizes for your queries by creating engines with varying configurations and compare the query performance.

The following code example creates a small and large engine, and then specifies which engine runs the same query to measure performance in Firebolt:

```sql
-- Create a small engine
CREATE ENGINE "small_engine" WITH
TYPE = "S"
NODES = 2;

-- Create a large engine
CREATE ENGINE "large_engine" WITH
TYPE = "L"
NODES = 8;

-- Activate the small engine for running the query
SELECT * FROM system_engines WHERE engine_name = 'small_engine';

EXPLAIN (ANALYZE)
SELECT gameid, SUM(currentplaytime) AS total_playtime
FROM playstats
GROUP BY gameid;

-- To run on the large engine, activate that engine and then run the query
SELECT * FROM system_engines WHERE engine_name = 'large_engine';

EXPLAIN (ANALYZE)
SELECT gameid, SUM(currentplaytime) AS total_playtime
FROM playstats
GROUP BY gameid;
```

## Automate migration

Automating the migration process from Redshift to Firebolt can streamline the transition, reduce manual effort, and ensure consistency. By leveraging modern data engineering tools like [dbt](https://www.getdbt.com/) (Data Build Tool) and [Apache Airflow](https://airflow.apache.org/), you can automate the critical steps of data extraction, schema conversion, query translation, and performance optimization.

### Automate data migration with Airflow

You can automate the data migration process from Redshift to Firebolt using Apache Airflow, which helps you create workflows to export data from Redshift, store it in S3, and load it into Firebolt.

Use Airflow to run Redshift's `UNLOAD` command on a scheduled basis to export data from Redshift tables to Amazon S3 as follows:

```python
unload_data = PostgresOperator(
    task_id='unload_data_from_redshift',
    sql="UNLOAD ('SELECT * FROM your_table') TO 's3://your-bucket/your_table/' CREDENTIALS 'aws_access_key_id={{ var.value.aws_access_key }};aws_secret_access_key={{ var.value.aws_secret_key }}' PARALLEL OFF DELIMITER ',';",
    postgres_conn_id='redshift_connection',
    dag=dag
)
```
Once the data is in Amazon S3, use another Airflow task to run Firebolt’s [COPY FROM]({% link sql_reference/commands/data-management/copy-from.md %}) command to load the data into your Firebolt tables as follows:

```python
load_data_to_firebolt = FireboltOperator(
    task_id='load_data_into_firebolt',
    sql="COPY INTO your_table FROM 's3://your-bucket/your_table/' TYPE = PARQUET;",
    firebolt_conn_id='firebolt_connection',
    dag=dag
)
```

After migrating the schema and data, test the performance of different Firebolt engine configurations to ensure optimal query performance. Use Airflow to automate performance testing by running queries across various engine sizes and comparing the results to help you identify the best engine size for your workload.

The following code example runs a query 
```python
performance_test = FireboltOperator(
    task_id='performance_testing',
    sql="EXPLAIN (ANALYZE) SELECT gameid, SUM(currentplaytime) FROM playstats GROUP BY gameid;",
    firebolt_conn_id='firebolt_connection',
    dag=dag
)
```

You can also orchestrate your entire migration pipeline using a DAG (Directed Acyclic Graph) that includes tasks for exporting data, loading it into Firebolt, transforming the schema, and testing performance.

The following code example uses a DAG to automate migrating data, transforming schema and testing performance using Airflow:

```python
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.firebolt_operator import FireboltOperator
from airflow.operators.python_operator import PythonOperator

dag = DAG('redshift_to_firebolt_migration', default_args=default_args, schedule_interval='@daily')

unload_task = PostgresOperator(
    task_id='unload_data_from_redshift',
    sql="UNLOAD ('SELECT * FROM your_table') TO 's3://your-bucket/your_table/' CREDENTIALS 'aws_access_key_id={{ var.value.aws_access_key }};aws_secret_access_key={{ var.value.aws_secret_key }}' PARALLEL OFF DELIMITER ',';",
    postgres_conn_id='redshift_connection',
    dag=dag
)

load_task = FireboltOperator(
    task_id='load_data_to_firebolt',
    sql="COPY INTO your_table FROM 's3://your-bucket/your_table/' TYPE = PARQUET;",
    firebolt_conn_id='firebolt_connection',
    dag=dag
)

dbt_task = PythonOperator(
    task_id='run_dbt_for_schema_conversion',
    python_callable=run_dbt_model,
    dag=dag
)

performance_test = FireboltOperator(
    task_id='performance_testing',
    sql="EXPLAIN (ANALYZE) SELECT gameid, SUM(currentplaytime) FROM playstats GROUP BY gameid;",
    firebolt_conn_id='firebolt_connection',
    dag=dag
)

unload_task >> load_task >> dbt_task >> performance_test
```

For more information, see Firebolt's guide to [Connecting to Airflow]({% link Guides/integrations/airflow.md %}).

### Automate data migration with dbt

You can use dbt to automate the generation of Firebolt schemas and adjust Redshift queries for Firebolt's indexing features. Use dbt to convert Redshift’s `SORTKEY` and `DISTKEY` into Firebolt’s primary and aggregating indexes. Create dbt models to define Firebolt-compatible schemas and apply them automatically.

The following code example uses dbt to create a Firebolt schema:

```sql
-- Redshift to Firebolt schema conversion
CREATE FACT TABLE playstats (
  gameid INT,
  playerid INT,
  currentscore BIGINT
)
PRIMARY INDEX (gameid, playerid);
```

Use dbt to replace Redshift-specific functions with Firebolt equivalents, like converting `SUPER` to `TEXT` for JSON handling as follows:

```sql
-- Redshift JSON function converted to Firebolt
SELECT JSON_VALUE(event_data, 'user_id') AS user_id
FROM events;
```

For more information, see Firebolt's documentation to integrate with [dbt]({% link Guides/integrations/connecting-with-dbt.md %}).

## Post-migration validation and maintenance
