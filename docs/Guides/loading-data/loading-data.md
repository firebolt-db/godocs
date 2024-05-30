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

Loading data into Firebolt is described in the [Getting started tutorial](../getting-started.md) and consists of three steps.

1. To provide Firebolt with the right permissions to load data from your Amazon S3 bucket, you must create AWS access keys and secret IDs. For instructions on how to create the access key credentials in AWS, see [Creating Access Key and Secret ID](../loading-data/creating-access-keys-aws.md).

2. Using the credentials created above, you can now load your data into Firebolt using the [COPY FROM](../loading-data/copy-from.md) command. For information on its syntax and parameters, click [here](../../sql_reference/commands/data-management/copy-from.md).

3. Loading data into Firebolt is also performed using external tables. To learn more about how to run the [CREATE EXTERNAL TABLE](../../sql_reference/commands/data-definition/create-external-table.md) command to load your data into Firebolt, see [Work With External Tables](../loading-data/working-with-external-tables.md).


<!-- For information about using Apache Airflow to incrementally load data chronologically, see [Incrementally loading data with Airflow](incrementally-loading-data.md). -->
