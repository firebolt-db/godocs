---
layout: default
title: SHOW ENGINES
description: Reference and syntax for the SHOW ENGINES command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Metadata commands
---

# SHOW ENGINES

Returns a table with a row for each Firebolt engine defined in the current Firebolt account, with columns containing information about each engine as listed below.

## Syntax

```sql
SHOW ENGINES;
```

## Returns

The returned table has the following columns.

| Column name                 | Data Type   | Description |
| :---------------------------| :-----------| :-----------|
| engine_name                 | TEXT      | The name of the engine. |
| region                      | TEXT      | The AWS Region in which the engine was created. |
| spec                        | TEXT      | The specification of nodes comprising the engine. |
| scale                       | INTEGER         | The number of nodes in the engine. |
| status                      | TEXT      | The engine status. For more information, see [Viewing and understanding engine status](../../working-with-engines/understanding-engine-fundamentals.md#viewing-and-understanding-engine-status). |
| attached_to                 | TEXT      | The name of the database to which the engine is attached. |
| version                     | TEXT      | The engine version. |

## Example

The following example highlights engines with descriptive columns: 

```sql
SHOW ENGINES;
```

| database_name |	compressed_size |	uncompressed_size |	description |	created_on |	created_by	|region	| attached_engines |	errors |
|:-------|:-------|:--------|:-------|:-----|:--------|:-------|:------|:-------|
| AdTechDB_v4 |	1.99015E+12 |	3.47886E+13 |	New Demo DB | firebolt-demo |	2022-06-15T11:48:31.683328Z	|SA Demo	us-east-1	| AdTechDB_v4_Analytics (default), AdTechDB_v4_Analytics_Small, AdTechDB_v4_demo_ingestion, AdTechDB_v4_overnight_example |	-
