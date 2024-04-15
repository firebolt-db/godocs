---
layout: default
title: Load data
description: Understand options for loading data into Firebolt from your data lake.
parent: Guides
nav_order: 3
has_children: true
has_toc: false
---

# Load data

Loading data into Firebolt is described in the [Getting started tutorial](../getting-started.md) and consists of four steps.

1. Provide firebolt with the right permissions to load data from your Amazon S3 bucket. See [Use AWS roles to access S3](https://docs.firebolt.io/godocs/Guides/loading-data/configuring-aws-role-to-access-amazon-s3.html) for further instructions.

2. Create an *external table* as a connector from Firebolt to your external data source. For more information, see [Working with external tables](working-with-external-tables.md).  

  In the table definition, you specify credentials that allow Firebolt to read from the data source. For more information, see [CREATE EXTERNAL TABLE](../../sql_reference/commands/data-definition/create-external-table.md) and [Using AWS roles to access S3](configuring-aws-role-to-access-amazon-s3.md). Data that you ingest must be in an Amazon S3 bucket in the same AWS Region as the Firebolt database. For available Regions, see [Available AWS Regions](../../Reference/available-regions.md).

3. Create a fact or dimension table to store the data in Firebolt to be queried. For more information, see [Working with tables](../../Overview/working-with-tables/working-with-tables.md).  

4. Use an `INSERT` command using a general purpose engine to load data from the external data source into the fact or dimension table. For more information, see [INSERT](../../sql_reference/commands/data-management/insert.md).

<!-- For information about using Apache Airflow to incrementally load data chronologically, see [Incrementally loading data with Airflow](incrementally-loading-data.md). -->
