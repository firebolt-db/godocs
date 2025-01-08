---
layout: default
title: Tables
description: Use this reference to learn about the metadata available for Firebolt tables using the information schema.
parent: Information schema
grand_parent: SQL reference
---

# Information schema for tables

You can use the `information_schema.tables` view to return information about each table in a database. The view is available for each database and contains one row for each table in the database. You can use a `SELECT` query to return information about each table as shown in the example below.

```sql
SELECT
  *
FROM
  information_schema.tables;
```

## Columns in information_schema.tables

Each row has the following columns with information about each table.

| Column Name                 | Data Type   | Description |
| :---------------------------| :-----------| :-----------|
| table_catalog               | TEXT        | The name of the database. |
| table_schema                | TEXT        | The name of the schema. |
| table_name                  | TEXT        | The name of the table. |
| table_type                  | TEXT        | The table's type, e.g. `BASE TABLE`, `EXTERNAL` `VIEW`. |
| table_owner                 | TEXT        | The owner of the table, `NULL` if there is none. |
| created                     | TIMESTAMPTZ | Not applicable for Firebolt. |
| last_altered                | TIMESTAMPTZ | Not applicable for Firebolt. |
| last_altered_by             | TEXT        | Not applicable for Firebolt. |
| primary_index               | TEXT        | An ordered array of the column names comprising the primary index definition, if applicable. |
| number_of_rows              | BIGINT      | The number of rows in the table. |
| compressed_bytes            | BIGINT      | The compressed size of the table in bytes. |
| uncompressed_bytes          | BIGINT      | The uncompressed size of the table in bytes. |
| compression_ratio           | NUMERIC     | The compression ratio (`<uncompressed_bytes>`/`<compressed_bytes>`). |
| number_of_tablets           | INTEGER     | The number of tablets comprising the table. |
| fragmentation               | DECIMAL     | Table fragmentation percentage (between 0-100). |
| type                        | TEXT        | The table's type. |
| location_name               | TEXT        | Not applicable for Firebolt. |
| ddl                         | TEXT        | The text of the SQL statement that created the table. |
| self_referencing_column_name| NULL        | Not applicable for Firebolt. |
| reference_generation        | NULL        | Not applicable for Firebolt. |
| user_defined_type_catalog   | NULL        | Not applicable for Firebolt. |
| user_defined_type_schema    | NULL        | Not applicable for Firebolt. |
| user_defined_type_name      | NULL        | Not applicable for Firebolt. |
| is_insertable_into          | TEXT        | `YES` if the table is insertable, `NO` otherwise. |
| is_typed                    | TEXT        | Always `NO`. |
| commit_action               | NULL        | Not applicable for Firebolt. |
