---
layout: default
title: DROP ACCOUNT
description: Reference and syntax for the DROP ACCOUNT command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Database object commands
---

# DROP ACCOUNT
Deletes an account.

## Syntax

```DROP ACCOUNT [ IF EXISTS ] <account_name> [ RESTRICT | CASCADE ];```


| Parameter  | Description |
| :--------- | :---------- |
| `<account_name>`  | The name of the account to delete. |   
| RESTRICT or CASCADE | An optional parameter to specify deletion mode.<br>RESTRICT mode prevents dropping the account if there is any sub-object contained in the account.<Br>By default, if the account contains no objects, it will just be dropped.<br>CASCADE mode automatically drops the account and all the sub-objects it contains (databases, engines, users, roles, etc.).

{: .note} 
All engines in your accounts must be in a stopped state before running the `DROP ACCOUNT … CASCADE` statement.                 

## Example

The following command will delete the "my_account" account. 

```DROP ACCOUNT my_account```
