---
layout: default
title: ALTER USER
description: Reference and syntax for the ALTER USER command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Database object commands
---

# ALTER USER

Updates the configuration of the specified user.

For more information, see [Managing users](../../../Guides/managing-your-organization/managing-users.md).

## Syntax

```sql
ALTER USER <user_name> SET
	[LOGIN_NAME = <login_name> | DEFAULT ]
        [SERVICE_ACCOUNT_NAME = <service_account> | DEFAULT ]
        [ DEFAULT_DATABASE = <database_name> | DEFAULT ]
        [ DEFAULT_SCHEMA = <schema_name> | DEFAULT ]
	[ DEFAULT_ENGINE = <engine_name> | DEFAULT ];
```
or 

```ALTER USER <user_name> RENAME TO <new_user_name>;```

| Parameter | Description |
| :--- | :--- |
| `<user_name>`                              | The name of the user. If the user name contains spaces or non-alphanumeric characters, it must be enclosed in single or double quotes.  |
| `<new_user_name>` | The new name of the user, used with the `RENAME TO` option. The new user name can be any string, and can also contain spaces and non-alpha-numeric characters such as exclamation points (!), percent signs (%), at signs(@), dot signs (.), underscore signs (_), minus signs (-), and asterisks (*). If the string contains spaces or non-alphanumeric characters, it must be enclosed in single or double quotes.
| `<login_name>` | An optional parameter to specify the name of the login to link the user with, used with the `SET` option. This cannot be used in conjunction with the SERVICE_ACCOUNT parameter - a user can be linked to a login OR a service account but not both. |
| `<service_account>` | An optional parameter to specify the name of the service account to link the user with, used with the `SET` option. This cannot be used in conjunction with the LOGIN_NAME parameter - a user can be linked to a login OR a service account but not both. |
| `<database_name>`                      | An optional parameter to define a default database for the user (for future purposes). Used with the `SET` option. |
| `<schema_name>` | An optional parameter to define a default engine for the user (for future purposes). Used with the `SET` option. |
| `<engine_name>` | An optional parameter to define a default engine for the user (for future purposes).Used with the `SET` option. |

## Example

The following command will rename the "alex" account to "alexs".

```ALTER USER "alex" RENAME TO "alexs";```

This command will link the user "alex" to the "alexs@acme.com" login.

```ALTER USER alex SET LOGIN_NAME="alexs@acme.com";```
