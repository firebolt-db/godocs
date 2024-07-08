---
layout: default
title: Storage history
description: Use this reference to learn about the storage consumption of your catalogs (databases)
parent: Information schema
grand_parent: SQL reference
---

# Information schema for storage history

You can use the `information_schema.storage_history` view to return information about the storage consumption of your catalogs (databases).
Due to the nature of this view's computation, it is eventually consistent. DROP / INSERT / UPDATE / VACUUM operations may take up to 2 days to be fully reflected.

In the example below, a filter is applied to look at the metrics of all catalogs over the last week.
By default, the view shows data as far back as each catalog has existed.

```sql
SELECT
  *
FROM
  information_schema.storage_history
WHERE
  usage_date > now() - INTERVAL '7 days'
  and catalog_id is not null
LIMIT 100;
```

Dropped catalogs display NULL `catalog_name`, but are trackable by `catalog_id`.

Rows not attributed to any one catalog (NULL `catalog_id`) carry special meaning. This storage consumption is account-wide. It covers inactive data (garbage files that are preserved for the duration of a 1 week fail-safe period), as well as active in-flight data (any new files that were not yet transactionally attributed to a catalog during consumption computation).

This example shows how to look up storage consumption not associated with any particular catalog.

```sql
SELECT
  *
FROM
  information_schema.storage_history
WHERE
  catalog_id is null
LIMIT 100;
```

## Columns in information_schema.storage_history

Each row has the following columns with information about storage consumption.

| Column Name              | Data Type   | Description                                                    |
|:-------------------------|:------------|:---------------------------------------------------------------|
| catalog_name             | TEXT        | Catalog (database) for which storage is reported               |
| catalog_id               | TEXT        | Catalog (database) id for which storage is reported            |
| usage_date               | DATE        | Date for which the usage is reported                           |
| active_data_size_bytes   | BIGINT      | Number of bytes consumed by active data                        |
| inactive_data_size_bytes | BIGINT      | Number of bytes consumed by inactive data                      |
