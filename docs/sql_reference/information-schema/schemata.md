---
layout: default
title: Schemata
description: Use this reference to learn about the metadata available about schemas using the information schema.
parent: Information schema
grand_parent: SQL reference
---

# Information schema for schemata

You can use the `information_schema.schemata` view to return information about schemas available in the database.
You can use a `SELECT` query to return information about each schema as shown in the example below.
```sql
SELECT
  *
FROM
  information_schema.schemata;
```

## Columns in information_schema.schemata

Each row has the following columns with information about the schema.

|  Column Name    | Data Type | Description                                                             |
|:----------------|:----------|:------------------------------------------------------------------------|
| catalog_name    | TEXT      | Name of the catalog.                                                    |
| schema_name     | TEXT      | Name of the schema.                                                     |
| schema_owner    | TEXT      | Owner of the schema.                                                    |
| default_character_set_catalog | TEXT | The catalog that contains the character set. Defaults to NULL. |
| default_character_set_schema  | TEXT | The schema that contains the character set. Defaults to NULL.  |                       |
| default_character_set_name    | TEXT | Default character set of the schema. Defaults to `UTF-8`.      |
| sql_path        | TEXT      | SQL path of the schema.                                                 |
| description     | TEXT      | Description of the schema.                                              |

{: .note}


