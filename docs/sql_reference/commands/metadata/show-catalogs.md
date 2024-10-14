---
layout: default
title: SHOW CATALOGS
description: Reference and syntax for the SHOW CATALOGS command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Metadata commands
---

# SHOW CATALOGS

Returns a table with a row for each catalog (i.e., database) defined in the current Firebolt account, with columns containing information as listed below.

## Syntax

```sql
SHOW CATALOGS;
```

## Returns

The returned table has the following columns.

| Column name     | Data Type   | Description                                                                     |
|:----------------|:------------|:--------------------------------------------------------------------------------|
| catalog_name    | TEXT        | The name of the catalog.                                                        |
| catalog_owner   | TEXT        | Current owner of the catalog. Default owner is the user who created the catalog |
| created         | TIMESTAMPTZ | Time the catalog was created (UTC)                                              |
| last_altered    | TIMESTAMPTZ | The date and time that the database was last modified (UTC)                     |
| last_altered_by | TEXT        | User/principal who edited the catalog                                           |
| ddl             | TEXT        | Complete DDL of the database.                                                   |
| description     | TEXT        | User provided description of the database                                       |

## Example

The following example shows information about CATALOGS in the account: 

```sql
SHOW CATALOGS;
```

| catalog_name | catalog_owner | created                       | last_altered                  | last_altered_by | ddl                                                              | description   |
|:-------------|:--------------|:------------------------------|:------------------------------|:----------------|:-----------------------------------------------------------------|:--------------|
| AdTechDB_v4  | firebolt-demo | 2024-09-03 11:48:31.683328+00 | 2024-09-03 11:48:31.683328+00 | firebolt-demo   | CREATE DATABAE AdTechDB_v4 () WITH DESCRIPTION=\'DB for AdTech\' | DB for AdTech |
