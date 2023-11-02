---
layout: default
title: Service accounts
description: Learn about creating service account users for Firebolt.
nav_order: 6
parent: Manage organization
grand_parent: Guides
---

# Manage service accounts
{: .no_toc}

Create a service account for programmatic access **only** to Firebolt. Service accounts can be linked to users, instead of logins which provide full access. For each service account, a secret is generated to use for authentication. You can add, edit, delete and generate secrets for service accounts using SQL or in the UI. 

To view all users, click **Govern** to open the govern space, then choose **Service Accounts** from the menu, or query the [information_schema.service_accounts](../../sql_reference/information-schema/service-accounts.md) view. 

{: .note}
Managing service accounts requires the org_admin role.

## Creating a service account 

### SQL 
To create a service account using SQL, use the [`CREATE SERVICE ACCOUNT`](../../sql_reference/commands/access-control/create-service-account.md) statement. For example:

```sql
CREATE SERVICE ACCOUNT IF NOT EXISTS "sa1" WITH DESCRIPTION = "service account 1";
```

### UI
To create a service account via the UI:

![Configure > Service accounts](../../assets/images/serviceaccountspage.png)

1. Click **Configure** to open the configure space, then choose **Service accounts** from the menu.
2. From the Service accounts page, choose **Create a service account**.
3. Enter a unique name for your service account. This name must start with a letter, and may contain only alphanumeric characters, or the underscore(_) character.
4. Optionally, you can:
  - Choose a **network policy** to apply from the list of existing [network policies](./network-policies.md) configured for your organization. 
  - Specify a description for the service account.
5. Choose **Create**. 

## Generating a secret for a service account
A service account secret is used to generate an access token for accessing Firebolt API programmatically with the service account. 

### SQL 
To generate a secret for a service account using SQL, use the ```CALL fb_GENERATESERVICEACCOUNTKEY(`<name>`)``` statement, where `<name>` is the name of the service account. The command returns both the service account ID and secret. For example:

```sql
CALL fb_GENERATESERVICEACCOUNTKEY('sa1')
```

### UI
To generate a secret for a service account via the UI:

1. Click **Configure** to open the configure space, then choose **Service accounts** from the menu.
2. Search for the relevant service account using the top search filters, or by scrolling through the list of service accounts. Hover over the right-most column to make the service account menu appear, then choose **Create a new secret**.
3. The **New secret for service account" menu with the newly generated secret will appear.

<img src="../../assets/images/newsecret.png" alt="New secret" width="500"/>

**Make a note of the secret once generated** - it can't be retrieved later.  If the secret is lost (or needs to be rotated), you can always generate a new secret, calling the same generation function, or by creating a new secret in the UI. 

{: .note}
Generating a new secret for your service account user replaces any previous secret (which cannot be used once a new one is generated). Make a note of the secret and keep it in a secured location.

## Authenticate with a service account via the REST API
Create a service account with  `IS_ORGANIZATION_ADMIN` set, obtain the service account ID and secret either using UI or SQL.
One can set  `IS_ORGANIZATION_ADMIN` for a service account only using SQL:
```sql
ALTER SERVICE ACCOUNT sa1 SET IS_ORGANIZATION_ADMIN = true
```

Next, to authenticate Firebolt using service accounts via Firebolt’s REST API, 
send the following request to receive an authentication token:

```bash
curl POST --location 'https://id.app.firebolt.io/oauth/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=client_credentials' \
--data-urlencode 'audience=https://api.firebolt.io' \
--data-urlencode 'client_id={service account id}' \
--data-urlencode 'client_secret={service account secret}'
```

**Response:**
```json
{
  "access_token":"eyJz93a...k4laUWw",
  "token_type":"Bearer",
  "expires_in":86400
}
```

where:

| Property                          | Data type | Description                                                                                |
| :------------------------------   | :-------- |:-------------------------------------------------------------------------------------------|
| id                                | TEXT      | The service account ID ([created here](#creating-a-service-account)).                      |
| secret                            | TEXT      | The service account secret ([generated here](#generating-a-secret-for-a-service-account)). |


Use the returned access_token to authenticate with Firebolt.

## Editing a service account 

### SQL 
To edit a service account using SQL, use the [`ALTER SERVICE ACCOUNT`](../../sql_reference/commands/access-control/alter-service-account.md) statement. For example:

```sql
ALTER SERVICE ACCOUNT sa1 SET NETWORK_POLICY_NAME = my_network_policy
```
or: 
```sql
ALTER SERVICE ACCOUNT sa1 SET IS_ORGANIZATION_ADMIN = true
```

### UI 
To edit a service account via the UI:

1. Click **Configure** to open the configure space, then choose **Service accounts** from the menu.
2. Search for the relevant service account using the top search filters, or by scrolling through the list of service accounts. Hover over the right-most column to make the service account menu appear, then choose **Edit service account**.
3. Edit the desired fields and choose **Save**.

{: .caution}
The `is_organization_admin` property of a service account cannot be seen or edited in the UI.

## Deleting a service account 

### SQL 
To delete a service account using SQL, use the [`DROP SERVICE ACCOUNT`](../../sql_reference/commands/access-control/drop-service-account.md) statement. For example:

```sql
DROP SERVICE ACCOUNT sa1;
```

### UI 
To delete a service account via the UI:
1. Click **Configure** to open the configure space, then choose **Service accounts** from the menu.
2. Search for the relevant service account using the top search filters, or by scrolling through the list of service accounts. Hover over the right-most column to make the service account menu appear, then choose **Delete service account**.

If the service account is linked to users, you will need to confirm that you will also be deleting those users by choosing **Delete users permanently**.





