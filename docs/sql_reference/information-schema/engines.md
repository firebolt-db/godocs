---
layout: default
title: Engines
parent: Information schema
grand_parent: SQL reference
---

# Information schema for engines

You can use the `information_schema.engines` view to return information about each engine in an account. The view is available for each database and contains one row for each engine in the account. You can use a `SELECT` query to return information about each engine as shown in the example below, which uses a `WHERE` clause to return all engines attached to databases that begin with `deng`.

```sql
SELECT
  *
FROM
  information_schema.engines
WHERE
  attached_to ILIKE 'deng%'
```

## Columns in information_schema.engines

Each row has the following columns with information about each engine.

| Column Name                 | Data Type   | Description |
| :---------------------------| :-----------| :-----------|
| engine_name                 | TEXT      | The name of the engine. |
| region                      | TEXT      | The AWS Region in which the engine was created. |
| spec                        | TEXT      | The specification of nodes comprising the engine. |
| scale                       | INTEGER   | The number of nodes in the engine. |
| status                      | TEXT      | The engine status. For more information, see [Viewing and understanding engine status](../../Overview/understanding-engine-fundamentals.md#viewing-and-understanding-engine-status). |
| attached_to                 | TEXT      | The name of the database to which the engine is attached. |
| version                     | TEXT      | The engine version.|
| url                         | TEXT      | The engine url. |
| warmup                      | TEXT      | The warmup method of the engine. |
| auto_stop                   | BIGINT    | The engine auto stop in seconds. |
| engine_type                 | TEXT      | The type of the engine. |
