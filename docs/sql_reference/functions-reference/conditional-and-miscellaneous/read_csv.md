---
layout: default
title: READ_CSV
description: Reference material for READ_CSV function
grand_parent: SQL functions
parent: Conditional and miscellaneous functions
great_grand_parent: SQL reference
---

# READ_CSV

A Table-valued function (TVF) that takes an Amazon S3 URL, Credentials and relevant CSV options, and returns a table of data from the target file.

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
| `<compression>`               | The compression of the the file. It is infered from the extenssion then not set.                 | `TEXT`                |
| `<aws_key_id>`                | AWS key ID.                                                                                      | `TEXT`                |
| `<aws_secret_key>`            | AWS secret key.                                                                                  | `TEXT`                |
| `<aws_arn>`                   | AWS Role ARN.                                                                                    | `TEXT`                |
| `<aws_arn_role_external_id>>` | External ID for AWS Role.                                                                        | `TEXT`                |
| `<are_credentials_encrypted>>`| Are credentials encrypted                                                                        | `BOOL`                |
| `<header>>`                   | Should the first row of the CSV file be considered a header row.                                 | `TEXT`                |
| `<delimiter>>`                | Field delimiter. Comma by default `,`                                                            | `TEXT`                |
| `<quote>>`                    | Which quote symbol used for strings columns. Accepts only 'DOUBLE_QUOTES' or 'SINGLE_QUOTE'.     | `TEXT`                |
| `<null_string>>`              | String that will be parsed as `NULL`                                                             | `TEXT`                |
| `<escape>>`                   | Escape character                                                                                 | `TEXT`                |
| `<skip_blank_lines>>`         | Skip the file's blank line when set to `TRUE`                                                    | `BOOL`                |
| `<empty_field_as_null>>`      | Consider empty fields as null when set to `TRUE`                                                 | `BOOL`                |


Apart from `url`, all parameters are optional..

If you provide either `aws_key_id` or `aws_secret_key`, you must provide both.

If `aws_arn_role_external_id` is provided, then `aws_arn` must also be provided.

If `aws_key_id` and `aws_secret_key` are provided, then `aws_arn` and `aws_arn_role_external_id` must both be set to `NULL`. Similarly, if `aws_arn` and `aws_arn_role_external_id` are provided, then `aws_key_id` and `aws_secret_key` must both be set to `NULL`.

## Return Type

The result is a table with the data from the CSV file. Each columns is read and parsed as `STRING`.

## Example

In the next code examples, we read the following file from the bucket 's3://bucket/data.csv':

```csv
name, rank, note
Dave, 95, NONE
John, 60, 'need coaching'
Gene, 70, "improved"
Carl, 85,
```


**Query:**
```sql
select * from read_csv(url => 's3://bucket/data.csv');
```
**Returns**:
```
| f0 | f1 | f2 |
| :--- | :--- | :--- |
| name | rank | note |
| Dave | 95 | NONE |
| John | 60 | 'need coaching' |
| Gene | 70 | improved |
| Carl | 85 | null |
```

**Query:**
```sql
select * from read_csv(url => 's3://bucket/data.csv',
    header => true);
```
**Returns**:
```
| name | rank | note |
| :--- | :--- | :--- |
| Dave | 95 | NONE |
| John | 60 | 'need coaching' |
| Gene | 70 | improved |
| Carl | 85 | null |

```

**Query:**
```sql
select * from read_csv(url => 's3://bucket/data.csv',
    null_string => 'NONE');
```
**Returns**:
```
| f0 | f1 | f2 |
| :--- | :--- | :--- |
| name | rank | note |
| Dave | 95 | null |
| John | 60 | 'need coaching' |
| Gene | 70 | improved |
| Carl | 85 | null |
```

**Query:**
```sql
select * from read_csv(url => 's3://bucket/data.csv', header => true,
    quote => 'DOUBLE_QUOTE');
```
**Returns**:
```
| name | rank | note |
| :--- | :--- | :--- |
| Dave | 95 | NONE |
| John | 60 | 'need coaching' |
| Gene | 70 | improved |
| Carl | 85 | null |
```

**Query:**
```sql
select * from read_csv(url => 's3://bucket/data.csv', header => true,
    empty_field_as_null => false);
```
**Returns**:
```
| name | rank | note |
| :--- | :--- | :--- |
| Dave | 95 | NONE |
| John | 60 | 'need coaching' |
| Gene | 70 | improved |
| Carl | 85 |  |
```