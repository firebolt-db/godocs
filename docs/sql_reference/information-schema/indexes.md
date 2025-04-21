---
redirect_from:
  - /general-reference/information-schema/indexes.html
layout: default
title: Indexes
description: Use this reference to learn about the metadata available for Firebolt indexes using the information schema.
parent: Information schema
grand_parent: SQL reference
---

# Information schema for indexes
You can use the `information_schema.indexes` view to return information about each index in a database. The view is available for each database and contains one row for each index in the database. You can use a `SELECT` query to return information about each index.

In order to view index information, you need the USAGE privilege on both the [schema]({% link Overview/Security/Role-Based Access Control/database-permissions/schema-permissions.md %}#schema-level-privileges) and the [database]({% link Overview/Security/Role-Based Access Control/database-permissions/index.md %}#database-level-privileges). You also need ownership of the table or the necessary [table-level privileges]({% link Overview/Security/Role-Based Access Control/database-permissions/table-permissions.md %}#table-level-privileges) required for the intended action. 

The following query returns all aggregating indexes defined within the current database.

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
| index_owner                   | TEXT    | The owner of the table, which is the owner of the index. |
| index_definition              | TEXT    | The part of the index statement that specifies the columns and any aggregations included in the index. |
| compressed_bytes              | BIGINT    | The compressed size of the index, in bytes. |
| uncompressed_bytes            | BIGINT    | The uncompressed size of the index, in bytes. |
| number_of_tablets             | BIGINT    | The number of tablets in the index. |
| created                       | TIMESTAMPTZ | Time that the index was created. |
