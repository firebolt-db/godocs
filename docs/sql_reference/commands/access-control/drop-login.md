---
layout: default
title: DROP LOGIN
description: Reference and syntax for the DROP LOGIN command.
grand_parent:  SQL commands
parent: Access control
---

# DROP LOGIN
Deletes an account.

For more information, see [Managing logins](../../../Guides/managing-your-organization/managing-logins.md).

## Syntax

```sql
DROP LOGIN [ IF EXISTS ] <login_name>;
```
{: .note}
If the login is linked to a user, it can not be dropped. In order to drop a login linked to a user, the link must be reset `alter user foo set login="new-login@acme.com"|DEFAULT` or the user dropped.

## Parameters 
{: .no_toc} 

| Parameter  | Description |
| :--------- | :---------- |
| `<login_name>`  | The name of the login to delete. |    

## Example

The following command will delete the "alexs@acme.com" login. 

```sql
DROP LOGIN "alexs@acme.com";
```
