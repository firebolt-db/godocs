---
layout: default
title: Migrate from Redshift 
description: Learn how to migrate your workflow from Redshift
nav_order: 1 
parent: Migrate to Firebolt
has_toc: true
has_children: false
---

# Migrate from Redshift to Firebolt

Migrating from Amazon Redshift to Firebolt unlocks significant improvements in performance, scalability, and cost efficiency for analytics workloads. Firebolt’s modern, decoupled architecture eliminates many of the constraints of Redshift’s monolithic cluster approach, enabling faster query performance, elastic compute scaling, and optimized workload management.

This guide provides a step-by-step approach to migrating from Redshift to Firebolt, covering:

* **Schema transformation** &ndash; Adapting Redshift’s `SORT` and `DIST` keys to Firebolt’s indexing model.
* **Data migration** &ndash; Exporting Redshift data and loading it efficiently into Firebolt.
* **Query adaptation** &ndash; Translating Redshift SQL to Firebolt for improved performance.
* **Performance optimization** &ndash; Using Firebolt’s indexing and compute elasticity to maximize speed.

### Key considerations

Migrating from Redshift to Firebolt is more than just moving data. It requires rethinking how workloads are managed and optimized. Unlike Redshift’s single-cluster model, Firebolt allows for independent compute engines, for workload isolation and cost efficiency. A simple one-to-one migration may not fully use Firebolt’s capabilities, so careful planning is required.

The following sections will guide you through understanding Firebolt’s architecture, selecting the right compute engines, transforming your schema, and optimizing query performance to ensure a seamless and efficient migration.

Topics:
* [Architectural differences](#architectural-differences) &ndash; Firebolt separates compute from storage, enabling independent scaling, workload isolation, and cost efficiency.
* [Schema differences](#schema-differences)
* [Exporting data from Redshift](#exporting-data-from-redshift)
* [Loading data into Firebolt](#loading-data-into-firebolt)
* [Translating queries](#translating-queries)
* [Performance testing and optimization](#performance-testing-and-optimization)
* [Automated migration](#automated-migration)
* [Post-migration validation and maintenance](#post-migration-validation-and-maintenance)
* [Best practices](#best-practices)

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
| [Use separate Firebolt engines for different workloads](#use-separate-firebolt-engines-for-different-workloads) | Prevents resource contention and improves workload isolation. | Assign dedicated engines for ingestion, analytics, and transformations to avoid competition for resources. |
| [Scale compute and storage independently](#scale-compute-and-storage-independently) | Allows flexible resource allocation without overprovisioning. | Increase compute resources for analytics without expanding storage, and scale engines independently based on workload needs. |
| [Pause idle engines to reduce costs](#pause-idle-engines-to-reduce-costs) | Lowers operational costs while keeping data accessible. | Use auto-stop settings to pause unused engines and restart them on demand. |
| [Optimize queries with indexing](#optimize-queries-with-indexing) | Speeds up query processing and reduces scan times. | Use primary indexes for efficient filtering and aggregating indexes for precomputed aggregations. |
 

##### Use separate Firebolt engines for different workloads

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
##### Scale compute and storage independently

Firebolt allows scaling compute without affecting storage, unlike Redshift, where storage grows with compute. You can allocate more compute resources for analytics while keeping storage unchanged. Use smaller engines for intermittent workloads.

The following code example shows how to scale an engine for high-currency analytics:
```sql
ALTER ENGINE "analytics_engine" SET NODES = 10;
```
##### Pause idle engines to reduce costs

Firebolt engines consume credits only when engines are running, so pausing unused engines can significantly reduce costs. In Redshift, charges are based on cluster uptime, even if it is idle. In Firebolt, you can pause an engine without losing access to stored data.

The following code example creates an engine that automatically pauses after 30 minutes of inactivity:

```sql
CREATE ENGINE "adaptive_engine" WITH
TYPE = "L"
AUTO_STOP = 30
AUTO_START = TRUE;
```

##### Optimize queries with indexing

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
| [Replace SORTKEY and DISTKEY with indexes](#replace-sortkey-and-distkey-with-indexes) | Reduces manual optimization, improves query efficiency | Use primary, aggregating, and join indexes instead of `SORTKEY` and `DISTKEY`. |
| [Optimize schema for columnar storage](#optimize-schema-for-columnar-storage)  | Improves data pruning, query performance, and reduces joins | Use fact tables for large datasets, primary indexes for filtering, aggregating indexes for precomputed calculations, and denormalize frequently joined tables. |
| [Convert JSON SUPER columns to `TEXT`](#convert-json-super-columns-to-text)    | Enables flexible querying of semi-structured data | Store JSON as `TEXT`, extract values with `JSON_VALUE` and `JSON_EXTRACT`. |
| [Validate schema changes before migration](#validate-schema-changes-before-migration) | Ensures data consistency and query optimization   | Compare row counts, query execution times, and indexing efficiency between Redshift and Firebolt. |


#### Replace `SORTKEY` and `DISTKEY` with indexes

Amazon Redshift relies on `SORTKEY` and `DISTKEY` to optimize data distribution and query performance. `SORTKEY` determines the order in which data is physically stored, improving range queries and filtering, while `DISTKEY` controls how data is distributed across cluster nodes to balance query performance. These keys require manual selection and tuning based on query patterns, making performance optimization a complex and ongoing task.

One major limitation of Redshift’s approach is that scaling a cluster involves redistributing data across nodes, which can lead to performance degradation and downtime. When the cluster size changes, Redshift must redistribute data based on the defined `DISTKEY`, potentially causing imbalanced workloads and requiring manual re-optimization of data distribution.

Firebolt eliminates the need for manual data distribution and sorting by using indexes to optimize query execution automatically. [Primary indexes]({% link Overview/indexes/primary-index.md %}) improve scan efficiency by physically storing data in an ordered structure, [aggregating indexes]({% link Overview/indexes/aggregating-index.md %}) precompute results at ingestion time for faster aggregations, and join indexes optimize joins between large tables. Firebolt’s indexing strategy ensures faster query performance with minimal manual tuning, reducing the need for manual `VACUUM` and `ANALYZE` operations required in Redshift to maintain query efficiency.

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

#### Optimize schema for columnar storage

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

#### Convert JSON `SUPER` columns to `TEXT`

#### Validate schema changes before migration

## Exporting data from Redshift

## Loading data into Firebolt

## Translating queries

## Performance testing and optimization

## Automated migration

## Post-migration validation and maintenance

## Best practices