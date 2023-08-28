---
layout: default
title: UPDATE
description: Reference and syntax for the UPDATE command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Data management
---

# UPDATE

Updates rows in the specified table.

## Syntax

```sql
UPDATE <table> SET <column1> = <expression1> [, <column2> = <expression2> ...] WHERE <condition>
```

| Parameter | Description|
| :---------| :----------|
| `<table>`| The table name to update rows in. |
| `<column>`       | The name of the column to be updated. |
| `<expression>`      | An expression which computes a new value to populate the column. The expression can reference any column from the row being updated.
| `<condition>` | A Boolean expression. Only rows for which this expression returns `true` will be updated. Condition can have subqueries doing semijoin with other table(s). |

## Remarks
{: .no_toc}

Updated rows are marked for deletion, but are not automatically cleaned up. You can monitor fragmentation in `information_schema.tables` to understand how many rows are marked for deletion out of total rows; fragmentation = (rows marked for deletion / total rows). Total row count in `information_schema.tables` includes the number of rows marked for deletion. Query performance is not materially impacted by delete marks.
  
To mitigate fragmentation, use the [`VACUUM`](./vacuum.md) command to manually clean up deleted rows.

### Example with WHERE

This example applies an added level score for players who have completed more than `10` levels in a game: 

```sql
UPDATE levels SET levels = level + 1 WHERE level > 10
```

| nickname       | price | 
|:-----------|:-------|
| wand       |    120 | 
| broomstick |    270 | 
| robe       |     80 |
| cauldron   |     20 |    


Table after:

```
product
+------------+--------+----------+
| name       | price  | quantity |
+---------------------+----------+
| wand       |    120 |        9 |
| broomstick |    243 |       15 |
| robe       |     80 |        1 |
| cauldron   |     18 |      112 |
+------------+--------+----------+
```

### Example updating multiple columns

This example applies a discount and updates the quantity of a specific product.

```sql
UPDATE product SET price = 15, quantity = 100 WHERE name = 'quaffle'
```

Table before:

```
product
+------------+--------+----------+
| name       | price  | quantity |
+---------------------+----------+
| wand       |    120 |        9 |
| broomstick |    270 |       15 |
| quaffle    |        |          |
| robe       |     80 |        1 |
| cauldron   |     20 |      112 |
+------------+--------+----------+
```

Table after:

```
product
+------------+--------+----------+
| name       | price  | quantity |
+---------------------+----------+
| wand       |    120 |        9 |
| broomstick |    270 |       15 |
| quaffle    |     15 |      100 |
| robe       |     80 |        1 |
| cauldron   |     20 |      112 |
+------------+--------+----------+
```

### Known limitations

Below are some known limitations of the `UPDATE` command. 

* Only one `UPDATE` will be executed against a table at once.

* `UPDATE` cannot be used on tables that have certain aggregating indexes. An attempt to issue a `UPDATE` statement on a table with an aggregating index outside of the below defined will fail - these table level aggregating indexes need to be dropped first. `UPDATE` can be used on tables that have aggregating indexes containing the following aggregating functions:
  * [COUNT and COUNT(DISTINCT)](../../functions-reference/aggregation/count.md)
  * [SUM](../../functions-reference/aggregation/sum.md)
  * [AVG](../../functions-reference/aggregation/avg.md)
  * [PERCENTILE_CONT](../../functions-reference/aggregation/percentile-cont.md)
  * [PERCENTILE_DISC](../../functions-reference/aggregation/percentile-disc.md)
  * [ARRAY_AGG](../../functions-reference/aggregate-array/array-agg.md)
