---
layout: default
title: Understand query performance 
description: Guides to understanding query performance in Firebolt. 
parent: Guides
nav_order: 7
has_toc: true
has_children: true
---

# Understand query performance 
Firebolt's query planner and query engine always aim to provide the best possible performance for your SQL query.
To achieve this, Firebolt uses a variety of different optimization techniques under the hood.
The guides in this section allow you to learn about these optimizations.
They teach you when certain optimizations can be applied, and how you can use Firebolt's telemetry to check whether they were used for your queries.

As Firebolt aims to be the best data warehouse for data intensive applications, many optimizations focus on improving performance for homogeneous workloads.
These optimizations will only be applied when you run multiple queries with a similar structure in succession.
In these cases, it's especially useful to analyze query telemetry and see which optimizations are applied.

Note that all optimizations are applied transparently by Firebolt.
There are no special settings or configurations required to leverage these techniques.
However, understanding what types of optimizations Firebolt can perform can help you maximize the system's opportunities to improve the performance of your workload.

