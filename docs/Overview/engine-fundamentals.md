---
redirect_from:
  - /working-with-engines/choosing-an-engine.html
  - /Overview/understanding-engine-fundamentals.html
layout: default
title: Engine Fundamentals
description: Learn fundamental concepts about Firebolt Engines.
parent: Overview
has_children: true
has_toc: false
nav_order: 4
---

# Firebolt Engines
{: .no_toc}

 Engines are compute resources that process data and serve queries in Firebolt. Use engines to load data into Firebolt and run queries on the ingested data. 

Firebolt engines provide **full workload isolation**, so that multiple workloads run independently while sharing the same data. Engines are **decoupled from databases**, meaning:

* A single engine can run queries on multiple databases.
* A database can be queried using multiple engines.

 Start, stop and modify engines at any time using the SQL API. You can also **dynamically scale engines** based on workload needs without stopping them.

 This document explains engine configuration, scaling, monitoring, security and connection options.

**Topics**
* [Key engine concepts](#key-engine-concepts) &ndash; Learn about the `TYPE`, `NODES`, and `CLUSTERS` attributes that define a Firebolt engine’s configuration and scaling options.
* [Multi-dimensional elasticity](#multi-dimensional-elasticity) &ndash; Scale engines dynamically by adjusting engine attributes without stopping workloads.
* [Connecting to engines](#connecting-to-engines) &ndash; How to connect to a Firebolt engine using the UI, Engine URL, or third-party tools.
* [Monitoring engine usage](#monitoring-engine-usage) &ndash; Track engine performance using observability views in `information_schema` to optimize resource allocation.
* [Engine governance and security](#engine-governance-and-security) &ndash; Control engine access using [Role-Based Access Control (RBAC)]({% link Overview/Security/Role-Based Access Control/index.md %}) and account-level isolation to enforce security policies.
* [Viewing and understanding engine status](#viewing-and-understanding-engine-status) &ndash; Learn how to use `SHOW ENGINES` to check the status of all engines, including running, resizing, and stopped states.


## Key engine concepts

Engines in Firebolt are defined by four attributes: **Type**, **Family**, **Nodes**, and **Clusters**. These attributes determine the engine’s configuration and scaling options.

**Type** <br/>
The `TYPE` of engine defines the **compute node size** used as a building block for an engine. They are available in Small, Medium, Large, and X-Large sizes. Change the node type to **vertically scale** up or down. Small and medium engines are available for use right away. If you want to use a large or extra-large engine, reach out to [support@firebolt.io](mailto:support@firebolt.io).

**Family** <br />
Compute nodes can be storage-optimized with larger cache sizes or compute-optimized which have smaller caches. The default is storage-optimized.

**Nodes** <br />
This attribute represents the number (1 - 128) of compute nodes, allowing granular horizontal scaling to fine-tune query performance characteristics while avoiding overprovisioning and unnecessary cost. Both scaling in and out are supported.

**Clusters** <br />
A cluster is a collection of compute resources, described by “Type” and “Nodes” attributes. A given Firebolt engine can contain one or more clusters. The maximum number of clusters is specified by the max_clusters attribute. Only homogeneous cluster configurations (clusters with the same number of Nodes and Type) are supported within a single engine. Users can leverage the “min_clusters” and "max_clusters" attributes to support query concurrency scaling.

![An engine cluster in Firebolt](../assets/images/engine_cluster_type_M.png){: width="600" .centered}
 <br /> **An engine cluster with four nodes of type 'M'** 
 {: style="color: red; font-size: 90%; text-align: center;"}


![A Firebolt engine with two clusters, each cluster containing four nodes of type 'M'](../assets/images/Engine_two_clusters_type_M.png){: width="600" .centered}
 <br /> **A Firebolt engine with two clusters, each cluster containing four nodes of type 'M'** 
 {: style="color: red; font-size: 90%; text-align: center;"}

<br />
The four attributes:  `TYPE`, `NODES`, `MIN_CLUSTERS` and "MAX_CLUSTERS" &ndash; form the configuration of an engine.

To create an engine, use the [CREATE ENGINE command]({% link sql_reference/commands/engines/create-engine.md %}), specifying the node type to be used for the engine, number of clusters and number of nodes per cluster.

The following code example creates two clusters, each containing four nodes of type `M`, from the compute-optimized family:

```sql
CREATE ENGINE IF NOT EXISTS MyEngine 
WITH TYPE = M 
FAMILY = COMPUTE_OPTIMIZED
NODES = 4 
MIN_CLUSTERS = 2;
MAX_CLUSTERS = 2;
```

For a full list of engine attributes, see [CREATE ENGINE](../sql_reference/commands/engines/create-engine.md)


## Multi-dimensional elasticity

Firebolt engines enable dynamic and fully online scaling operations, meaning you do not need to stop your engines to scale them. You can scale an engine along three dimensions: 

| Scaling Type          | Action                      | Example SQL Command                     |
|----------------------|---------------------------|-----------------------------------------|
| **Vertical Scaling** | Change the node type and family | `ALTER ENGINE MyEngine SET TYPE = L FAMILY = SO;` |
| **Horizontal Scaling** | Change the number of nodes | `ALTER ENGINE MyEngine SET NODES = 3;`  |
| **Concurrency Scaling** | Change the number of clusters | `ALTER ENGINE MyEngine SET MIN_CLUSTERS = 2 MAX_CLUSTERS = 2;` |

You can scale up or down using the engine type and family, scaling out or in with number of nodes and add or remove clusters for concurrency scaling. This multidimensional scaling allows you to fine-tune the price-performance characteristics of engines and dynamically scale your compute resources based on your workload requirements.

Use the [ALTER ENGINE]({% link sql_reference/commands/engines/alter-engine.md %}) to modify the configuration of an engine to dynamically scale the engine even while it is running, without impacting the workload. 

**Best practices**

* Use a **larger node type** to improve performance for both single queries and multiple concurrent queries, especially as data size grows
* Increase the number of nodes for finer control over scaling, such as distributing workloads across multiple smaller nodes or when further vertical scaling is not possible.
* Increase the **number of clusters** to support higher query concurrency.

The following code example uses `ALTER ENGINE` to horizontally scale an engine from two to three nodes:

```sql
ALTER ENGINE MyEngine SET NODES = 3;
```

The following code example changes the type of node used in an engine from ‘M’ to ‘L’:

```sql
ALTER ENGINE MyEngine SET TYPE = L;
```

The following code example changes more than one attribute at the same time:

```sql
ALTER ENGINE MyEngine SET NODES = 3 TYPE = L FAMILY = COMPUTE_OPTIMIZED;
```

For more information on modifying engines, see [ALTER ENGINE]({% link sql_reference/commands/engines/alter-engine.md %}).


## Connecting to engines

You can connect to an engine using the following methods:

* Firebolt's [user interface](https://go.firebolt.io/login).
* An engine URL.
* Third-party [connectors]({% link Guides/integrations/integrations.md %}) such as Airflow and DBT.

The engine URL is based on your account name and org name, with the following format:

`<account-name>.<org-name>.region.firebolt.io` 

The combined length of `account-name` and `org-name` must not exceed 62 characters.

## Monitoring engine usage

You can use the observability views in `information_schema` to track engine performance and usage.

| View | Description |
|------|-------------|
| `engine_metrics_history` | Captures CPU and RAM usage every **30 seconds** and retains data for **30 days**. |
| `engine_running_queries` | Lists active queries and queries waiting to be processed. |

You can use the information in the previous [information_schema views]({% link sql_reference/information-schema/index.md %}) to decide whether you need to change the engine configuration type, number of nodes or clusters based on your workload needs.

The [engine_metrics_history]({% link sql_reference/information-schema/engine-metrics-history.md %}) view gathers engine resource utilization metrics such as CPU and RAM consumption at a given time snapshot. Utilization snapshots are captured every 30 seconds and retained for 30 days, allowing users to understand engine utilization and consumption trends. 

The following code example retrieves CPU and RAM usage for `MyEngine`:

```sql
SELECT * 
FROM information_schema.engine_metrics_history 
WHERE engine_name = 'MyEngine' 
ORDER BY event_time DESC;
```

The [engine_running_queries]({% link sql_reference/information-schema/engine-running-queries.md %}) view exposes information about queries currently running or waiting to be run in the system.  Based on the number of queries that are queued and waiting to run, you can modify the engine configuration to best suit your performance requirements.


The following code example retrieves currently running queries:

```sql
SELECT * 
FROM information_schema.engine_running_queries;
```

If the previous query shows that queries remain in the queue for too long, increase the number of nodes or clusters. 

To understand how information views can help with engine resizing, see [Working with Engines](../Guides/operate-engines/sizing-engines.md).


## Engine governance and security

Firebolt provides **account-level isolation** and **Role Based Access Control (RBAC)** to provide strict governance over data access and infrastructure costs.

**Account isolation**

You can create multiple accounts within a given organization, where each account can represent a fully isolated environment such as development, test, or production. This enables engines across different environments to be fully isolated from each other. 

**RBAC for engine management**

The Firebolt [RBAC model]({% link Guides/security/rbac.md %}) allows administrators to control user actions on resources that are created within a given account. For example, administrators can control which users are allowed to modify the configuration of engines and control which users can create new engines. 

The following code example creates an engine administrator role and grants it full permissions on `MyEngine`:

```sql
CREATE ROLE engine_admin;
GRANT ALL PRIVILEGES ON ENGINE MyEngine TO engine_admin;
```

For more information on using RBAC for engines, see [Governing Engines](../Guides/operate-engines/rbac-for-engines.md). 

## Viewing and understanding engine status

Use [SHOW ENGINES]({% link sql_reference/commands/metadata/show-engines.md %}) to list all engines and their statuses in your Firebolt account as follows:

| `SHOW ENGINES` and UI |   Description                     
| :-------------------- | :------------------------------- | 
| STARTING              | The engine is provisioning resources, and will be ready to use soon.   |
| RUNNING               | The engine is running queries or available to run queries. The engine can be modified while it is running.|
| RESIZING              | The engine is currently being resized after an `ALTER ENGINE` command. The engine will be in this state when the user has issued a request to change the engine `TYPE`, number of `NODES` or number of `CLUSTERS`. |
| DRAINING              | The engine is completing running queries before shutting down. |
| STOPPING              | The engine is shutting down and cannot accept new queries. |
| STOPPED               | The engine is fully stopped and not available to run queries. |



