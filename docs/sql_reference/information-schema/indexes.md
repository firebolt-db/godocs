---
layout: default
title: Indexes
description: Use this reference to learn about the metadata available for Firebolt indexes using the information schema.
parent: Information schema
grand_parent: SQL reference
---

# Information schema for indexes
You can use the `information_schema.indexes` view to return information about each index in a database. The view is available for each database and contains one row for each index in the database. You can use a `SELECT` query to return information about each index.

The following query returns all aggregating indexes defined within the current database

```sql
SELECT
  *
FROM
  information_schema.indexes
WHERE
  index_type='aggregating`;
```

## Columns in information_schema.indexes

Each row has the following columns with information about the database.

| Column Name                   | Data Type | Description |
| :-----------------------------| :-------- | :---------- |
| table_catalog                 | TEXT    | Name of the catalog. Firebolt provides a single ‘default’ catalog. |
| table_schema                  | TEXT    | Name of the database. |
| table_name                    | TEXT    | The name of the table for which the index is defined. |
| index_name                    | TEXT    | The name defined for the index. |
| index_type                    | TEXT    | One of either `primary` or `aggregating`. |
| index_definition              | TEXT    | The part of the index statement that specifies the columns and any aggregations included in the index. |
| index_compressed_size         | BIGINT    | The compressed size of the index, in bytes. |
| index_uncompressed_size       | BIGINT    | The uncompressed size of the index, in bytes. |
| number_of_tablets             | BIGINT    | The number of tablets in the index. |
