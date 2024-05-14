---
layout: default
title: Engine Consumption
description: Understand how to calculate engine consumption.
parent: Overview
nav_order: 3
published: true
---

This page provides details on the engine consumption metric, Firebolt Units (FBU).  We provide examples on how to calculate both FBUs available to an engine and the actual FBUs consumed by a running engine. To understand what Firebolt Engines are, visit [Understanding Engine Fundamentals](../Overview/understanding-engine-fundamentals.md).

For tracking engine consumption, Firebolt uses a metric named Firebolt Units (FBU). The number of FBUs available to an engine is determined by the three attributes of an engine: Node Type, Number of nodes and Number of clusters. Each node type offers a minimum number of FBUs as shown below:

|      Engine Type      |  Firebolt Units (FBUs) per Hour  |      
| :-------------------- | :------------------------------- | 
|      Small (S)        |              8                   |
|      Medium (M)       |              16                  |
|      Large (L)        |              32                  |
|      XLarge (XL)      |              64                  |

As you add more nodes and more clusters to your engine, the number of FBUs available to the engine increases linearly. The available FBUs for a given engine configuration is calculated as below:
 
**Available FBU = (FBU of node Type x Nodes x Clusters)**
{: style="text-align: center;"}


**Example 1:**
You create an engine with the following configuration: TYPE = “S”, NODES = 2, CLUSTERS=1 <br />
This engine will have 16 FBUs available per hour (8 x 2 x 1). When you modify the engine configuration with a scale out operation to use 3 nodes, the available FBUs per hour goes up accordingly to 24 FBUs (8 x 3 x 1).

**Example 2:**
You create an engine with the following configuration: TYPE = “L”, NODES = 3, CLUSTERS=2 <br />
This engine will have 192 FBUs available per hour (32 x 3 x 2).  When you scale down the engine to use a “M” type node, the available FBUs per hour will come down accordingly to 96 FBUs (16 x 3 x 2).

The actual FBUs consumed by the engine can be different from the available FBUs. FBUs are consumed only when an engine is in a running state. The FBUs consumed by an engine depends on both the current configuration of the engine - node type, number of nodes and number of clusters -  and the duration for which the running has been running in that configuration. Since Firebolt provides per-second billing, the consumed FBU is calculated at per-second granularity, as shown below: <br />

**FBU Consumed  = (Available FBU per Hour / 3600) x (Duration for which engine was running in seconds)**
{: style="text-align: center;"}


**Example 1:**
You create an engine with the following configuration: TYPE = “S”, NODES = 2, CLUSTERS=1 <br />
Available FBU per hour for this engine is 16. Let us say the engine was actually running only for 15 minutes during the hour. So, the engine would have consumed 4 FBUs for that hour.


**Example 2:**
You create an engine with the following configuration: TYPE = “L”, NODES = 3, CLUSTERS=2 <br />
Available FBU per hour for this engine is 192. Let us say that the engine was only running for 40 seconds to quickly ingest a small amount of data. The consumed FBU is calculated as below:

FBU Consumed = (192/3600) x 40 = 2.13 
{: style="text-align: center;"}

## Impact of Resize Operations on Engine Consumption
When you perform scaling operations on an engine, whether it is scaling up/down or scaling out/in, additional compute resources (clusters) are added to the engine. These new clusters will have the new node type for a scale up/down operation and have the desired number of nodes for a scale out/in operation. The old clusters will be removed after they finish executing the currently running queries while new queries will be directed to the new clusters. Consequently, there will be a period of time, when both old and new clusters will be running concurrently, which will show in the engine consumption.

**Example 1:**
You create an engine with the following configuration: TYPE = “S”, NODES = 2, CLUSTERS=1
Available FBU per hour for this engine is 16. 

**First 15 minutes during the hour:**  The engine is running in the above configuration. <br />
**After first 15 minutes:** The engine is scaled out to use 5 nodes, keeping the same node type and same number of clusters. <br />
The old cluster with two nodes continues to run for 5 minutes to finish executing the queries. <br />
The new cluster with five nodes runs for the next fifteen minutes. <br />

The consumed FBU is calculated as follows:

**Minutes 1-15:** Only one cluster with two nodes is running, consuming 4 FBUs <br />
**Minutes 16-20:** Two clusters running. Cluster with two nodes consumes 1.3 FBU and Cluster with five nodes consumes 3.3 FBU. <br />
**Minutes 20-30:** Only cluster with five nodes is running and consumes 6.7 FBU <br />

Total number of FBUs consumed for the hour = 4 + 1.3 + 3.3 + 6.7 = 15.3 FBUs

**Example 2:**
You create an engine with the following configuration: TYPE = “L”, NODES = 2, CLUSTERS=1
Available FBU per hour for this engine is 64. 

**First 15 minutes during the hour:**  The engine is running in the above configuration. <br />
**After first 15 minutes:** The engine is scaled down to use “M” type nodes, keeping the same number of nodes and same number of clusters. <br /> 
The old cluster with “L” type nodes continues to run for 5 minutes to finish executing the queries. <br />
The new cluster with “M” type nodes runs for the next fifteen minutes. <br />

The consumed FBU is calculated as follows:

**Minutes 1-15:** Only one cluster with two “L” type nodes is running, consuming 16 FBUs <br />
**Minutes 16-20:** Two clusters running. Cluster with two “L” type nodes consumes 5.3 FBU and Cluster with two “M” type nodes consumes 2.7 FBU. <br />
**Minutes 20-30:** Only cluster with two “M” type nodes is running and consumes 5.3 FBU <br />

Total number of FBUs consumed for the hour = 16 + 5.3 + 2.7 + 5.3 = 29.3 FBUs


