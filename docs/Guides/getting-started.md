---
layout: default
title: Getting started
description: Follow this getting started tutorial to create a database in a Firebolt data warehouse, load a sample data set from Amazon S3, and run queries over the data.
nav_order: 1
parent: Guides
has_toc: true
---

# Get started with Firebolt

{:.no_toc}
Welcome to the beginning of your journey with Firebolt! This tutorial guides you through all of the steps that you need to run a basic workflow which includes setting up your Firebolt account, creating a database and engine, importing a sample dataset, creating indexes, and running a query. If you run into issues, reach out to [support@firebolt.io](support@firebolt.io) for help.

For those seeking a more interactive learning experience, we invite you to join one of our comprehensive, [instructor-led Firebolt workshops](https://www.firebolt.io/on-demand-workshop). These hands-on sessions are crafted to deepen your understanding of Firebolt’s capabilities and how to leverage them for your data analytics needs.

To get started, you must register and create a Firebolt account. Then, you can either use the Firebolt SQL workspace, or use a **Load data** wizard to create a database and engine, and load data. Then, you can run your first query to obtain baseline performance statistics. Next, you can tune your workflow using Firebolt’s optimization strategies to reduce query run times. You can set a primary index and use aggregating indexes to speed up your query times significantly. Lastly, you can export your data to an external table. These steps are illustrated in the following workflow:

<img src="../assets/images/architecture-workflow.png" alt="Get Started" width="500"/>

* Topic ToC
{:toc}

## Use the Load data wizard

The **Load data** wizard guides you through creating a database and engine, and loading data from an Amazon S3 bucket. You can specify basic configurations including what character to use as a file delimiter, which columns to import and their schema. After you load your data, continue your workflow in the SQL workspace to run and optimize a query, and export to an external table. Even though the **Load data** wizard creates a database and engine for you, the following **Create a Database** and **Create an Engine** sections in this guide contains general information about billing for engine runtime and schema. 

When you login for the first time, a welcome window will offer to forward you to the **Load data** wizard. Afterwards, you can select the plus (+) icon next to **Databases** in the left navigation pane and select **Load data**.  For detailed information about how to use the Load data wizard, see [Load data](../Guides/loading-data/loading-data.md). 

## Use the SQL workspace

You can also use the SQL workspace to create a database and engine, and load data. If you use the SQL workspace, you can customize your workflow to handle more unique workflows than with the **Data loading** wizard. 

## Register with Firebolt

<img src="../assets/images/GS-register.png" alt="New DB +" width="500"/>

1. [Register](https://go.firebolt.io/signup) with Firebolt. Fill in your email, name, choose a password, and select ‘Get Started’.

2. Firebolt will send a confirmation to the address that you provided. To complete your registration, select ‘Verify’ in the email to take you to Firebolt’s [login page](https://go.firebolt.io/login). 

3. Type in your email and password and click ‘Log In’.

{: .note}
New accounts receive 600 Firebolt unit (FBU) credits ($200+) to get started exploring Firebolt’s capabilities.

Firebolt’s billing is based on engine runtime, measured in seconds. We also pass through AWS S3 storage costs at the rate of $23 per TB. The amount that you spend is dependent primarily on which engines you use and how long those engines are running.

You can view your total cost in FBU up to the latest second and in $USD up to the latest day. For more information, see the following **Create a Database** section. For more information about costs, see [Data Warehouse Pricing](https://www.firebolt.io/pricing). If you need to buy additional credits, connect Firebolt with your AWS Marketplace account. For more information about AWS Marketplace, see the following section: [Registering though AWS Marketplace section](#register-through-the-aws-marketplace)

## Create a Database

<img src="../assets/images/GS-database.png" alt="New DB +" width="500"/>

Firebolt decouples storage and compute resources so that multiple engines can run computations on the same database. You can also configure different engine sizes for different workloads. These workloads can run in parallel or separately. Because storage is decoupled from storage, you must first create both a database and an engine before you can run your first query. The following instructions show you how to create a database and then an engine, but you can also create the engine first. 

Firebolt’s structure is organized as follows:
* A database holds the elements that you need to run queries such as tables, views and information schema.  
* An [engine](./../Overview/engine-fundamentals.md) provides the compute resources for ingesting data and running queries. For more information on using Firebolt engines and how to select the correct size for your workload, see [Operate engines](./../Overview/../Guides/operate-engines/operate-engines.md).

{: .note}
If you used the **Load data** wizard, Firebolt has already created a database for you, and you can skip the following step.

1) In the left navigation pane, select the **+** to the right **Databases**.

    <img src="../assets/images/Create%20%2B%20(Highlighted).png" alt="New DB +" width="700"/>

2)  Select **Create new database**. 

    <img src="../assets/images/Create%20New%20DB%20From%20%2B.png" alt="New DB" width="700"/>

3)  Enter the name for your database in the **Database Name** field. For this example, use “tutorial_database” as your database name. In Firebolt, the names of engines and databases are **case-sensitive**. If you are using both uppercase and lowercase characters in their names, enclose their name inside double quotes (“) when you refer to them in SQL.

    <img src="../assets/images/Tutorial%20DB.png" alt="New DB Name" width="700"/>

Firebolt creates a new database with the following two default schemas:
* **Public** - A namespace where you can create and manage your database objects including tables, engines and queries. The default schema includes **tables**, **external tables**, and **views**.
* **Information_schema** - A standardized set of read-only views that provide metadata about database objects including tables, engines, cost information, and queries.

You can find these schema by selecting your database under **Databases** in the left navigation pane. Next to the name of your database, select the drop-down arrow to expand and view the schemas and their contents. You can view your total cost in FBU up to the latest second and in $USD up to the latest day in **Information_schema**. 

If you’re using the Firebolt SQL workspace, expand **Information_schema** and then **Views** to show the following:
* **engine_metering_history** - contains information including about billing cost in FBU up to the latest second in **consumed_fbu**.
* **engine_billing** - contains information about billing cost in US dollars up to the latest day in **billed_cost**. 

To see values for the previous costs, select the **More options** icon (<!--- ADD ICON FOR THIS--->) next to either **consumed_fbu** or **billed_cost**, Then select **Preview data**. You can also run a query in the script tab as shown in the following code example:

```sql
SELECT * 
FROM information_schema.engine_metering_history 
```

## Create an Engine

<img src="../assets/images/GS-engine.png" alt="New DB +" width="500"/>

To process a query, you must use an engine. You can either create an engine based on the following recommendations, or use the system engine. You can only use the system engine to run metadata-related queries, but it is always running, so you don’t have to wait for it to start. You can use the system engine to process data in any database. If you create your own engine, there is a small start up time associated with it. 

Firebolt recommends the following initial engine configurations based on where you are in your exploration of Firebolt’s capabilities. An FBU stands for a Firebolt Unit, and is equivalent to 35 US cents. 

Each FBU is related to the amount of time 

| Task                           | Expected Usage |
| :----------------------------  | :----------- --|
| Ingest initial data            |  4-16 FBU      |
| Run test queries               |  8-32 FBU      |
| Find optimal query performance |  32-240 FBU    |
| Find optimal test integrations |  32-240 FBU    |

Engines can cache the following dataset sizes:
* A small (S) engine can cache 1.8 TB of data. 
* A medium (M) engine can cache 3.7 TB. 
* A large (L) engine can cache 7.5 TB of data. 
* An extra-large (XL) engine can cache 15 TB of data. 
  

Small and medium engines are available for use right away. If you want to use a large or extra-large engine, reach out to support@firebolt.io. The default engine configuration uses a small node, which is sufficient for this tutorial. To learn more about how to select the correct engine size for your workload, see [Sizing Engines](../Guides/operate-engines/sizing-engines.md).

By default, when you login to Firebolt’s workspace for the first time, Firebolt creates a SQL workspace in a tab called **Script 1**. The following apply:
* The database that **Script 1** will run using is located directly below the tab name. If you want to change the database, select another database from the drop-down list. 
  
* An engine must be running to process the script in a selected tab. The name and status of the engine that **Script 1** uses for computation is located to the right of the current selected database. To change either the engine or the status, select the drop-down arrow next to the engine name. You can select a new engine and change its status from **Stopped** to **Running** by selecting **Start engine**. If you select **Run** at the bottom of the workspace, the selected engine starts automatically. Select **Stop engine** to change the status to **Stopped**. Firebolt automatically stops your engine after 20 minutes of inactivity.

{: .note}
Because an engine is a dedicated compute node that nobody else can use, you are charged for each second that your engine is **Running**, even if it’s not processing a query. 

If you used the **Load data** wizard, Firebolt has already created an engine for you, and you can skip the following step.

1. Select the **(+)** icon next to **Databases**.

2. Select **Create new engine** from the drop-down list. 

3. Enter the name of your engine in the **New engine name** text box. For this example, enter “tutorial_engine” as your engine name.

## Load Data

<img src="../assets/images/GS-load.png" alt="New DB +" width="500"/>

This tutorial uses Firebolt’s sample dataset, from the fictional “Ultra Fast Gaming Inc” company. This dataset is publicly available and does not require access credentials. If your personal dataset requires access credentials, you will need to provide them. For examples of how to provide access credentials and more complex loading workflows, see [Loading data](../Guides/loading-data/loading-data.md). For more information about AWS access credentials, see [Creating Access key and Secret ID](../Guides/loading-data/creating-access-keys-aws.md)

{: .note}
If you used the **Load data** wizard, skip ahead to the following **Query data** section.

Use [COPY FROM](../../sql_reference/../docs/sql_reference/commands/data-management/copy-from.md) in the SQL workspace to copy data directly from a source into a Firebolt managed table.

1. Enter the following  into the **Script 1** tab to load data using the following steps:
  ```sql
  COPY INTO tutorial FROM 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv' WITH HEADER=TRUE;
  ```
  For examples of more complex loading workflows, see [Load data](../Guides/loading-data/loading-data.md).

2. Select **Run**.
  
3. In the left navigation pane under the **Tutorial_Database**, **Tables** now contains the **tutorial** table. 
  
4. Expand the drop down menu next to **Columns** to view the name and data format of each column. 

5. Select the three dots next to the data type of each column name to open a pop-up that allows you to insert the name of the column into your SQL script. You can also select **Preview data**.

6. To view the contents of  the **tutorial** table, run a SELECT query as shown in the following code example. To run this in a new tab, select the (+) icon next to the **Script 1** tab.
  ```sql
  SELECT
    *
  FROM
    tutorial
  ```
  
7. Select **Run**. The bottom of your workspace includes information about your processing job in the following tabs:
  * The **Results** tab at the bottom of your Firebolt workspace shows the contents returned by your query. After running the previous SELECT statement, the **Results** tab should display column names and values for the data in the tutorial. 
     * Select the filter icon (<img src="../assets/images/filter-icon.png" alt="AggIndex" width="12"/>) to change which columns are shown.
     * Select the **More options** icon (<img src="../assets/images/more options icon.png" alt="AggIndex" width="12"/>) to export the contents of the **Results** tab to a JSON or CSV file.
  * The Statistics tab shows information about running your query including how long it took to run and its status. After running the previous SELECT statement, the **Statistics** tab shows the status of the statement, its STATUS as having succeeded or failed, how long it took to run the query, the number of rows processed, the amount of data scanned, and <HOT QUERY what is it?>
     * Select the **More options** icon (<img src="../assets/images/more options icon.png" alt="AggIndex" width="12"/>) to export the contents of the **Statistics** tab to a JSON or CSV file.
  * The **Query Profile** tab contains metrics for each operator used in your query and a **Query id**.  Select an operation to view its metrics. These metrics include the following:
     * The output cardinality - the number of rows that each operator produced.
     * The thread time - the sum of the wall clock time that threads spent to run the selected operation across all nodes.
     * The CPU time - the sum of the time that threads that ran the operator were scheduled on a CPU core.
     * The output types - the data types of the result of the operator.

You can use these metrics to analyze and measure the efficiency and performance of your query. For example, If the CPU time is much smaller than thread time, the input-output (IO) latency may be high or the engine that you are using may be running multiple queries at the same time. For more information, see [Example with ANALYZE](../sql_reference/commands/queries/explain.md). 

  * The **Engine monitoring** tab shows monitoring information including the percent CPU, memory, disk use and cache read. Information is shown from the last 5 minutes by default. Select a different time interval from the drop-down menu next to **Last 5 minutes**. You can also select the **Refresh** icon next to the drop-down menu to update the graphical information.
  * The **Query history** tab shows detailed information associated with each query, listed by its **Query id**. This information includes the query status, start time, number of rows and bytes scanned during the load, user and account information. You can choose the following options at the top of the bottom panel:
    * Select the **Refresh** icon to update the query history and ID.
    * Select the filter icon (<img src="../assets/images/filter-icon.png" alt="AggIndex" width="12"/>) to remove or add columns to display. 
    * Select the **More options** icon (<img src="../assets/images/more options icon.png" alt="AggIndex" width="12"/>) to export the contents of the Query history tab to a JSON or CSV file.
  
For more information about Firebolt’s SQL workspace, see <!--- ADD DEVELOP WORKSPACE LINK--->

## Run Query

<img src="../assets/images/GS-query.png" alt="New DB +" width="500"/>

1. Select the (+) icon next to the Script 2 tab to open a new tab.

2. Enter the following simple query, which fetches a list of databases associated with your account:
  ```sql
  SHOW DATABASES;
  ```

3. Select **Run** to process the query. Firebolt uses the engine listed to the right of your database to run your query and its status of **Running** or **Stopped**. You can select a different engine from the dropdown menu next to the engine (<img src="../assets/images/engine-icon.png" alt="AggIndex" width="12"/>) icon. 
   
   If your engine is **Stopped**, Firebolt may prompt you to start your engine. Select **Start Engine**. Engine startup typically requires a few moments to complete, as Firebolt prepares your environment for data analysis.

For more information about Firebolt’s SQL workspace, see <!--- ADD DEVELOP WORKSPACE LINK--->

## Optimize your workflow

<img src="../assets/images/GS-optimize.png" alt="New DB +" width="500"/>

Firebolt uses a number of optimization strategies to reduce query times. Over small datasets like those specified in this guide, the uplift may not be noticeable. However, these strategies can dramatically improve query performance for larger datasets. The following sections discuss how [primary indexes](./getting-started.md#primary-indexes), [partition keys](./getting-started.md#partition-keys), and [aggregating indexes](./getting-started.md#aggregating-indexes) to do the following:
* Reduce the amount of data that the query scans.
* Pre-calculate values that are used repeatedly during computations.

### Primary Indexes

One of Firebolt’s key optimization strategies is to select a primary index for columns that are used frequently in WHERE, JOIN, GROUP_BY, and clauses used for sorting. In Firebolt, a primary index is a type of sparse index. Thus, selecting the best primary index can reduce query run times significantly by reducing the data set that the query searches over. Selecting primary indexes also allows Firebolt to manage updates, deletions and insertions to tables and provide optimal query performance.

If you have more than one primary index, the order that they are listed is important. Specify the column that has a large number of unique values, or high cardinality, first, followed by columns with lower cardinality. A sort order with the previous characteristics allows Firebolt to prune, or eliminate irrelevant data, so that it doesn’t have to scan it in query processing. Pruning significantly enhances query performance.

You can create a primary index **only** when you create a table. If you want to change the primary index, you must create a new table. The following example shows how to use [CREATE TABLE](../../sql_reference/commands/../../docs/sql_reference/commands/data-definition/create-fact-dimension-table.md) to create a new `levels` table, define the schema, and set two primary indexes:

```sql
CREATE TABLE IF NOT EXISTS levels (
    "LevelID" INT,
    "Name" TEXT,
    "GameID" INT,
    "LevelType" TEXT,
    "MaxPoints" INT,
    "PointsPerLap" DOUBLE,
    "SceneDetails" TEXT
)
PRIMARY INDEX "LevelID", "Name";
```

In the previous code example, the primary index contains two values. The first value, LevelID, is required in order to create a primary index. The second value, `Name`, and any following values are optional. Firebolt will use all listed primary indexes to optimize query scans. If Name has lower cardinality than `LevelID`, then Firebolt can optimize these indexes to eliminate scanning over irrelevant data.  For more information about primary indexes and sort order, see [Primary Indexes](./working-with-indexes/using-primary-indexes.md).

To read data into the `levels` table, enter the following into a new script tab:
```sql
COPY INTO levels
FROM 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv'
WITH TYPE = CSV
HEADER = TRUE;
```
### Aggregating Indexes

Another key optimization strategy includes pre-calculating aggregate values for columns that are frequently used in functions that combine data such as COUNT, SUM, MAX, MIN, AVG, JOIN, and GROUP BY. Rather than computing aggregate values each time they are used in a calculation, the results are accessed from storage, which helps run queries quickly and saves compute resources.

An aggregating index combines columns into a statistical result. You can calculate an aggregate index on an entire table, or more efficiently, calculate them over a subset of table columns. You can also use your knowledge of which dimensions and aggregate functions are used most often for your use case to predefine what table dimensions and which aggregate functions to use. 

Once you create aggregate indexes, Firebolt maintains them automatically for you. If you load new data into your table or alter it, your aggregate indexes are automatically updated. You can also have multiple aggregate indexes for a single table. When you query a table with multiple aggregate indexes, Firebolt will automatically select the best index to use to optimize performance.

From the **tutorial** table that you created in the previous step, assume you want to run a query to look at the AVG(NumberOfLaps), grouped by LevelType. The following example code shows you how to create an aggregating index **levels_agg_idx** on the **LevelType** column to pre-calculate the average number of laps for each level. 

```sql
CREATE AGGREGATING INDEX
  levels_agg_idx
ON tutorial (
  "LevelType" 
  , AVG("NumberOfLaps")
  );
```

After you run the script,  the ``levels_agg_idx` aggregate index listed in the left navigation pane under **Indexes** in the **tutorial** table. Any queries that run over the tutorial table that use an average of the **NumberOfLaps** column grouped by **LevelType** will now use the levels_agg_idx index instead of reading the entire table to calculate it.

For more information, see [Aggregating indexes](./working-with-indexes/using-aggregating-indexes.md).

### Clean up data and resources

<img src="../assets/images/GS-cleanup.png" alt="New DB +" width="500"/>

After you’ve completed the steps in this guide, avoid incurring costs associated with the exercises by doing the following:
* [Stop any running engines.](#stop-any-running-engines)
* [Remove data from storage.](#remove-data-from-storage)

#### Stop any running engines

Firebolt shows you the status of your current engine next to the engines icon ((<img src="../assets/images/engine-icon.png" alt="AggIndex" width="12"/>)) under your script tab as either **Stopped** or **Running**. To shut down your engine, select your engine from the drop-down list next to the name of the engine, and then select one of the following:
* Stop engine - Allow all of the currently running queries to finish running and then shut down the engine. Selecting this option will allow the engine to run for as long as it takes to complete all queries running on the selected engine.
* Terminate all queries and stop - Stop the engine and stop running any queries. Selecting this option stops the engine in about 20-30 seconds.  

#### Remove data from storage

To remove a table and all of its data, enter [DROP TABLE](../../sql_reference/commands/data-definition/../../../docs/sql_reference/commands/data-definition/drop-table.md) into a script tab, as shown in the following code example:

`DROP TABLE levels`

To remove a database and all of its associated data, do the following:
a. Select the database from the left navigation bar. 
b. Select the more options (<img src="../assets/images/more options icon.png" alt="AggIndex" width="12"/>) icon.
c. Select **Delete database**. Deleting your database will permanently remove your database from Firebolt. You cannot undo this action.
d. Select **Delete**.

### Export data 

If you want to save your data outside of Firebolt, you can use [COPY TO](./../sql_reference/commands/data-management/copy-to.md) to export data to an external table. This section shows how to set the minimal AWS permissions and use a COPY TO to export data to an [AWS S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html). You may have to reach out to your administrator to obtain or change AWS permissions.

a. Set permissions to write to an AWS S3 bucket
  
  Firebolt must have the following permissions to write to an AWS S3 bucket:
    i. AWS access key credentials. The credentials must be associated with a user with permissions to write objects to the bucket. Specify access key credentials using the following syntax: 
    
    ```sql
    CREDENTIALS = (AWS_KEY_ID = '<aws_key_id>' AWS_SECRET_KEY = '<aws_secret_key>')
    ```
    In the previous credentials example, `<aws_key_id>` is the AWS access key id associated with a user or role. An access key has the following form: `AKIAIOSFODNN7EXAMPLE`.
    
    `<aws_secret_key>` is the AWS secret key. A secret key has the following form: `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`.

    ii. An AWS IAM policy statement attached to a user role. Firebolt requires the following minimum permissions in the IAM policy: 
    ```sql
      {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:Get*",
                "s3:List*",
                "s3:PutObject",
                "s3:DeleteObject"
            ],									
            "Resource": [
                "arn:aws:s3:::my_s3_bucket",
                "arn:aws:s3:::my_s3_bucket/*"
            ]
        }
    ]
}
    ```
For more information about AWS access keys and roles, see [Creating Access Key and Secret ID in AWS](./loading-data/creating-access-keys-aws.md)

a. **Export to an AWS S3 bucket**
Use [COPY TO](../../sql_reference/commands/../../docs/sql_reference/commands/data-management/copy-to.md) select all the columns from a table and export to an AWS S3 bucket as shown in the following code example. 
```sql
COPY (SELECT * FROM test_table)
  TO 's3://my_bucket/my_fb_queries'
  CREDENTIALS = (AWS_ROLE_ARN='arn:aws:iam::123456789012:role/my-firebolt-role');
```
In the previous code example, the role ARN [(Amazon Resource Name)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) identifies the AWS IAM role that specifies the access for users or services. An ARN follows the following structure: arn:aws:iam::account-id:role/role-name. Because TYPE is omitted from COPY TO, the file or files will be written in the default CSV format. Because `COMPRESSION` is also omitted, the output data is compressed using GZIP (`*.csv.gz`) format.

Firebolt assigns a query ID, that has the following example format `16B903C4206098FD`, to the query at runtime. If the size of the compressed output exceeds the default of 16 MB, Firebolt writes multiple GZIP files. In the following example, the size of the output is 40 MB, so Firebolt writes 4 files.

```sql
s3://my_bucket/my_fb_queries/
  16B903C4206098FD_0.csv.gz
  16B903C4206098FD_1.csv.gz
  16B903C4206098FD_2.csv.gz
  16B903C4206098FD_3.csv.gz
```

See [COPY TO](./../sql_reference/commands/data-management/copy-to.md) for more information. 

#### Register through the AWS Marketplace

If you have exhausted your initial $200 credit, you can continue to use Firebolt after registering through the [AWS Marketplace](https://aws.amazon.com/marketplace). You must set up an account for billing in order to continue using Firebolt’s engines to run queries.

**To register**

1. On the [Firebolt Workspace page](https://go.firebolt.io/), select the **Configure**((<img src="../assets/images/configure-icon.png" alt="AggIndex" width="12"/>)) icon from the left navigation pane. 
2. Under **Organization settings**, select **Billing**.
3. Click **Connect to AWS Marketplace** to take you to the Firebolt page on AWS Marketplace.
4. On the AWS Marketplace page, click the **View Purchase Options** on the top right hand corner of the screen.
5. Click **Setup Your Account**.

Your account should now be associated with AWS Marketplace.

### Next Steps

Now that you have successfully created your first engine and database, ran your first query, created indexes, copied data into, and exported data out of Firebolt, you can continue exploring Firebolt’s capabilities.

#### Learn more about Firebolt
* Learn about Firebolt’s unique [architecture](../Overview/architecture-overview.md).
* Learn more about creating tables and [managing your data](../Overview/data-management.md) in order to let Firebolt provide the fastest query times. 
* Learn about the [engines](../Overview/engine-fundamentals.md) that Firebolt uses to process queries and how to select the right size.
* Learn how to [load](../overview/../Guides/loading-data/loading-data.md) different kinds of data.
* Learn more about [querying data](../overview/../guides/../Guides/query-data/index.md).
* Learn more about using [indexes](../overview/using-indexes.md) to optimize your query times.
* Learn how to [set up your organization](../Guides/managing-your-organization/index.md) to use Firebolt.
* Learn how to [integrate Firebolt](../guides/../Guides/integrations/integrations.md) with third party tools and applications.


















