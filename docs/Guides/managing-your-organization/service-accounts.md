---
layout: default
title: Service accounts
description: Learn about creating service account users for Firebolt.
nav_order: 6
parent: Manage organization
---

# Set up programmatic access to Firebolt
{: .no_toc}

Service accounts in Firebolt are used exclusively for **programmatic access**, allowing applications and automated systems to securely interact with Firebolt resources. Service accounts are specifically designed for applications, scripts, or automated processes that require continuous or recurring access to Firebolt resources. They are different from regular user accounts, which are for individuals. Each service account has both an ID and a secret, used for authentication.

{: .note}
You must have the **organization admin** role to manage service accounts. In Firebolt, the org_admin role grants administrative privileges over the entire organization. This role allows users to manage critical organization-wide settings, including creating and managing service accounts, users, roles, network policies, and other administrative tasks. The org_admin has comprehensive control to ensure proper access management and security within the organization. This role is essential for those overseeing Firebolt's infrastructure and ensuring compliance with the organization's security policies.

Administrators use service accounts to control how external tools and applications access Firebolt, ensuring access is limited to necessary resources. Service accounts are linked to specific users within the organization, giving administrators control over what data and permissions they have. This helps enforce security rules, track usage, and audit system access in a clear and controlled way.

You can access a Firebolt database programmatically using either of the following:

*  The [Firebolt API](https://docs.firebolt.io/godocs/Guides/query-data/using-the-api.html#firebolt-api) - directly interacts with Firebolt’s data warehouse using HTTP requests.
*  The [Firebolt drivers](https://docs.firebolt.io/godocs/Guides/developing-with-firebolt/) - use a third party tool or programming language to integrate with Firebolt’s data warehouse. Firebolt supports several languages including Python, Node, .Net, and Go.

Service accounts must be linked to a [user account](https://docs.firebolt.io/godocs/Guides/managing-your-organization/managing-users.html). The Service account provides access to the organization, and the associated user provides access to an account within the organization. To use Firebolt programmatically, you must authenticate with an ID and a secret. These are generated when you create a service account. You can add, delete and generate secrets for service accounts using SQL scripts in the Develop Space or through the user interface (UI) in the Configure Space. 

Follow these steps to gain programmatic access to Firebolt:

1. Create a service account
    You can create a service account using SQL scripts in the **Develop Space** or through the user interface (UI) in the **Configure Space**.

    **Create a service account using the UI**
    Login to Firebolt’s [Workspace](https://go.firebolt.io/login). If you haven’t yet registered with Firebolt, see the [Get Started guide](https://docs.firebolt.io/Guides/getting-started/). If you encounter any issues, reach out to support@firebolt.io for help. Then, do the following:

    1. Select the Configure icon () in the left navigation pane to open the Configure Space. 
    2.  Select Service accounts on the left sub-menu bar.
    3. Select the **+ Create a service account** button at the top right of the **Configure Space**.
    4. In the **Create a service account** window that appears, enter the following:
        *  Name - The name of the service account. 
        * Network policy - A security feature that defines a list of allowed and blocked IP addresses or ranges to manage access at the organization level, login level, or for service accounts. For more information, see [Manage network policies](https://docs.firebolt.io/Guides/security/network-policies.html).
        * Description - A descriptor of the service account.
    5. Toggle **Is organization admin** to designate the service account as an account with administrative privileges in your organization. In Firebolt, the org_admin role provides full administrative privileges over the organization, allowing management of users, service accounts, network policies, and other organization-wide settings.
    6. Select **Create** to finish creating the service account.


## Creating a service account 

### SQL 
To create a service account using SQL, use the [CREATE SERVICE ACCOUNT](../../sql_reference/commands/access-control/create-service-account.md) statement. For example:

```sql
CREATE SERVICE ACCOUNT IF NOT EXISTS "sa1" WITH DESCRIPTION = 'service account 1';
```

### UI
To create a service account via the UI:

![Configure > Service accounts](../../assets/images/serviceaccountspage.png)

1. Click **Configure** to open the configure space, then choose **Service accounts** from the menu.
2. From the Service accounts page, choose **Create a service account**.
3. Enter a unique name for your service account. This name must start with a letter, and may contain only alphanumeric characters, or the underscore(_) character.
4. Optionally, you can:
  - Choose a **network policy** to apply from the list of existing [network policies](../security/network-policies.md) configured for your organization. 
  - Specify a description for the service account.
  - Set the service account as organisation admin, which enables fully managing the organization.
5. Choose **Create**. 

{: .note}
At this point, it's required to create a user and associate the service account to it. 

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
3. The **New secret for service account** menu with the newly generated secret will appear.

<img src="../../assets/images/newsecret.png" alt="New secret" width="500"/>

**Make a note of the secret once generated** - it can't be retrieved later.  If the secret is lost (or needs to be rotated), you can always generate a new secret, calling the same generation function, or by creating a new secret in the UI. 

{: .note}
Generating a new secret for your service account user replaces any previous secret (which cannot be used once a new one is generated). Make a note of the secret and keep it in a secured location.

## Authenticate with a service account via the REST API
1. Create a service account with the `IS_ORGANIZATION_ADMIN` property set to `TRUE` using either the UI or SQL. 
2. Obtain the service account ID and secret. 
3. Create a user and assign desired roles for the service account. Link the service account with this created user. 
4. Authenticate using the service account via Firebolt’s REST API, send the following request to receive an authentication token:

```bash
curl -X POST --location 'https://id.app.firebolt.io/oauth/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=client_credentials' \
--data-urlencode 'audience=https://api.firebolt.io' \
--data-urlencode "client_id=${service_account_id}" \
--data-urlencode "client_secret=${service_account_secret}"
```

**Response:** # ignore Response
```json
{
  "access_token":"eyJz93a...k4laUWw",
  "token_type":"Bearer",
  "expires_in":86400
}
```

where:

| Property               | Data type | Description                                                                                |
|:-----------------------| :-------- |:-------------------------------------------------------------------------------------------|
| service account id     | TEXT      | The service account ID ([created here](#creating-a-service-account)).                      |
| service account secret | TEXT      | The service account secret ([generated here](#generating-a-secret-for-a-service-account)). |


Use the returned access_token to authenticate with Firebolt.

## Editing a service account 

### SQL 
To edit a service account using SQL, use the [ALTER SERVICE ACCOUNT](../../sql_reference/commands/access-control/alter-service-account.md) statement. For example:

```sql
ALTER SERVICE ACCOUNT sa1 SET NETWORK_POLICY = my_network_policy
```

### UI 
To edit a service account via the UI:

1. Click **Configure** to open the configure space, then choose **Service accounts** from the menu.
2. Search for the relevant service account using the top search filters, or by scrolling through the list of service accounts. Hover over the right-most column to make the service account menu appear, then choose **Edit service account**.
3. Edit the desired fields and choose **Save**.

## Deleting a service account 

### SQL 
To delete a service account using SQL, use the [DROP SERVICE ACCOUNT](../../sql_reference/commands/access-control/drop-service-account.md) statement. For example:

```sql
DROP SERVICE ACCOUNT sa1;
```

### UI 
To delete a service account via the UI:
1. Click **Configure** to open the configure space, then choose **Service accounts** from the menu.
2. Search for the relevant service account using the top search filters, or by scrolling through the list of service accounts. Hover over the right-most column to make the service account menu appear, then choose **Delete service account**.
{: .note}
If the service account is linked to any users, deletion will not be permitted. The service account must be unlinked from all users before deletion. 





