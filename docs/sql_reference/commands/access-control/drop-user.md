---
layout: default
title: DROP USER
description: Reference and syntax for the DROP USER command.
grand_parent:  SQL commands
parent: Access control
---

# DROP USER
Deletes a user.

For more information, see [Managing users](../../../Guides/managing-your-organization/managing-users.md).

{: .warning}
A user cannot be dropped if it owns objects. In this case, an error message will be displayed, and you need to manually drop the objects, or transfer ownership.

for more information, see [Ownership](../../../Guides/security/ownership.md).

## Syntax

```sql
DROP USER [ IF EXISTS ] <user_name> ;
```

## Parameters 
{: .no_toc} 

| Parameter  | Description |
| :--------- | :---------- |
| `<user_name>`  | The name of the user to delete. If the user name contains spaces or non-alphanumeric characters, it must be enclosed in single or double quotes. |               

## Example

The following command will delete the "alex" user. 

```sql
DROP USER alex;
```
