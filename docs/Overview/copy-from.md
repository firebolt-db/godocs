---
layout: default
title: COPY FROM
description: Understand how to load data into Firebolt using the COPY FROM command
parent: Overview
nav_order: 4
---
# COPY FROM
{: .no_toc}

This topic provides an overview on how to load data into Firebolt using the `COPY FROM` command. 

The `COPY FROM` command enables you to ingest data from AWS S3 into Firebolt.  This command provides a simple syntax and does not require an exact match to your source data, giving you the flexibility to address various scenarios when loading data, such as:

* Copy all source columns into the target table
* Copy only a select list of columns into the target table
* Automatically discover the schema while ingesting the data
* Limit the number of rows loaded into the table
* Error handling

`COPY FROM` supports a range of file formats, including:

* `Parquet`
* `CSV/TSV`

You can use `COPY FROM` for both loading initial data and loading incremental data.

## Initial Data Load
Use the `COPY FROM` command to efficiently load large batches of data into Firebolt. This command is atomic, ensuring ACID-compliance, and enables loading large initial datasets quickly and reliably into an empty table.

## Incremental Data Load
`COPY FROM` allows you to append new data to existing tables without interrupting your workload, useful for ingesting data incrementally. You can use incremental data loading to regularly update data repositories with new information as it becomes available.

## Concurrency and Data Loading
The `COPY FROM` command allows different tables to be loaded simultaneously and in parallel. A single table can be populated from multiple sources and by multiple clients at once. 

## Automatic Schema Discovery
You can leverage automatic schema discovery provided by `COPY FROM`  to manage sizable data sources where manual schema definition can be cumbersome and error-prone. For data formats like Parquet and ORC that already include table-level metadata, Firebolt automatically reads this metadata to facilitate the creation of corresponding target tables. For formats where column-level metadata might not be available, such as `CSV` and `JSON`, `COPY FROM` infers column types based on the data content itself. While this process aims to accurately identify data types, it operates on a "best effort" basis, balancing type correctness with practical usability constraints. Additionally, for CSV files that often contain column names in the first line, COPY FROM uses this line as column headers and deduces the column types from the subsequent data, streamlining the initial data loading process significantly. 

## Handling Bad Data
`COPY FROM` provides robust mechanisms to identify and isolate bad data during the loading process.

## Handling partitioned data
`COPY FROM` effectively manages the loading of partitioned data, ensuring that data is inserted into the correct partitions based on predefined rules or schema setups, optimizing query performance and data management.

## Filtering data to be loaded
You can use the `LIMIT` clause to control the amount of data loaded into tables, for example when managing data previews and sample loads. 

`COPY FROM` also supports an `OFFSET` clause, allowing users to skip a specified number of rows in each input file before starting the data load. This is useful when users need to exclude certain initial data entries from being loaded.

### Example for LIMIT Clause

```sql
COPY INTO T1(c1 int) FROM … LIMIT 10
```
This example will load only the first 10 rows into table T1, provided the source file contains at least 10 rows. If both `OFFSET` and `LIMIT` are used, the `OFFSET` rows are skipped before the `LIMIT` rows are counted and loaded, which can help fine-tune the data ingestion process to meet specific requirements.  Note that the `LIMIT` clause is non-deterministic, and will not reliably return the same data unless `ORDER BY` is used.

## Loading compressed data
`COPY FROM` supports loading data directly from compressed files, and supports the following compression methods:

* CSV supports GZIP
* Parquet supports GZIP and Snappy

You can use the `COMPRESSION` parameter to specify the compression method to use.
The `COPY` command will auto-detect the compression type based on the file extension when this parameter is not specified.







