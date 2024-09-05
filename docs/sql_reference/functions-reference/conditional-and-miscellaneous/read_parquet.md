---
layout: default
title: READ_PARQUET
description: Reference material for READ_PARQUET function
grand_parent: SQL functions
parent: Conditional and miscellaneous functions
great_grand_parent: SQL reference
---

# READ_PARQUET

A table-valued function (TVF) that accepts a URL to an Amazon bucket containing a Parquet file and credentials. `READ_PARQUET` returns a table with data from the specified Parquet file.

## Syntax

```sql
READ_PARQUET ( 
    url => <file_url>
    [, aws_key_id => <aws_key_id>]
    [, aws_secret_key => <aws_secret_key>]
    [, are_credentials_encrypted => <are_credentials_encrypted>]
    )
```

## Parameters

| Parameter                     | Description                                                                                      | Supported input types |
|:------------------------------|:-------------------------------------------------------------------------------------------------|:----------------------|
| `<url>`                       | The location of the Amazon S3 bucket containing your files. The expected format is `s3://{bucket_name}/{full_file_path}`.          | `TEXT`                |
| `<aws_key_id>`                | The AWS key ID.                                                                                      | `TEXT`                |
| `<aws_secret_key>`            | The AWS secret key.                                                                                  | `TEXT`                |
| `<are_credentials_encrypted>>`| Set to `TRUE` if the `aws_key_id` and `aws_secret_key` are provided in encrypted form.                                                                        | `BOOL`                |

The following apply:

* The `url` can be passed as either the first positional parameter or a named parameter. For example, the following two queries will both read the same file:

    ```sql
    SELECT * FROM READ_PARQUET('s3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/playstats/TournamentID=92/cc2a2a0b4e8b4fb39abf20a956e7cc3e-0.parquet');
    SELECT * FROM READ_PARQUET(url => 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/playstats/TournamentID=92/cc2a2a0b4e8b4fb39abf20a956e7cc3e-0.parquet');
    ```

* Credentials are optional. 

* If you provide either `aws_key_id` or `aws_secret_key`, you must provide both.

## Return Type

The result is a table with data from the Parquet files. Columns are read and parsed using their inferred data types.

## Example

**Query:**
In the following example, the `url` is set as the first positional parameter and reads a Parquet file.

   ```sql
   SELECT * FROM READ_PARQUET('s3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/playstats/TournamentID=92/cc2a2a0b4e8b4fb39abf20a956e7cc3e-0.parquet') LIMIT 5;
```

**Returns**:

| GameID | PlayerID | Timestamp | SelectedCar | CurrentLevel | CurrentSpeed | CurrentPlayTime | CurrentScore | Event | ErrorCode |
|:---------|:---------|:--------------------|:---------|:---------|:---------|:---------|:---------|:---------|:----------|
| 1       | 845     | 2022-10-27 13:36:33| Solara  | 1       | 0       | 0       | 0       | Brake   | NoError  |
| 1       | 845     | 2022-10-27 13:36:33| Solara  | 1       | 339     | 0.9872  | 2       | RightTurn| GraphicsFreeze |
| 1       | 845     | 2022-10-27 13:36:34| Solara  | 1       | 288     | 1.9744  | 20      | Tilt     | NoError  |
| 1       | 845     | 2022-10-27 13:36:35| Solara  | 1       | 260     | 2.9616  | 53      | Block    | TextNotFound |
| 1       | 845     | 2022-10-27 13:36:36| Solara  | 1       | 196     | 3.9488  | 81      | FullSpeed| NoError  |

