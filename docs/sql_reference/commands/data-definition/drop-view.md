---
layout: default
title: DROP VIEW
description: Reference and syntax for the DROP VIEW command.
<<<<<<< HEAD:docs/sql_reference/commands/data-definition/drop-view.md
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Data definition
=======
parent:  SQL commands
>>>>>>> rn/gh-pages:docs/sql-reference/commands/drop-view.md
---

# DROP VIEW

Deletes a view.

## Syntax
{: .no_toc}

```sql
DROP VIEW [IF EXISTS] <view_name> [CASCADE]
```
## Parameters
{: .no_toc}

| Parameter     | Description                         |
| :------------- | :----------------------------------- |
| `<view_name>` | The name of the view to be deleted. |
| `CASCADE`       | When specified, causes all dependent database objects such as views and aggregating indexes to be dropped also. |
