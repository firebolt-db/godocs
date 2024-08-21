---
layout: default
title: LIST_OBJECTS
description: Reference material for LIST_OBJECTS function
parent: Conditional and miscellaneous functions
---

# LIST_OBJECTS

Table-valued function which takes an Amazon S3 URL and credentials as parameters.

The resulting table lists objects and prefixes from the URL up until the next slash.

Each row in the output contains four columns:  object_name (`TEXT`), object_type (`TEXT`), object_bytes (`BIGINT`), and file_timestamp (`TIMESTAMPTZ`).

## Syntax

{: .no_toc}

```sql
LIST_OBJECTS ( url => <url>[, aws_key_id => <aws_key_id>][, aws_secret_key => <aws_secret_key>])
```

## Parameters

{: .no_toc}

| Parameter                     | Description                                                                                      | Supported input types |
|:------------------------------|:-------------------------------------------------------------------------------------------------|:----------------------|
| `<url>`                       | The Amazon S3 location. The expected format is 's3://{bucket_name}/{optional_prefix}'.               | `TEXT`                |
|:------------------------------|:-------------------------------------------------------------------------------------------------|:----------------------|
| `<aws_key_id>`                | An AWS key ID.                                                                                      | `TEXT`                |
|:------------------------------|:-------------------------------------------------------------------------------------------------|:----------------------|
| `<aws_secret_key>`            | An AWS secret key.                                                                                  | `TEXT`                |


The AWS credential parameters, `aws_key_id`, `aws_secret_key` are optional, and are not required to access public buckets.

If you provide either `aws_key_id` or `aws_secret_key`, you must provide both.

## Return Type

The output is a table with four columns: object_name (`TEXT`), object_type (`TEXT`), object_bytes (`BIGINT`), and last_modified (`TIMESTAMPTZ`).

The object_name contains both the full path and the file extension.

The object_type can be either “file” or “folder”.

If object_type = "folder", then the object_bytes and last_modified columns will contain `NULL` values because folders do not have associated sizes or timestamps.

If object_type = “file”, the following apply:
1. The `last_modified` column is populated from the `LastModified` attribute in Amazon S3. AWS does not expose the creation timestamp, so the values in this column only differ from the creation time if an immutable object has been overwritten.

2. The `object_bytes` column contains values in bytes.

Note: Amazon S3 is not a traditional filesystem. AWS refers to what we commonly think of as "folders" as “common_prefixes”, and "files" as “objects”.

## Example

{: .no_toc}

The following code examples show how to list all objects (folders) that start with a specified prefix within an Amazon S3 bucket. You can specify either a part of the prefix or the full prefix. For example, the urls ending with the prefixes `fire` or `firebolt_sample_dataset` both return identical results because both are valid matches for the `firebolt_sample_dataset` folder.

```sql
SELECT * FROM list_objects(url => 's3://firebolt-publishing-public/help_center_assets/fire')
```

and

```sql
SELECT * FROM list_objects(url => 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset')
```


**Both return**:

| object_name (TEXT)                                          | object_type (TEXT) | object_bytes (BIGINT) |  last_modified (TIMESTAMPTZ) |
|:------------------------------------------------------------|:-------------------|:----------------------|:-----------------------------|
| help_center_assets/firebolt_sample_dataset/                 | folder             | NULL                  | NULL                         |

The following code example shows how to list all objects (files, folders, and associated metadata) that start with a specified prefix in an Amazon S3 bucket:

```sql
SELECT * FROM list_objects(url => 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/')
```

**Returns**:

| object_name (TEXT)                                          | object_type (TEXT) | object_bytes (BIGINT) |  last_modified (TIMESTAMPTZ) |
|:------------------------------------------------------------|:-------------------|:----------------------|:-----------------------------|
| help_center_assets/firebolt_sample_dataset/players.json     | file               | 1,421,277             | 2023-02-27 10:49:13+01       |
|:------------------------------------------------------------|:-------------------|:----------------------|:-----------------------------|
| help_center_assets/firebolt_sample_dataset/levels.csv       | file               | 83,596                | 2023-02-27 11:06:52+01       |
|:------------------------------------------------------------|:-------------------|:----------------------|:-----------------------------|
| help_center_assets/firebolt_sample_dataset/tournaments.csv  | file               | 83,351                | 2022-12-15 15:34:14+01       |
|:------------------------------------------------------------|:-------------------|:----------------------|:-----------------------------|
| help_center_assets/firebolt_sample_dataset/games.json       | file               | 872                   | 2023-02-27 13:18:54+01       |
|:------------------------------------------------------------|:-------------------|:----------------------|:-----------------------------|
| help_center_assets/firebolt_sample_dataset/rankings/        | folder             | NULL                  | NULL                         |
|:------------------------------------------------------------|:-------------------|:----------------------|:-----------------------------|
| help_center_assets/firebolt_sample_dataset/playstats/       | folder             | NULL                  | NULL                         |

The following code examples show how to list all objects (files and associated metadata) that start with a specified prefix in an Amazon S3 bucket. The urls ending with the prefixes `lev` or `levels.csv` return identical results because both are valid matches for the `levels.csv` file.

```sql
SELECT * FROM list_objects(url => 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/lev')
```

and

```sql
SELECT * FROM list_objects(url => 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv')
```

**Both Return**:

| object_name (TEXT)                                          | object_type (TEXT) | object_bytes (BIGINT) |  last_modified (TIMESTAMPTZ) |
|:------------------------------------------------------------|:-------------------|:----------------------|:-----------------------------|
| help_center_assets/firebolt_sample_dataset/levels.csv       | file               | 83,596                | 2023-02-27 11:06:52+01       |


The following code example shows how to use your Amazon credentials to list objects in an Amazon S3 bucket that is not publicly accessible:

```sql
SELECT * FROM list_objects(url => 's3://example_bucket/foo.csv', aws_key_id => 'my_key_id', aws_secret_key => 'my_secret_key')
```

**Returns**:

| object_name (TEXT)                                          | object_type (TEXT) | object_bytes (BIGINT) |  last_modified (TIMESTAMPTZ) |
|:------------------------------------------------------------|:-------------------|:----------------------|:-----------------------------|
| foo.csv                                                     | file               | 10                    | 2024-06-12 9:30:00 UTC       |
