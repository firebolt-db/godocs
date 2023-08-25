---
layout: default
title: SHOW TABLES
description: Reference and syntax for the SHOW TABLES command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Metadata commands
---

# SHOW TABLES

Returns a table with a row for each table in the current database, with columns containing information for each table as listed below.

## Syntax

```sql
SHOW TABLES;
```

## Returns

The returned table has the following columns.


| Column name                 | Data Type   | Description |
| :---------------------------| :-----------| :-----------|
| table_name                  | TEXT      | The name of the table. |
| state                       | TEXT      | The current table state. |
| table_type                  | TEXT      | One of `FACT`, `DIMENSION`, or `EXTERNAL`. |
| column_count                | INTEGER         | The number of columns in the table. |
| primary_index               | TEXT      | An ordered array of the column names comprising the primary index definition, if applicable. |
| schema                      | TEXT      | The text of the SQL statement that created the table. |
| number_of_rows              | INTEGER         | The number of rows in the table. |
| size                        | DOUBLE PRECISION | The compressed size of the table. |
| size_uncompressed           | DOUBLE PRECISION | The uncompressed size of the table. |
| compression_ratio           | DOUBLE PRECISION | The compression ratio (`<size_uncompressed>`/`<size>`). |
| number_of_tablets           | INTEGER         | The number of tablets comprising the table. |

## Example

The following example returns information about tables in the database queried:

```sql
SHOW TABLES;
```

| table_name |	state |	table_type |	column_count |	primary_index |	schema |	number_of_rows |	size	| size_uncompressed	| compression_ratio	| number_of_tablets|
|:---|:-----|:----|:-----|:-----|:-----|:-----|:------|:------|:-----|:-----|
| ex_games |	Valid |	EXTERNAL |	1 |		"CREATE EXTERNAL TABLE IF NOT EXISTS ""ex_games"" (""src"" text NOT NULL) | ""OBJECT_PATTERN"" = 'help_center_assets/firebolt_sample_dataset/games.json' ""TYPE"" = (""JSON"" ""PARSE_AS_TEXT"" = 'TRUE') ""URL"" = 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/'" |	0 |	0.00 B |	0.00 B |	0	|0|
