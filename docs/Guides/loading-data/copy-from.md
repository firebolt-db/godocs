---
layout: default
title: COPY FROM
description: Provide examples on using the COPY FROM command to load data into Firebolt
parent: Load data
nav_order: 1
---
# COPY FROM
{: .no_toc}

## Data Loading
### Bulk Insert for New Tables
The `COPY FROM` command facilitates efficient bulk data ingestion: 

```sql
COPY sales
FROM 's3://data-bucket/initial_sales_data.csv'
WITH TYPE = 'CSV', HEADER= TRUE, DELIMITER= ',', 
```
### Appending New Data
For ongoing operations, COPY FROM supports appending new data without disrupting current analytics:

```sql
COPY sales
FROM 's3://data-bucket/daily_sales.csv'
WITH (TYPE  = 'CSV', HEADER = TRUE)
```

## Schema
### Automatic Schema Discovery
Automatic schema discovery can simplify data ingestion, especially from formats that include metadata, such as Parquet For formats that do not include metadata, such as `CSV`, automatic schema discovery infers column types based on the data content itself. While this process aims to accurately identify data types, it operates on a "best effort" basis.

```sql
COPY product_catalog
FROM 's3://data-bucket/products.parquet'
WITH (TYPE = 'PARQUET', AUTO_CREATE = TRUE)
```

### Manual Schema Definition
You can also manually map data between your src schema and target schema within the COPY FROM statement. With this feature you can map each column by name or by index.

```sql
COPY target_table (target_col1, target_col2, target_col3)
FROM 's3://data-bucket/example.csv
WITH (TYPE = 'CSV', HEADER = true, FIELD_DELIMITER = ',', NULL_AS = 'NULL');
```
## Managing Data
### Handling Bad Data
Firebolt provides several options for error handling, such as setting parameters for the maximum number of errors to tolerate before aborting the operation.

```sql
COPY sales
FROM 's3://data-bucket/sales_data.csv'
WITH (TYPE  = 'CSV', HEADER = TRUE, ERROR_FILE = <externalLocation>, ERROR_FILE_CREDENTIALS = <credentials>, MAX_ERRORS_PER_FILE = 5
)
```

### Partitioning Data
Firebolt's 'COPY FROM' command supports  handling partitioned data, which is common when working with structured formats like Parquet and ORC. Firebolt supports the 'PATTERN' clause, which allows users to define regular expressions that specify file names and paths to match, optimizing the data scanning and enumeration process by pushing predicates down to the storage layer whenever possible:

```sql
COPY logs
FROM 's3://data-bucket/logs/'
WITH (TYPE  = 'CSV', PATTERN = 'year=2022/month=4/*.csv.gz')
```
This command specifies that only CSV files in the /year=2022/month=4/ directory should be loaded, which filters out data at the storage level.

### Pattern Options and Examples:
{: .no_toc} 

| `PATTERN = '*/*/*.csv.gz`                              | This pattern loads all CSV.GZ files from all folders three levels deep. This is typically used for comprehensive initial loads but can be time-consuming due to the extensive file enumeration required.                                                                                                                
| `PATTERN = 'year*/*/*.csv.gz`                      | This loads all CSV.GZ files from folders starting with 'year', across three directory levels. It offers a faster enumeration than the broader pattern by focusing on directories that match the specific starting string. | 

| `PATTERN = 'year*/*/*.csv.gz`                      | This loads all CSV.GZ files from folders starting with 'year', across three directory levels. It offers a faster enumeration than the broader pattern by focusing on directories that match the specific starting string. | 

| `PATTERN = 'year=2024/month=4/*.csv.gz`                      | Targets CSV files specifically from April 2024, significantly speeding up data enumeration by narrowing down to a specific month.

| `PATTERN = 'country=Canada/*.csv.gz`                      | Loads CSV files stored under directories marked for 'Canada', which is ideal for country-specific data operations.

| `PATTERN = 'country=[A-z]+/*.csv.gz`                      | Matches any country name consisting of one or more letters, allowing for dynamic data loading based on country names.

| `PATTERN = 'year=[0-9][0-9][0-9][0-9]/month=[0-9]/*.csv.gz`                      | Specifically loads CSV files based on a fully numeric year and single-digit month, providing precise control over the data load timeframe.

### Filtering Data to Be Loaded
Firebolt allows for data filtering using LIMIT and OFFSET clauses, useful for managing data volumes during initial tests or previews:

```sql
COPY sample_data
FROM 's3://data-bucket/large_dataset.csv'
WITH (TYPE  = 'CSV', HEADER = TRUE, LIMIT = 100)
```

This loads 100 rows and is useful for sampling or testing data loads.

### Loading Compressed Data
Firebolt supports loading data from compressed files, enhancing speed and efficiency:

```sql
COPY logs
FROM 's3://data-bucket/logs.gz'
WITH (TYPE = 'CSV', COMPRESSION = 'GZIP')
```

### Column Mismatch
Firebolt's `COPY FROM` command supports the `ALLOW_COLUMN_MISMATCH` option, which determines how Firebolt responds to discrepancies between the source data and the target table.

`COLUMN MATCH` is defined as the condition where all required columns from the source data exist in the target table. This involves a few considerations:
1. With Column Mapping: If column mapping is used, the required columns include all source columns explicitly mentioned by the user plus any columns that are automatically selected by Firebolt.
2. Without Column Mapping: If no column mapping is specified, all columns in the target table are considered required.

ALLOW COLUMN MISMATCH Option Settings:
* `ALLOW_COLUMN_MISMATCH` = TRUE: This setting allows for a mismatch between the source and target, such that if certain columns are missing in the source data, the data load will still proceed. Missing columns will not be populated in the target table, and only the matching columns will be updated.
* `ALLOW_COLUMN_MISMATCH` = FALSE: This is the default setting. If there is any discrepancy in either the presence or order of columns (by index or name), Firebolt will halt the data load and throw an error, indicating that there is a missing column.

```sql
COPY target_table
FROM 's3://data-bucket/data.csv'
WITH (format = 'CSV', header = true, COLUMN MATCH = TRUE)
```
This command attempts to load data from a `CSV` file into target_table, allowing for some columns in the source data to be missing. Firebolt will ignore these discrepancies and load only the data that matches the existing columns of the target table.

To handle column mismatches effectively:
1. Understand Your Data: Familiarize yourself with both the source data structure and the target table schema to anticipate potential mismatches.
2. Use Column Mapping: When possible, explicitly map source columns to target table columns to clarify how data should be loaded and to prevent errors.
3. Monitor Errors: Pay close attention to error logs when `COLUMN MATCH` = FALSE. These logs can provide insights into which columns are causing issues and need attention.
4. Adjust Your Schema: If frequent mismatches occur, consider adjusting your target table schema to better align with your typical data sources, or preprocess your data to ensure compatibility.

## Supported File Formats
Firebolt's `COPY FROM` supports the following file formats:
* `Parquet`
* `CSV/TSV`
