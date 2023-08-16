---
layout: default
title: DELETE
description: Reference and syntax for the DELETE command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Data management
---

# DELETE

Deletes rows from the specified table.

## Syntax

```sql
DELETE FROM <table> WHERE <expression>
```
## Parameters 
{: .no_toc} 

| Parameter | Description|
| :---------| :----------|
| `<table>`| The table to delete rows from. |
| `<expression>` | A Boolean expression. Only rows for which this expression returns `true` will be deleted. Condition can have subqueries doing semijoin with other table(s). |

{: .note}
The `DELETE FROM <table>` without `<expression>` will delete *all* rows from the table. It is equivalent to a [TRUNCATE TABLE](../commands/truncate-table.md) statement.

## Remarks
{: .no_toc}

Deleted rows are marked for deletion, but are not automatically cleaned up. You can monitor fragmentation in `information_schema.tables` to understand how many rows are marked for deletion out of total rows; fragmentation = (rows marked for deletion / total rows). Total row count in `information_schema.tables` includes the number of rows marked for deletion. Query performance is not materially impacted by delete marks.
  
To mitigate fragmentation, use the [`VACUUM` (Beta)](vacuum.md) command to manually clean up deleted rows.

## Example 

The following example deletes entries from the `levels` table where the `level` is equal to `0`: 

`DELETE FROM levels WHERE level = 0`

Table before:

| nickname   | level  |
|:-----------| :------|
| esimpson       |    8 |
| sabrina21 |    4 |
| kennthpark    |      0 |
| rileyjon       |     2 |
| aaronbutler   |     1 |
| ywilson    |      0 |



**Returns**:

| nickname   | level  |
|:-----------| :------|
| esimpson       |    8 |
| sabrina21 |    4 |
| rileyjon       |     2 |
| aaronbutler   |     1 |



<!-- ### Example with subqueries

```sql
DELETE FROM levels WHERE 
  name IN (SELECT name FROM inventory WHERE amount = 0) OR
  name NOT IN (SELECT name FROM inventory)
```

Tables before:

```
product
+------------+--------+
| name       | price  |
+---------------------+
| wand       |    125 |
| broomstick |    270 |
| robe       |     80 |
| cauldron   |     25 |
+------------+--------+

inventory
+------------+--------+
| name       | amount |
+---------------------+
| wand       |      3 |
| cauldron   |     18 |
| robe       |      0 |
| bludger    |      5 |
+------------+--------+
```

Table after:
```
product
+------------+--------+
| name       | price  |
+---------------------+
| wand       |    125 |
| cauldron   |     25 |
+------------+--------+
``` -->


### Known limitations

Below are some known limitations of the `DELETE` command. 

* Only one `DELETE` will be executed against a table at once.

* `DELETE` cannot be used on tables that have certain aggregating indexes, or join indexes. An attempt to issue a `DELETE` statement on a table with a join index or aggregating index outside of the below defined will fail- these table level aggregating or join indexes need to be dropped first. `DELETE` can be used on tables that have aggregating indexes containing the following aggregating functions, starting in **DB version 3.15.0:**
  * [COUNT and COUNT(DISTINCT)](../functions-reference/count.md)
  * [SUM](../functions-reference/sum.md)
  * [AVG](../functions-reference/avg.md)
  * [PERCENTILE_CONT](../functions-reference/percentile-cont.md)
  * [PERCENTILE_DISC](../functions-reference/percentile-disc.md)
  * [ARRAY_AGG/NEST](../functions-reference/array-agg.md)

* Queries against tables with deleted rows are supported and can be run. However, expect slower performance.

* `DELETE` marks are always loaded during engine warm-up, regardless of engine policy. This can increase engine start time if there are significant number of deletions.
