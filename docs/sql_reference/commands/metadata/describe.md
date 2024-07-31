---
layout: default
title: DESCRIBE
description: Reference and syntax for the DESCRIBE table command.
grand_parent:  SQL commands
parent: Metadata commands
---

# DESCRIBE

Lists all columns and data types for the table. Once the results are displayed, you can also export them to CSV or JSON.

## Syntax
{: .no_toc}

```sql
DESCRIBE <table_name>
```

## Parameters  
{: .no_toc} 

| Parameter      | Description                           |
| :-------------- | :------------------------------------- |
| `<table_name>` | The name of the table to be described. |

## Example 

The following lists all columns and data types for the table named `players`:

```sql
DESCRIBE prices
```

**Returns:**

| table_name | column_name | data_type | nullable |
|:------------|:-------------|:-----------|:----------|
| players     | agecategory        | TEXT      |        0 |
| players     | email         | INTEGER   |        0 |
| players | nickname | TEXT | 0 | 

