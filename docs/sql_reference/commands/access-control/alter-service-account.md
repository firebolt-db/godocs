---
layout: default
title: ALTER SERVICE ACCOUNT
description: Reference and syntax for the ALTER SERVICE ACCOUNT command.
great_grand_parent: SQL reference
grand_parent: SQL commands
parent: Access control
---

# ALTER SERVICE ACCOUNT

## ALTER SERVICE ACCOUNT SET

Updates the configuration of the specified service account.

For more information, see [Service accounts]({% link Guides/managing-your-organization/service-accounts.md %}).

### Syntax

```sql
ALTER SERVICE ACCOUNT <service_account_name> SET 
      [ NETWORK_POLICY = <network_policy_name> | DEFAULT ] 
      [ DESCRIPTION = <description> | DEFAULT ]
      [ IS_ORGANIZATION_ADMIN = { TRUE | FALSE } ]
      [ CONNECTION_PREFERENCE = { PUBLIC_ONLY | PRIVATE_ONLY | PREFER_PUBLIC | PREFER_PRIVATE | DEFAULT } ]
      [ IS_ENABLED = { TRUE | FALSE } ]
```

### Parameters

{: .no_toc}

| Parameter                | Description |
|:-------------------------|:------------|
| `<service_account_name>` | The name of the service account to edit. |
| `<description>`          | An optional description for the service account. |
| `<network_policy_name>`  | An optional parameter to define the network policy to link to the edited service account. Specifying `DEFAULT` will detach any linked network policy. |         
| `IS_ORGANIZATION_ADMIN`  | A `BOOLEAN` value specifying if the service account is an organization admin. By default, this value is `FALSE`. |         
| `IS_ENABLED`             | A `BOOLEAN` value specifying whether authentication with this service account should be possible. Disable the service account to prevent access without dropping it. |
| `CONNECTION_PREFERENCE`  | Defines how the service account connects to Firebolt. The default value is `PREFER_PUBLIC` if not specified. See **Connection preferences** for details. |
| `<new_name>`             | The new name of the service account. Must start with a letter and may contain only alphanumeric, digit, or underscore (_) characters. |

#### Connection Preferences  

The `CONNECTION_PREFERENCE` parameter determines how a [service account]({% link Guides/managing-your-organization/service-accounts.md %}) accesses Firebolt:  

* **`PUBLIC_ONLY`**: Allows access only through public APIs.  
* **`PRIVATE_ONLY`**: Allows access only through AWS PrivateLink.  
* **`PREFER_PUBLIC`** (Default): Prefers public APIs but can use AWS PrivateLink if needed.  
* **`PREFER_PRIVATE`**: Prefers AWS PrivateLink but can use public APIs if needed.  

### Example

The following code example assigns the network policy `my_network_policy` to the `serviceaccount1` service account:

```sql
ALTER SERVICE ACCOUNT "serviceaccount1" SET NETWORK_POLICY = "my_network_policy";
```

## ALTER SERVICE ACCOUNT RENAME TO

Renames a service account.

### Syntax

```sql
ALTER SERVICE ACCOUNT <service_account_name> RENAME TO <new_service_account_name>;
```

### Parameters

{: .no_toc}

| Parameter          | Description                                |
|:-------------------|:-------------------------------------------|
| `<service_account_name>`     | The name of the service account to rename. |
| `<new_service_account_name>` | The new name of the service account.       |

### Example

The following command will rename the service account "machine_user" to "ai_agent".

```sql
ALTER SERVICE ACCOUNT "machine_user" RENAME TO "ai_agent";
```

## ALTER SERVICE ACCOUNT OWNER TO

Changes the owner of a service account.

You can view the current owner in the `service_account_owner` column of the `information_schema.service_accounts` view.

For more information, see [ownership]({% link Guides/security/ownership.md %}).

### Syntax

```sql
ALTER SERVICE ACCOUNT <service_account_name> OWNER TO <identity>
```

### Parameters

{: .no_toc}

| Parameter                | Description                                                                      |
|:-------------------------|:---------------------------------------------------------------------------------|
| `<service_account_name>` | The name of the service account to change the owner of.                          |
| `<identity>`             | The new owner of the service account, which can be the name of another login or service account. |
