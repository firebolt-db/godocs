---
layout: default
title: Optimize query performance
description: Guides to optimizing query performance in Firebolt.
parent: Guides
has_toc: false
has_children: true
---

# Optimize query performance
Firebolt employs various optimizations across components like the query planner and execution engine to maximize SQL query performance.

The guides in this section show you the following:
* What optimizations Firebolt uses to improve query performance.
* How and when Firebolt applies these optimizations.
* How you can use Firebolt's telemetry to verify their usage.

Firebolt offers optimizations tailored to different workloads.
Some optimizations apply to individual queries and take effect immediately when an engine starts.
Others become powerful at the workload level, leveraging artifacts and telemetry from previous queries to enhance performance.

This section covers both types of optimizations.
Although Firebolt automatically applies these optimizations, understanding them can help you further improve your query performance.

## Optimizations on a per-query basis
Firebolt applies specific optimizations at the individual query level to ensure efficient performance, even for complex queries.
These optimizations take effect immediately when you create an account and start your first engine.

* [Spilling intermediate query state](./understand-spilling.md) to the local SSD cache. This allows processing queries whose working set exceeds main memory.
* Firebolt has advanced support for correlated subqueries. These are automatically decorrelated by our query planner to maximize performance.


## Workload-level optimizations
Homogeneous workloads with repeated query structures can benefit significantly from workload-level optimizations.
Examples for such workloads are customer-facing, high-concurrency data apps, or internal BI workloads.
For these workloads, Firebolt leverages multiple different optimizations.

* [Reusing query sub-results](./understand-query-performance-subresult.md) to reduce redundant calculations across queries.
* History-based query optimization, which leverages past query patterns to improve query plans for new queries.

