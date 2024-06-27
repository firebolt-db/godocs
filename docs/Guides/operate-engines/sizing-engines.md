---
layout: default
title: Sizing Engines
description: Learn how to size engines initially and use engine observability to monitor and resize engines
nav_order: 3
parent: Operate Engines
grand_parent: Guides
---
# Sizing Engines
{: .no_toc}

Selecting an appropriate engine size for your workload depends on multiple factors such as the size of your active dataset, latency and throughput requirements of your workload, your considerations for price-performance and the number of users and queries your workload is expected to handle concurrently. Our guidance is to start small with an engine size that fits your active dataset and monitor the workload using the engine observability metrics (see below). Based on these metrics, you can then dynamically resize your engine to meet the needs of your workload. 

# Initial Sizing
**ELT Workloads** <br />
{: .fs-6}
For the ELT workloads, the engine size would depend on the number of files and the size of the files used to ingest the data. You can parallelize the ingest process with additional nodes, which can provide improved performance.

**Queries** <br />
{: .fs-6}
For query processing, our recommendation is to start with an engine configuration that can fit your active dataset. Firebolt Engines cache the data locally, which helps serve queries at low latencies. The cache size provided by the engines varies depending on the type of node used in your engines, as shown below. <br />

| Node Type      | Cache Size   |
| :--------------| :------------|
| S              | 1.8TB |
| M              | 3.7TB |
| L              | 7.5TB |
| XL             | 15TB  |

<br />

While you can use the size of the active dataset to start with a certain node type, the number of nodes to use can depend on the complexity of the query, as determined by the number and size of the tables, the number of joins used and filtering criteria, among other factors. Depending on the complexity of the query, you can start with fewer nodes, and leverage the observability metrics (discussed below) to dynamically scale your engine to a configuration that meets your requirements.

# Using Observability Metrics to Resize an Engine
Firebolt provides engine observability metrics that give visibility into how the engine resources are being utilized by your workloads. Use the [Information_Schema.engine_metrics_history](../../sql_reference/information-schema/engine-metrics-history.md) view  to understand how much CPU, RAM and disk are utilized by your workloads. In addition, this view also provides details on how often your queries hit the local cache and how much of your query data is spilling onto the disk. These metrics can help you decide whether your engine needs a different node type and/or whether you need to add more nodes to improve the query performance. Use the [Information_Schema.engine_running_queries](../../sql_reference/information-schema/engine-running-queries.md) view to understand how many queries are waiting in the queue to be executed. If there are a number of queries still waiting to be executed, adding another cluster to your engine may help improve the query throughput. 

**TIP:** You also have the option to run your workload simultaneously on engines with different configurations and use these metrics to identify which configuration best fits your needs. 

**NOTE:** You will need to have the appropriate [RBAC](../working-with-engines/rbac-for-engines.md) permissions to use the engine observability metrics.




