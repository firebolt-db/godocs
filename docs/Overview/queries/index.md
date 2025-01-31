---
layout: default
title: Queries
description: Learn about running queries, improving performance, and query optimizations in Firebolt.
parent: Overview
nav_order: 7
has_toc: false
has_children: true

---

# Queries
Firebolt is designed to run SQL queries efficiently, using advanced optimizations at both the query and workload levels. This section provides an overview of how Firebolt processes queries, the optimizations applied during query handling, and the tools available for monitoring and improving performance. For guidance on how to run queries and interact with data in Firebolt, see [Query data]({% link Guides/query-data/index.md %}).  

## Optimizations on a per-query basis
Firebolt applies specific optimizations at the individual query level to ensure efficient performance, even for complex queries.
These optimizations take effect immediately when you create an account and start your first engine.

* [Spilling intermediate query state](./understand-spilling.md) to the local SSD cache. This allows processing queries whose working set exceeds main memory.
* Firebolt has advanced support for correlated subqueries. These are automatically decorrelated by our query planner to maximize performance.

## Workload-level optimizations
Homogeneous workloads with repeated query structures can benefit significantly from workload-level optimizations.
Examples for such workloads are customer-facing, high-concurrency data apps, or internal BI workloads.
For these workloads, Firebolt leverages multiple different optimizations.

* [Reusing query sub-results and result caching](./understand-query-performance-subresult.md) to reduce redundant calculations across queries.
* [History-based query optimization](./understand-query-performance-hbs.md), which leverages past query patterns to improve query plans for new queries.

## Query telemetry and monitoring  
Firebolt provides the following tools to monitor and analyze query performance:  

- **`EXPLAIN` command**: View the query plan to understand how Firebolt executes your query.  
- **Telemetry data**: Analyze metrics such as runtime, memory usage, and data processed.  
- **Query history**: Use views like `information_schema.engine_query_history` to monitor query performance details over time.  