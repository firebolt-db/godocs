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
DELETE FROM <table> [[AS] <alias>] [USING <from_item>] WHERE <condition>
```
## Parameters 
{: .no_toc} 

| Parameter | Description|
| :---------| :----------|
| `<table>`| The table to delete rows from. |
| `<from_item>` | A table expression allowing columns from other tables to appear in the `WHERE` condition. This uses the same syntax as the `FROM` clause of a `SELECT` statement; for example, an alias for the table name can be specified. Do not repeat the target table as a `from_item` unless you wish to set up a self-join (in which case it must appear with an alias in the `from_item`). |
| `<condition>` | A Boolean expression. Only rows for which this expression returns `true` will be deleted. Condition can have subqueries doing semi-join with other table(s). |

{: .note}
The `DELETE FROM <table>` without `<expression>` will delete *all* rows from the table. It is equivalent to a [TRUNCATE TABLE](./truncate-table.md) statement.

## Remarks
{: .no_toc}

Deleted rows are marked for deletion, but are not automatically cleaned up. You can monitor fragmentation in [information_schema.tables](../../information-schema/tables.md) to understand how many rows are marked for deletion out of total rows; fragmentation = (rows marked for deletion / total rows). Total row count in `information_schema.tables` excludes the number of rows marked for deletion. Query performance is not materially impacted by delete marks.
  
To mitigate fragmentation, use the [VACUUM](vacuum.md) command to manually clean up deleted rows.

## Example 

The following example deletes entries from the `products` table where the `quantity` is less than `10`: 

```sql
DELETE FROM products WHERE quantity < 10
```

Table before:

| product | quantity |
|:-|:-|
| wand | 9 |
| broomstick | 21 |
| robe | 1 |
| quidditch gloves | 10 |
| cauldron | 16 |
| quill | 100 |

Table after:

| product | quantity |
|:-|:-|
| broomstick | 21 |
| quidditch gloves | 10 |
| cauldron | 16 |
| quill | 100 |


### Example specifying other tables in the USING clause

This example deletes all the products from stores that went out of business.

```sql
DELETE FROM products USING suppliers WHERE products.product = suppliers.product AND suppliers.store = 'Ollivanders'
```

Table `products` before:

| product | quantity |
|:-|:-|
| wand | 9 |
| broomstick | 21 |
| robe | 1 |
| quidditch gloves | 10 |
| cauldron | 16 |
| quill | 100 |

Table `suppliers` before:

| product | store |
|:-|:-|
| wand | Ollivanders |
| broomstick | Quality Quidditch Supplies |
| robe | Madam Malkin’s |
| quidditch gloves | Quality Quidditch Supplies |
| cauldron | Apothecary |
| quill | Amanuensis Quills |

Table `products` after:

| product | quantity |
|:-|:-|
| broomstick | 21 |
| robe | 1 |
| quidditch gloves | 10 |
| cauldron | 16 |
| quill | 100 |

### Known limitations

Below are some known limitations of the `DELETE` command. 

* `DELETE`/`UPDATE` will perform slower on the following aggregate functions:
  * [MIN](../../functions-reference/aggregation/min.md)
  * [MIN_BY](../../functions-reference/aggregation/min-by.md)
  * [MAX](../../functions-reference/aggregation/max.md)
  * [MAX_BY](../../functions-reference/aggregation/max-by.md)
  * [ANY_VALUE](../../functions-reference/aggregation/any_value.md)
  * [APPROX_COUNT_DISTINCT](../../functions-reference/aggregation/approx-count-distinct.md)

* Queries against tables with deleted rows are supported and can be run. However, expect slower performance.
