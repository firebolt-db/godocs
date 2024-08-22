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

`url` can be passed as either the first positional parameter or a named parameter.

```sql
-- Both queries are equivalent
select * from read_parquet(url => 's3://bucket/data.parquet');
select * from read_parquet('s3://bucket/data.parquet');
```

Credentials are optional. 

If you provide either `aws_key_id` or `aws_secret_key`, you must provide both.

If `aws_arn_role_external_id` is provided, then `aws_arn` must also be provided.

If `aws_key_id` and `aws_secret_key` are provided, then `aws_arn` and `aws_arn_role_external_id` must both be set to `NULL`. Similarly, if `aws_arn` and `aws_arn_role_external_id` are provided, then `aws_key_id` and `aws_secret_key` must both be set to `NULL`.

## Return Type

The result is a table with the data from the Parquet file. Columns are read and parsed using their inferred datatypes.

## Example

In the following example `url` is set as the first positional parameter but it can be passed as a named parameter as well (e.g `url => 's3://bucket/data.parquet'`).

**Query:**
```sql
select * from read_parquet('s3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/playstats/TournamentID=92/cc2a2a0b4e8b4fb39abf20a956e7cc3e-0.parquet') limit 5;
```
**Returns**:
| Column1 | Column2 | Column3            | Column4 | Column5 | Column6 | Column7 | Column8 | Column9 | Column10 |
|---------|---------|--------------------|---------|---------|---------|---------|---------|---------|----------|
| 1       | 845     | 2022-10-27 13:36:33| Solara  | 1       | 0       | 0       | 0       | Brake   | NoError  |
| 1       | 845     | 2022-10-27 13:36:33| Solara  | 1       | 339     | 0.9872  | 2       | RightTurn| GraphicsFreeze |
| 1       | 845     | 2022-10-27 13:36:34| Solara  | 1       | 288     | 1.9744  | 20      | Tilt     | NoError  |
| 1       | 845     | 2022-10-27 13:36:35| Solara  | 1       | 260     | 2.9616  | 53      | Block    | TextNotFound |
| 1       | 845     | 2022-10-27 13:36:36| Solara  | 1       | 196     | 3.9488  | 81      | FullSpeed| NoError  |

