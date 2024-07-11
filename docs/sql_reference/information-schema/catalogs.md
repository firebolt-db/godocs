---
layout: default
title: Catalogs
description: Use this reference to learn about the metadata available for Firebolt databases using the information schema.
parent: Information schema
grand_parent: SQL reference
---

# Information schema for catalogs

You can use the `information_schema.catalogs` view to return information about catalogs (databases in SQL terminology). You can use a `SELECT` query to return information about each database as shown in the example below.

```sql
SELECT
  *
FROM
  information_schema.catalogs;
```

## Columns in information_schema.catalogs

Each row has the following columns with information about the database.

| Column Name                   | Data Type  | Description |
| :-----------------------------| :--------- | :---------- |
| catalog_name                  | TEXT        | Name of the database. |
| default_collation             | TEXT        | Always 'POSIX'. |
| default_character_set         | TEXT        | Always 'UTF-8'. |
| description                   | TEXT        | The description of the database. |
| created                       | TIMESTAMPTZ | The time the database was created. |
| ddl                           | TEXT        | The text of the SQL statement that created the database. |
| catalog_owner                 | TEXT        | The owner of the database, `NULL` if there is none. |
| last_altered                  | TIMESTAMPTZ | Time the database was last altered. |
| last_altered_by               | TEXT        | Name of the last user to alter the database. |
