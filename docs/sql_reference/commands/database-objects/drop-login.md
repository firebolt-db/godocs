---
layout: default
title: DROP LOGIN
description: Reference and syntax for the DROP LOGIN command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Database object commands
---

# DROP LOGIN
Deletes an account.

## Syntax

```sql
DROP LOGIN [ IF EXISTS ] <login_name> [ RESTRICT | CASCADE ]; 
```

| Parameter  | Description |
| :--------- | :---------- |
| `<login_name>`  | The name of the login to delete. |   
| RESTRICT or CASCADE | An optional parameter to specify deletion mode.<br>RESTRICT mode prevents dropping the account if there is any user linked to the login.<Br>By default, if the login is not linked to any users, it will just be dropped.<br>CASCADE mode automatically drops all users linked to the login in all the accounts in the organization.               

## Example

The following command will delete the "alexs@acme.com" login. 

```sql
DROP LOGIN "alexs@acme.com";
```
