---
layout: default
title: Differences between Firebolt Core and Managed Firebolt
nav_order: 5
parent: Firebolt Core
---

# Differences between Firebolt Core and Managed Firebolt

Firebolt Core contains almost all of the features available in [managed Firebolt](https://www.firebolt.io/), allowing many workloads to run interchangeably between the two editions. Nevertheless, some relevant differences exist and are outlined below.

* There are **no built-in security features** in Firebolt Core. The features outlined in [Security](../Overview/Security/security.md) are only available in [managed Firebolt](https://www.firebolt.io/). In particular, the following restrictions apply.
    * There is **no authentication** mechanism in Firebolt Core. Anyone that can access the HTTP query endpoint of a Firebolt Core node can submit queries to the cluster (see also [Connect](./firebolt-core-connect.md)).
    * There is **no role-based access control** in Firebolt Core, and attempting to use the respective SQL commands will result in an error.
    * There is **no encryption** of network traffic within a Firebolt Core cluster. This applies both to inter-node traffic and to traffic to or from users.
* There are only **limited features for automatic management and optimization** in Firebolt Core. In particular, the following restrictions apply.
    * There is **no support for online upgrades** in Firebolt Core. Version upgrades must be done explicitly (see also [Deployment and Operational Guide](./firebolt-core-operation.md)).
    * There is **no support for auto-scaling** in Firebolt Core. Resizing a Firebolt Core cluster is usually not possible at all (see also [Architecture](./firebolt-core-architecture.md)).
    * There is **no support for auto-vacuum** in Firebolt Core. [VACUUM](../sql_reference/commands/data-management/vacuum.md) can still be run manually.
    * There is **no admission controller** in Firebolt Core. Clients are responsible for load-balancing and ensuring that data is distributed evenly (see also [Connect](./firebolt-core-connect.md)), as well as for retrying failed queries.
* Some further limitations apply to database objects managed by Firebolt Core (e.g. tables or views).
    * There is **no storage-compute isolation** in Firebolt Core (see also [Architecture](./firebolt-core-architecture.md)). As a result, managed database objects are tied to one specific Firebolt Core cluster which cannot be resized.
    * There is **no support for zero-copy cloning** in Firebolt Core.
    * There is **no support for [DIMENSION](../sql_reference/commands/data-definition/create-fact-dimension-table.md) tables** in Firebolt Core. All tables are sharded across nodes.
* **At most one write transaction** can be active at a time in Firebolt Core (see also [Connect](./firebolt-core-connect.md)). Attempting to start concurrent write transactions will result in an error.
* There is **no support for [asynchronous query execution](../API-reference/using-async-queries.md)** in Firebolt Core.

As a result of the above limitations, only a subset of the [documented SQL dialect](../sql_reference/index.md) is available in Firebolt Core. Most importantly, the following statements are **unavailable** in Firebolt Core.

* [Information Schema](../sql_reference/information-schema/index.md) tables pertaining to features not available in Firebolt Core (e.g. [Accounts](../sql_reference/information-schema/accounts.md)) will return placeholder results.
* [Access Control](../sql_reference/commands/access-control/index.md) SQL commands are not available in Firebolt Core and attempting to use them will result in an error.
* [Data Definition](../sql_reference/commands/data-definition/index.md) SQL commands pertaining to features not available in Firebolt Core (e.g. [CREATE ACCOUNT](../sql_reference/commands/data-definition/create-account.md)) are not available and attempting to use them will result in an error.
* [Engine Commands](../sql_reference/commands/engines/index.md) are not available in Firebolt Core and attempting to use them will result in an error.
* [RECOMMEND DDL](../sql_reference/commands/queries/recommend_ddl.md) is not available in Firebolt Core and attempting to use it will result in an error.