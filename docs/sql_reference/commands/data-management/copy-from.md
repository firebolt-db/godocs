---
layout: default
title: COPY
description: Reference and syntax for the COPY command that copies data between a file and a table. 
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Data management
---

# COPY
{: .no_toc}

Copies data from S3 to firebolt table.

* Topic ToC
{:toc}

## Syntax

```sql
COPY [INTO] <table_name> [ ( <column_name> [default Default_value] [ { $source_column_number | source_column_name } ] [, ...] ) ] 
FROM <externalLocation>
[ WHERE <condition> ]
[ LIMIT <count> [ OFFSET <start> ] ]
[ WITH <options> ]

<options>:
    [ CREDENTIALS = ( <credentials> ) ] 
    [ PATTERN = <regex_pattern> ]
    [ TYPE = { **AUTO** | CSV | PARQUET } ]
    [ AUTO_CREATE = { **TRUE** | FALSE } ]
    [ ON_ERROR = { **CONTINUE** | ABORT } ]
    [ ERROR_FILE = <externalLocation> ]
    [ ERROR_FILE_CREDENTIALS = <credentials> ]
    [ MAX_ERRORS_PER_FILE = <max_errors_num> | <max_error_pct> ]
    [ <csv_options> ]

<credentials>:
    { AWS_KEY_ID = '<aws_key_id>' AWS_SECRET_KEY = '<aws_secret_key>' | AWS_ROLE_ARN = '<role_arn>' [AWS_ROLE_EXTERNAL_ID = '<external_id>'] }

<csv_options>:
    [ HEADER = { **FALSE** | TRUE  } ]
    [ DELIMITER = 'character' ]
    [ QUOTE = { **DOUBLE_QUOTE** | SINGLE_QUOTE | 'character' } ]
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
| `<column_name>`          | Optional. The name of the target column(s) in the table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `<externalLocation>`     | The path to an S3 location where the query result file or files are saved. If ends with `/` it interpreted as directory otherwise as single file. Folder example: `s3://my_bucket/my_folder/`. File example: `s3://my_bucket/my_folder/my_file`.                                                                                                                                                                                                                                                                                                                                                                                                             |
| `CREDENTIALS`            | The Amazon S3 credentials for accessing the specified `<externalLocation>`. See [CREDENTIALS](#credentials) below.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `PATTERN`                | A regular expression pattern string (glob). For additional explenation visit: https://en.wikipedia.org/wiki/Glob_(programming).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `TYPE`                   | Specifies the file type Firebolt expects to ingest given the `PATTERN`. If not specified it will be auto detected by the suffix of a file. If a file referenced using `PATTERN` does not conform to the specified `TYPE`, an error occurs. For more information, see [TYPE](#type).                                                                                                                                                                                                                                                                                                                                                                          |
| `AUTO_CREATE`            | Specifies if the table can be automatically created by working alongside with automatic schema discovery. By default, automatic table creation is enabled (value: TRUE). If value is TRUE and the target table already exists, `AUTO_CREATE` is ignored.                                                                                                                                                                                                                                                                                                                                                                                                     |
| `ON_ERROR`               | Specifies if encountered error                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `ERROR_FILE`             | Defines an optional file where rejected records will be stored. See `externalLocation` parameter definition above for format details. If the specified path doesn't exist, a folder will be created on the behalf of the user. A child directory is created with the name "rejectedrows", and within this directory, another folder is created based on the time of load submission in the format YearMonthDay -HourMinuteSecond + QueryID (Ex. 20220330-173205/<query_id>/). In this folder, two types of files are written: 1) the reason (error) file and the data (row) file. If `ERRORFILE` is omitted, error files are created in the source location. |
| `ERROR_FILE_CREDENTIALS` | The Amazon S3 credentials for accessing the specified `<externalLocation>` for error file creation. See [CREDENTIALS](#credentials) below.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `MAX_ERRORS_PER_FILE`    | Specifies the maximum number of rejected rows per file. Maximum number of errors per file can be expressed as either an absolute number of errors (max_errors_num) or a percentage (max_error_pct, representing the number of bad rows divided by the total number of rows). Once the threshold is reached, the `COPY` statement aborts processing that file but continues loading other files.                                                                                                                                                                                                                                                              |
| `HEADER`                 | Specifies that the file contains a header line with the names of each column in the file. If set to true the first line will be interpreted as file schema column names.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `DELIMITER`              | Specifies .... Accepted formats are: DD-MM-YYYY, MM-DD-YYYY, YYYY-MM-DD,  YYYY-DD-MM, YYYY/MM/DD, YYYY/DD/MM, DD/MM/YYYY, MM/DD/YYYY, YYYYMMDD, YYYYDDMM, DDMMYYYY, MMDDYYYY                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `QUOTE`                  | Specifies .... Accepted formats are: DD-MM-YYYY, MM-DD-YYYY, YYYY-MM-DD,  YYYY-DD-MM, YYYY/MM/DD, YYYY/DD/MM, DD/MM/YYYY, MM/DD/YYYY, YYYYMMDD, YYYYDDMM, DDMMYYYY, MMDDYYYY                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `ESCAPE`                 | Specifies .... Accepted formats are: DD-MM-YYYY, MM-DD-YYYY, YYYY-MM-DD,  YYYY-DD-MM, YYYY/MM/DD, YYYY/DD/MM, DD/MM/YYYY, MM/DD/YYYY, YYYYMMDD, YYYYDDMM, DDMMYYYY, MMDDYYYY                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `NULL_STRING`            | Specifies .... Accepted formats are: DD-MM-YYYY, MM-DD-YYYY, YYYY-MM-DD,  YYYY-DD-MM, YYYY/MM/DD, YYYY/DD/MM, DD/MM/YYYY, MM/DD/YYYY, YYYYMMDD, YYYYDDMM, DDMMYYYY, MMDDYYYY                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `EMPTY_FIELD_AS_NULL`    | Specifies .... Accepted formats are: DD-MM-YYYY, MM-DD-YYYY, YYYY-MM-DD,  YYYY-DD-MM, YYYY/MM/DD, YYYY/DD/MM, DD/MM/YYYY, MM/DD/YYYY, YYYYMMDD, YYYYDDMM, DDMMYYYY, MMDDYYYY                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `SKIP_BLANK_LINES`       | Specifies .... Accepted formats are: DD-MM-YYYY, MM-DD-YYYY, YYYY-MM-DD,  YYYY-DD-MM, YYYY/MM/DD, YYYY/DD/MM, DD/MM/YYYY, MM/DD/YYYY, YYYYMMDD, YYYYDDMM, DDMMYYYY, MMDDYYYY                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `DATE_FORMAT`            | Specifies .... Accepted formats are: DD-MM-YYYY, MM-DD-YYYY, YYYY-MM-DD,  YYYY-DD-MM, YYYY/MM/DD, YYYY/DD/MM, DD/MM/YYYY, MM/DD/YYYY, YYYYMMDD, YYYYDDMM, DDMMYYYY, MMDDYYYY                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `TIMESTAMP_FORMAT`       | Specifies... Accepted formats are: YYYY-MM-DD HH24, YYYY-MM-DD"T"HH24, YYYY-MM-DD HH24:MI, YYYY-MM-DD"T"HH24:MI, YYYY-MM-DD HH24:MI:SS, YYYY-MM-DD"T"HH24:MI:SS, YYYY-MM-DD HH24:MI:SS TZHTZM, YYYY-MM-DD HH24:MI:SS TZH:TZM, YYYY-MM-DD HH24:MITZH:TZM, YYYY-MM-DD"T"HH24:MITZH:TZM, YYYY-MM-DD HH24:MI:SSTZH, YYYY-MM-DD HH24:MI:SSTZH:TZM, YYYY-MM-DD"T"HH24:MI:SSTZH:TZM, YYYY-MM-DD HH24:MI:SS.FF, YYYY-MM-DD"T"HH24:MI:SS.FF, YYYY-MM-DD HH24:MI:SS.FF TZHTZM, YYYY-MM-DD HH24:MI:SS.FF TZH:TZM, YYYY-MM-DD HH24:MI:SS.FFTZH, YYYY-MM-DD HH24:MI:SS.FFTZH:TZM, YYYY-MM-DD"T"HH24:MI:SS.FFTZH:TZM                                                       |

## CREDENTIALS

Firebolt needs permissions to write query results to the specified S3 location. You can specify IAM credentials using either the Amazon Resource Name (ARN) of an IAM role or AWS access keys, and the specified credentials must be associated with a user or role with permissions to write objects to the bucket.

### Specifying an IAM Role

Specify an AWS IAM Role ARN using the syntax shown below.

```sql
CREDENTIALS = (AWS_ROLE_ARN=<role_arn>) [AWS_ROLE_EXTERNAL_ID='<external_id>']
```

* `<role_arn>` is the ARN of a role that you have configured for Firebolt access to the specified `<externalLocation>`, for example, `arn:aws:iam::123456789012:role/my-firebolt-access-role`.
* `<external_id>` is an optional arbitrary string that you assign to an IAM role when you create it, for example, `99291`.

For more information about creating roles for Firebolt, see [Using AWS roles to access Amazon S3](../../../Guides/loading-data/configuring-aws-role-to-access-amazon-s3.md).

### Specifying AWS access keys

Specify access key credentials using the syntax shown below.

```sql
CREDENTIALS = (AWS_KEY_ID = '<aws_key_id>' AWS_SECRET_KEY = '<aws_secret_key>')
```

* `<aws_key_id>` is the AWS access key id associated with a user or role, for example, `AKIAIOSFODNN7EXAMPLE`.
* `<aws_secret_key>` is the AWS secret key, for example, `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`.

For more information about access keys, see [Programmatic access](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys) in the *AWS General Reference*.

### Least privileged permissions

The example AWS IAM policy statement below demonstrates the minimum actions that must be allowed for Firebolt to write query files to an example S3 location. A permissions policy that allows at least these actions for the `<s3_location>` that you specify in the `COPY TO` statement must be attached to the user or role specified in the `CREDENTIALS` clause.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:Get*",
                "s3:List*",
                "s3:PutObject",
                "s3:DeleteObject"
            ],
            "Resource": [
                "arn:aws:s3:::my_s3_bucket",
                "arn:aws:s3:::my_s3_bucket/*"
            ]
        }
    ]
}
```

## TYPE

Specifies the type of the files in S3. The following types and type options are supported.

### CSV Types

```sql
TYPE = (CSV [ <type option> ])
```
or 
```sql
TYPE = (CSV)
[ <type option> ]
```

notes on csv format:
new line sequence will be \n or \n\r or \r.

The following type options allow configuration for ingesting different CSV file formats.

* `[ALLOW_DOUBLE_QUOTES = {TRUE|FALSE}]`  
  `[ALLOW_SINGLE_QUOTES = {TRUE|FALSE}]`  
With `ALLOW_DOUBLE_QUOTES = TRUE` or `ALLOW_SINGLE_QUOTES = TRUE` you define that unescaped double or single quotes in CSV input file will not cause an error to be generated on ingest. By default `ALLOW_DOUBLE_QUOTES` and `ALLOW_SINGLE_QUOTES` are set to `TRUE`.

* `[ALLOW_COLUMN_MISMATCH = {TRUE|FALSE}]`  
With `ALLOW_COLUMN_MISMATCH = TRUE` the number of delimited columns in a CSV input file can be fewer than the number of columns in the corresponding table. By default, `ALLOW_COLUMN_MISMATCH` is set to `FALSE`, and an error is generated if the number of columns is fewer than the number of columns defined in the external table. If set to `TRUE`, and an input file record contains fewer columns than defined in the external table, the non-matching columns in the table are loaded with `NULL` values.

* `[ALLOW_UNKNOWN_FIELDS = {TRUE|FALSE}]`  
With `ALLOW_UNKNOWN_FIELDS = TRUE` the number of delimited columns in a CSV input file can be more than the number of columns in the corresponding table. By default, `ALLOW_UNKNOWN_FIELDS` is set to `FALSE`, and an error is generated if the number of columns is more than the number of columns defined in the external table. If set to `TRUE`, and an input file record contains more columns than defined in the external table, the non-matching columns in the table are loaded with `NULL` values.

* `[ESCAPE_CHARACTER = {‘<character>’|NONE}`  
With `ESCAPE_CHARACTER = '<character>'` you can define which character is used to escape, to change interpretations from the original. By default, the `ESCAPE_CHARACTER` value is set to `\`. If, for example, you want to use `"` as a value and not as delimiter for string, you can escape like `\"`, with the default escape character.

* `[FIELD_DELIMITER = '<field_delimeter>']`  
With `FIELD_DELIMITER = '<field_delimeter>'`, you can define a custom field delimiter to separate fields for ingest. By default, the `FIELD_DELIMITER` is set as `,`.

* `[NEW_LINE_CHARACTER = '<new_line_character>']`  
With `NEW_LINE_CHARACTER = '<new_line_character>'`, you can define a custom new line delimiter to separate entries for ingest. By default, the `NEW_LINE_CHARACTER` is set as the end of line character `\n`, but also supports other end of line conventions, such as `\r\n`, `\n\r`, and `\r`, as well as multi-character delimiters, such as `#*~`.

* `[NULL_CHARACTER = '<null_character>']`  
With `NULL_CHARACTER = '<null_character>'` you can define which character is interpreted as `NULL`. By default, the `NULL_CHARACTER` value is set to `\\N`. 

* `[SKIP_BLANK_LINES {TRUE|FALSE}]`  
With `SKIP_BLANK_LINES = TRUE` any blank lines encountered in the CSV input file will be skipped. By default, `SKIP_BLANK_LINES` is set to `FALSE`, and an error is generated if blank lines are enountered on ingest.

* `[SKIP_HEADER_ROWS = {1|0}]`  
With `SKIP_HEADER_ROWS = 1`, Firebolt assumes that the first row in each file read from S3 is a header row and skips it when ingesting data. When set to `0`, which is the default if not specified, Firebolt ingests the first row as data.  

### JSON Types
* `TYPE = (JSON [PARSE_AS_TEXT = {'TRUE'|'FALSE'}])`  
With `TYPE = (JSON PARSE_AS_TEXT = 'TRUE')`, Firebolt ingests each JSON object literal in its entirety into a single column of type `TEXT`. With `TYPE = (JSON PARSE_AS_TEXT = 'FALSE')`, Firebolt expects each key in a JSON object literal to map to a column in the table definition. During ingestion, Firebolt inserts the key's value into the corresponding column.  

### Other Types
* `TYPE = (ORC)`
* `TYPE = (PARQUET)`
* `TYPE = (AVRO)`
* `TYPE = (TSV)`

All type options for CSV above, except for `FIELD_DELIMITER`, are also supported for the TSV file type.

## Examples

* [COPY all source columns into target table](#copy-all-source-columns-into-target-table)
* [COPY with explicit list of columns](#copy-with-explicit-list-of-columns)
* [COPY with auto-schema discovery](#copy-with-auto-schema-discovery)

### COPY all source columns into target table

```sql
COPY INTO public.games FROM <S3 bucket>;
```

### COPY with explicit list of columns

```sql
COPY INTO test_table (c1 1, c2 3) FROM <S3_bucket> WITH
TYPE = CSV CREDENTIALS = '...' ENCODING = UTF8  QUOTE_CHARACTER = DOUBLE_QUOTE  TRUNCATE = ON;
```

### COPY with auto-schema discovery

```sql
COPY INTO test_table FROM <S3_bucket> WITH
TYPE = PARQUET CREDENTIALS = '...' ENCODING = UTF8 QUOTE_CHARACTER = DOUBLE_QUOTE AUTO_CREATE = ON TRUNCATE = ON;
```