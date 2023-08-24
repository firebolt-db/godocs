---
layout: default
title: ALTER TABLE...DROP PARTITION
description: Reference and syntax for the ALTER TABLE...DROP PARTITION command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Data ingest and movement commands
---

# ALTER TABLE...DROP PARTITION

Use `ALTER TABLE...DROP PARTITION` to delete a partition from a fact or dimension table.

{: .warning}
Dropping a partition deletes the partition and the data stored in that partition.

## Syntax

```sql
ALTER TABLE <table> DROP PARTITION <value1>[,...<value2]
```
## Parameters 
{: .no_toc} 

| Parameter          | Description                                  | Mandatory? Y/N |
| :------------------ | :-------------------------------------------- | :-------------- |
| `<table>`     | Name of the table from which to drop the partition.                         | Y              |
| `<value1>[,...<value2>]` | An ordered set of one or more values corresponding to the partition key definition. This specifies the partition to drop. When dropping partitions with composite keys (more than one key value), specify all key values in the same order as they were defined. Only partitions with values that match the entire composite key are dropped. | Y              |

## Examples

See the examples in [Working with partitions](../../working-with-partitions.md#examples).
