---
layout: default
title: DROP VIEW
description: Reference and syntax for the DROP VIEW command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Data definition
---

# DROP VIEW

Deletes a view.

## Syntax

```sql
DROP VIEW [IF EXISTS] <view_name> [CASCADE]
```

| Parameter     | Description                         |
| :------------- | :----------------------------------- |
| `<view_name>` | The name of the view to be deleted. |
| `CASCADE`       | When specified, causes all dependent database objects such as views and aggregating indexes to be dropped also. |
