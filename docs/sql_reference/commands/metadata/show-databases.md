---
layout: default
title: SHOW DATABASES
description: Reference and syntax for the SHOW DATABASES command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Metadata commands
---

# SHOW DATABASES

Returns a table with a row for each database defined in the current Firebolt account, with columns containing information as listed below.

## Syntax

```sql
SHOW DATABASES;
```

## Returns

The returned table has the following columns.

| Column name      | Data Type   | Description |
| :----------------| :-----------| :-----------|
| database_name    | TEXT      | The name of the database. |
| region           | TEXT      | The AWS Region in which the database was created. |
| created_on       | TIMESTAMP   | The date and time that the database was created (UTC). |
| created_by       | TEXT      | The user name of the Firebolt user who created the database. |
| errors           | TEXT      | Any error messages associated with the database. |

## Example

The following example shows information about databases in the account: 

```sql
SHOW DATABASES;
```

| database_name	| compressed_size	| uncompressed_size	| description	| created_on	| created_by	| region	| attached_engines	| errors |
|:----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:------|
| AdTechDB_v4	| NULL	| NULL	| New Demo DB| 2022-06-15T11:48:31.683328Z	| firebolt-demo	| SA Demo	us-east-1	| NULL	| NULL |
