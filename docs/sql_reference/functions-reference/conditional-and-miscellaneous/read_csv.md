---
layout: default
title: READ_CSV
description: Reference material for READ_CSV function
grand_parent: SQL functions
parent: Conditional and miscellaneous functions
great_grand_parent: SQL reference
---

# READ_CSV

A Table-valued function (TVF) that takes an Amazon S3 URL, credentials and relevant CSV options, and returns a table of data from the target file.

This TVF returns a table with the data from the CSV file. Each cell is read as a `STRING`.

## Syntax

```sql
READ_CSV ( 
    url => <file_url>
    [, compression => <file_compression>]
    [, aws_key_id => <aws_key_id>]
    [, aws_secret_key => <aws_secret_key>]
    [, aws_arn => <aws_arn>]
    [, aws_arn_role_external_id => <aws_arn_role_external_id>]
    [, are_credentials_encrypted => <are_credentials_encrypted>]
    [, aws_arn_role_external_id => <aws_arn_role_external_id>]
    [, header => <csv_has_header_row>]
    [, delimiter => <field_delimiter>]
    [, quote => {'DOUBLE_QUOTE'|'SINGLE_QUOTE'}]
    [, null_string => <null_string>]
    [, escape => <escape_character>]
    [, skip_blank_lines => <skip_blank_lines>]
    [, empty_field_as_null => <empty_field_as_null>]
    )
```

## Parameters

| Parameter                     | Description                                                                                      | Supported input types |
|:------------------------------|:-------------------------------------------------------------------------------------------------|:----------------------|
| `<url>`                       | Amazon S3 files location. The expected format is 's3://{bucket_name}/{full_file_path}'.          | `TEXT`                |
| `<compression>`               | The compression of the the file. If is not set it will be inferred from the extension.           | `TEXT`                |
| `<aws_key_id>`                | AWS key ID.                                                                                      | `TEXT`                |
| `<aws_secret_key>`            | AWS secret key.                                                                                  | `TEXT`                |
| `<aws_arn>`                   | AWS Role ARN.                                                                                    | `TEXT`                |
| `<aws_arn_role_external_id>`  | External ID for AWS Role.                                                                        | `TEXT`                |
| `<are_credentials_encrypted>` | True if the `aws_key_id` and `aws_secret_key` are provided in encrypted form.                    | `BOOL`                |
| `<header>`                    | Should the first row of the CSV file be considered a header row.                                 | `TEXT`                |
| `<delimiter>`                 | Field delimiter. Comma by default `,`                                                            | `TEXT`                |
| `<quote>`                     | Which quote symbol used for strings columns. Accepts only 'DOUBLE_QUOTES' or 'SINGLE_QUOTE'.     | `TEXT`                |
| `<null_string>`               | String that will be parsed as `NULL`                                                             | `TEXT`                |
| `<escape>`                    | Escape character                                                                                 | `TEXT`                |
| `<skip_blank_lines>`          | Skip the file's blank line when set to `TRUE`                                                    | `BOOL`                |
| `<empty_field_as_null>`       | Consider empty fields as null when set to `TRUE`                                                 | `BOOL`                |

`url` can be passed as either the first positional parameter or a named parameter.

```sql
-- Both queries are equivalent
select * from read_csv(url => 's3://bucket/data.parquet');
select * from read_csv('s3://bucket/data.parquet');
```

Apart from `url`, all parameters are optional. 

Parameters must be named, i.e. specified using the syntax "=>" .

If you provide either `aws_key_id` or `aws_secret_key`, you must provide both.

If `aws_arn_role_external_id` is provided, then `aws_arn` must also be provided.

If `aws_key_id` and `aws_secret_key` are provided, then `aws_arn` and `aws_arn_role_external_id` must both be set to `NULL`. Similarly, if `aws_arn` and `aws_arn_role_external_id` are provided, then `aws_key_id` and `aws_secret_key` must both be set to `NULL`.

## Return Type

The result is a table with the data from the CSV file. Each cell is read as a `STRING`.

## Example

In those example `url` is set as the first positional parameter but it can be passed as a named parameter as well (e.g `url => 's3://bucket/data.csv'`).

**Query:**
```sql
select * from read_csv('s3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv');
```
**Returns**:

| f0 | f1 | f2 | f3 | f4 | f5 | f6 | f7 | f8 | f9 |
|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|
| LevelID | GameID | Level | Name | LevelType | NextLevel | MinPointsToPass | MaxPoints | NumberOfLaps |
| 1 | 1 | 1 | Thunderbolt Circuit | FastestLap | 2 | 5 | 20 | 5 |
| 2 | 1 | 2 | Velocity Vale | FirstToComplete | 3 | 15 | 30 | 10 |
| 3 | 1 | 3 | Raceway Ridge | FastestLap | 4 | 25 | 40 | 20 |
| 4 | 1 | 4 | Nitro Narrows | FirstToComplete | 5 | 60 | 100 | 10 |
| 5 | 1 | 5 | Thunder Road | FirstToComplete | 6 | 80 | 150 | 15 |
| 6 | 1 | 6 | Burnout Boulevard | Drift | 7 | 50 | 80 | 8 |
| 7 | 1 | 7 | Speed Street | FastestLap | 8 | 40 | 70 | 7 |
| 8 | 1 | 8 | Racing Ravine | FastestLap | 9 | 60 | 100 | 20 |
| 9 | 1 | 9 | Drift District | Drift | 10 | 100 | 250 | 25 |
| 10 | 1 | 10 | Acceleration Alley | FirstToComplete | null | 200 | 500 | 50 |


**Query:**
```sql
select * from read_csv('s3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv', 
        header=>true);
```
**Returns**:

| LevelID | GameID | Level              | Name                | LevelType       | NextLevel | MinPointsToPass | MaxPoints | NumberOfLaps |
|:------- |:------ |:------------------ |:------------------- |:--------------- |:--------- |:--------------- |:--------- |:------------ |
| 1  | 1 | Thunderbolt Circuit | FastestLap       | 2 | 5  | 20 | 5  | 20 |
| 2  | 1 | Velocity Vale      | FirstToComplete  | 3 | 15 | 30 | 10 | 10 |
| 3  | 1 | Raceway Ridge      | FastestLap       | 4 | 25 | 40 | 20 | 20 |
| 4  | 1 | Nitro Narrows      | FirstToComplete  | 5 | 60 | 100| 10 | 10 |
| 5  | 1 | Thunder Road       | FirstToComplete  | 6 | 80 | 150| 15 | 15 |
| 6  | 1 | Burnout Boulevard  | Drift            | 7 | 50 | 80 | 8  | 8  |
| 7  | 1 | Speed Street       | FastestLap       | 8 | 40 | 70 | 7  | 7  |
| 8  | 1 | Racing Ravine      | FastestLap       | 9 | 60 | 100| 20 | 20 |
| 9  | 1 | Drift District     | Drift            | 10| 100| 250| 25 | 25 |
| 10 | 1 | Acceleration Alley | FirstToComplete  |   | 200| 500| 50 | 50 |


**Query:**
```sql
select * from read_csv('s3://bucket/data.csv', header => true,
    empty_field_as_null => false);
```
**Returns**:

| LevelID | GameID | Level              | Name                | LevelType       | NextLevel | MinPointsToPass | MaxPoints | NumberOfLaps |
|:------- |:------ |:------------------ |:------------------- |:--------------- |:--------- |:--------------- |:--------- |:------------ |
| 1       | 1      | Thunderbolt Circuit| FastestLap          | 2               | 5         | 20              | 5         | 20           |
| 2       | 1      | Velocity Vale      | FirstToComplete     | 3               | 15        | 30              | 10        | 10           |
| 3       | 1      | Raceway Ridge      | FastestLap          | 4               | 25        | 40              | 20        | 20           |
| 4       | 1      | Nitro Narrows      | FirstToComplete     | 5               | 60        | 100             | 10        | 10           |
| 5       | 1      | Thunder Road       | FirstToComplete     | 6               | 80        | 150             | 15        | 15           |
| 6       | 1      | Burnout Boulevard  | Drift               | 7               | 50        | 80              | 8         | 8            |
| 7       | 1      | Speed Street       | FastestLap          | 8               | 40        | 70              | 7         | 7            |
| 8       | 1      | Racing Ravine      | FastestLap          | 9               | 60        | 100             | 20        | 20           |
| 9       | 1      | Drift District     | Drift               | 10              | 100       | 250             | 25        | 25           |
| 10      | 1      | Acceleration Alley | FirstToComplete     | null            | 200       | 500             | 50        | 50           |
