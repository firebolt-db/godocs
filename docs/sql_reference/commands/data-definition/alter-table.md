---
layout: default
title: ALTER TABLE
description: Reference and syntax for the ALTER TABLE command.
grand_parent:  SQL commands
parent: Data definition
---

# ALTER TABLE

Updates the specified table.


## ALTER TABLE DROP PARTITION

Use to delete a partition from a fact or dimension table.

{: .warning}
Dropping a partition deletes the partition and the data stored in that partition.

### Syntax

```sql
ALTER TABLE <table> DROP PARTITION <value1>[,...<value2]
```

### Parameters 
{: .no_toc} 

| Parameter          | Description                                  |
| :------------------ | :-------------------------------------------- |
| `<table>`     | Name of the table from which to drop the partition. |
| `<value1>[,...<value2>]` | An ordered set of one or more values corresponding to the partition key definition. This specifies the partition to drop. When dropping partitions with composite keys (more than one key value), specify all key values in the same order as they were defined. Only partitions with values that match the entire composite key are dropped. |

### Examples

See the examples in [Working with partitions](../../../Overview/working-with-tables/working-with-partitions.md).

## ALTER TABLE OWNER TO

Change the owner of a table. The current owner of a table can be viewed in the `information_schema.tables` view on `table_owner` column.

check [ownership](../../../Guides/security/ownership.md) page for more info.

### Syntax

```sql
ALTER TABLE <table> OWNER TO <user>
```

### Parameters 
{: .no_toc}

| Parameter          | Description                                  |
| :------------------ | :-------------------------------|
| `<table>` | Name of the table to change the owner of. |
| `<user>`  | The new owner of the table.               |
