---
layout: default
title: DROP USER
description: Reference and syntax for the DROP USER command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Database object commands
---

# DROP USER
Deletes a user.

## Syntax

```sql
DROP USER [ IF EXISTS ] <user_name> ; 
```

| Parameter  | Description |
| :--------- | :---------- |
| `<user_name>`  | The name of the user to delete. If the user name contains spaces or non-alphanumeric characters, it must be enclosed in single or double quotes. |               

## Example

The following command will delete the "alex" user. 

```sql
DROP USER alex;
```
