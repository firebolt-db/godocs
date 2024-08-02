---
layout: default
title: LIST_OBJECTS
description: Reference material for LIST_OBJECTS function
grand_parent: SQL functions
parent: Conditional and miscellaneous functions
great_grand_parent: SQL reference
---

# LIST_OBJECTS

Table-valued function which takes an Amazon S3 URL and credentials as parameters.

The resulting table lists objects and prefixes from the URL up until the next slash.

Each row in the output contains four columns:  object_name (`TEXT`), object_type (`TEXT`), object_bytes (`BIGINT`), and file_timestamp (`TIMESTAMPTZ`).

## Syntax

{: .no_toc}

```sql
LIST_OBJECTS ( url => <url>[, aws_key_id => <aws_key_id>][, aws_secret_key => <aws_secret_key>][, aws_arn => <aws_arn>][, aws_arn_role_external_id => <aws_arn_role_external_id>])
```

Positional parameters are supported in addition to named parameters. Positional parameters must be provided in the following order: `url`, `aws_key_id`, `aws_secret_key`, `aws_arn`, and `aws_arn_role_external_id`. If they are not specified, the last four parameters default to `NULL`.

## Parameters

{: .no_toc}

| Parameter                     | Description                                                                                      | Supported input types |
|:------------------------------|:-------------------------------------------------------------------------------------------------|:----------------------|
| `<url>`                       | Amazon S3 location. The expected format is 's3://{bucket_name}/{optional_prefix}'.               | `TEXT`                |
|:------------------------------|:-------------------------------------------------------------------------------------------------|:----------------------|
| `<aws_key_id>`                | AWS key ID.                                                                                      | `TEXT`                |
|:------------------------------|:-------------------------------------------------------------------------------------------------|:----------------------|
| `<aws_secret_key>`            | AWS secret key.                                                                                  | `TEXT`                |
|:------------------------------|:-------------------------------------------------------------------------------------------------|:----------------------|
| `<aws_arn>`                   | AWS Role ARN.                                                                                    | `TEXT`                |
|:------------------------------|:-------------------------------------------------------------------------------------------------|:----------------------|
| `<aws_arn_role_external_id>>` | External ID for AWS Role.                                                                        | `TEXT`                |

The credential parameters, `aws_key_id`, `aws_secret_key`, `aws_arn`, and `aws_arn_role_external_id`, are optional.

If you provide either `aws_key_id` or `aws_secret_key`, you must provide both.

If `aws_arn_role_external_id` is provided, then `aws_arn` must also be provided.

If `aws_key_id` and `aws_secret_key` are provided, then `aws_arn` and `aws_arn_role_external_id` must both be set to `NULL`. Similarly, if `aws_arn` and `aws_arn_role_external_id` are provided, then `aws_key_id` and `aws_secret_key` must both be set to `NULL`.

## Return Type

The output is a table with four columns: object_name (`TEXT`), object_type (`TEXT`), object_bytes (`BIGINT`), and last_modified (`TIMESTAMPTZ`).

The object_name contains both the full path and the file extension.

The object_type can be either “file” or “folder”.

If object_type = "folder", the object_bytes and last_modified columns will contain `NULL` values because folders do not have associated sizes or timestamps.

If object_type = “file”, the following apply:
1. The `last_modified` column is populated from the `LastModified` attribute in Amazon S3. AWS does not expose the creation timestamp, so the values in this column only differ from the creation time if an immutable object has been overwritten.

2. The `object_bytes` column contains values in bytes.

Note: Amazon S3 is not a traditional filesystem. AWS refers to what we commonly think of as "folders" as “common_prefixes”, and "files" as “objects”.

## Example

{: .no_toc}

In the following code examples, the Amazon S3 bucket contains the following files: USA/Washington/Kirkland.csv, USA/Washington/Seattle.csv, USA/California/LosAngeles.csv, and USA/DC.csv.

```sql
SELECT * FROM list_objects(url => 's3://my_bucket/', aws_key_id => 'my_key_id', aws_secret_key => 'my_secret_key')
```

**Returns**:

| object_name (TEXT) | object_type (TEXT) | object_bytes (BIGINT) |  last_modified (TIMESTAMPTZ) |
|:----------------------------------------|:-----------------------------------------------------|
| USA/               | folder             | NULL                  | NULL                         |

```sql
SELECT * FROM list_objects(url => 's3://my_bucket/USA/Washington/', aws_role_arn => 'my_aws_role_arn', aws_role_external_id => 'my_aws_role_external_id')
```

**Returns**:

| object_name (TEXT) | object_type (TEXT) | object_bytes (BIGINT) |  last_modified (TIMESTAMPTZ) |
|:----------------------------------------|:-----------------------------------------------------|
| USA/Washington/    | folder             | NULL                  | NULL                         |
|:----------------------------------------|:-----------------------------------------------------|
| USA/California/    | folder             | NULL                  | NULL                         |
|:----------------------------------------|:-----------------------------------------------------|
| USA/DC.csv         | file               | 10                    | 2024-06-12 9:30:00 UTC       |

```sql
SELECT * FROM list_objects('s3://my_bucket/USA/Washington', 'my_key_id', 'my_secret_key)
```

and

```sql
SELECT * FROM list_objects('s3://my_bucket/USA/Wa', NULL, NULL, 'my_aws_role_arn', 'my_aws_role_external_id')
```

**Both Return**:

| object_name (TEXT) | object_type (TEXT) | object_bytes (BIGINT) |  last_modified (TIMESTAMPTZ) | 
|:----------------------------------------|:-----------------------------------------------------|
| USA/Washington/    | folder             | NULL                  | NULL                         |

