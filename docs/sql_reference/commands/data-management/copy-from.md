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

Loads data from an AWS S3 bucket into Firebolt using `COPY FROM`. `COPY FROM` can accommodate different data loading workflows including the following:


* Automatically discover the schema during data loading.
* Use `PATTERN` to select multiple files or directories.
* Load multiple files in parallel into a target table, automatically creating the table if it doesn't exist.
* Load metadata about your source files into a table.
* Handle errors during data loading.


<!-- This comment is needed for both the list above and the list below to render. -->

## Table of contents
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
    [ QUOTE = { 'character' | **DOUBLE_QUOTE** | SINGLE_QUOTE } ]
    [ ESCAPE = 'character' ]
    [ NULL_STRING = 'string' ]
    [ EMPTY_FIELD_AS_NULL = { **TRUE** | FALSE } ]
    [ SKIP_BLANK_LINES = { **FALSE** | TRUE } ]
    [ DATE_FORMAT = <date_format> ]
    [ TIMESTAMP_FORMAT = <timestamp_format> ]

```

## Parameters

{: .no_toc}

| Parameter                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:--------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<table_name>`             | The name of the target table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `<column_mapping>`         | This feature is only available if the target table already exists. You can use `column_mapping` to specify the mapping between the source and target schema. Select a column in the source file to map to the target file using either the name of the column or its index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `<column_name>`            | The name of a target column in a table. If `<source_column_index/name>` is not specified, source columns will be automatically mapped to target columns based on name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `<default_value>`          | A replacement value for any `NULL` value generated by mapping the source to the target. This data type of `default_value` must be compatible with the data type of the target column.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `<source_column_index>`    | The index position of the column in the source data to be mapped. If you are specifying multiple source files, `source_column_index` specifies the index for all source files. The index starts at `1`, and can be as large as `2^64-1`, which allows for a very large number of columns. If you prefix the index inside a command or query, precede the column index with a dollar sign (`$`) character. For example, prefix the index as shown in the following `COPY INTO` statement: `CREATE TABLE t(a text, b text); COPY INTO t(a $1, b $2) FROM 's3://my_bucket/my_folder/my_file';`.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `<source_column_name>`     | The name of the column in the source data to be mapped. If you are specifying multiple source files, `source_column_name` specifies the column name for all source files.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `<externalLocations>`      | One or multiple paths to an Amazon S3 bucket that contains source files. If `externalLocations` ends with a forward slash (`/`), Firebolt interprets its value as a folder. Otherwise, `externalLocations` is treated as the location for a single file. An example folder has the following format: `s3://my_bucket/my_folder/`. An example file has the following format: `s3://my_bucket/my_folder/my_file`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `<directoryLocation>`      | The Amazon S3 path to a directory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `CREDENTIALS`              | The Amazon S3 credentials for accessing the specified `<externalLocations>`. For more information, see [CREDENTIALS](../data-definition/create-external-table.md#credentials).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `PATTERN`                  |  	A string that represents a [glob pattern](https://en.wikipedia.org/wiki/Glob_(programming)), or regular expression, used to match filenames or other strings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `TYPE`                     | The file type that Firebolt should expect when loading files identified by `PATTERN`. If `TYPE` is unspecified, Firebolt automatically detects the file type using the file’s suffix. If a file matched by `PATTERN` does not match the specified `TYPE`, Firebolt will generate an error.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `AUTO_CREATE`              |  	Specify whether Firebolt should automatically create a table if it doesn’t already exist. The default setting is `TRUE`, allowing automatic table creation. If `AUTO_CREATE` is set to `FALSE`, Firebolt will generate an error if the target table is missing. If the target table already exists, `AUTO_CREATE` is ignored.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `ALLOW_COLUMN_MISMATCH`    | Set to `FALSE` to specify that all required columns must appear in the source files. A required column includes those specified in `<column_mapping>`, which are specified using either a name or index. If `ALLOW_COLUMN_MISMATCH` is set to `FALSE`, the source file must contain each required column by name or have enough columns to meet the required index. Missing data rows for required columns will trigger a row-based error for CSV or TSV files, or a file-based error for Parquet files.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `ERROR_FILE`               | The Amazon S3 location where error files will be written. See the previous `<externalLocations>` parameter definition for implementation. No error files are created by default or if the specified path doesn’t exist. If `ERROR_FILE` is specified, a subdirectory is created based on the time of load submission in the format: `YearMonthDay-HourMinuteSecond + QueryID`, such as: `20220330-173205`). For CSV files, this directory will contain a `rejected_rows.csv` file containing erroneous data rows, and an `error_reasons.csv` file, containing the reasons that the errors were generated. Because Parquet doesn't produce row-based error files, on error, only an `error_reasons.csv` file is generated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `ERROR_FILE_CREDENTIALS`    | The Amazon S3 credentials required to write an error file to `<externalLocations>`. For more information, see [CREDENTIALS](../data-definition/create-external-table.md#credentials).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `MAX_ERRORS_PER_FILE`      | Specify the maximum number of rows that can be rejected per file. `MAX_ERRORS_PER_FILE` can be integer or percentage in the format "integer%", such as `100%`. The only valid percentage options are `0%` and `100%`. By default, no errors are allowed. If `MAX_ERRORS_PER_FILE` is set to `100%`, then all errors are allowed. If the threshold is exceeded, an error will occur.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

### Parameters for CSV files

| Parameter             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:----------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `HEADER`              | Specify if the file contains a header line containing the column names. If HEADER is TRUE, the first line will be interpreted to contain column names.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `DELIMITER`           | Specify the character used to separate fields. The default delimiter is a comma (`,`).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `NEWLINE`             | Specify the character used to delimit rows. The default delimiter is `\n`. If `NEWLINE` is `\n`, then `\r`, `\r\n`, and `\n\r` are also treated as newline delimiters. Custom delimiters are allowed only if the target table already exists.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `QUOTE`               | Specify the character used for quoting fields. The default is `DOUBLE_QUOTE`, or (`"`). If `SINGLE_QUOTE` is specified, the quote character will be set to (`'`).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `ESCAPE`              | Specify the character used to escape special characters. The default character is the quote (`'`) character.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `NULL_STRING`         | Specify the string used to represent NULL values. The default is an empty string, which means that no specific null string is defined.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `EMPTY_FIELD_AS_NULL` | Specify whether empty fields should be interpreted as `NULL` values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `SKIP_BLANK_LINES`    | Specify whether to ignore blank lines.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `DATE_FORMAT`         | Specify the date format for parsing text into date columns. This format will apply to all columns loaded as date columns. For supported formats, see [TO_DATE](../../functions-reference/date-and-time/to-date.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `TIMESTAMP_FORMAT`    | Specify the timestamp format for parsing text into timestamp columns. The format will apply to all columns loaded as timestamp columns. For supported formats, see [TO_TIMESTAMP](../../functions-reference/date-and-time/to-timestamp.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                             |


`COPY FROM` supports the following file formats:

* `Parquet`
* `CSV/TSV`

## Examples

### Automatic Schema Discovery
You can use the automatic schema discovery feature in `COPY FROM` to handle large data sources instead of manually defining it. The following apply:

* **Parquet files** - Firebolt automatically reads metadata in Parquet files to create corresponding target tables.
* **CSV files** - Firebolt infers column types based on the data content itself. Use `WITH HEADER=TRUE` if your CSV file contains column names in the first line. `COPY FROM` deduces the column types from your data, streamlining the initial data loading process significantly.

Automatic schema discovery operates on a "best effort" basis, and attempts to balance accuracy with practical usability, but it may not always be error-free.

The following query reads `levels.csv`, a sample dataset from the fictional [Ultra Fast Gaming Inc](https://help.firebolt.io/t/ultra-fast-gaming-firebolt-sample-dataset/250). The example implicitly uses automatic schema creation with `AUTO_CREATE=TRUE`, which defaults to `TRUE`, and also triggers automatic table creation:

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
You can use the `PATTERN` feature, which uses [regular expressions](https://en.wikipedia.org/wiki/Glob_(programming)), to select several files that match the specified pattern to populate an existing target table. The following example uses the `*.csv` pattern to read all files ending in `.csv` into the `pattern_target` table:

```sql
COPY pattern_target FROM 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv'
WITH TYPE=CSV HEADER=TRUE PATTERN='*.csv';
```

### Load multiple files and directories in parallel
You can use `COPY FROM` to read multiple sources and from multiple directories into a single table, simultaneously. The following code example reads any file ending in `.parquet` from multiple directories into `table_from_multiple_directories`.

```sql
COPY table_from_multiple_directories FROM 
    's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/playstats/TournamentID=1/',
    's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/playstats/TournamentID=10/',
    's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/playstats/TournamentID=100/'
WITH pattern='*.parquet';
```

The following code example reads two CSV files into `table_from_multiple_files`:

```sql
COPY table_from_multiple_files FROM 
's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv',
's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/tournaments.csv'
WITH HEADER=TRUE;
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

The first three rows of the sample output follow:

| LevelID | date_of_creation      |
|---------|-----------------------|
| 1       | 2023-02-27 10:06:52   |
| 2       | 2023-02-27 10:06:52   |
| 3       | 2023-02-27 10:06:52   |

### Error handling
The following sections show you how to handle errors for both CSV and Parquet files.

#### Column mismatch errors in CSV

When there is a mismatch between source and target table columns, Firebolt generates an error. To demonstrate this error, the following example creates a table that contains a `LevelID2` column, which is defined as `NOT NULL`. By default, Firebolt will attempt to insert `NULL` values into the missing column, which does not appear in the `levels.csv` dataset, causing an error:

```sql
CREATE TABLE col_mismatch_csv ("LevelID2" int NOT NULL);

COPY col_mismatch_csv FROM 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv'
WITH HEADER=TRUE MAX_ERRORS_PER_FILE='100%';
```
In the previous code example, when `COPY FROM` does not see the same column name in the target table `col_mismatch_csv`, it tries to fill the column with `NULL` values. Because `LevelID2` is defined with a constraint that it cannot have `NULL` values, the query generates the following error:
`ERROR: The INSERT INTO statement failed because it tried to insert a NULL into the column LevelID2, which is NOT NULL. Please specify a value or redefine the column's logical constraints.`

##### Allow all errors
The previous code example uses `MAX_ERRORS_PER_FILE='0%'`, which causes the loading job to fail if there is a single error. You can change this behavior to allow errors. The following code example allows all errors, and the load job completes even if no data loads into the target table:

```sql
CREATE TABLE table_all_errors ("LevelID2" int NOT NULL);

COPY table_all_errors FROM 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv'
WITH HEADER=TRUE MAX_ERRORS_PER_FILE='100%';
```

##### Allow no errors, except column name mismatch
If you want to allow column name mismatch, but no other errors, you can define the table to allow `NULL` values when you create the table to insert into as follows:

```sql
COPY table_only_col_mismatch
  FROM 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv'
WITH HEADER=TRUE MAX_ERRORS_PER_FILE='0%';
```

The previous code example creates a table `table_only_col_mismatch` that contains only a single column `LevelID2`, that contains only `NULL` values.

##### Column data type mismatch

If you try to load data into a column in an existing table that has a different data type than the source data, `COPY FROM` generates a casting error. To demonstrate this error, the following example intentionally creates a table that defines the `LevelID` column incorrectly as an integer, instead of as text, and then attempts to copy data into it:

```sql
CREATE TABLE col_mismatch_type_csv ("LevelID" int NOT NULL);

COPY col_mismatch_type_csv
  FROM 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv'
WITH TYPE=CSV HEADER=FALSE;
```

The previous code example generates the following error:
`ERROR: Unable to cast text 'LevelID' to integer`.

In the previous code example, the query generates an error because the default value for `MAX_ERRORS_PER_FILE` is `0`. You can set `MAX_ERRORS_PER_FILE` to `100%` to allow all errors,  as shown in the following section.

##### Allow all errors, and write them to file

You can also allow all errors, so that the loading job continues until it has attempted to load all rows in your dataset, and write any errors that are generated into an Amazon S3 bucket.  If your bucket requires access credentials, you must specify them so that Firebolt can write the error files on your behalf. If you allow all errors, data rows that load without error are ingested in row order. For CSV files, a loading job that specifies writing error files will write files with the following syntax to your Amazon S3 bucket:

* `error_reasons.csv` - An error file that contains all the reasons that a row generated an error.
* `rejected_rows.csv` - An error file that contains all the rejected rows in row order.

Parquet doesn't produce row-based error files. On error, only a `error_reasons.csv` file is generated.

The previous files will have an order appended to the name such as `error_reasons_0.csv`.

The following code example allows all errors, provides credentials, and writes two error files to an Amazon S3 bucket: 

```sql
COPY table_write_errors FROM 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv'
CREDENTIALS = (
    AWS_KEY_ID = 'YOUR_AWS_KEY_ID',
    AWS_SECRET_KEY = 'YOUR_AWS_SECRET_KEY'
)
WITH HEADER=FALSE MAX_ERRORS_PER_FILE='100%' error_file='s3://bucket_name/error_directory/';
```
To provide your credentials in the previous example, do the following:

* Replace the `<aws_key_id>` with an AWS access key that is associated with an AWS user or AWS IAM role. The AWS access key is a 20-character string such as `AKIAIOSFODNN7EXAMPLE`.
* Replace the `<aws_secret_key>` with an AWS secret access key associated with the user or role associated with the AWS access key. The AWS secret access key is a 40-character string such as `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`.

##### Read errors from file

The previous `COPY FROM` example created two error files, one that describes the errors and one that contains the rows that had errors. Use `COPY FROM` to load an error file that describes the error reasons.  The following code example shows how to read all files that begin with `error_reasons` and end with `.csv` into an `error_reasons` table:

```sql
COPY error_reasons FROM 's3://bucket_name/error_directory/' 
WITH PATTERN='*error_reasons*.csv' HEADER=TRUE;
```

The following code returns the contents of the `error_reasons` table:

```sql
SELECT * from error_reasons;
```

The following output shows an example of the contents of the `error_reasons` table:

| file_name                          | source_line_num | error_message            |
|------------------------------------|-----------------|--------------------------|
| firebolt_sample_dataset/levels.csv | 1               | Error while casting      |


The following code reads all files that begin with `rejected_rows` and ends with `.csv` into a rejected_rows table:

```sql
COPY rejected_rows FROM 's3://bucket_name/error_directory/'
WITH PATTERN='*rejected_rows*.csv' HEADER=FALSE;
```

The following code returns the contents of the `rejected_rows` table:

```sql
SELECT * FROM rejected_rows;
```

The following output shows an example of the contents of the `rejected_rows` table:

| f0 (TEXT) | f1 (TEXT) |
|-----------|-----------|
| a         | b         |

##### Column mapping and default values
You can map a specific source column to a target column, and specify a default value to replace any `NULL` values generated during mapping. The following code example takes an existing column `LevelID` from the `levels.csv` sample dataset, and maps it into a column `LevelID_team_A` in a `target_csv_7` table. It also maps a column `Country`, which doesn’t exist in the `levels.csv` dataset, into a `LevelsID_team_B` column, and specifies a default value of `50` to replace `NULL` values during mapping: 

```sql
CREATE TABLE target_default_mapping ("LevelID_team_A" text, "LevelID_team_B" text);
COPY target_default_mapping("LevelID_team_A" "LevelID", "LevelID_team_B" default 50 "Country")
  FROM 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv'
WITH HEADER=TRUE;
```
#### Type mismatch errors in Parquet files

If you read a column from a Parquet file into a table with an incompatible data type, the mapping generates a casting error. A loading job that specifies writing error files will write the following to your Amazon S3 bucket:

* `error_reasons.csv` - An error file that contains all the reasons that a row generated an error.
* `rejected_rows.csv` - An error file that contains all the rejected rows in row order.

The following code uses the Firebolt sample `players` dataset which has a column `PlayerID` with a data type of `INTEGER`, and attempts to read it into an existing column with a `DATE` data type:

```sql
CREATE TABLE IF NOT EXISTS
 players (
   PlayerID DATE,
   Nickname TEXT,
   Email TEXT);

COPY players FROM 's3://firebolt-sample-datasets-public-us-east-1/gaming/parquet/players/'
WITH TYPE=PARQUET MAX_ERRORS_PER_FILE='0%'
ERROR_FILE='s3://bucket_name/parquet_error_directory/';
```

Use the following sample code to view a table that contains the contents of all error files that contain `error_reasons` and end in `.csv`:

```sql
COPY error_reasons FROM 's3://bucket_name/parquet_error_directory/'
WITH PATTERN='*error_reasons*.csv' HEADER=TRUE;

SELECT * FROM error_reasons;
```

| file_name                                                                      | source_line_num | error_message                                                                           |
|-------------------------------------------------------------------------------|----------------|-----------------------------------------------------------------------------------------|
| gaming/parquet/players/11afd184-d2d4-4471-b23c-a14f4c0945a2_1_0_0.snappy.parquet | 0              | Can not assignment cast column playerid from type integer null to type date null         |

The previous example created a file-based error, or one that affects the entire file during processing, such as errors caused by incorrect format or missing files. Thus, the query does not produce the `rejected_rows` error file. 




