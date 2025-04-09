---
layout: default
title: ALTER LOGIN
description: Reference and syntax for the ALTER LOGIN command.
great_grand_parent: SQL reference
grand_parent: SQL commands
parent: Access control
---

# ALTER LOGIN

## ALTER LOGIN SET

Updates the configuration of the specified login.

For more information, see [Managing logins]({% link Guides/managing-your-organization/managing-logins.md %}).

### Syntax

```sql
ALTER LOGIN <login_name> SET 
      [ IS_PASSWORD_ENABLED = { TRUE | FALSE } ]
      [ IS_MFA_ENABLED = { TRUE | FALSE } ]
      [ NETWORK_POLICY = <network_policy_name> | DEFAULT ]
      [ IS_ORGANIZATION_ADMIN = { TRUE | FALSE } ]
      [ IS_ENABLED = { TRUE | FALSE } ]
      [ FIRST_NAME = <first_name> ]
      [ LAST_NAME = <last_name> ] 
```

### Parameters

{: .no_toc}

| Parameter                     | Description                                                                                                                                                                                          |
|:------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<login_name>`                | The name of the login in the form of an email address. The login must be unique within the organization.                                                                                             |
| `IS_PASSWORD_ENABLED`         | A `BOOLEAN` value specifying if login with password is enabled. By default this is `TRUE` and passwords can be used to log in.                                                                       |
| `IS_MFA_ENABLED`              | A `BOOLEAN` value specifying if the login has multi-factor authentication (MFA) enabled. By default this value is `FALSE`. If set to `TRUE`, an enrollment email will be sent to the `<login_name>`. |
| `<network_policy_name>`       | An optional parameter to define the network policy to link to the created login. Specifying `DEFAULT` will detach any linked network policy.                                                         |         
| `IS_ORGANIZATION_ADMIN`       | A `BOOLEAN` value specifying if the login is an organization admin. By default this value is `FALSE`.                                                                                                |         
| `IS_ENABLED`                  | A `BOOLEAN` value specifying whether authentication with this login should be possible. Disable login if you want to prevent access to the system without dropping it.                               |  
| `<first_name>`, `<last_name>` | The first and last name of the user to use the login. If the parameter is included, these values cannot be empty.                                                                                    |

### Example

This command will link the network policy “my_network_policy” to the "alexs@acme.com" login. 

```sql
ALTER LOGIN "alexs@acme.com" SET NETWORK_POLICY = "my_network_policy";
```

## ALTER LOGIN RENAME TO

Renames a login.

A login that was created using single sign-on (SSO) cannot be renamed.
{: .note}

### Syntax

```sql
ALTER LOGIN <login_name> RENAME TO <new_login_name>
```

### Parameters

{: .no_toc}

| Parameter          | Description                                                                                                                                                                    |
|:-------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<login_name>`     | The name of the login to rename.                                                                                                                                               |
| `<new_login_name>` | The new name of the login in the form of an email address. The login must be unique within the organization. If the `login` was created using SSO, it cannot be renamed. |

### Example

The following command will rename the "alexs@acme.com" login to "alexspotter@acme.com".

```sql
ALTER LOGIN "alexs@acme.com" RENAME TO "alexspotter@acme.com";
```

## ALTER LOGIN OWNER TO

Changes the owner of a login.

You can view the current owner in the `login_owner` column of the `information_schema.logins` view.

For more information, see [ownership]({% link Guides/security/ownership.md %}).

### Syntax

```sql
ALTER LOGIN <login_name> OWNER TO <identity>
```

### Parameters

{: .no_toc}

| Parameter      | Description                                                            |
|:---------------|:-----------------------------------------------------------------------|
| `<login_name>` | The name of the login to change the owner of.                          |
| `<identity>`   | The new owner of the login, which can be the name of another login or service account. |

### Example

The following command will set login "bob@acme.com" owner to "alice@acme.com".

```sql
ALTER LOGIN "bob@acme.com" OWNER TO "alice@acme.com";
```
