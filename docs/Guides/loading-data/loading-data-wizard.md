---
layout: default
title: Load data using a wizard
description: Understand options for loading data using a data load wizard.
parent: Load data
nav_order: 3
has_children: false
has_toc: true
---


# Load data using a wizard

The **Load data** wizard can help you get started loading data from an Amazon S3 bucket using a simple workflow. You can use the wizard to both create an engine and load your data. The wizard also guides you through setting up an AWS connection. To use the wizard, you will need the uniform resource locator (URL) of an Amazon S3 bucket. If credentials are required to access the data that you want to load, you will also need an AWS Key ID and your AWS Secret Key. In most steps in the wizard, you can view the SQL commands associated with your selections in the **Load data** main window by selecting **Show SQL script** in the left navigation pane at the bottom of the window.

To use the wizard, use the following steps:
1. Log into the Firebolt workspace.
2. Select the (+) icon from the left navigation pane next to **Databases**.
3. Select **Load data** from the drop-down menu.
4. In the window that appears, set up an AWS connection.
    1. If you are using public data and no credentials are required to access it, provide the URL for your Amazon S3 bucket, and select **Next step**.
    2. If credentials are required, Firebolt needs to provide this information to AWS in order to retrieve data on your behalf. Provide the URL for your Amazon S3 bucket, AWS Key ID, and AWS Secret Key. The following apply:
        1. The AWS Key ID is an AWS access key that is associated with an AWS user or AWS IAM role. The AWS access key is a 20-character string such as ‘AKIAIOSFODNN7EXAMPLE’.
        2. The AWS Secret Key is an AWS secret access key associated with the user or role associated with the AWS access key. The AWS secret access key is a 40-character string such as ‘wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY’. For more information about these credentials, see [Create Access Key and Secret ID in AWS](creating-access-keys-aws.md).
    3. If you aren’t ready to use your own data, you can use a Firebolt test dataset from the fictional company, [Ultra Fast Gaming Inc](https://help.firebolt.io/t/ultra-fast-gaming-firebolt-sample-dataset/250). Enter the following Amazon S3 bucket into Amazon S3 storage URL:
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
  
    4. Select the number of clusters next to **Number of clusters**. A cluster is a group of nodes that work together. The following apply:

        - If you increase the number of clusters, you add the number of compute nodes that you selected for each added cluster.
        - You can use multiple clusters to speed up data loading and also to provide high availability.
        - If one cluster experiences performance issues, the other clusters are not affected by it.
        - A higher number of clusters also means increased costs for compute resources.
  
        You can see the total cost per hour for your selection under **Advanced settings**, given in Firebolt Units (FBU). Each FBU is equivalent to 33 US cents, or ⅓ USD. Find the right balance between cost and speed for your workload. You must use at least one cluster.

    5. Select the down arrow next to **Advanced settings** for more options for your engine including setting a time to stop the engine after a period of inactivity.

7. Select the data that you want to load. Firebolt’s **Load data** wizard currently supports files in both CSV and Parquet formats. The contents of your S3 bucket are shown automatically in the next window after your engine loads them. You can toggle **Supported files** to filter the list to show only supported file formats. If you are using Firebolt’s test data set, select the box next to `levels.csv`.
8. Select **Next step**.
9. Specify the table inside a database that you want to load your data into. Select an existing database from the drop-down list next to **Select database** or **Create new database**.
    1. If you created a new database, enter a new database name and a new table to load your data into. Select **Next step**.
    2. If you selected an existing database, select the table in the database from the drop-down list next to **Select table**, or **Create new table**. Provide a new table name and select **Next step**.

10. You can preview your data in the **Format data** step using the default formatting and error handling, or after using a custom configuration.

    To change how to format your data, toggle off Use default formatting to show custom options. You can specify custom formatting including a file delimiter, quote character, and escape character.

    To change how to handle errors, toggle off Use default error handling. You can specify a file to write errors to with AWS credentials and how many errors you want to allow when you load your data.

11. Select **Next step**.
12. Map the values in your data to columns into the target table. Firebolt automatically detects the schema of your data and displays information including the detected column names, type, and a preview of the data in the next window. By default, each column has a checkbox next to its name. Deselect the box if you don’t want to load the column. You can adjust the schema for the following items:
    1. Data type - you can change the [data type](../../sql_reference/data-types.md) of the column.
    2. **Nullable** - toggle this switch to `ON` if the columns in your data can contain `NULL` values. If this value is toggled off for a column, and that column contains `NULL` values, then the wizard will generate an error and stop loading.
    3. **Primary index** - toggle this switch to `ON` for the columns you want to include in your primary index.

        One of Firebolt’s key optimization strategies is to use a primary index that ties to columns that are used frequently in `WHERE`, `JOIN`, `GROUP_BY`, and other clauses used for sorting. Selecting the best primary index, which is a sparse index, can reduce query run times significantly by reducing the data set that the query scans. A primary index also allows Firebolt to manage updates, deletions and insertions to tables and provide optimal query performance.

        If you multiple columns as a primary indexes, they will be added in sort order. For example, if you select `column_1` first, then select `column_3`, then `column_3` will be added as a primary index after `column_1`. This means `column_1` will be used first as a sparse index, followed by `column_3`. If you choose more than one primary index, the order of sorting appears next to the toggle switch under the **Primary Index** column. In the previous example, the number `1` appears next to `column_1` and a number `2` appears next to `column_3`.

        To achieve optimal results, choose indexes in the order of their cardinality, or the number of unique values. Start with the column that has the highest number of unique values as your first primary index, followed by the column with the next highest cardinality. For more information about how to choose a primary index, see [Primary indexes](../../Guides/working-with-indexes/using-primary-indexes.md).

13. Select **Next step**.
14. The **Review configuration** window displays your selections in SQL code. If you want to change the configuration, you must go back through the **Load data** wizard workflow to the section that you want to change and amend your selection. You cannot edit the SQL code in the **Review configuration** window.
15. Select **Run ingestion** to load your data. The **Load data** wizard completes and your configuration will run in the Firebolt SQL workspace. The main window contains the SQL script that configures your load data selections, and may contain several queries.
16. You can view the results of each query that was configured by the **Load data** wizard in the bottom window under **Results**. If you need to edit the queries, you can enter the change into the SQL editor directly and select **Run**.
17. You can view information about your query in the **Statistics** tab. This information contains the status of the query, how long it took to run, and the number of rows processed during load.
18. You can view metrics in the **Query Profile** tab for each operator used in your query. Select an operation to view metrics. These metrics can include the following:
    1. The output cardinality - the number of rows each operator produced.
    2. The thread time - the sum of the wall clock time that threads spent to run the selected operation across all nodes.
    3. The CPU time - the sum of the time that threads that ran the operator were scheduled on a CPU core.
    4. The output types - the data types of the result of the query.
    
    You can use these metrics to analyze and measure the efficiency and performance of your query. For example, If the CPU time is much smaller than thread time, the input-output (IO) latency may be high or the engine that you are using may be running multiple queries at the same time. For more information, see [Example with ANALYZE (Beta)](../../sql_reference/commands/queries/explain.md).

19. You can view monitoring information including the percent CPU, memory, disk use and cache read in the **Engine monitoring** tab. Information is shown from the last 5 minutes by default. Select a different time interval from the drop-down menu next to **Last 5 minutes**. You can also select the **Refresh** icon next to the drop-down menu to update the graphical information.
20. You can view detailed information associated with each query in the **Query history** tab. This information includes the query status, start time, number of rows and bytes scanned during the load, user and account information. You can choose the following options at the top of the bottom panel:
    1. Select the **Refresh** icon to update the query history and ID.
    2. Select the filter icon (<img src="../../assets/images/filter-icon.png" alt="filter icon" width="12"/>) to remove or add columns to display.
    3. Select the **More options** icon (<img src="../../assets/images/more options icon.png" alt="more options icon" width="12"/>) to export the contents of the Query history tab to a JSON or CSV file.