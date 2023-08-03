---
layout: default
title: Managing logins
description: Learn about user permissions and how to add and remove logins in a Firebolt account.
nav_order: 3
parent: Managing your organization
grand_parent: Guides
---

# Managing logins
{: .no_toc}

< Say something about what level logins live at (is it org or account?) and about how logins must be linked to users. > To view all logins, click **Configure** to open the configure space, then choose **Logins** from the menu, or query the [information_schema.logins](../../Reference/information-schema/logins.md) view. 

You can add, edit or delete logins using SQL or in the UI. 

### Create a new login

{: .note}
Creating a login requires the org_admin role.

#### SQL 
To create a login using SQL, use the [`CREATE LOGIN`] statement. For example:

```
CREATE LOGIN "alexs@acme.com" WITH FIRST_NAME = "Alex" LAST_NAME = "Summers";
```

#### UI
To create a login via the UI:
1. Click **Configure** to open the configure space, then choose **Accounts** from the menu:

< screenshot >

2. From the Logins page, choose **Create Login**.
3. Enter the following details:
    - First name: specifies the first name of the user that uses the login. 
    - Last name: specifies the last name of the user that uses the login.
    - Login name: specifies the login in the form of an email address. This must be unique within your organization.
4. Optionally, you can:
    - Associate a [network policy] with the login by choosing a network policy name under the network policy attached field.
    - Enable password log, which specifies if the login can authenticate Firebolt using a password.
    - Enable MFA. Read more about how to use MFA [here].
    - Set the login as org_admin, which enables fully managing the organization.


### Edit an existing login

{: .note}
Editing a login requires the org_admin role.

#### SQL 
To edit an existing login using SQL, use the [`ALTER LOGIN`] statement. For example:

```
ALTER LOGIN "alexs@acme.com" SET IS_ORGANIZATION_ADMIN = True;
```

#### UI
To edit a login via the UI:
1. Click **Configure** to open the configure space, then choose **Logins** from the menu:

< screenshot >

2. Search for the relevant login using the top search filters, or by scrolling through the list of logins. Hover over the right-most column to make the login menu appear, then choose **Edit login**.
Edit the required fields and choose **Save**.

### Deleting an existing login

{: .note}
Deleting a login requires the org_admin role.

#### SQL 
To delete an existing login using SQL, use the [`DROP LOGIN`] statement. For example:

```
DROP LOGIN "alexs@acme.com";
```

#### UI
To delete a login via the UI:
1. Click **Configure** to open the configure space, then choose **Logins** from the menu:

< screenshot >

2. Search for the relevant login using the top search filters, or by scrolling through the logins list. Hover over the right-most column to make the login menu appear, then choose **Delete login**.

If the login is linked to users, you will need to confirm that you will also be deleting those users by choosing **Delete users permanently**.
