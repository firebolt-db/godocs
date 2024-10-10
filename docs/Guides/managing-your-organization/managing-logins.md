---
layout: default
title: Manage logins
description: Learn about user permissions and how to add and remove logins in a Firebolt account.
nav_order: 5
parent: Manage organization
---

# Manage logins
{: .no_toc}

Logins are managed at the organization level and are used for authentication. Logins are a combination of a login name (email), first name, last name, and password, unless you've configured [Single Sign-On (SSO)](../security/sso/sso.md). Moreover, logins can be configured with advanced authentication properties such as [MFA](../security/enabling-mfa.md) and [network policies](../security/network-policies.md). Logins are linked to users at the account level, so that roles may be managed separately per account. A user must be linked to either a login or a service account for programmatic use to gain access to Firebolt. You can add, edit or delete logins using SQL or in the UI. 

To view all logins, click **Configure** to open the configure space, then choose **Logins** from the menu, or query the [information_schema.logins](../../sql_reference/information-schema/logins.md) view. 

{: .note}
Managing logins requires the org_admin role.

## Create a new login

### SQL 
To create a login using SQL, use the [CREATE LOGIN](../../sql_reference/commands/access-control/create-login.md) statement. For example:

```sql
CREATE LOGIN "alexs@acme.com" WITH FIRST_NAME = 'Alex' LAST_NAME = 'Summers';
```

### UI
To create a login via the UI:
1. Click **Configure** to open the configure space, then choose **Logins** from the menu:

![Configure > Logins](../../assets/images/loginspage.png)

2. From the Logins management page, choose **Create Login**.
3. Enter the following details:
    - First name: specifies the first name of the user for the login. 
    - Last name: specifies the last name of the user for the login.
    - Login name: specifies the login in the form of an email address. This must be unique within your organization.
4. Optionally, you can:
    - Associate a [network policy](../security/network-policies.md) with the login by choosing a network policy name under the **Network policy attached** field.
    - Enable password login, which specifies if the login can authenticate Firebolt using a password.
    - Enable multi-factor authentication (MFA). Read more about how to configure MFA [here](../security/enabling-mfa.md).
    - Set the login as **organisation admin**, which enables fully managing the organization.

## Edit an existing login

### SQL 
To edit an existing login using SQL, use the [ALTER LOGIN](../../sql_reference/commands/access-control/alter-login.md) statement. For example:

```sql
ALTER LOGIN "alexs@acme.com" SET NETWORK_POLICY = my_network_policy
```

### UI
To edit a login via the UI:
1. Click **Configure** to open the configure space, then choose **Logins** from the menu.

2. Search for the relevant login using the top search filters, or by scrolling through the list of logins. Hover over the right-most column to make the login menu appear, then choose **Edit login details**.
Edit the desired fields and choose **Save**.

{: .note}
Login name can not be changed for logins that were provisioned via SSO.

<img src="../../assets/images/editlogin.png" alt="Edit login" width="500"/>

## Deleting an existing login

### SQL 
To delete an existing login using SQL, use the [DROP LOGIN](../../sql_reference/commands/access-control/drop-login.md) statement. For example:

```sql
DROP LOGIN "alexs@acme.com";
```

### UI
To delete a login via the UI:
1. Click **Configure** to open the configure space, then choose **Logins** from the menu.

2. Search for the relevant login using the top search filters, or by scrolling through the logins list. Hover over the right-most column to make the login menu appear, then choose **Delete login**.
{: .note}
If the login is linked to any users, deletion will not be permitted. The login must be unlinked from all users before deletion.
