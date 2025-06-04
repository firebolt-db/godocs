---
redirect_from:
- /godocs/Guides/working-with-engines/understand-autoscaling.html
title: Understanding Autoscaling
description: Learn how autoscaling works in Firebolt engines.
nav_order: 3
parent: Operate Engines
---
# Understanding Autoscaling
{: .no_toc}

This is a technical guide to understanding how concurrency autoscaling works in Firebolt engines. 
For overview of autoscaling, see the [Concurrency auto-scaling]({% link Guides/operate-engines/working-with-engines-using-ddl.md %}#concurrency-auto-scaling).

## Basic operation 

Firebolt engines can scale for concurrency by changing the number of clusters that belong to a single engine. 
You set the bounds with the `MIN_CLUSTERS` and `MAX_CLUSTERS` options in [CREATE ENGINE]({% link sql_reference/commands/engines/create-engine.md %}) 
and [ALTER ENGINE]({% link sql_reference/commands/engines/alter-engine.md %}) commands. When demand rises above the current 
capacity, Firebolt adds one new cluster; when load drops, it removes one. 
After each adjustment the service observes a short stabilization window before it evaluates the next scale decision, 
preventing thrashing during bursty traffic.

When a stopped engine starts, it starts with the minimum number of clusters.

## Auto-scaling metrics

The autoscaler bases its decisions on three workload signals:
- **CPU utilization** – averaged across nodes in each cluster, then averaged across clusters
- **RAM utilization** – averaged in the same way
- **Query queue time** – the maximum time any waiting query in the engine has spent in the queue

The exact thresholds and the way metrics are aggregated are tuned by Firebolt and can be changed without notice. Current default thresholds are:

| Metric                | Thresholds for adding clusters(any) | Thresholds for removing clusters (all) |
| -----------------------|-------------------------------------|----------------------------------------|
| CPU utilization       | over 90%                            | under 75%                              |
| RAM utilization       | over 70%                            | under 50%                              |
| Max query queue time  | over 3 seconds                      | under 1 second                         |


The current default stabilization window **is 1 minute**.

For monitoring engine stats, please refer to [Monitoring Engine Usage]({% link Overview/engine-fundamentals.md %}#monitoring-engine-usage).

This is **concurrency auto-scaling**: it creates extra clusters so that new queries can start promptly. 
It does **not** re-plan or speed up queries that were already running. 
Adding more clusters will not make a single large query finish faster. 
If an individual query needs more processing power, consider scaling the engine **up or out** (larger `TYPE` or more `NODES`) instead. 
For general sizing advice, see the [Sizing Engines guide]({% link Guides/operate-engines/sizing-engines.md %}).
{: .note}

## Monitoring autoscaling

You can check how many clusters an engine is using at any moment — and what its minimum and maximum limits are — 
via [information_schema.engines]({% link sql_reference/information-schema/engines.md %}) table.

You can see how an engine changed the number of clusters over time via 
[information_schema.engine_history]({% link sql_reference/information-schema/engine-history.md %}) table.