---
layout: default
title: Process Data
nav_order: 3
parent: Firebolt Core
---

# Process Data

Firebolt Core is all about high-throughput, low-latency data processing. As outlined in [Connect](./firebolt-core-connect.md), all communication with Firebolt Core ultimately occurs through SQL and data processing is no exception. Firebolt Core generally supports the full SQL dialect documented in our [SQL reference](../sql_reference/index.md), except a few exceptions that concern features specific to our managed Cloud data warehouse (e.g. RBAC or engine management commands). A complete list of differences between Firebolt Core and the managed Firebolt Cloud data warehouse can be found in [Differences between Firebolt Core and managed Firebolt](./firebolt-core-differences.md). 

The remainder of this page focuses specifically on importing, managing, and exporting data in Firebolt Core.

## Importing External Data

External data can be imported into Firebolt Core from several different sources and in several different formats.

* Raw data files stored on [Amazon S3](https://aws.amazon.com/s3/) or [Google Cloud Storage](https://cloud.google.com/storage).
    * The easiest way to access such data is to import it into a SQL table using [COPY FROM](../sql_reference/commands/data-management/copy-from.md). `COPY FROM` supports many convenience features such as schema discovery or metadata filtering, and can easily adapt to different data loading workflows.
    * Alternatively, you can also create an [external table](../sql_reference/commands/data-definition/create-external-table.md) encompassing all relevant data files. This has the advantage that no data is persistently stored and thus duplicated on the Firebolt Core cluster itself, but fewer convenience features are available for external tables than for `COPY FROM`.
    * Data files can also be read directly with the [read_parquet(..)](../sql_reference/functions-reference/table-valued/read_parquet.md) or [read_csv(..)](../sql_reference/functions-reference/table-valued/read_csv.md) table-valued functions.
* [Apache Iceberg](https://iceberg.apache.org/) tables can be read through the [read_iceberg(..)](../sql_reference/functions-reference/table-valued/read_iceberg.md) table-valued function.
    * We currently support a subset of Iceberg catalogs, including file-based catalogs, REST catalogs, and the Databricks Unity catalog.
    * We currently support data files stored on [Amazon S3](https://aws.amazon.com/s3/) or [Google Cloud Storage](https://cloud.google.com/storage).

Note that data stored on [Google Cloud Storage](https://cloud.google.com/storage) can currently only be accessed through the S3 interoperability layer exposed by GCS. In order to access such data from Firebolt Core, you will need to navigate to the "Access keys for your user account" section of the [Interoperability](https://console.cloud.google.com/storage/settings;tab=interoperability) tab in your Cloud Storage settings and generate an access key & secret for your account there. These will then need to be specified as the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` parameters of the respective SQL command or function (e.g. [CREATE LOCATION](../sql_reference/commands/data-definition/create-location.md), [CREATE EXTERNAL TABLE](../sql_reference/commands/data-definition/create-external-table.md), or [read_iceberg(..)](../sql_reference/functions-reference/table-valued/read_iceberg.md)).

## Managing Metadata & Data

In addition to processing external data, Firebolt Core can also manage relational data itself. Most [DDL](../sql_reference/commands/data-definition/index.md) and all [DML](../sql_reference/commands/data-management/index.md) commands are supported in Firebolt Core for this purpose. It is important to note, however, that Firebolt Core provides no compute-storage isolation. In other words, data managed by one Firebolt Core cluster cannot be shared with any other Firebolt Core cluster. Furthermore, tables are sharded across all nodes, which means that a Firebolt Core cluster containing such tables cannot be resized to a different number of nodes (see also [Differences between Firebolt Core and managed Firebolt](./firebolt-core-differences.md)).

Please refer to [Deployment and Operational Guide](./firebolt-core-operation.md) for further details about setting up persistent storage for the managed data used in Firebolt Core nodes.

## Exporting Data

Data can be exported from Firebolt Core through the following means.

* [COPY TO](../sql_reference/commands/data-management/copy-to.md) writes raw data files to [Amazon S3](https://aws.amazon.com/s3/) or [Google Cloud Storage](https://cloud.google.com/storage).
* Alternatively, you can also process query results within your client application (see [Connect](./firebolt-core-connect.md)). If the only goal is to persist query results to raw data files (e.g. in an ETL pipeline), doing this in the client will generally be slower than using `COPY TO` due to the added cost of serializing and transferring data to the client.

Analogously to reading data, writing data to [Google Cloud Storage](https://cloud.google.com/storage) currently goes through the S3 interoperability layer exposed by GCS and requires a suitable access key & secret ([see above](#importing-external-data) for details).

## Examples

The Firebolt Core GitHub repository contains some [examples](https://github.com/firebolt-db/firebolt-core/tree/main/examples) for the different ways to ingest and export data in Firebolt Core.