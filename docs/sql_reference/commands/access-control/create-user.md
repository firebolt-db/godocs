---
layout: default
title: CREATE USER
description: Reference and syntax for the CREATE USER command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Access control
---

# CREATE USER
Creates a new user.

For more information, see [Managing users](../../../Guides/managing-your-organization/managing-users.md).

## Syntax

```sql
CREATE USER [ IF NOT EXISTS ] <user_name>  
[ WITH 
[LOGIN_NAME = <login_name> | SERVICE_ACCOUNT_NAME = <service_account> ]
[DEFAULT_DATABASE = <database_name> ]
[DEFAULT_SCHEMA = <schema_name> ]
[DEFAULT_ENGINE = <engine_name> ]
[ROLE = <role> ]
]
```


| Parameter  | Description |
| :--------- | :---------- |
| `<user_name>`                              | The name of the user. The user name can be any string, and can also contain spaces and non-alpha-numeric characters such as exclamation points (!), percent signs (%), at signs(@), dot signs (.), underscore signs (_), minus signs (-), and asterisks (*). If the string contains spaces or non-alphanumeric characters, it must be enclosed in single or double quotes.  |
| `<login_name>` | An optional parameter to specify the name of the login to link the user with. This cannot be used in conjunction with the SERVICE_ACCOUNT parameter - a user can be linked to a login OR a service account but not both. |
| `<service_account>` | An optional parameter to specify the name of the service account to link the user with. This cannot be used in conjunction with the LOGIN_NAME parameter - a user can be linked to a login OR a service account but not both. |
| `<database_name>`                      | An optional parameter to define a default database for the user (for future purposes). |
| `<schema_name>` | An optional parameter to define a default engine for the user (for future purposes). |
| `<engine_name>` | An optional parameter to define a default engine for the user (for future purposes). |
| `<role>` | An optional parameter to define a role for the user. Additional roles can be granted after the user is created. If no role is specified, the user is granted no roles. |

## Example

The following command will create a user "alex" linked to the "alexs@acme.com". 

```CREATE USER alex WITH LOGIN_NAME="alexs@acme.com";```
