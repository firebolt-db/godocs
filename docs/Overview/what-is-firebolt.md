---
layout: default
title: What is Firebolt?
description: Learn why Firebolt excels in fast query processing for data-intensive applications.
nav_order: 1
parent: Overview
---

# What is Firebolt? 

Firebolt is a next-generation cloud data warehouse that delivers query responses in **milliseconds**. Firebolt's independent scaling optimizes resources, and isolates workloads to prevent interference. This system ensures efficient performance while maintaining separation between tasks. Firebolt delivers fast and consistent results even for:

* Very large data sets.
* Demanding, data-intensive applications.
* Datasets with high concurrency.
* Highly complex queries and diverse workloads.

Firebolt's architecture decouples compute, storage, and management layers, allowing each to scale independently, as shown in the following diagram. This design provides precise resource allocation based on workload demands, ensuring optimal performance without  allocating excess resources. Firebolt's distributed query engine scales near-linearly, maintaining consistent performance for even petabyte-sized data volumes.

![Firebolt Architecture](../assets/images/architecture-visual.png)

Firebolt is engineered to support diverse workload requirements, offering separate engines for ELT, batch analytics, and interactive analytics. This workload isolation ensures predictable performance across all operations, by preventing any single workload from impacting others. With compatibility for popular file formats such as Parquet, JSON, CSV, AVRO, and ORC, Firebolt integrates smoothly into existing data ecosystems.

## Why Firebolt?

**Unparallelled Price-Performance Ratio** <img src="../assets/images/bolt-icon.png" alt="bolt icon" width="30"/>

Firebolt is engineered to provide the lowest price to performance ratio in the industry. This isn’t just theory—our architecture ensures that real-time insights are delivered faster, even at petabyte scale, with zero compromise on performance.

**Concurrency at Scale** <img src="../assets/images/concurrency-icon.png" alt="concurrency icon" width="30"/>

With support for up to 2000 concurrent queries, Firebolt ensures that your applications can handle heavy query loads while maintaining consistent performance. This high level of concurrency ensures that your data-intensive applications can efficiently process high throughput with reliable performance, even under heavy workloads.

**Flexible Infrastructure** <img src="../assets/images/infrastructure-icon.png" alt="infastructure icon" width="30"/>

Firebolt's fully decoupled architecture allows compute, storage, and core services to scale independently. This three-dimensional scaling lets you optimize resources, while lowering operational costs. With fine-grain control, you can scale precisely to meet your specific workload needs, and avoid the wasteful allocation of excess resources.

**SQL Simplicity** <img src="../assets/images/checkmark-icon.png" alt="checkmark icon" width="30"/>

Firebolt supports a PostgreSQL-compliant SQL dialect, allowing your teams to harness the power of Firebolt without the need to learn a new query language. This simplifies data provisioning, processing, and management, ensuring compatibility with existing workflows. Firebolt supports both structured and [semi-structured data](../Guides/working-with-semi-structured-data/working-with-semi-structured-data.md), so that you can analyze diverse datasets within a single platform.

## Supported frameworks and workloads

![Firebolt frameworks](../assets/images/firebolt-frameworks.png)

Firebolt provides SDKs for Python, Java, .Net, Node, and Go, so you can quickly build and integrate Firebolt into applications using these frameworks. You can use these SDKs to programmatically control and optimize data workflows, from ingestion to analysis, within custom applications including those for ingestion, analytics, and extract, load, transform (ELT) workflows. These SDKs also integrate with open-source tools such as [Apache Airflow](https://airflow.apache.org/) and [dbt](https://www.getdbt.com/product/what-is-dbt). You can use the [Firebolt command line interface (CLI)](https://docs.firebolt.io/godocs/Guides/query-data/using-the-cli.html) to efficiently manage resources such as engines, databases, tables, and queries from the command line.

## Firebolt platform capabilities

**Data Management** <img src="../assets/images/data-management.png" alt="data management icon" width="30"/>

Firebolt is designed for performance and efficiency, minimizing effort through automated features. It offers a robust architecture with capabilities like parallel data ingestion, ACID DML, and optimized storage, so that it can handle large, complex datasets. Automated indexing and backend optimization ensure that performance remains consistent, even during data modifications including inserting, updating, or deleting records. Firebolt also supports structured and semi-structured data, so that you can integrate into existing workflows and perform tasks such as creating tables, ingesting data, and managing transactions.

For more information, see [Data management](../Overview/data-management.md).

**Query Processing** <img src="../assets/images/query-processing-icon.png" alt="query processing icon" width="30"/>

Firebolt's query processing is designed for high concurrency and low latency, scaling dynamically based on workload demands. It uses an optimizer that creates efficient execution plans by considering data distribution, indexes, and past query patterns. The distributed runtime system employs multithreading and tiered caching for faster processing, while resource-aware scheduling and efficient memory usage maximize cluster performance. This setup ensures fast, consistent query execution, even with complex queries or large datasets.

You can use the Firebolt **Develop Space** to edit and run SQL scripts, manage databases, and view query results. The space features a document editor with auto-complete and script templates. You can also rename, copy, or export scripts, and either run SQL snippets or an entire script with real-time result display. The **Develop Space** interface supports switching between light and dark modes and exporting query results for further use.

You can also use the Firebolt API for programmatic access to performing tasks including querying, managing resources, and automating workflows. For more information, see the [Firebolt API](../Guides/query-data/using-the-api.md), and Firebolt [functions glossary](../sql_reference/functions-reference/functions-glossary.md).

**Security** <img src="../assets/images/security-icon.png" alt="security icon" width="30"/>

Firebolt uses a layered approach to security, ensuring data protection at all levels. It includes network security with TLS 1.2, identity management with multi-factor authentication (MFA) and Single Sign-On (SSO), and role-based access control (RBAC) to manage permissions. Firebolt also safeguards data at rest and in transit through encryption, while allowing fine-tuned control over access with network policies. This comprehensive security framework ensures that data is protected and accessible only to authorized users.

**Observability** <img src="../assets/images/observability-icon.png" alt="observability icon" width="30"/>

Firebolt's observability features offer detailed metrics on CPU, RAM, disk usage, and cache efficiency through the [engine_metrics_history](../sql_reference/information-schema/engine-metrics-history.md) and [engine_running_queries views](../sql_reference/information-schema/engine-running-queries.md). These metrics can help you optimize engine configurations and resource allocation. Firebolt also integrates with [OpenTelemetry](https://opentelemetry.io/), allowing users to track telemetry data for deeper insights into performance across distributed systems. This integration enhances observability and helps users make informed adjustments. Access to these tools is governed by role-based access control [(RBAC)](../Guides/security/rbac.md) permissions, ensuring secure management of system resources.

**Collaborative Workspace** <img src="../assets/images/workspace-icon.png" alt="collaborative workspace icon" width="30"/>

Delivering insights or data products requires collaboration between multiple roles, including data architects, engineers, developers, and DevOps. The **Firebolt Workspace** supports coordination across teams by providing visibility across the entire data lifecycle. It offers dedicated areas for security and governance, data modeling, exploration, SQL development, and performance management, ensuring each role can efficiently contribute to the process.

## Next Steps

### Get Started with Firebolt today!

Learn how to load and query your data with our [Get Started](../Guides/getting-started/index.md) and [Load data](../Guides/loading-data/loading-data.md) guides or use one of Firebolt’s test data sets. Sign-up to access our $200 credits. No credit card needed. 

### Firebolt resources

Explore our competitive pricing options [here](https://www.firebolt.io/pricing).

Need help? Firebolt’s support team is here to assist you with:
* Onboarding.
* Troubleshooting query performance.
* Optimizing database configurations.
* Addressing data loading issues.
* Providing best practices for data modeling.

Contact [support@firebolt.io](mailto:support@firebolt.io). 






