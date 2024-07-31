---
layout: default
title: SHOW COLUMNS
description: Reference and syntax for the SHOW COLUMNS command.
grand_parent:  SQL commands
parent: Metadata commands
---

# SHOW COLUMNS

Lists columns and their properties for a specified table. Returns `<table_name>`, `<column_name>`, `<data_type>`, 
and `nullable` (`TRUE` if nullable, `FALSE` if not) for each column.

## Syntax

```sql
SHOW COLUMNS <table>;
```
## Parameters  
{: .no_toc} 

| Parameter      | Description                           |
| :-------------- | :------------------------------------- |
| `<table>` | The name of the table to be analyzed. |

## Example
The following example highlights all of the columns from the `tournaments` table: 

```sql
SHOW COLUMNS tournaments;
```

| table_name | 	column_name           | 	data_type	| nullable | 
|:-------|:-----------------------|:--------|:--------|
| tournaments | 	enddatetime           | TIMESTAMP | FALSE |
| tournaments | 	gameid                | INTEGER | FALSE |
| tournaments	| name	                  | TEXT	| FALSE |
| tournaments	| rulesdefinition	       | TEXT |	FALSE |
| tournaments	| SOURCE_FILE_NAME	      | TEXT	| FALSE |
| tournaments	| SOURCE_FILE_TIMESTAMP	 | TIMESTAMP	| FALSE |
| tournaments	| startdatetime	         | TIMESTAMP	| FALSE |
| tournaments | 	totalprizedollars     |	INTEGER	| FALSE |
| tournaments	| tournamentid           |	INTEGER	| FALSE |

