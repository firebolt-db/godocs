---
layout: default
title: DROP ACCOUNT
description: Reference and syntax for the DROP ACCOUNT command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Data definition
---

# DROP ACCOUNT
Deletes an account.

For more information, see [Managing accounts](../../../Guides/managing-your-organization/managing-accounts.md).

## Syntax

```sql
DROP ACCOUNT [ IF EXISTS ] <account_name> [ RESTRICT | CASCADE ];
```

## Parameters 
{: .no_toc} 

| Parameter  | Description |
| :--------- | :---------- |
| `<account_name>`  | The name of the account to delete. |   
| RESTRICT or CASCADE | An optional parameter to specify deletion mode.<br>RESTRICT mode prevents dropping the account if there is any sub-object contained in the account.<Br>By default, if the account contains no objects, it will just be dropped.<br>CASCADE mode automatically drops the account and all the sub-objects it contains (databases, engines, users, roles, etc.).

{: .note} 
All engines in your accounts must be in a stopped state before running the `DROP ACCOUNT … CASCADE` statement.                 

## Example

The following command will delete the "dev" account. 

```sql
DROP ACCOUNT dev
```
