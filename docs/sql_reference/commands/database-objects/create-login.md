---
layout: default
title: CREATE LOGIN
description: Reference and syntax for the CREATE LOGIN command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Database object commands
---

# CREATE LOGIN
Creates a new login.

## Syntax

```sql
CREATE LOGIN [ IF NOT EXISTS ] <login_name> 
	WITH [IS_PASSWORD_ENABLED = { TRUE | FALSE }, ]
            [, IS_MFA_ENABLED = { TRUE | FALSE } ]
            [, NETWORK_POLICY_NAME = <network_policy_name> ]
            [, IS_ORGANIZATION_ADMIN = { TRUE | FALSE } ]
	FIRST_NAME = <first_name>,
	LAST_NAME = <last_name> 
```


| Parameter  | Description |
| :--------- | :---------- |
| `<login_name>`                              | The name of the login in the form of an email address. The login must be unique within the organization.   |
| `<network_policy_name>`                      | An optional parameter to define the network policy to link to the created login. |         
| `<first_name>`, `<last_name>` | The first and last name of the user that will use the created login. |

## Example

The following command will create an account in the US East (N. Virginia) region.

```CREATE LOGIN "alexs@acme.com" WITH FIRST_NAME = "Alex" LAST_NAME = "Summers";```
