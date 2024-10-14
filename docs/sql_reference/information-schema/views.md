---
layout: default
title: Views
description: Use this reference to learn about the metadata available for Firebolt views using the information schema.
parent: Information schema
grand_parent: SQL reference
---

# Information schema for views
You can use the `information_schema.views` view to return information about each view in a database. The view is available for each database and contains one row for each view in the database. You can use a `SELECT` query to return information about each view as shown in the example below.

```sql
SELECT
  *
FROM
  information_schema.views;
```

## Columns in information_schema.views

Each row has the following columns with information about each view.

| Column Name                 | Data Type   | Description |
| :---------------------------| :-----------| :-----------|
| table_catalog               | TEXT      | The name of the catalog. Firebolt offers a single ‘default’ catalog. |
| table_schema                | TEXT      | The name of the database. |
| table_name                  | TEXT      | The name of the view. |
| view_definition             | TEXT      | The query statement that defines the view. |
| check_option                | NULL        | Not applicable for Firebolt. |
| is_updatable                | TEXT        | Always `NO`. |
| insertable_into             | TEXT        | Always `NO`. |
| is_trigger_updatable        | TEXT        | Always `NO`. |
| is_trigger_deletable        | TEXT        | Always `NO`. |
| is_trigger_insertable_into  | TEXT        | Always `NO`. |
| created                     | TIMESTAMPTZ   | Time that the view was created. |
| view_owner                  | TEXT      | The owner of the view. |
| last_altered                | TIMESTAMPTZ   | Time that the view was last changed. |
| last_altered_by             | TEXT   | The user who last altered this view. |
