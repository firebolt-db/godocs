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
This tutorial teaches you how to create a database, ingest a sample dataset from Amazon S3 into Firebolt, and run fundamental analytics queries over the data. To perform this tutorial, you need an active Firebolt account. If you don't have one, [Schedule a call](https://www.firebolt.io/getting-started-now) to get set up, and [register for our hands-on Firebolt workshop](https://hi.firebolt.io/lp/hands-on-firebolt-workshop) to get an interactive, instructor-led tutorial on Firebolt. 

{: .note}
This tutorial uses Firebolt's sample dataset, from the fictional gaming company "Ultra Fast Gaming Inc." This dataset is publicly available with the access credentials shared below.


1. Topic toC
{:toc}

## Create your first database
To start working with data, you first create a database and a *Firebolt engine*. An engine represents the compute resources that are attached to a database for a certain workload. A database always has one *general purpose engine* that can write to the Firebolt file format (F3) for data ingestion and run analytics queries. We use that single-engine set up in this tutorial. Many databases are set up with additional *analytics engines* that can only query, and are configured to optimize different query workloads. For more information, see [Work with engines](./working-with-engines/working-with-engines.md).

**To create a database and engine**
1. From the **Databases** page, choose **New Database**.  

2. Enter a **Database name** (we use *Tutorial* in this topic).  

3. Under **Database engines**, leave the default engine selected. Firebolt will name the engine *Tutorial_general_purpose*.  

4. Choose **Create database**.  
![](../../assets/images/newdb.png)  
Firebolt adds your database to the **Databases** page. 


## Run your first query
Before we ingest the sample data and run a query over it, we'll go to the SQL workspace for the database and run a simple query to demonstrate how to start an engine. For more information about the SQL workspace, see [Query data](./query-data/using-the-sql-editor.md).

**To open your database, start an engine, and run a query**
1. From the **Database** page, find the database that you created in the list, and then choose the **Open in SQL workspace icon** (**>_**) next to the **Database name**.  

2. In the **Script 1** tab, type the simple query below that returns a list of databases in your account.  
```sql
SHOW DATABASES;
```  

3. Choose **Run Script** and note that the **Using** list indicates the engine that Firebolt uses to run the script, for example, `Tutorial_general_purpose`.  
![](../assets/images/showdb.png)  

4. When Firebolt prompts you to start the engine, choose **Start Engine**. The engine will take a few minutes to set up.

## Ingest data
Ingesting data into Firebolt is a three-step process. You:

1. Create an external table.  

2. Create a fact or dimension table.  

3. Run an `INSERT` command from the external table to the fact or dimension table.

### Create an external table
An *external table* is a special, virtual table that serves as a connector to your data source. After the external table is created, you ingest data by running an `INSERT` command from that external table into a *fact table* or *dimension table*. The `INSERT` command must run on a general purpose engine. After the data is available in fact and dimension tables, you can run analytics queries over those tables using any engine. Although it's possible, we don't recommend running analytics queries on external tables. For more information on using external tables, see [CREATE EXTERNAL TABLE](../sql_reference/commands/data-definition/create-external-table.md). To learn more about how to set up AWS roles to access your data on S3,  see [Use AWS roles to access S3](loading-data/configuring-aws-role-to-access-amazon-s3.md).

**To create an external table**
1. Choose the plus symbol (**+**) next to **Script 1** to create a new script tab, **Script 2**, in the SQL workspace.

2. Copy and paste the query below into the **Script 2** tab.
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
    MaxPlayTimeSeconds INTEGER,
    LevelIcon TEXT
) 
-- The URL specifies the data source in S3.
-- All files in the location that match the OBJECT_PATTERN
-- will be processed during ingestion.
URL = 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/'
-- These credentials specify a role or AWS key credentials
-- with permission to read from the S3 location.
-- These credentials are commented out for this tutorial because the bucket
-- is publicly accessible.
-- CREDENTIALS = ( AWS_KEY_ID = '******' AWS_SECRET_KEY = '******' )
OBJECT_PATTERN = 'help_center_assets/firebolt_sample_dataset/levels.csv'
TYPE = (CSV SKIP_HEADER_ROWS = 1);
```  

3. Choose **Run Script**.  
Firebolt creates the external table. When finished, the external table `ex_levels` appears on the object panel of the database.  
![](../assets/images/exlevels.png)  

4. Choose the vertical ellipses next to **Script 2**, choose **Save script**, enter a name (for example, *MyExTableScript*) and then press ENTER to save the script.

### Create a fact table
In this step, you'll create a Firebolt fact table called `levels`, which you use in the next step as the target for an `INSERT` command.

When creating a fact or dimension table, you will specify a *primary index*. Firebolt uses the primary index when it ingests data so that it is saved to S3 for highly efficient pruning and sorting when the data is queried. A primary index is required when creating a fact table, and recommended for dimension tables. For more information, see [Using primary indexes](./working-with-indexes/using-primary-indexes.md). 

The fact table that we create in this step specifies the `LevelID` column for the primary index. For more information about choosing columns for a primary index, see [How to choose primary index columns](./working-with-indexes/using-primary-indexes.md#how-to-choose-primary-index-columns).

**To create a fact table**
1. Create a new script tab.  

2. Copy and paste the query below into the script tab.  
```sql
CREATE FACT TABLE IF NOT EXISTS levels
(
    LevelID INTEGER UNIQUE,
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
    LevelIcon BYTEA,
    SOURCE_FILE_NAME TEXT,
    SOURCE_FILE_TIMESTAMP TIMESTAMP
) 
PRIMARY INDEX LevelID;
```  

3. Choose **Run Script**.  
Firebolt creates the fact table. When finished, the table `levels` appears on the object panel of the database.  
![](../assets/images/createfacttable.png)

### Use INSERT to ingest data
You can now use the `INSERT` command to copy the data from the external table into the fact table. During this operation, Firebolt ingests the data from your source into Firebolt.

{: .note}
Use `source_file_name` in the `WHERE` clause to specify which records to load from Amazon S3 and improve the performance of the read from S3. 

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
    DECODE(REPLACE(LevelIcon,'"',''),'BASE64'),
    SOURCE_FILE_NAME, 
    SOURCE_FILE_TIMESTAMP 
FROM ex_levels WHERE SOURCE_FILE_TIMESTAMP > (SELECT COALESCE(MAX(SOURCE_FILE_TIMESTAMP), '1980-01-01'::TIMESTAMP) FROM levels);
```
3. Choose **Run Script**.  
The query results pane indicates a **Status** of **Running** as shown below.  
![](../assets/images/running.png)  
The **Status** changes to **Success** when the ingestion is complete as shown below.
![](../assets/images/success.png)

## Query the ingested data
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
