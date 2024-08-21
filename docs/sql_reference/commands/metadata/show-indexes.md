---
layout: default
title: SHOW INDEXES
description: Reference and syntax for the SHOW INDEXES command.
parent: Metadata commands
---

# SHOW INDEXES

Returns a table with a row for each Firebolt index defined in the current database, with columns containing information about each index as listed below.

## Syntax

```sql
SHOW INDEXES;
```

## Returns

The returned table has the following columns.

| Column name                 | Data Type   | Description |
| :---------------------------| :-----------| :-----------|
| index_name                  | TEXT      | The name of the index. |
| table_name                  | TEXT      | The name of the table associated with the index. |
| type                        | TEXT      | One of `primary` or `aggregating`. |
| expression                  | ARRAY (TEXT)| An ordered array of the expression in SQL that defined the index. |
| size_compressed             | DOUBLE PRECISION | The size of the index in bytes. |
| size_uncompressed           | DOUBLE PRECISION  | The uncompressed size of the index in bytes. |
| compression_ratio           | DOUBLE PRECISION  | The compression ratio (`<size_uncompressed>`/`<size_compressed>`).
| number_of_segments          | INTEGER      | The number of segments comprising the table. |

## Example

The following example returns information about indexes in the database queried: 

```sql
SHOW INDEXES;
```

| index_name | table_name |	type |	expression |	size_compressed |	size_uncompressed |	compression_ratio |	number_of_tablets |
|:-----|:-----|:----|:------|:-----|:-----|:-------|:------|
| players_join_idx |	players	| join |	["playerid","nickname","email","agecategory"]	| 819.98 KiB	| 819.98 KiB	| 1	| 0 |