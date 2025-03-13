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

- [Use separate Firebolt engines for different workloads](#use-separate-firebolt-engines-for-different-workloads)  
- [Scale compute and storage independently](#scale-compute-and-storage-independently)  
- [Pause idle engines to reduce costs](#pause-idle-engines-to-reduce-costs)  
- [Optimize queries with indexing](#optimize-queries-with-indexing)  

##### Use separate Firebolt engines for different workloads

Unlike Redshift, where all queries run in a shared cluster, Firebolt enables workload isolation by assigning dedicated compute engines for different tasks. This ensures that data loading processes no longer compete with analytical queries, maintaining consistent performance.  

Firebolt engines support both read and write operations on shared data while maintaining strong consistency across engines, eliminating the need for manual synchronization.  

Additionally, Firebolt optimizes workload execution dynamically based on configuration, resource utilization, and query history. This helps balance latency and throughput, ensuring that resources are used efficiently.  

Allocate dedicated engines for critical workloads such as real-time dashboards or high-volume data transformation pipelines to maximize efficiency.

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

## Exporting data from Redshift

## Loading data into Firebolt

## Translating queries

## Performance testing and optimization

## Automated migration

## Post-migration validation and maintenance

## Best practices