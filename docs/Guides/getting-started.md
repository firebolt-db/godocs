---
layout: default
title: Get started
description: Follow this getting started tutorial to create a database in a Firebolt data warehouse, load a sample data set from Amazon S3, and run queries over the data.
nav_order: 1
parent: Guides
has_toc: true
---
# Getting started tutorial
{:.no_toc}
Welcome to the beginning of your journey with Firebolt! This guide is designed to smoothly onboard you to Firebolt and guide you through the initial setup of your Firebolt account. You'll learn to create your first database, set up an engine optimized for high-speed analytics, and import a sample dataset from Amazon S3 into your Firebolt environment. Following that, we'll dive into executing some basic analytics queries to demonstrate the power and speed of Firebolt analytics.

For those seeking a more interactive learning experience, we invite you to join one of our comprehensive, instructor-led Firebolt workshop. These hands-on session are crafted to deepen your understanding of Firebolt's capabilities and how to leverage them for your data analytics needs. Secure your spot [here](https://www.firebolt.io/on-demand-workshop) and elevate your Firebolt skills.

1. Topic toC
{:toc}

## Create a Firebolt Account
1. Select 'Get Started' after completing the registration form at [go.firebolt.io](go.firebolt.io)

[ADD UPDATE IMAGES - DEV IN FLIGHT]

2. Select 'Verify' on the confirmation email you recieve

[ADD UPDATE IMAGES - DEV IN FLIGHT]

3. Type in your email and password and click 'Log In'

[ADD UPDATE IMAGES - DEV IN FLIGHT]

4. Optionally, you can rename your account if you choose. 

And that's it! You're ready to get started with Firebolt. 

{: .note}
New accounts get 600 Firebolt credits ($200+) to get started exploring with Firebolt. Once you run out of credits, we recommend you to connect Firebolt with your AWS Marketplace account so you can get back to making the most of Firebolt. See [Registering though AWS Marketplace](https://special-disco-436d3e6a.pages.github.io/Guides/getting-started.html#register-through-AWS-Marketplace) below.

## Getting Started with Your First Database and Engine
Embarking on your data journey with Firebolt begins with creating a *database* and a Firebolt *engine* which can be tailored to your specific workload needs. An engine in Firebolt is essentially the powerhouse, providing the compute resources dedicated to a database for executing tasks (see [Understanding Engines](https://special-disco-436d3e6a.pages.github.io/Overview/understanding-engine-fundamentals.html) to learn more). By default, every database is equipped with one general purpose engine capable of writing to the Firebolt file format (F3) for both data ingestion and analytics queries. We use that single-engine set up in this tutorial. For more information on using Firebolt engines, see [Work with engines](./working-with-engines/working-with-engines.md).


**Steps to Create Your Database and Engine:**
1. Click the **+** next to **Databases**
![image](https://github.com/firebolt-analytics/firebolt-docs-staging/assets/9532728/c3b90bc7-5d9d-4ef5-8dc5-61e2d14d048a)

2. Click **Create new database**. 
![image](https://github.com/firebolt-analytics/firebolt-docs-staging/assets/9532728/192ed3a0-811f-46a5-a95d-845ad0557558)

3. Enter the name for your database in the **Database Name** field. For the purposes of this guide, we'll use "Tutorial_Database" as our database name.
![image](https://github.com/firebolt-analytics/firebolt-docs-staging/assets/9532728/95fd38aa-4533-44a1-893a-4b14c49f274f)


4. Click the **+** next to **Databases** again.
![image](https://github.com/firebolt-analytics/firebolt-docs-staging/assets/9532728/c3b90bc7-5d9d-4ef5-8dc5-61e2d14d048a)

5. Click **Create new engine**.
![image](https://github.com/firebolt-analytics/firebolt-docs-staging/assets/9532728/fb932444-d246-45e1-ba50-1937788d9aad)

6. Enter the name of your engine in the **New engine name** field. For the purposes of this guide, we'll use "Tutorial_Engine" as our engine name.
![image](https://github.com/firebolt-analytics/firebolt-docs-staging/assets/9532728/c4e19be7-d880-442b-9570-5887eddef3f2)

{: .note}
The default configuration is a small node. This will be more than enough for this tutorial. 

## Executing Your First Query
Before we dive into ingesting sample data, let's familiarize ourselves with the SQL workspace of your database. This initial step not only demonstrates how to activate your engine but also acquaints you with the process of executing queries within Firebolt. For a deeper dive into the SQL workspace and its capabilities, our [Query Data](./query-data/using-the-sql-editor.md) guide is an excellent resource.

**Steps to Access Your Database, Activate the Engine, and Execute Your First Query:**
1. From the **Database page**, locate the database you've previously created ("Tutorial_Database"). Click the **Open in SQL workspace icon** (**>_**).

2. Upon entering the SQL workspace, you'll be greeted by the "Script 1" tab. This is where you'll craft your queries. To get started, enter the following simple query, designed to fetch a list of databases associated with your account:

```sql
SHOW DATABASES;
```  

3. Select **Run Script** to execute the query. You'll notice the **Using** dropdown menu, which displays the engine Firebolt employs to run your script. In this instance, it will indicate "Tutorial_Engine".

{: .note}
At this time, Firebolt may prompt you to initiate your engine if it's not already active. Select **Start Engine** to start your engine. Engine startup typically requires a few moments to complete, preparing your environment for data analysis.

By following these steps, you've not only executed your first query but also successfully set the stage for more advanced data exploration. This is just the beginning of what's possible with Firebolt - let's continue by adding some data. 

## Add Data
Now that you can select databases, select engines, and run queries, let's add some sample data. For this tutorial we will explore adding data in two ways; 
1. Creating and using an external table [TODO ADD SECTION HYPERLINK]
2. Use `COPY FROM` [TODO ADD SECTION HYPERLINK]

{: .note}
This tutorial uses Firebolt's sample dataset, from the fictional gaming company "Ultra Fast Gaming Inc." This dataset is publicly available with the access credentials shared below.

### Creating and using an external table
#### Step 1: Create an External Table
An *external table* is a special, virtual table that serves as a connector to your data source. After the external table is created, you ingest data by running an `INSERT` command from that external table into a *fact table* or *dimension table*. The `INSERT` command must run on a general purpose engine. After the data is available in fact and dimension tables, you can run analytics queries over those tables using any engine. 

{: .note}
Although it's possible, we don't recommend running analytics queries on external tables. For more information on working with external tables, see [Work with external tables](https://special-disco-436d3e6a.pages.github.io/Guides/loading-data/working-with-external-tables.html).

**Creating Your External Table:**
1. Choose the plus symbol (**+**) next to script tab to create a new script tab in the SQL workspace.

![image](https://github.com/firebolt-analytics/firebolt-docs-staging/assets/9532728/d5309d2b-70d3-4901-9321-6d57c0cf0665)

2. Copy and paste the query below into the new tab.

```sql
CREATE EXTERNAL TABLE IF NOT EXISTS ex_levels (
-- Column definitions map to data fields
-- in the source data file and are specified
-- as sources in the INSERT INTO statement for ingestion. 
    LevelID INTEGER,
    GameID INTEGER,
    Level INTEGER,
    Name TEXT,
    LevelType TEXT,
    NextLevel INTEGER NULL,
    MinPointsToPass INTEGER,
    MaxPoints INTEGER, 
    NumberOfLaps INTEGER,
    MaxPlayers INTEGER,
    MinPlayers INTEGER,
    PointsPerLap REAL,
    MusicTrack TEXT,
    SceneDetails TEXT,
    MaxPlayTimeSeconds INTEGER
) 

URL = 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/'

-- CREDENTIALS = ( AWS_KEY_ID = '******' AWS_SECRET_KEY = '******' )
OBJECT_PATTERN = 'help_center_assets/firebolt_sample_dataset/levels.csv'
TYPE = (CSV SKIP_HEADER_ROWS = 1);
```  

{: .note} 
'URL =' specifies the data source in S3. All files in the location that match the 'OBJECT_PATTERN' and will be processed during ingestion. 'CREDENTIALS =' specify a role or AWS key credentials with permission to read from the S3 location. These credentials are commented out for this tutorial because the bucket is publicly accessible.

3. Click **Run**. When completed the external table `ex_levels` appears on the object panel of the database.  

![image](https://github.com/firebolt-analytics/firebolt-docs-staging/assets/9532728/4957ede5-d9e9-47b5-b550-77f6a2be8f77)

5. [Optional] Choose the vertical ellipses next to script, choose **Rename script**, enter a name (for example, *MyExTableScript*) and then press ENTER to update the name.

![image](https://github.com/firebolt-analytics/firebolt-docs-staging/assets/9532728/ea7359d0-3815-42a1-9823-61923faf19dc)
![image](https://github.com/firebolt-analytics/firebolt-docs-staging/assets/9532728/207e9595-40f8-4d1f-910f-0a0e685843be)

#### Step 2: Create a Fact Table
In this step, you'll create a Firebolt fact table called `levels`, which you use in the next step as the target for an `INSERT INTO` command. 

When creating a fact or dimension table, you will specify a *primary index*. Firebolt uses the primary index when it ingests data so that it is saved to S3 for highly efficient pruning and sorting when the data is queried. A primary index is required when creating a fact table, and recommended for dimension tables. For more information, see [Using primary indexes](./working-with-indexes/using-primary-indexes.md). 

The fact table that we create in this step specifies the `LevelID` column for the primary index. For more information about choosing columns for a primary index, see [How to choose primary index columns](/using-indexes/using-primary-indexes.md#how-to-choose-primary-index-columns).

**To create a fact table**
1. Create a new script tab.  

2. Copy and paste the query below into the script tab.  
```sql
CREATE FACT TABLE IF NOT EXISTS levels
(
    LevelID INTEGER,
    GameID INTEGER,
    Level INTEGER,
    Name TEXT,
    LevelType TEXT,
    NextLevel INTEGER NULL,
    MinPointsToPass INTEGER,
    MaxPoints INTEGER, 
    NumberOfLaps INTEGER,
    MaxPlayers INTEGER,
    MinPlayers INTEGER,
    PointsPerLap REAL,
    MusicTrack TEXT,
    SceneDetails TEXT,
    MaxPlayTimeSeconds INTEGER,
    SOURCE_FILE_NAME TEXT,
    SOURCE_FILE_TIMESTAMP TIMESTAMP
) 
PRIMARY INDEX LevelID;
```  

3. Click **Run Script**. When finished, the table `levels` appears on the object panel of the database.  

#### Step 3: Use INSERT INTO to ingest data
You can now use the `INSERT INTO` command to copy the data from the external table into the fact table. During this operation, Firebolt ingests the data from your source into Firebolt.

**To run an `INSERT` command that ingests data**
1. Create a new script tab.
2. Copy and paste the query below into the script tab.  
```sql
INSERT INTO levels
SELECT
    LevelID,
    GameID,
    Level,
    Name,
    LevelType,
    NextLevel,
    MinPointsToPass,
    MaxPoints, 
    NumberOfLaps,
    MaxPlayers,
    MinPlayers,
    PointsPerLap,
    MusicTrack,
    SceneDetails,
    MaxPlayTimeSeconds,
    $source_file_name, 
    $source_file_timestamp 

FROM ex_levels;
```
3. Choose **Run Script**.  
The query results pane indicates a **Status** of **Running** as shown below.  
![](../assets/images/running.png)  
The **Status** changes to **Success** when the ingestion is complete as shown below.
![](../assets/images/success.png)

[NEEDS UPDATED SCREENSHOTS]

#### Step 4: Query the ingested data
Now that the data has been ingested into the `levels` table, you can run analytics queries over the table that benefit from the speed and efficiency of Firebolt.

To verify that you inserted the data into the table, run a simple `SELECT` query like the one below.

```sql
SELECT
  *
FROM
  levels
```
The values shown in the query results pane should be similar to those shown below.
![](../assets/images/results.png)

[NEEDS UPDATED SCREENSHOTS]

### Using COPY FROM [IN PROGRESS, WILL REORDER ONCE TUTORIAL IS VALIDATED]
`COPY FROM` allows you to copy data directly to a Firebolt table. For more information, see COPY FROM [TODO LINK]

1. Choose the plus symbol (**+**) next to **Script 1** to create a new script tab, **Script 2**, in the SQL workspace.
2. Copy and paste the query below into the **Script 2** tab.

```sql
CREATE FACT TABLE IF NOT EXISTS tutorial (
 LevelID INTEGER,
 GameID INTEGER,
 Level INTEGER,
 Name TEXT,
 LevelType TEXT,
 NextLevel INTEGER NULL,
 MinPointsToPass INTEGER,
 MaxPoints INTEGER, 
 NumberOfLaps INTEGER,
 MaxPlayers INTEGER,
 MinPlayers INTEGER,
 PointsPerLap REAL,
 MusicTrack TEXT,
 SceneDetails TEXT,
 MaxPlayTimeSeconds INTEGER,
 LevelIcon TEXT
);


COPY INTO tutorial FROM 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/';
``` 
You can specify a role or AWS key credentials with permission to read from the S3 location using 'CREDENTIALS =' but we are using a publicly accessible datset for this tutorial. 

3. To verify that you inserted the data into the table, run a simple `SELECT` query like the one below.

```sql
SELECT
  *
FROM
  tutorial
```

And that's it! You've successfully copied data from S3 into a Firebolt table. 

## Next Steps
Now that you have successfully created your first engine and database in Firebolt, run your first query, and copied data to Firebolt you can start exploring what else Firebotl has to offer! Below are a few examples to get you started. 

### Configure an aggregating index
An aggregating index enables you to take a subset of table columns and predefine dimensions and measures to aggregate. Many aggregations are supported&mdash;from `SUM`, `MAX`, and `MIN` to more complex aggregations such as `COUNT` and `COUNT(DISTINCT)`. At query runtime, instead of calculating the aggregation on the entire table and scanning all rows, Firebolt uses the pre-calculated values in the aggregating index. For more information, see [Aggregating indexes](./working-with-indexes/using-aggregating-indexes.md).

From the `levels` fact table that you created in the previous step, assume you want to run a query to look at the `AVG(NumberOfLaps)`, grouped by `LevelType`. You can create an aggregating index to speed up these queries by running the statement below.

```sql
CREATE AGGREGATING INDEX
  levels_agg_idx
ON levels (
  LevelType 
  , AVG(NumberOfLaps)
  );
```

After you run the script, you see the `levels_agg_idx` index listed in the object pane. Any queries that run over the `levels` table that combine any of these fields and aggregations defined in the index will now use the index instead of reading the entire table.

### Use COPY TO to export data to S3
The example below shows a `COPY TO` statement with minimal parameters that specifies an `AWS_ROLE_ARN`. Because `TYPE` is omitted, the file or files will be written in CSV format, and because `COMPRESSION` is omitted, they are compressed using GZIP  (`*.csv.gz`).

```sql
COPY (SELECT * FROM test_table)
  TO 's3://my_bucket/my_fb_queries'
  CREDENTIALS = (AWS_ROLE_ARN='arn:aws:iam::123456789012:role/my-firebolt-role');
```

Firebolt assigns the query ID `16B903C4206098FD` to the query at runtime. The compressed output is 40 MB, exceeding the default of 16 MB, so Firebolt writes 4 files as shown below.

```bash
s3://my_bucket/my_fb_queries/
  16B903C4206098FD_0.csv.gz
  16B903C4206098FD_1.csv.gz
  16B903C4206098FD_2.csv.gz
  16B903C4206098FD_3.csv.gz
```
See [COPY TO](https://special-disco-436d3e6a.pages.github.io/sql_reference/commands/data-management/copy-to.html) for more information. 

## Register through AWS Marketplace
This registration is a prerequisite for starting engines and running queries after your initial trial credits. 

**To register**
1. On the [Firebolt page](https://go.firebolt.io/login?redirect=%2F), navigate to the **Configuration menu**. Click **Billing**. 

2. Click **Connect to AWS Marketplace**. This will take you to the Firebolt page available on AWS Marketplace.

3. On the AWS Marketplace page, click the **View Purchase Options** on the top right hand corner of the screen. 
 
4. Click **Setup Your Account**. 

Your account should now be associated with AWS Marketplace. 

{: .note}
For guidance on configuring AWS roles for seamless access to your S3 data, see our detailed walkthrough on [Using AWS Roles for S3 Access](https://docs.firebolt.io/godocs/Guides/loading-data/configuring-aws-role-to-access-amazon-s3.html).
