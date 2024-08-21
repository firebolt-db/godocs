---
layout: default
title: Storage Metering History
description: Use this reference to learn about the metadata available about storage metering history using the information schema.
parent: Information schema
---

# Information schema for storage metering history

You can use the `information_schema.storage_metering_history` view to see daily information about aggregated storage consumption within an account.

```sql
SELECT
  *
FROM
  information_schema.storage_metering_history;
```

## Columns in information_schema.storage_metering_history

Each row has the following columns.

| Column Name            | Data Type | Description                                                |
|:-----------------------|:----------|:-----------------------------------------------------------|
| usage_date             | DATE      | Date for which the usage is reported                       |
| consumed_gib_per_month | NUMERIC   | Number of bytes consumed by the account for the given date |
