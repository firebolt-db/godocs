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

This guide shows you the following workflows for loading data:
* Topic ToC
{:toc}

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

        If you select more than one column as a primary index, they will be added in order of sorting. For example, if you select `column_1` first, then select `column_3`, then `column_3` will be added as a primary index after `column_1`. This means `column_1` will be used first as a sparse index, followed by `column_3`. If you choose more than one primary index, the order of sorting appears next to the toggle switch under the **Primary Index** column. In the previous example, the number `1` appears next to `column_1` and a number `2` appears next to `column_3`.

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

## Load data using SQL statements
If the functionality in the **Load data** wizard does not meet your needs, or you prefer to write directly in SQL, you can enter SQL and run it in the Firebolt SQL workspace.

Before you can load data using a SQL script, you must register with Firebolt, and create a database and an engine.

For more information on how to register, create a database and engine using the Firebolt UI, see the [Get Started](../../Guides/getting-started.md) guide. To create an engine using SQL, use [CREATE ENGINE](../../sql_reference/commands/engines/create-engine.md). You can check how many engines are defined in your current account using [SHOW ENGINES](../../sql_reference/commands/metadata/show-engines.md). For more information and examples of how to create engines, see [Work with engines using DDL](../../Guides/operate-engines/working-with-engines-using-ddl.md). To create a database, use [CREATE DATABASE](../../sql_reference/commands/data-definition/create-database.md). You can check how many databases are defined in your current account using [SHOW DATABASES](../../sql_reference/commands/metadata/show-databases.md). Next, log into the Firebolt workspace and enter SQL into the script tab.



### The simplest COPY FROM workflow
Although there are many options to handle different data loading workflows, `COPY FROM` requires only two parameters:

1. The name of the table that you are loading data into.
2. A location to load the data from.

An example of the **simplest** way to invoke `COPY FROM` is:

```sql
COPY INTO tutorial FROM 
's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/
levels.csv' WITH HEADER=TRUE AUTO_CREATE=TRUE;
```
The previous code creates a table named `tutorial`, reads a CSV file with headers from a public Amazon S3 bucket, automatically generates a schema, and loads the data. If the data is contained in an Amazon S3 bucket with restricted access, you will need to provide credentials as shown in the following example:

```sql
COPY INTO tutorial 
FROM 's3://your_s3_bucket/your_file.csv'
CREDENTIALS = (
AWS_KEY_ID = '<aws_key_id>', 
AWS_SECRET_KEY = '<aws_secret_key>'
)
 WITH HEADER=TRUE AUTO_CREATE=TRUE;
 ```

To provide your credentials in the previous example, do the following:

- Replace the <aws_key_id> with an AWS access key that is associated with an AWS user or AWS IAM role. The AWS access key is a 20-character string such as ‘AKIAIOSFODNN7EXAMPLE’.
- Replace the <aws_secret_key> with an AWS secret access key associated with the user or role associated with the AWS access key. The AWS secret access key is a 40-character string such as ‘wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY’.

For more information about how to create an AWS access key and AWS secret key, see [Creating Access Key and Secret ID in AWS](../../Guides/loading-data/creating-access-keys-aws.md).

### Define a schema, create a table, and load data

You can also load data into an existing table using your own schema definition. Defining your own schema, instead of automatically detecting it, can give you finer control over data ingestion.

1. Create the target table.
   
    Create a table to load the data into, as shown in the following code example:
    ```sql
    CREATE TABLE IF NOT EXISTS levels (
    LevelID INT,
    Name TEXT,
    GameID INT,
    LevelType TEXT,
    MaxPoints INT,
    PointsPerLap DOUBLE,
    SceneDetails TEXT
   );
   ```
    The previous code example creates a table named `levels`, and defines each of the columns with a name and data type. For more information about the kinds of data that Firebolt supports, see [Data types](../../sql_reference/data-types.md).

2. Run COPY FROM.

    Use COPY FROM to load the data from an Amazon S3 bucket into the levels table, as shown in the following code example:

    ```sql
    COPY INTO levels
    FROM 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv'
    WITH TYPE = CSV
    HEADER = TRUE;
    ```
    The previous code example reads data from a Firebolt test data set from the fictional [Ultra Fast Gaming Inc](https://help.firebolt.io/t/ultra-fast-gaming-firebolt-sample-dataset/250) company. The `levels` data set is in CSV format, but Firebolt can also read files with `TSV`, `JSON` and `Parquet` formats. If you are reading in a `CSV` file and specify `HEADER = TRUE`, then Firebolt expects the first line of your file to contain column names.

### Load multiple files into a table

You can use the `PATTERN` option in `COPY FROM` to load several files at the same time from an Amazon S3 bucket. The `PATTERN` option uses standard regular expressions. For more information about regular expressions, see the Wikipedia [glob programming](https://en.wikipedia.org/wiki/Glob_`(programming`)) article.

```sql
COPY INTO nyc_restaurant_inspections FROM 
's3://firebolt-sample-datasets-public-us-east-1/nyc_sample_datasets/nyc_restaurant_inspections/parquet/'
WITH PATTERN="*.parquet" AUTO_CREATE=TRUE TYPE=PARQUET;
```

In the previous code example, the following apply:
    
- **COPY INTO**: Specifies the target table to load the data into.
- **FROM**: Specifies the S3 bucket location of the data.
- **WITH PATTERN**= "*.parquet": Uses a regular expressions pattern with wildcards (*) to include all Parquet files in the directory.
- **AUTO_CREATE=TRUE**: Automatically creates the table and the schema if the table does not already exist. Parquet files include rich data, and typically have schema information for simple and high-fidelity schema creation. Specifying AUTO_CREATE to TRUE ensures the schema in the Parquet file is preserved after loading.
- **TYPE = PARQUET**: Specifies the data format as Parquet.

### Filter data before loading using OFFSET and LIMIT

You can use `COPY FROM` with the `LIMIT` and `OFFSET` clauses to filter out data before you load it into Firebolt. The following example demonstrates how to filter the source data by skipping the first five rows of data and inserting only the next three rows. 

```sql
COPY offset_limit
FROM 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv'
OFFSET 5 LIMIT 3
WITH TYPE = CSV HEADER = TRUE;
```
In the previous code example, the following apply:

- **OFFSET**: Specifies a non-negative number of rows that are skipped before returning results from the query.
- **LIMIT**: Restricts the number of rows that are included in the result set.
- **TYPE = CSV**: Specifies the data format as CSV.
- **HEADER**: Specifies that the first row of the source file contains column headers.

For more information about `OFFSET` and `LIMIT`, see [SELECT Query Syntax](../../sql_reference/commands/queries/select.md).

### Aggregating data during data load

If you frequently use [aggregation functions](../../sql_reference/functions-reference/aggregation/index.md) such as `COUNT`, `MAX`, or `SUM`, you can perform these aggregations on top of  an external table without loading the raw data into Firebolt. This approach allows you to avoid costs associated with importing and storing the dataset, particularly if you don’t need to store the originating data set.

To aggregate data, first create an external table. Then, define a table in the Firebolt database with the desired aggregations. Finally, insert data from the external table into the internal table as follows:
    
1. Create an external table linked to files in an Amazon S3 bucket.

    The following code creates an external table that links to files in Amazon S3 bucket. The table has a defined schema that match the type and names of the originating data:
    ```sql
    CREATE EXTERNAL TABLE IF NOT EXISTS ex_playstats (
      GameID INTEGER,
      PlayerID INTEGER,
      StatTime TIMESTAMPNTZ,
      SelectedCar TEXT,
      CurrentLevel INTEGER,
      CurrentSpeed REAL,
      CurrentPlayTime BIGINT,
      CurrentScore BIGINT,
      Event TEXT,
      ErrorCode TEXT,
      TournamentID INTEGER) 
    URL = 's3://firebolt-sample-datasets-public-us-east-1/gaming/parquet/playstats/'
    OBJECT_PATTERN = '*'
    TYPE = (PARQUET);
    ```
    
    The previous code uses `OBJECT_PATTERN` to link all (*) files inside the specified directory contained in `URL`, and `TYPE` to specify the file format.

2. Define a table in the Firebolt database with the desired aggregations, as shown in the following code example:

    ```sql
    CREATE TABLE IF NOT EXISTS playstats_max_scores (
      PlayerID INTEGER,
      TournamentID INTEGER,
      MaxCurrentLevel INTEGER,
      MaxCurrentSpeed REAL,
      MaxCurrentScore BIGINT
    ) PRIMARY INDEX TournamentID, PlayerID;
   ```
    The previous code creates a table with the aggregate values `MaxCurrentLevel`, `MaxCurrentSpeed`, and `MaxCurrentScore`. 

3. Insert data from the external table into the internal table using the aggregate functions, as shown in the following code example:

    ```sql
    INSERT INTO playstats_max_scores 
    SELECT PlayerID,  
      TournamentID,
      MAX(CurrentLevel),
      MAX(CurrentSpeed),
      MAX(CurrentScore)
    FROM ex_playstats
    GROUP BY ALL
    ```

    The previous code calculates the aggregate function `MAX` before loading the data into the `playstats_max_scores` table.

### Update an existing table from an external table

To load only new and updated data from an Amazon S3 bucket into an existing table, use an external table and two temporary tables. This section guides you through creating a new table, which will serve as the existing table in a complete example. If you already have an existing table, its schema definition must include the file  timestamp and file name metadata. For more information about these metadata columns, see **Using metadata virtual columns** in [Work with external tables](./working-with-external-tables.md). 

The full workflow involves creating an internal source data table, an external table linked to the source data, and two temporary tables for the latest timestamp and updated data. The `updates_table` selects new data and uses an inner join to insert these records into your existing table, as illustrated in the diagram below:

<img src="../../assets/images/workflow_update_from_external_table.png" alt="Use an external table and two temporary tables to update a main internal table by timestamp." width="700"/>

1. Create a table

    The following code example shows you how to create a `players` table from a sample players dataset, and then copy data from a parquet file in an Amazon S3 bucket into it:

    ```sql
    CREATE TABLE IF NOT EXISTS
    players (
      PlayerID INTEGER,
      Nickname TEXT,
      Email TEXT,
      AgeCategory TEXT,
      Platforms ARRAY (TEXT NULL),
      RegisteredOn PGDATE,
      IsSubscribedToNewsletter BOOLEAN,
      InternalProbabilityToWin DOUBLE PRECISION,
      SOURCE_FILE_NAME TEXT,
      SOURCE_FILE_TIMESTAMP TIMESTAMPNTZ)
      PRIMARY INDEX agecategory, registeredon;
    ```
    The previous code example defines the schema for the players table, which includes the [metadata columns](./working-with-external-tables.md) `SOURCE_FILE_NAME` and `SOURCE_FILE_TIMESTAMP`. 

   
2. Create an external table

    Use an external table to query the source data directly to compare it to data in your existing table. The advantages of using an external table to check for new data are as follows:
  
      * An external table links to the data source without loading it into a database, which avoids costs associated with importing and storing it. 
      * Using an external table isolates data operations to reduce the risk of corrupting data contained in the main `players` table.
   
    The following code example creates an external players_ext table linked to the source data:

    ```sql
    CREATE EXTERNAL TABLE IF NOT EXISTS
    players_ext (
      PlayerID INTEGER,
      Nickname TEXT,
      Email TEXT,
      AgeCategory TEXT,
      Platforms ARRAY (TEXT NULL),
      RegisteredOn PGDATE,
      IsSubscribedToNewsletter BOOLEAN,
      InternalProbabilityToWin DOUBLE PRECISION)
    URL = 's3://firebolt-sample-datasets-public-us-east-1/gaming/parquet/players/'
    OBJECT_PATTERN = '*'
    TYPE = (PARQUET);
    ```
    The previous code example defines the schema for parquet data and links to all parquet files in the Amazon S3 bucket that contains the source data.
   
    If you are using an external table to link to data in parquet format, the order of the columns in the external table does not have to match the order of the columns in the source data. If you are reading data in csv format, the order must match the order in the source data.

3. Copy data from the `players_ext` external table into an internal `players` table, as shown in the following code example:
    ```sql
    INSERT INTO players
    SELECT *,
    $SOURCE_FILE_NAME,
    $SOURCE_FILE_TIMESTAMP
    FROM players_ext
    ```
4. Create a temporary table that contains the most recent timestamp from your existing table, as shown in the following code example:
    ```sql
    CREATE TABLE IF NOT EXISTS control_maxdate AS (
    SELECT MAX(source_file_timestamp) AS max_time
    FROM players
    );
    ```
    The previous code example uses an aggregate function `MAX` to select the most recent timestamp from the existing `players` table.

5. Create a temporary table to select and store data that has a newer timestamp than that contained in the control_maxdate table, as shown in the following code example:
    ```sql
    CREATE TABLE IF NOT EXISTS updates_table AS (
    WITH external_table AS (
    SELECT *,
      $SOURCE_FILE_NAME AS source_file_name_new,
      $SOURCE_FILE_TIMESTAMP AS source_file_timestamp_new,
    FROM players_ext
    WHERE $source_file_timestamp > (SELECT max_time FROM control_maxdate)
    AND playerid IN (SELECT DISTINCT playerid FROM players)
    )
    SELECT
    e.*
    FROM players f
    INNER JOIN external_table e
    ON f.playerid = e.playerid
    );
    ```

    The previous code example creates an `updates_table` using a `SELECT` statement to filter out data that is older than the previously recorded timestamp. The code includes a table alias `e`, which refers to `external_table`, and the table alias `f`, which refers to the `players` table. The `INNER JOIN` uses `playerid` to match rows in the external table to those in the `player` table, and then updates the `players` table.

6. Delete records from the original players table that have been updated, based on matching player IDs in the `updates_table`, as shown in the following code example: 
    ```sql
    DELETE FROM players
    WHERE playerid IN (SELECT playerid FROM updates_table);
    ```
7. Insert updated records from the `updates_table`, including a new timestamp, into the `players` table to replace the deleted records from the previous step, as shown in the following example:
    ```sql
    INSERT INTO players
    SELECT
    playerid,
    nickname,
    email,
    agecategory,
    platforms,
    registeredon,
    issubscribedtonewsletter,
    internalprobabilitytowin,
    source_file_name_new,
    source_file_timestamp_new
    FROM updates_table;
    ```
8. Insert any entirely new, rather than updated, records into the `players` table, as shown in the following code example:
    ```sql
    INSERT INTO players
    SELECT *,
    $SOURCE_FILE_NAME,
    $SOURCE_FILE_TIMESTAMP
    FROM players_ext
    WHERE $SOURCE_FILE_TIMESTAMP > (SELECT max_time FROM control_maxdate)
    AND playerid NOT IN (SELECT playerid FROM players);
    ```
9. Clean up resources. 
    Remove the temporary tables used in the update process as shown in the following code example:
    ```sql
    DROP TABLE IF EXISTS control_maxdate;
    DROP TABLE IF EXISTS updates_table;
    ```
### Load source file metadata into a table
When you load data from an Amazon S3 bucket, Firebolt uses an external table which holds metadata about your source file to map into a Firebolt database. You can load metadata from the virtual columns contained in the external file into a table. You can use the name, timestamp and file size to determine the source of a row of data in a table. When adding data to an existing table, you can use this information to check whether new data is available, or to determine the vintage of the data. The external table associated with your source file contains the following fields: 

* `source_file_name` - the name of your source file.
* `source_file_timestamp` - the date that your source file was created in the Amazon S3 bucket that it was read from.
* `source_file_size` - the size of your source file in bytes.

The following code example shows you how to create and load metadata into a `levels_meta` table, which contains only the metadata:
```sql
    CREATE TABLE levels_meta (
      day_of_creation date, 
      name_of_file text, 
      size_of_file int);
    COPY levels_meta(
      day_of_creation $source_file_timestamp, 
      name_of_file $source_file_name, 
      size_of_file $source_file_size) 
    FROM  's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv'
    WITH AUTO_CREATE = TRUE
    HEADER = TRUE
    TYPE = CSV;
```
The following code shows you how to read in the source data from the Amazon S3 bucket and add the metadata as new columns in that table:
```sql
CREATE TABLE IF NOT EXISTS levels_meta_plus (
	"LevelID" INT,
	"Name" TEXT,
	"GameID" INT,
	"LevelType" TEXT,
	"MaxPoints" INT,
	"PointsPerLap" DOUBLE,
	"SceneDetails" TEXT,
	day_of_creation date,
	name_of_file text,
	size_of_file int
);

COPY INTO levels_meta_plus (
  "LevelID",    
   "GameID",
   "Name",
  "LevelType",
  "MaxPoints",
  "PointsPerLap",
  "SceneDetails",
  day_of_creation $source_file_timestamp,  
  name_of_file $source_file_name,      	
  size_of_file $source_file_size
)
FROM  's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv'
WITH
HEADER = TRUE
TYPE = CSV;
```
For more information about metadata, see **Using metadata virtual columns** in [Work with external tables](./working-with-external-tables.md).

### Continue loading even with errors

By default, if Firebolt runs into an error when loading your data, the job will stop loading and end in error. If you want to continue loading your data even in the presence of errors, set `MAX_ERRORS_PER_FILE` to a percentage larger than `0`. Then, `COPY FROM` will continue to load data until it exceeds the specified percent based on the total number of rows in your data. If you enter an integer number between `0` and `100`, `COPY FROM` will interpret the integer as a percentage of rows. 

For example, if `MAX_ERRORS_PER_FILE` is set to 3, `COPY FROM` will continue to load data until more than `3` percent of the rows loaded contain an error. Once `COPY FROM` passes this threshold, the load job will stop and return an error. If you enter the text, `3%`, `COPY FROM` will also interpret the value as `3%` of the rows. If  `MAX_ERRORS_PER_FILE` is set to either `100` or `100%`, the load process will continue even if every row in every file has an error. If all rows have errors, no data will load into the target table.

The following code example loads a sample CSV data set with headers, and will finish the loading job even if every row contains an error. 
```sql
COPY INTO new_levels_auto
FROM 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv'
WITH AUTO_CREATE = TRUE
HEADER = TRUE
TYPE = CSV
MAX_ERRORS_PER_FILE = '100%';
```
In the previous code example, the following apply:
 * `COPY INTO new_levels_auto`: Creates a new table named `new_levels_auto`. The `INTO` clause is optional. If the table already exists, `COPY FROM` will add the rows to the existing table.
* `FROM`: Specifies the S3 bucket location of the data. In this example, the dataset is located in a publicly accessible bucket, so you do not need to provide credentials.
* `AUTO_CREATE=TRUE`: Creates a  target table and automatically infers the schema.
* `HEADER=TRUE`: Specifies that the first row of the source file contains column headers.
* `TYPE`: Specifies the data format of the incoming data. 
* `MAX_ERRORS_PER_FILE`: Specified as a string or literal text. In the previous example, `MAX_ERRORS_PER_FILE` uses text.

### Log errors during data load

`COPY FROM` supports an option to generate error files that describe the errors encountered and note the rows with errors. To store these files in an Amazon S3 bucket, you must provide credentials to allow Firebolt to write to the bucket.

The following example sets an error handling threshold and specifies an Amazon S3 bucket as the source data and another to write the error file:
```sql 
COPY INTO my_table
FROM 's3://my-bucket/data.csv'
CREDENTIALS = (
    AWS_KEY_ID = 'YOUR_AWS_KEY_ID',
    AWS_SECRET_KEY = 'YOUR_AWS_SECRET_KEY'
)
MAX_ERRORS_PER_FILE = 5%
ERROR_FILE = 's3://my-bucket/error_logs/'
ERROR_FILE_CREDENTIALS = (
    AWS_KEY_ID = 'YOUR_AWS_KEY_ID',
    AWS_SECRET_KEY = 'YOUR_AWS_SECRET_KEY'
)
HEADER = TRUE
```

In the previous code example, the following apply:
* `COPY INTO`: Specifies the target table to load the data into.
* `FROM`: Specifies the S3 bucket location of the data.
* `Credentials`: Specifies AWS credentials to access information in the Amazon S3 bucket that contains the source data. For more Information about credentials and how to set them up, see the previous **The simplest COPY FROM workflow** section in this guide.
* Error Handling:
    * `MAX_ERRORS_PER_FILE = 5%`: Allows errors in up to `5%` of the rows per file before the load data job fails.
    * `ERROR_FILE`: Specifies the Amazon S3 bucket location to write the error file.
* `HEADER = TRUE`: Indicates that the first row of the CSV file contains column headers.

**How to examine the error files**

If you specify an S3 path with the necessary permissions for an error file and the `COPY FROM` process encounters errors, two different files will be generated in your bucket. The following queries show you how to load these error files into new tables so that you can query and examine the error details and the corresponding rows.

The following query loads the `error_reasons` csv file, which contains a header with column names:

```sql
COPY error_reasons FROM 's3://my-bucket/error_logs/' 
WITH PATTERN='*error_reasons*.csv' HEADER=TRUE;

SELECT * from error_reasons;
```
The following query loads a file containing all rows that encountered errors. Although this file has no header, the table schema should match that of the source file where the errors occurred.

```sql 
COPY rejected_rows FROM 's3://my-bucket/error_logs/'
WITH PATTERN='*rejected_rows*.csv' HEADER=FALSE;

SELECT * FROM rejected_rows;
```

You can also configure parameters such as `MAX_ERRORS_PER_FILE`, `ERROR_FILE`, and `ERROR_FILE_CREDENTIALS` to manage how errors are handled, ensure data integrity and record errors for future review. For more information about `ERROR_FILE` or `ERROR_FILE_CREDENTIALS`, see the **Parameters** section of [COPY FROM](../../sql_reference/commands/data-management/copy-from.md).

### More complex `COPY FROM` use cases

You can construct more complex workflows using any of the additional options in `COPY FROM`. These include the following:

* Use source files located in multiple directories.
* Write the contents of an existing table in different formats to an Amazon S3 bucket.
* Load a data file that doesn’t have a header.
* Use a different delimiter other than the default comma (,) value to read a CSV file.

There are many additional options available in `COPY FROM`. For information about the syntax, parameter descriptions, and additional examples, see [COPY FROM](../../sql_reference/commands/data-management/copy-from.md).

<!-- For information about using Apache Airflow to incrementally load data chronologically, see [Incrementally loading data with Airflow](incrementally-loading-data.md). -->
