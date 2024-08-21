---
layout: default
title: Storage Billing
description: Use this reference to learn about the metadata available about storage billing using the information schema.
parent: Information schema
---

# Information schema for storage billing

You can use the `information_schema.storage_billing` view to see daily billing information for storage in all the accounts across all the regions in organization.

```sql
SELECT
  *
FROM
  information_schema.storage_billing;
```

## Columns in information_schema.storage_billing

Each row has the following columns.

| Column Name            | Data Type | Description                                          |
|:-----------------------|:----------|:-----------------------------------------------------|
| account_name           | TEXT      | Account for which the storage is billed              |
| region                 | TEXT      | Region where the data is stored                      |
| usage_date             | DATE      | Date for which the usage is reported                 |
| consumed_gib_per_month | NUMERIC   | Amount of data billed for the given date in GiB      |
| billed_cost            | NUMERIC   | The cost for the storage consumed for the given date |
| is_credit              | BOOLEAN   | Indicates whether costs were used as credit          |
