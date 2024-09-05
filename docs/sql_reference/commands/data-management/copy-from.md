---
layout: default
title: COPY FROM
description: Reference and syntax for the COPY command that copies data from S3 files into a Firebolt table.
great_grand_parent: SQL reference
grand_parent: SQL commands
parent: Data management
---
# COPY FROM
{: .no_toc}

This guide shows you how to load data from an AWS S3 bucket into Firebolt using `COPY FROM`. `COPY FROM` can accommodate different data loading workflows including the following:


* Copy all source columns simultaneously into a target table.
* Copy only a specific set of columns into a target table.
* Automatically discover the schema during data loading.
* Limit the number of rows loaded into the table.
* Handling errors during data loading.


<!-- This comment is needed for both the list above and the list below to render. -->


* Topic ToC
{:toc}

## Syntax

```sql
COPY
[INTO] <table_name> [ <column_mapping> ] 
FROM <externalLocations>
[ LIMIT <count> ]
[ OFFSET <start> ]
[ WITH <options> ]

<column_mapping>:
    ( <column_name> [DEFAULT <default_value>] [ { $<source_column_index> | <source_column_name> } ] [, ...] )

<options>:
    [ CREDENTIALS = ( <credentials> ) ] 
    [ PATTERN = <regex_pattern> ]
    [ TYPE = { **AUTO** | CSV | TSV | PARQUET } ]
    [ AUTO_CREATE = { **TRUE** | FALSE } ]
    [ ALLOW_COLUMN_MISMATCH = { **TRUE** | FALSE } ]
    [ ERROR_FILE = <directoryLocation> ]
    [ ERROR_FILE_CREDENTIALS = <credentials> ]
    [ MAX_ERRORS_PER_FILE = { integer | '<percentage>' } ]
    [ <csv_options> ]

<credentials>:
    { AWS_KEY_ID = '<aws_key_id>' AWS_SECRET_KEY = '<aws_secret_key>' }

<csv_options>:
    [ HEADER = { **FALSE** | TRUE  } ]
    [ DELIMITER = 'character' ]
    [ NEWLINE = 'string' ]
    [ QUOTE = { **DOUBLE_QUOTE** | SINGLE_QUOTE } ]
    [ ESCAPE = 'character' ]
    [ NULL_STRING = 'string' ]
    [ EMPTY_FIELD_AS_NULL = { **TRUE** | FALSE } ]
    [ SKIP_BLANK_LINES = { **FALSE** | TRUE } ]
    [ DATE_FORMAT = <date_format> ]
    [ TIMESTAMP_FORMAT = <timestamp_format> ]

```

## Parameters

{: .no_toc}


| `<table_name>`           | The name of the target table.                    | Parameter                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `<column_mapping>`       | (Optional) This feature is only available if the target table already exists. You can use `column_mapping` to specify the mapping between the source and target schema. Select a column in the source file to map to the target file using either the name of the column or its index.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `<column_name>`          | The name of a target column in a table. If `<source_column_index/name>` not specified, source columns will be automatically mapped to target columns based on name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `<default_value>`        | A replacement value for any `NULL` value generated by mapping the source to the target. This data type of `default_value` must be compatible with the data type of the target column.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `<source_column_index>`  | The index position of the column in the source data to be mapped. If you are specifying multiple source files, `source_column_index` specifies the index for all source files. The index starts at 1, and can be as large as 2^64-1, which allows for a very large number of columns. If you prefix the index inside a command or query, preceed the column index with a dollar sign (`$`) character. For example, prefix index as shown in the following `COPY INTO` statement: `CREATE TABLE t(a text, b text); COPY INTO t(a $1, b $2) FROM 's3://my_bucket/my_folder/my_file';`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `<source_column_name>`   | The name of the column in the source data to be mapped. If you are specifying multiple source files, `source_column_name` specifies the column name for all source files.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `<externalLocations>`     | One or multiple paths to an Amazon S3 location containing source files. If `externalLocations` ends with a forward slash (`/`), Firebolt interprets its value as a directory. Otherwise, `externalLocations` is treated as single file. An example folder has the following format: `s3://my_bucket/my_folder/`. An example file has the following format: `s3://my_bucket/my_folder/my_file`.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `<directoryLocation>` |  The Amazon S3 path to a directory.
| `CREDENTIALS`            | The Amazon S3 credentials for accessing the specified `<externalLocations>`. For more information, see [CREDENTIALS](../data-definition/create-external-table.md#credentials).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `PATTERN`                | A string that represents a [glob pattern](https://en.wikipedia.org/wiki/Glob_(programming)), or regular expression, used to match filenames or other strings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `TYPE`                   | The file type that Firebolt should expect when loading files identified by `PATTERN`. If `TYPE` is unspecified, Firebolt automatically detects the file type using the file's suffix. If a file matched by `PATTERN` does not match the specified `TYPE`, Firebolt will generate an error.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `AUTO_CREATE`            | Specify whether Firebolt should automatically create a table if it doesn't already exist. The default setting is `TRUE`, allowing automatic table creation. If `AUTO_CREATE` is set to `FALSE`, Firebolt will generate an error if the target table is missing. If the target table already exists, `AUTO_CREATE` is ignored.                                                                                                                                                                                                                                                                                                                                                                                                       |
| `ALLOW_COLUMN_MISMATCH`  | Set to `FALSE` to specify that all **required** columns must appear in the source files. A required column includes those specified in `<column_mapping>`, which are specified using either a name or index. If `ALLOW_COLUMN_MISMATCH` is set to `FALSE`, the source file must contain each required column by name or have enough columns to meet the required index. Missing data rows for required columns will trigger a row-based error for CSV or TSV files, or a file-based error for Parquet files. |
| `ERROR_FILE`             | The Amazon S3 location where error files will be written. See the `<externalLocations>` parameter definition above for implementation. No error files are created by default or if the specified path doesn't exist. If `ERROR_FILE` is specified, a subdirectory is created based on the time of load submission in the format: YearMonthDay-HourMinuteSecond + QueryID, such as: 20220330-173205/<query_id>/). This directory will contain a rejected_rows.csv file containing erroneous data rows, and an error_reasons.csv file, containing the reasons that the errors were generated.                                                                                                            |
| `ERROR_FILE_CREDENTIALS` | The Amazon S3 credentials required to write an error file to `<externalLocations>`. For more information, see [CREDENTIALS](../data-definition/create-external-table.md#credentials).                                                                                                                                                                                                  |
| `MAX_ERRORS_PER_FILE`    | Specify the maximum number of rows that can be rejected per file. `MAX_ERRORS_PER_FILE` can be integer or percentage in the format 'integer%', such as `100%`. The only valid percentage options are `0%` and `100%`. By default, no errors are allowed. If `MAX_ERRORS_PER_FILE` is set to `100%`, then all errors are allowed. If the threshold is exceeded, an error will occur.|                                                                          |

### Parameters for CSV files

| Parameter             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:----------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `HEADER`              | Specify if the file contains a header line containing the column names. If `HEADER` is `TRUE`, the first line will be interpreted to contain column names.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `DELIMITER`           | Specify the character used to separate fields. The default delimiter is a comma (`,`).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `NEWLINE`             | Specify the character used to delimit rows. The default delimiter is `\n`. If NEWLINE is `\n`, then `\r`, `\r\n`, and `\n\r` are also treated as newline delimiters. Custom delimiters are allowed only if the target table already exists.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `QUOTE`               | Specify the character used for quoting fields. The default is double quote (`"`). If a single quote is specified, the quote character will be set to (`'`).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `ESCAPE`              | Specify the character used to escape special characters. The default character is the quote (`'`) character.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `NULL_STRING`         | Specify string used to represent `NULL` values. The default is an empty string, which means that no specific null string is defined.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `EMPTY_FIELD_AS_NULL` | Specify whether empty fields should be interpreted as `NULL` values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `SKIP_BLANK_LINES`    | Specify whether to ignore blank lines.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `DATE_FORMAT`         | Specify the date format for parsing text into date columns. This format will apply to all columns loaded as date columns. For supported formats, see [TO_DATE](../../functions-reference/date-and-time/to-date.md).                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `TIMESTAMP_FORMAT`    | Specify the timestamp format for parsing text into timestamp columns. The format will apply to all columns loaded as timestamp columns. For supported formats, see [TO_TIMESTAMP](../../functions-reference/date-and-time/to-timestamp.md).                                                                                                                                                                                                                                                                                                                                                                                           |


Notes:
Non-existing columns:
By default if a column does not exist in the source file it will produce nulls.
For CSV format it applies to missing fields as well.

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
You can leverage automatic schema discovery provided by `COPY FROM`  to manage sizable data sources where manual schema definition can be cumbersome and error-prone. For data formats like Parquet that already include table-level metadata, Firebolt automatically reads this metadata to facilitate the creation of corresponding target tables. For formats where column-level metadata might not be available, such as `CSV`, `COPY FROM` infers column types based on the data content itself. While this process aims to accurately identify data types, it operates on a "best effort" basis, balancing type correctness with practical usability constraints. Additionally, for CSV files that contain column names in the first line, `COPY FROM` uses this line as column headers and deduces the column types from the subsequent data, streamlining the initial data loading process significantly.

## Handling Bad Data
`COPY FROM` provides robust mechanisms to identify and isolate bad data during the loading process.

```sql
COPY sales
FROM 's3://data-bucket/sales_data.csv'
WITH TYPE = CSV HEADER = TRUE ERROR_FILE = <externalLocation> ERROR_FILE_CREDENTIALS = <credentials> MAX_ERRORS_PER_FILE = 5
```

## Handling partitioned data
`COPY FROM` effectively manages the loading of partitioned data, ensuring that data is inserted into the correct partitions based on predefined rules or schema setups, optimizing query performance and data management.

## Filtering data to be loaded

When loading data into tables, you can filter data using these options:

1. `LIMIT`: Controls the number of rows loaded. Useful for previews or creating sample datasets.

2. `OFFSET`: Behaves in the same way as the `OFFSET` clause in `SELECT` queries. Skips a specified number of rows in the final result set before ingestion.

Both `LIMIT` and `OFFSET` apply to the entire result set, not to individual files.

Note that `COPY FROM` currently does not support an `ORDER BY` clause. Because of this, the results when using `OFFSET` can be different every time you run the command.

```sql
COPY tournament_results
FROM 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/rankings/TournamentID=1/'
LIMIT 50 OFFSET 50;
```

This command reads all the files in the specified directory and then applies the offset and limit clause. 
As long as all source files combined have at least 100 rows, the result set will have exactly 50 rows.

# Examples

### Setup
The following examples use a simple dataset that you can create using these simple instructions:

Create sample of data in 2 different formats and push it to existing Amazon S3 bucket (engine should have write access to this bucket otherwise, credentials need to be provided).

Create three rows of data with two different data types and push it to an existing Amazon S3 bucket (your Firebolt engine should have write access to this bucket, otherwise credentials need to be provided).
```sql
CREATE TABLE sample_table(a int not null, b text not null);
INSERT INTO sample_table VALUES (1,row1),(2,row2),(3,row3);

COPY (SELECT * FROM sample_table ORDER BY 1)
TO 's3://bucket_name/data_directory/' TYPE=CSV FILE_NAME_PREFIX='sample'
INCLUDE_QUERY_ID_IN_FILE_NAME=FALSE SINGLE_FILE=TRUE COMPRESSION=NONE;

COPY (SELECT * FROM sample_table ORDER BY 1)
TO 's3://bucket_name/data_directory/' TYPE=PARQUET FILE_NAME_PREFIX='sample'
INCLUDE_QUERY_ID_IN_FILE_NAME=FALSE SINGLE_FILE=TRUE COMPRESSION=NONE;
```

### Schema and format discovery (target table does not exist)
```sql
COPY target_csv_0 FROM 's3://bucket_name/data_directory/sample.csv'
WITH HEADER=TRUE;

SELECT * FROM target_csv_0 ORDER BY 1;
```

| a (BIGINT) | b (TEXT) |
|:-----------|:---------|
| 1          | row1     |
| 2          | row2     |
| 3          | row3     |

### No schema discovery
Target table exists, read by name, using pattern.
```sql
CREATE TABLE target_csv_1 (b text not null, a int not null);

COPY target_csv_1 FROM 's3://bucket_name/data_directory/'
WITH TYPE=CSV HEADER=TRUE PATTERN='*.csv';

SELECT * FROM target_csv_1 ORDER BY 1;
```

| b (TEXT) | a (INTEGER) |
|:---------|:------------|
| row1     | 1           |
| row2     | 2           |
| row3     | 3           |

### Read by name mismatch
None of the columns [not_a, not_b] exists in csv file so they all get null values.
```sql
CREATE TABLE target_csv_2 (not_a int not null, not_b text not null);

COPY target_csv_2 FROM 's3://bucket_name/data_directory/sample.csv'
WITH HEADER=TRUE MAX_ERRORS_PER_FILE='0%';
```
```ignorelang
ERROR: The INSERT INTO statement failed because it tried to insert a NULL into the column not_a, which is NOT NULL. Please specify a value or redefine the column's logical constraints.
```

###  Allow errors
Read by name mismatch results empty.
```sql
CREATE TABLE target_csv_2_a (not_a int not null, not_b text not null);

COPY target_csv_2_a FROM 's3://bucket_name/data_directory/sample.csv'
WITH TYPE=CSV HEADER=TRUE MAX_ERRORS_PER_FILE='100%';

SELECT * FROM target_csv_2_a;


| not_a (INTEGER) | not_b (TEXT) |
|:----------------|:-------------|
```
### Insert into nullable columns
Read by name mismatch, no error allowed, insert null into nullable columns.
```sql
CREATE TABLE target_csv_2_b (not_a int null, not_b text null);

COPY target_csv_2_b FROM 's3://bucket_name/data_directory/sample.csv'
WITH TYPE=CSV HEADER=TRUE MAX_ERRORS_PER_FILE='0%';

SELECT * FROM target_csv_2_b;
```

| not_a (INTEGER) | not_b (TEXT) |
|:----------------|:-------------|
| NULL            | NULL         |
| NULL            | NULL         |
| NULL            | NULL         |


### No header
Read the header row (a,b) into the table as a data row.
```sql
CREATE TABLE target_csv_3 (not_a int not null, not_b text not null);

COPY target_csv_3 FROM 's3://bucket_name/data_directory/sample.csv'
WITH TYPE=CSV HEADER=FALSE;
```
```ignorelang
ERROR: Unable to cast text 'a' to integer
```
Header row will be sent into error file, and the other data rows will be ingested in sequential order (because `HEADER=FALSE`).
```sql
COPY target_csv_3 FROM 's3://bucket_name/data_directory/sample.csv'
WITH HEADER=FALSE MAX_ERRORS_PER_FILE='100%' error_file='s3://bucket_name/error_directory/';

SELECT * FROM target_csv_3 ORDER BY 1;
```

| not_a (INTEGER) | not_b (TEXT) |
|:----------------|:-------------|
| 1               | row1         |
| 2               | row2         |
| 3               | row3         |

Let's view the error reasons file that was generated:
```sql
COPY error_reasons_0 FROM 's3://bucket_name/error_directory/' 
WITH PATTERN='*error_reasons*.csv' HEADER=TRUE;

SELECT * from error_reasons_0;
```

| file_name (TEXT)          | source_line_num (BIGINT) | error_message (TEXT) |
|:--------------------------|:-------------------------|:---------------------|
| data_directory/sample.csv | 1                        | Error while casting  |

Let's view the error reasons file that was generated:
```sql
COPY rejected_rows FROM 's3://bucket_name/error_directory/'
WITH PATTERN='*rejected_rows*.csv' HEADER=FALSE;

SELECT * FROM rejected_rows;
```

| f0 (TEXT) | f1 (TEXT) |
|:----------|:----------|
| a         | b         |

## Column selection
Source column `a` mapped (inserted) into target column `b`.
Source column `c` mapped (inserted) into target column `a` with a default value (in case there is any null value).
Column `c` does not exist, hence it generates nulls that is replaced by the default value `44`.
```sql
CREATE TABLE target_csv_4 (a int, b text);

COPY target_csv_4(b a, a default 44 c) FROM 's3://bucket_name/data_directory/sample.csv'
WITH HEADER=TRUE;

SELECT * FROM target_csv_4 ORDER BY 1;
```

| a (INTEGER) | b (TEXT) |
|:------------|:---------|
| 44          | 1        |
| 44          | 2        |
| 44          | 3        |

## Type mismatch error with parquet format
```sql
CREATE TABLE target_parquet_1 (a date not null, b text not null);

COPY target_parquet_1 FROM 's3://bucket_name/data_directory/sample.parquet'
WITH TYPE=PARQUET MAX_ERRORS_PER_FILE='100%' ERROR_FILE='s3://bucket_name/parquet_error_directory/';

SELECT count(*) as num_rows FROM target_parquet_1;
```

| num_rows (BIGINT) |
|:------------------|
| 0                 |

Let's view the error reasons:
```sql
COPY error_reasons_1 FROM 's3://bucket_name/parquet_error_directory/'
WITH PATTERN='*error_reasons*.csv' HEADER=TRUE;

SELECT * FROM error_reasons_1;
```

| file_name (TEXT)              | source_line_num (BIGINT) | error_message (TEXT)                                                      |
|:------------------------------|:-------------------------|:--------------------------------------------------------------------------|
| data_directory/sample.parquet | 0                        | Can not assignment cast column a from type integer null to type date null |

There is no rejected rows as this was a file based error.
```sql
COPY rejected_rows_1 FROM 's3://bucket_name/parquet_error_directory/'
WITH PATTERN='*rejected_rows*.csv' HEADER=FALSE;
```
```ignorelang
ERROR: No file found in s3 bucket: local-dev-bucket, pattern: rejected_rows*.csv. check url and object pattern.
```

### Metadata columns
```sql
CREATE TABLE target_csv_5 (a int not null, b text not null);

COPY target_csv_5(a, b $source_file_name) FROM 's3://bucket_name/data_directory/sample.csv'
WITH TYPE=CSV HEADER=TRUE;

SELECT * FROM target_csv_5 ORDER BY 1;
```

| a (INTEGER) | b (TEXT)                  |
|:------------|:--------------------------|
| 1           | data_directory/sample.csv |
| 2           | data_directory/sample.csv |
| 3           | data_directory/sample.csv |


### Multiple URLs

Multiple directories:

```sql
COPY target_table FROM 
    's3://bucket_name/directory_1/'
    ,'s3://bucket_name/directory_2/' 
WITH pattern='*.csv';
```

Multiple single files:

```sql
COPY target_table FROM 
's3://bucket_name/csv_file/data_1.csv'
,'s3://bucket_name/csv_file/data_2.csv'
,'s3://bucket_name/csv_file/data_3.csv';
```

