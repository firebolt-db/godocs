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

You can load data into Firebolt from an Amazon S3 bucket using two different workflows.

If you want to get started quickly, load data using a Load data wizard in the Firebolt workspace. If you want a more customized experience, you can write SQL scripts to handle each part of your workflow. This guide shows you how to load data using both the wizard and SQL, and some common data loading workflows and errors.

Before you can load data, you must first register with Firebolt, then create a database and an engine. For information about how to register, see [Get Started](../getting-started.md). To create a database and engine, the following apply:
- If you use the Load data wizard, the user interface (UI) guides you through creating an engine and database.
- If you want to use the Firebolt SQL UI, you can select buttons to create a database and engine. See [Get Started](../getting-started.md) for more information.
- If you want to write your own SQL script, you must use `CREATE DATABASE` and `CREATE ENGINE` before you can load data.

Use the previous guidance to select the best workflow for your use case, as shown in the following diagram:
<img src="../../assets/images/load_data_workflow.png" alt="The load data workflow includes using the load data wizard or SQL to create a database, engine, and then load data." width="700"/>

Firebolt saves metadata including virtual columns, and the source file’s name, size and timestamp when mapping from your data from an Amazon S3 bucket to a Firebolt database. You can query this metadata directly for troubleshooting and analysis. For more information, see [Work with external tables](working-with-external-tables.md).

Optimizing your workflow for Firebolt starts when you load your data. Your data should load into tables that have primary indexes. You should also use other optimization strategies including aggregating indexes and warm tables. This guide shows you basic instructions for loading data into tables. For an introduction on optimization, see [Get Started](../getting-started.md). For more advanced information about primary and aggregating indexes, see [Work with indexes](../../Guides/working-with-indexes/index.md).

After you load your data, you can start running and optimizing your queries. A typical workflow has the previous steps followed by data and resource cleanup as shown in the following diagram:

<img src="../../assets/images/get_started_workflow.png" alt="The load data workflow includes using the load data wizard or SQL to create a database, engine, and then load data." width="700"/>

For more information on how to register, create a database and an engine, or the other steps in a typical workflow, see [Get Started](../getting-started.md).

## Load data using a wizard

The **Load data** wizard can help you get started loading data from an Amazon S3 bucket using a simple workflow. You can use the wizard to both create an engine and load your data. The wizard also guides you through setting up an AWS connection. To use the wizard, you will need the url of an Amazon S3 bucket. If credentials are required to access the data that you want to load, you will also need an AWS Key ID and your AWS Secret Key. In most steps in the wizard, you can view the SQL commands associated with your selections in the **Load data** main window by selecting **Show SQL script** in the left navigation pane at the bottom of the window.

To use the wizard, use the following steps:
1. Log into the Firebolt workspace.
2. Select the (+) icon from the left navigation pane next to **Databases**.
3. Select **Load data** from the drop-down menu.
4. In the window that appears, set up an AWS connection.
    1. If you are using public data and no credentials are required to access it, provide the url for your Amazon S3 bucket, and select **Next step**.
    2. If credentials are required, Firebolt needs to provide this information to AWS in order to retrieve data on your behalf. Provide the url for your Amazon S3 bucket, AWS Key ID, and AWS Secret Key. The following apply:
        1. The AWS Key ID is an AWS access key that is associated with an AWS user or AWS IAM role. The AWS access key is a 20-character string such as ‘AKIAIOSFODNN7EXAMPLE’.
        2. The AWS Secret Key is an AWS secret access key associated with the user or role associated with the AWS access key. The AWS secret access key is a 40-character string such as ‘wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY’. For more information about these credentials, see [Create Access Key and Secret ID in AWS](creating-access-keys-aws.md).
    3. If you aren’t ready to use your own data, you can use a Firebolt test dataset from the fictional company, [Ultra Fast Gaming Inc](https://help.firebolt.io/t/ultra-fast-gaming-firebolt-sample-dataset/250). Enter the following Amazon S3 bucket into Amazon S3 storage url:
`s3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/`. The name of the data set is `levels.csv`.
5. Select **Next step**.
6. Select an engine to load data. If the engine that you want to use already exists, select it from the dropdown list next to **Select engine for ingestion**. Otherwise, select **Create new engine** from the dropdown list, and do the following:
    1. Enter a name in the **New engine name** text box.
    2. Select an engine size from the drop-down list next to **Node type**. Consider the following when creating a new engine:
        1. If you are loading data and using Firebolt for the first time, use the smallest engine size (S) and a small dataset to try out Firebolt’s capabilities. Refer to the [Get Started](../getting-started.md) guide for more information.
        2. If you want to load larger datasets, Firebolt recommends choosing an engine that can fit your entire dataset into cache. The engine capacities are as follows:
            - A small (S) engine can cache 1.8 TB of data. 
            - A medium (M) engine can cache 3.7 TB. 
            - A large (L) engine can cache 7.5 TB of data. 
            - An extra large (XL) engine can cache 15 TB of data.

        Small and medium engines are available for use right away. If you want to use a large or extra-large engine, reach out to support@firebolt.io. For more information, see [Sizing Engines](../../Guides/operate-engines/sizing-engines.md).
    3. Select the number of compute nodes to use to load your data next to **Number of nodes**. A node is an individual compute unit within a compute cluster. 
        - Using more than one node allows Firebolt to load your data and perform operations on your data in parallel on multiple nodes within a single cluster, which speeds up the data loading process. 
        - A higher number of nodes also means increased costs for compute resources. You can see the total cost per hour for your selection under Advanced settings, given in Firebolt Units (FBU). Each FBU is equivalent to 33 US cents, or ⅓ USD. Find the right balance between cost and speed for your workload. You must use at least one node. 


<!-- For information about using Apache Airflow to incrementally load data chronologically, see [Incrementally loading data with Airflow](incrementally-loading-data.md). -->
