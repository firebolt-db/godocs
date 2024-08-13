---
layout: default
title: READ_PARQUET
description: Reference material for READ_PARQUET function
grand_parent: SQL functions
parent: Conditional and miscellaneous functions
great_grand_parent: SQL reference
---

# READ_PARQUET

A Table-Valued function which takes a Parquet's S3 url and credentials.

The resulting table is the data from the Parquet file with the inferred datatype.

## Syntax

```sql
READ_PARQUET ( 
    url => <file_url>
    [, aws_key_id => <aws_key_id>]
    [, aws_secret_key => <aws_secret_key>]
    [, aws_arn => <aws_arn>]
    [, aws_arn_role_external_id => <aws_arn_role_external_id>]
    [, are_credentials_encrypted => <are_credentials_encrypted>]
    )
```

## Parameters

| Parameter                     | Description                                                                                      | Supported input types |
|:------------------------------|:-------------------------------------------------------------------------------------------------|:----------------------|
| `<url>`                       | Amazon S3 files location. The expected format is 's3://{bucket_name}/{full_file_path}'.          | `TEXT`                |
| `<aws_key_id>`                | AWS key ID.                                                                                      | `TEXT`                |
| `<aws_secret_key>`            | AWS secret key.                                                                                  | `TEXT`                |
| `<aws_arn>`                   | AWS Role ARN.                                                                                    | `TEXT`                |
| `<aws_arn_role_external_id>>` | External ID for AWS Role.                                                                        | `TEXT`                |
| `<are_credentials_encrypted>>`| Are credentials encrypted                                                                        | `BOOL`                |

Credentials are optional. 

If you provide either `aws_key_id` or `aws_secret_key`, you must provide both.

If `aws_arn_role_external_id` is provided, then `aws_arn` must also be provided.

If `aws_key_id` and `aws_secret_key` are provided, then `aws_arn` and `aws_arn_role_external_id` must both be set to `NULL`. Similarly, if `aws_arn` and `aws_arn_role_external_id` are provided, then `aws_key_id` and `aws_secret_key` must both be set to `NULL`.

## Return Type

The result is a table with the data from the Parquet file. Columns are read and parsed using their inferred datatypes.

## Example

In the next code example, we read a parquet file from the bucket 's3://bucket/data.parquet' with the following data:

```
name, rank, note
Dave, 95, NONE
John, 60, 'need coaching'
Gene, 70, "improved"
```


**Query:**
```sql
select * from read_parquet(url => 's3://bucket/data.parquet');
```
**Returns**:
```
| f0 | f1 | f2 |
| :--- | :--- | :--- |
| name | rank | note |
| Dave | 95 | NONE |
| John | 60 | 'need coaching' |
| Gene | 70 | "improved" |
```