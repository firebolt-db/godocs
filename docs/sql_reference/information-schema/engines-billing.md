---
layout: default
title: Engines Billing
description: Use this reference to learn about the metadata available about engines billing using the information schema.
parent: Information schema
grand_parent: SQL reference
---

# Information schema for engines billing

You can use the `information_schema.engines_billing` view to see daily billing information for all the engines in all the accounts across all the regions in organization.

```sql
SELECT
  *
FROM
  information_schema.engines_billing;
```

## Columns in information_schema.engines_billing

Each row has the following columns.

| Column Name        | Data Type | Description                                                         |
|:-------------------|:----------|:--------------------------------------------------------------------|
| engine_name        | TEXT      | Name of the engine                                                  |
| account_name       | TEXT      | Account to which the engine belongs                                 |
| engine_description | TEXT      | Description of engine as entered by user when the engine is created |
| region             | TEXT      | Region where the engine was created                                 |
| usage_date         | DATE      | Date for which the usage is reported                                |
| consumed_fbu       | NUMERIC   | Number of FBUs consumed by the engine for the given date            |
| billed_cost        | NUMERIC   | The cost for the FBUs consumed for the given date                   |
| is_credit          | BOOLEAN   | Indicates whether costs were used as credit                         |
