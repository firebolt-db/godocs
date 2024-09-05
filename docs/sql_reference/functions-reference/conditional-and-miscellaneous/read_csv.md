---
layout: default
title: READ_CSV
description: Reference material for READ_CSV function
grand_parent: SQL functions
parent: Conditional and miscellaneous functions
great_grand_parent: SQL reference
---

# READ_CSV

A table-valued function (TVF) that accepts a URL to an Amazon bucket containing CSV files, credentials and CSV configuration options. `READ_CSV` returns a table with data from the specified CSV file, where each cell is read as `TEXT`.

## Syntax

```sql
READ_CSV ( 
    url => <file_url>
    [, compression => <file_compression>]
    [, aws_key_id => <aws_key_id>]
    [, aws_secret_key => <aws_secret_key>]
    [, are_credentials_encrypted => <are_credentials_encrypted>]
    [, header => <csv_has_header_row>]
    [, delimiter => <field_delimiter>]
    [, quote => { "'" | '"' | SINGLE_QUOTE | DOUBLE_QUOTE}]
    [, null_string => <null_string>]
    [, escape => <escape_character>]
    [, skip_blank_lines => <skip_blank_lines>]
    [, empty_field_as_null => <empty_field_as_null>]
    )
```

## Parameters

| Parameter                     | Description                                                                                      | Supported input types |
|:------------------------------|:-------------------------------------------------------------------------------------------------|:----------------------|
| `<url>`                       | The location of the Amazon S3 bucket containing your files. The expected format is `s3://{bucket_name}/{full_file_path}`.          | `TEXT`                |
| `<compression>`               | The [compression type](../../commands/data-definition/create-external-table.md#compression) of the input file. If `compression` is not set, `compression` is inferred from the file extension.           | `TEXT`                |
| `<aws_key_id>`                | The AWS key ID.                                                                                      | `TEXT`                |
| `<aws_secret_key>`            | The AWS secret key.                                                                                  | `TEXT`                |
| `<are_credentials_encrypted>` | Set to `TRUE` if the `aws_key_id` and `aws_secret_key` are provided in encrypted form.                    | `BOOL`                |
| `<header>`                    | Set to `TRUE` if the first row of the CSV file contains a header row containing the column names.                                 | `TEXT`                |
| `<delimiter>`                 | Specify the character used to separate fields. The default delimiter is a comma (`,`).                                                            | `TEXT`                |
| `<quote>`                     | Specify the character used for quoting fields. The default is double quote (`"`). If a single quote is specified, the quote character will be set to (`'`). Accepts only `DOUBLE_QUOTE`, `SINGLE_QUOTE`, `'`, or `"`.     | `TEXT`                |
| `<null_string>`               | Specify the string used to represent `NULL` values. The default is an empty string, which means that empty strings are interpreted as null values.                                                             | `TEXT`                |
| `<escape>`                    | Specify the character used to escape special characters. The default character is the quote (`'`) character.                                                                                 | `TEXT`                |
| `<skip_blank_lines>`          | Set to `TRUE` to ignore blank lines in the file.                                                     | `BOOL`                |
| `<empty_field_as_null>`       | Specify whether empty fields should be interpreted as `NULL` values. The default is `TRUE`. If set to `FALSE`, empty fields are interpreted as empty strings.                                               | `BOOL`                |

The following apply:

* The `url` can be passed as either the first positional parameter or a named parameter. For example, the following two queries will both read the same file:

    ```sql
    SELECT * FROM READ_CSV(url => 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv');
    SELECT * FROM READ_CSV('s3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv');
    ```

* All parameters, except for `url`, are optional. 

* Parameters must be named using the following syntax: `=>`.

* If you provide either `aws_key_id` or `aws_secret_key`, you must provide both.

## Return Type

The result is a table with the data from the CSV file. Each cell is read as a `TEXT`.

## Examples

**Query:**
In the following example, the `url` is set as the first positional parameter and reads a CSV file.

```sql
SELECT * FROM READ_CSV('s3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv');
```
**Returns**:

| f0 | f1 | f2 | f3 | f4 | f5 | f6 | f7 | f8 | ... |
|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|
| LevelID | GameID | Level | Name | LevelType | NextLevel | MinPointsToPass | MaxPoints | NumberOfLaps | ... |
| 1 | 1 | 1 | Thunderbolt Circuit | FastestLap | 2 | 5 | 20 | 5 | ... |
| 2 | 1 | 2 | Velocity Vale | FirstToComplete | 3 | 15 | 30 | 10 | ... |
| 3 | 1 | 3 | Raceway Ridge | FastestLap | 4 | 25 | 40 | 20 | ... |
| 4 | 1 | 4 | Nitro Narrows | FirstToComplete | 5 | 60 | 100 | 10 | ... |
| 5 | 1 | 5 | Thunder Road | FirstToComplete | 6 | 80 | 150 | 15 | ... |
| 6 | 1 | 6 | Burnout Boulevard | Drift | 7 | 50 | 80 | 8 | ... |
| 7 | 1 | 7 | Speed Street | FastestLap | 8 | 40 | 70 | 7 | ... |
| 8 | 1 | 8 | Racing Ravine | FastestLap | 9 | 60 | 100 | 20 | ... |
| 9 | 1 | 9 | Drift District | Drift | 10 | 100 | 250 | 25 | ... |
| 10 | 1 | 10 | Acceleration Alley | FirstToComplete | null | 200 | 500 | 50 | ... |


**Query:**
The following example accepts `url` as a named parameter and reads a CSV file with column names in the first row:

```sql
SELECT * FROM READ_CSV(url => 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv', 
        header => true);
```
**Returns**:

| LevelID | GameID | Level              | Name                | LevelType       | NextLevel | MinPointsToPass | MaxPoints | NumberOfLaps | ... |
|:------- |:------ |:------------------ |:------------------- |:--------------- |:--------- |:--------------- |:--------- |:------------ |:-- |
| 1  | 1 | Thunderbolt Circuit | FastestLap       | 2 | 5  | 20 | 5  | 20 | ... |
| 2  | 1 | Velocity Vale      | FirstToComplete  | 3 | 15 | 30 | 10 | 10 | ... |
| 3  | 1 | Raceway Ridge      | FastestLap       | 4 | 25 | 40 | 20 | 20 | ... |
| 4  | 1 | Nitro Narrows      | FirstToComplete  | 5 | 60 | 100| 10 | 10 | ... |
| 5  | 1 | Thunder Road       | FirstToComplete  | 6 | 80 | 150| 15 | 15 | ... |
| 6  | 1 | Burnout Boulevard  | Drift            | 7 | 50 | 80 | 8  | 8  | ... |
| 7  | 1 | Speed Street       | FastestLap       | 8 | 40 | 70 | 7  | 7  | ... |
| 8  | 1 | Racing Ravine      | FastestLap       | 9 | 60 | 100| 20 | 20 | ... |
| 9  | 1 | Drift District     | Drift            | 10| 100| 250| 25 | 25 | ... |
| 10 | 1 | Acceleration Alley | FirstToComplete  | null   | 200| 500| 50 | 50 | ... |


**Query:**
The following example reads a CSV with headers and reads empty values as empty strings, rather than null values:

```sql
SELECT * FROM READ_CSV(url => 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv',
        header => true, empty_field_as_null => false);
```
**Returns**:

| LevelID | GameID | Level              | Name                | LevelType       | ... |
|:------- |:------ |:------------------ |:------------------- |:--------------- |:--------- |
| 1       | 1      | Thunderbolt Circuit| FastestLap          | 2               | ...        |
| 2       | 1      | Velocity Vale      | FirstToComplete     | 3               | ...       |
| 3       | 1      | Raceway Ridge      | FastestLap          | 4               | ...        |
| 4       | 1      | Nitro Narrows      | FirstToComplete     | 5               | ...        |
| 5       | 1      | Thunder Road       | FirstToComplete     | 6               | ...        |
| 6       | 1      | Burnout Boulevard  | Drift               | 7               | ...        |
| 7       | 1      | Speed Street       | FastestLap          | 8               | ...        |
| 8       | 1      | Racing Ravine      | FastestLap          | 9               | ...        |
| 9       | 1      | Drift District     | Drift               | 10              | ...       |
| 10      | 1      | Acceleration Alley | FirstToComplete     |             | ...       |
