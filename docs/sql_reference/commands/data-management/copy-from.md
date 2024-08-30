---
layout: default
title: COPY FROM
description: Reference and syntax for the COPY command that copies data from S3 files into a Firebolt table.
great_grand_parent: SQL reference
grand_parent: SQL reference
parent: Data management
---
# COPY FROM
{: .no_toc}

This guide shows you how to load data from an AWS S3 bucket into Firebolt using `COPY FROM`. `COPY FROM` can accommodate different data loading workflows including the following:


* Automatically discover the schema during data loading.
* Load multiple files in parallel into a target table.
* Handle errors during data loading.


<!-- This comment is needed for both the list above and the list below to render. -->


* Topic ToC
{:toc}

## Syntax

```sql
COPY
[INTO] <table_name> [ <column_mapping> ] 
FROM <externalLocations>
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

| Parameter                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<table_name>`           | The name of the target table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `<column_mapping>`       | Optional. Only available of target table exists. Specify mapping between src schema and target schema. With this feature one can choose for each column in the target table a column from src files by name or by index.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `<column_name>`          | The name of a target column in the table. If `<source_column_index/name>` not specified, the src columns will be mapped by this name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `<default_value>`        | A value that replace each NULL value generated by the src. This value must be convertible to the target column datatype.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `<source_column_index>`  | The index of the src column that will be mapped (same index for all the files). This value range is [1,2^64-1]. It needs to follow the `$` character.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `<source_column_name>`   | The name of the src column that will be mapped (same name for all the files).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `<externalLocations>`     | One or multiple paths to S3 locations. If it ends with `/` it is interpreted as directory otherwise as single file. Folder example: `s3://my_bucket/my_folder/`. File example: `s3://my_bucket/my_folder/my_file`.                                                                                                                                                                                                                                                                                                                                                                                                             |
| `<directoryLocation>` | S3 path to a directory 
| `CREDENTIALS`            | The Amazon S3 credentials for accessing the specified `<externalLocations>`. See [CREDENTIALS](../data-definition/create-external-table.md#credentials).                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `PATTERN`                | A regular expression pattern string (glob). For additional explenation visit: https://en.wikipedia.org/wiki/Glob_(programming).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `TYPE`                   | Specify the file type Firebolt expects to ingest given the `PATTERN`. If not specified it will be auto detected by the suffix of a file. If a file referenced using `PATTERN` does not conform to the specified `TYPE`, an error occurs.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `AUTO_CREATE`            | Specify if the table can be automatically created by working alongside with automatic schema discovery. By default, automatic table creation is enabled (value: TRUE). If value is TRUE and the target table already exists, `AUTO_CREATE` is ignored.                                                                                                                                                                                                                                                                                                                                                                                                       |
| `ALLOW_COLUMN_MISMATCH`  | Specify if all required columns must appear in the src files. A column can be required by name or by index as described in `<column_mapping>`. If a column is required by name then a column with the same name must appear in the source files otherwise a file based error will be raised (and will be handled according to the error handling described in this doc). For the CSV and TSV formats it is possible that a column with that name exists but it does not appear in every row, which is considered as a row based error. If a column is required by index then the file must contain at least #index number of columns (file based error for parquet, row based error for CSV and TSV). |
| `ERROR_FILE`             | Defines S3 location where rejected records will be stored. See `<externalLocations>` parameter definition above for format details. By default or if the specified path doesn't exist, no error files will be created. If specified a child directory is created based on the time of load submission in the format YearMonthDay -HourMinuteSecond + QueryID (Ex. 20220330-173205/<query_id>/). In this folder, two types of files are written: 1) the reason (error) file: rejected_rows.csv. and the data (row) file: error_reasons.csv.                                                                                                                    |
| `ERROR_FILE_CREDENTIALS` | The Amazon S3 credentials for accessing the specified `<externalLocations>` for error file creation. See [CREDENTIALS](../data-definition/create-external-table.md#credentials).                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
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

`COPY FROM` supports the following file formats:

* `Parquet`
* `CSV/TSV`

## Examples

### Automatic Schema Discovery
You can use the automatic schema discovery feature in `COPY FROM` to handle large data sources, reducing the risk of errors that can arise from manual schema definition. The following apply:

* Parquet files - Firebolt automatically reads metadata in Parquet files to create corresponding target tables.
* CSV files - Firebolt infers column types based on the data content itself. Use `WITH HEADER=TRUE` if your CSV file contains column names in the first line. `COPY FROM` deduces the column types from your data, streamlining the initial data loading process significantly.

Automatic schema discovery operates on a "best effort" basis, and attempts to balance accuracy with practical usability, but it may not always be error-free.

The following query reads `levels.csv`, a sample dataset from the fictional [Ultra Fast Gaming Inc](https://help.firebolt.io/t/ultra-fast-gaming-firebolt-sample-dataset/250). The example implicitly uses automatic schema creation with `AUTO_CREATE=TRUE`, which defaults to `TRUE`, and also triggers automatic table creation.

```sql
COPY automatic_schema_table 
FROM 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv'
WITH HEADER=TRUE;
```

Use the following example code to display the table contents, ordered by the fourth column, followed by the fifth column:

```sql
SELECT * FROM automatic_schema_table ORDER BY 4,5;
```

### Use PATTERN to insert data into an existing table
You can use the `PATTERN` feature, which uses [regular expressions](https://en.wikipedia.org/wiki/Glob_(programming)), of `COPY FROM` to select several files that match the specified pattern to populate an existing target table. The following example uses the the `*.csv` pattern to read all files ending in `.csv` into the `pattern_target` table:

```sql
COPY pattern_target FROM 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv'
WITH TYPE=CSV HEADER=TRUE PATTERN='*.csv';
```

### Load multiple files and directories in parallel
You can use `COPY FROM` to read multiple sources and from multiple directories into a single table, simultaneously. The following code example reads any file ending in `.csv` from multiple directories into `table_from_multiple_directories`.

```sql
COPY table_from_multiple_directories FROM 
    's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/playstats/TournamentID=1/',
    's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/playstats/TournamentID=10/',
    's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/playstats/TournamentID=100/'

WITH pattern='*.parquet';
```

The following code example reads two files into `tarble_from_multiple_files`:

```sql
COPY table_from_multiple_files FROM 
's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv',
's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/tournaments.csv';
```

### Load metadata into a table
You can load metadata information about your source file into your table so that you can track the source name, timestamp, size, and etag information for each row. You can use the following metadata columns:

* $source_file_name - The full path of the source file in an Amazon S3 bucket, without the name of the bucket. For example, if your bucket is: `s3://my_bucket/xyz/year=2018/month=01/part-00001.parquet`, then `$source_file_name` is `xyz/year=2018/month=01/part-00001.parquet`.
* $source_file_timestamp - The timestamp in UTC, to the second when the source file was last modified in an Amazon S3 bucket.
* $source_file_size - The size in bytes of the source file.
* $source_file_etag - The [ETag](https://en.wikipedia.org/wiki/HTTP_ETag) of the file, often used for version control.

The following code creates the `levels` table, and populates it with information from the `LevelID` column and the timestamp from the source data:

```sql
CREATE TABLE levels ("LevelID" TEXT NOT NULL, date_of_creation TIMESTAMP);
COPY INTO levels("LevelID", date_of_creation $source_file_timestamp) FROM 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv' WITH HEADER=TRUE;
```

The following code example displays the contents of `levels`:

```sql
SELECT * FROM levels;
```

The first three rows of the sample output follows:

| LevelID | date_of_creation      |
|---------|-----------------------|
| 1       | 2023-02-27 10:06:52   |
| 2       | 2023-02-27 10:06:52   |
| 3       | 2023-02-27 10:06:52   |

### Error handling
The following sections show you how to handle errors for both CSV and Parquet files.

#### Column mismatch errors in CSV

When there is a mismatch between source and target table columns, Firebolt inserts `NULL` values into the missing columns. To demonstrate this error, the following example intentionally creates a table that contains a `LevelID2` column, which is defined as `NOT NULL`, that does not appear in the `levels.csv` dataset:

```sql
CREATE TABLE col_mismatch_csv ("LevelID2" int NOT NULL);

COPY col_mismatch_csv FROM 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv'
WITH HEADER=TRUE MAX_ERRORS_PER_FILE='0%';
```
In the previous code example, when `COPY FROM` does not see the same column name in the target table `col_mismatch_csv`, it fills the column with `NULL` values. Because `LevelID2` is defined with a constraint that it cannot have `NULL` values, the query generates the following error:
`ERROR: The INSERT INTO statement failed because it tried to insert a NULL into the column LevelID2, which is NOT NULL. Please specify a value or redefine the column's logical constraints.`

##### Allow all errors
The previous code example uses `MAX_ERRORS_PER_FILE='0%'`, which causes the loading job to fail if there is a single error. You can change this behavior to allow errors. The following code example allows all errors, and the load job completes even if no data loads into the target table:

```sql
CREATE TABLE table_all_errors ("LevelID2" int NOT NULL);

COPY table_all_errors FROM 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv'
WITH HEADER=TRUE MAX_ERRORS_PER_FILE='100%';
```

##### Allow no errors, except column name mismatch
If you want to allow column name mismatch, but no other errors, you can define the table to allow NULL values when you create the table to insert into as follows:

```sql
COPY table_only_col_mismatch
  FROM 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv'
WITH HEADER=TRUE MAX_ERRORS_PER_FILE='0%';
```

The previous code example creates a table `table_only_col_mismatch` that contains only a single column `LevelID2`, that contains only `NULL` values.

##### Column data type mismatch

If you try to load data into a column in an existing table that has a different data type than the incoming data, `COPY FROM` generates a casting error. To demonstrate this error, the following example intentionally creates a table that defines the `LevelID` column incorrectly as an integer, instead of as text, and then attempts to copy data into it:

```sql
CREATE TABLE col_mismatch_type_csv ("LevelID" int NOT NULL);

COPY col_mismatch_type_csv
  FROM 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv'
WITH TYPE=CSV HEADER=FALSE;
```

The previous code example generates the following error:
`ERROR: Unable to cast text 'LevelID' to integer`

In the previous code example, the query generates an error because the default value for `MAX_ERRORS_PER_FILE` is `0`. You can set `MAX_ERRORS_PER_FILE` to `100%` to allow all errors,  as shown in the following section.

##### Allow all errors, and write them to file

You can also allow all errors, so that the loading job continues until it attempts to load all rows in your dataset, and write any errors that are generated into an Amazon s3 bucket.  If your bucket requires access credentials, you must specify them so that Firebolt can write the error files on your behalf. If you allow all errors, data rows that load without error are ingested in row order. A loading job that specifies writing error files will write files with the following syntax to your Amazon S3 bucket:

* `error_reasons.csv` - An error file that contains all of the reasons that a row generated an error.
* `rejected_rows.csv` - An error file that contains all of the rejected rows in row order.

The previous files will have an order appended to the name such as `error_reasons_0.csv`.

The following code example allows all errors, provides credentials, and writes two error files to an Amazon S3  bucket: 

```sql
COPY table_write_errors FROM 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv'
CREDENTIALS = (
    AWS_KEY_ID = 'YOUR_AWS_KEY_ID',
    AWS_SECRET_KEY = 'YOUR_AWS_SECRET_KEY'
)
WITH HEADER=FALSE MAX_ERRORS_PER_FILE='100%' error_file='s3://bucket_name/error_directory/';
```
To provide your credentials in the previous example, do the following:

* Replace the <aws_key_id> with an AWS access key that is associated with an AWS user or AWS IAM role. The AWS access key is a 20-character string such as `AKIAIOSFODNN7EXAMPLE`.
* Replace the <aws_secret_key> with an AWS secret access key associated with the user or role associated with the AWS access key. The AWS secret access key is a 40-character string such as `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`.

##### Read errors from file

The previous `COPY FROM` example created two error files, one that describes the errors and one that contains the rows that had errors. Use `COPY FROM` to load an error file that describes the error reasons.  The following code example shows how to read all files that begin with `error_reasons` and end with `csv` into an `error_reasons` table:

```sql
COPY error_reasons FROM 's3://bucket_name/error_directory/' 
WITH PATTERN='*error_reasons*.csv' HEADER=TRUE;
```

The following code retruns the contents of the `error_reasons` table:

```sql
SELECT * from error_reasons;
```

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
You can use the `LIMIT` clause to control the amount of data loaded into tables, for example when managing data previews and sample loads. 

`COPY FROM` also supports an `OFFSET` clause, allowing users to skip a specified number of rows in each input file before starting the data load. This is useful when users need to exclude certain initial data entries from being loaded.

```sql
COPY sample_data
FROM 's3://data-bucket/large_dataset.csv' LIMIT 100 OFFSET 10
WITH TYPE = CSV HEADER = TRUE
```

## Examples



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



