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

This topic provides an overview on how to load data into Firebolt using the COPY FROM command. The `COPY FROM` command enables you to ingest data from AWS S3 into Firebolt.  This command provides a simple syntax and does not require an exact match to your source data, giving you the flexibility to address various scenarios when loading data, such as:

* Topic ToC
{:toc}

## Syntax

```sql
COPY
[INTO] <table_name> [ <column_mapping> ] 
FROM <externalLocation>
[ WHERE <condition> ]
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
    [ ERROR_FILE = <externalLocation> ]
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

| Parameter                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<table_name>`           | The name of the target table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `<column_mapping>`       | Optional. Only available of target table exists. Specify mapping between src schema and target schema. With this feature one can choose for each column in the target table a column from src files by name or by index.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `<column_name>`          | The name of a target column in the table. If `<source_column_index/name>` not specified, the src columns will be mapped by this name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `<default_value>`        | A value that replace each NULL value generated by the src. This value must be convertible to the target column datatype.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `<source_column_index>`  | The index of the src column that will be mapped (same index for all the files). This value range is [1,2^64-1]. It needs to follow the `$` character.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `<source_column_name>`   | The name of the src column that will be mapped (same name for all the files).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `<externalLocation>`     | The path to an S3 location where the query result file or files are saved. If ends with `/` it interpreted as directory otherwise as single file. Folder example: `s3://my_bucket/my_folder/`. File example: `s3://my_bucket/my_folder/my_file`.                                                                                                                                                                                                                                                                                                                                                                                                             |
| `CREDENTIALS`            | The Amazon S3 credentials for accessing the specified `<externalLocation>`. See [CREDENTIALS](../data-definition/create-external-table.md#credentials).                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `PATTERN`                | A regular expression pattern string (glob). For additional explenation visit: https://en.wikipedia.org/wiki/Glob_(programming).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `TYPE`                   | Specify the file type Firebolt expects to ingest given the `PATTERN`. If not specified it will be auto detected by the suffix of a file. If a file referenced using `PATTERN` does not conform to the specified `TYPE`, an error occurs.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `AUTO_CREATE`            | Specify if the table can be automatically created by working alongside with automatic schema discovery. By default, automatic table creation is enabled (value: TRUE). If value is TRUE and the target table already exists, `AUTO_CREATE` is ignored.                                                                                                                                                                                                                                                                                                                                                                                                       |
| `ALLOW_COLUMN_MISMATCH`  | Specify if all required columns must appear in the src files. A column can be required by name or by index as described in `<column_mapping>`. If a column is required by name then a column with the same name must appear in the source files otherwise a file based error will be raised (and will be handled according to the error handling described in this doc). For the CSV and TSV formats it is possible that a column with that name exists but it does not appear in every row, which is considered as a row based error. If a column is required by index then the file must contain at least #index number of columns (file based error for parquet, row based error for CSV and TSV). |
| `ERROR_FILE`             | Defines S3 location where rejected records will be stored. See `<externalLocation>` parameter definition above for format details. By default or if the specified path doesn't exist, no error files will be created. If specified a child directory is created based on the time of load submission in the format YearMonthDay -HourMinuteSecond + QueryID (Ex. 20220330-173205/<query_id>/). In this folder, two types of files are written: 1) the reason (error) file: rejected_rows.csv. and the data (row) file: error_reasons.csv.                                                                                                                    |
| `ERROR_FILE_CREDENTIALS` | The Amazon S3 credentials for accessing the specified `<externalLocation>` for error file creation. See [CREDENTIALS]((../../sql_reference/commands/data-definition/create-external-table.md#credentials)).                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `MAX_ERRORS_PER_FILE`    | Specify the maximum number of rejected rows per file. Can be integer or literal text in the format 'integer%' eg. '100%'. By default no errors are allowed (0). If '100%' is given then all errors are allowed. If the threshold is passed an error will be shown.                                                                                                                                                                                                                                                                                                                                                                                           |
| `HEADER`                 | Specify that the file contains a header line with the names of each column in the file. If set to true the first line will be interpreted as file schema column names.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `DELIMITER`              | Specify the delimiter character between fields. By default is `,`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `NEWLINE`                | Specify the delimiter character between rows. By default is `\n`. If NEWLINE is `\n`, then `\r`, `\r\n`, and `\n\r` are also treated as newline delimiters. Custom delimiters are only allowed if the target table already exists.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `QUOTE`                  | Specify the quote character. By default: DOUBLE_QUOTE (`"`). If specified SINGLE_QUOTE it means `'`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `ESCAPE`                 | Specify the escape character. By default is the `QUOTE` character.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `NULL_STRING`            | Specify the null string. By default is empty which means no null string.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `EMPTY_FIELD_AS_NULL`    | Specify whether empty fields are treated as null.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `SKIP_BLANK_LINES`       | Specify whether to skip blank lines.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `DATE_FORMAT`            | Specify the date format for parsing text into date columns. Will apply only and for all columns that will be ingested to date columns. For supported formats see formats in [TO_DATE](../../functions-reference/date-and-time/to-date.md)                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `TIMESTAMP_FORMAT`       | Specify the timestamp format for parsing text into timestamp columns. Will apply only and for all columns that will be ingested to timestamp columns. For supported formats see formats in [TO_TIMESTAMP](../../functions-reference/date-and-time/to-timestamp.md)                                                                                                                                                                                                                                                                                                                                                                                           |

notes:
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
You can leverage automatic schema discovery provided by `COPY FROM`  to manage sizable data sources where manual schema definition can be cumbersome and error-prone. For data formats like Parquet and ORC that already include table-level metadata, Firebolt automatically reads this metadata to facilitate the creation of corresponding target tables. For formats where column-level metadata might not be available, such as `CSV` and `JSON`, `COPY FROM` infers column types based on the data content itself. While this process aims to accurately identify data types, it operates on a "best effort" basis, balancing type correctness with practical usability constraints. Additionally, for CSV files that often contain column names in the first line, COPY FROM uses this line as column headers and deduces the column types from the subsequent data, streamlining the initial data loading process significantly. 

## Handling Bad Data
`COPY FROM` provides robust mechanisms to identify and isolate bad data during the loading process.

## Handling partitioned data
`COPY FROM` effectively manages the loading of partitioned data, ensuring that data is inserted into the correct partitions based on predefined rules or schema setups, optimizing query performance and data management.

## Filtering data to be loaded
You can use the `LIMIT` clause to control the amount of data loaded into tables, for example when managing data previews and sample loads. 

`COPY FROM` also supports an `OFFSET` clause, allowing users to skip a specified number of rows in each input file before starting the data load. This is useful when users need to exclude certain initial data entries from being loaded.

## Examples

### Setup
The following examples use a simple dataset that you can create using these simple instructions:

Create sample of data in 2 different formats and push it to existing S3 bucket (engine should have write access to this bucket otherwise, credentials need to be provided).

Create three rows of data with two different data types and push it to an existing S3 bucket (your Firebolt engine should have write access to this bucket, otherwise credentials need to be provided).
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
```

| not_a (INTEGER) | not_b (TEXT) |
|:----------------|:-------------|

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

SELECT * FROM target_parquet_1;
```

| a (DATE) | b (TEXT) |
|:---------|:---------|

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






