---
layout: default
title: TRUNCATE TABLE
description: Reference and syntax for the TRUNCATE TABLE command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Data management
---

# TRUNCATE TABLE
Removes all rows from a table. 

## Syntax

```sql
TRUNCATE TABLE <table_name> 
```

## Parameters 
{: .no_toc}

| Parameter       | Description                          |
| :-------------- | :------------------------------------ |
| `<table_name>`  | The name of the table to be truncated. |

### Example

```sql
TRUNCATE TABLE product;
```

Table before

```
product
+------------+--------+
| name       | price  |
+---------------------+
| wand       |    125 |
| broomstick |    270 |
| bludger    |      0 |
| robe       |     80 |
| cauldron   |     25 |
| quaffle    |      0 |
+------------+--------+
```

Table after

```
product
+------------+--------+
| name       | price  |
+---------------------+
```