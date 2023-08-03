---
layout: default
title: Managing users
description: Learn about user permissions and how to add and remove users in a Firebolt account.
nav_order: 6
parent: Managing your organization
grand_parent: Guides
---

# Managing Firebolt users
{: .no_toc}

< Say something about what level users live at (is it org or account?) and about how users can be linked to logins or service accounts.> To view all users, click **Govern** to open the govern space, then choose **Users** from the menu, or query the [information_schema.users](../../Reference/information-schema/users.md) view. 

You can add, edit or delete users using SQL or in the UI. 

### Create a new user

{: .note}
Creating a user requires the account_admin or security_admin role.

#### SQL 
To create a user using SQL, use the [`CREATE USER`] statement. For example:

```
CREATE USER "john";
```

#### UI
To create a user via the UI:
1. Click **Govern** to open the govern space, then choose **Users** from the menu:

< screenshot >

2. From the Users page, choose **Create user**.
3. Enter the new user's name. This user name can be any string - it can contain spaces, and non-alpha-numeric characters such as exclamation points (!), percent signs (%), at sign(@), dot sign (.), underscore sign (_), minus sign (-), and asterisks (*), but if the string contains these spaces or non-alphanumeric characters, it must be enclosed in single or double quotes. 

4. Optionally, you can:
  - Choose **Associate a login** or **Associate a service account**, then choose the relevant login/service account from the list.
  - Choose a **default database** for the user.
  - Choose a **default engine** for the user. 
  - Choose **roles** to be granted to the user. 

### Edit an existing user

{: .note}
Editing a user requires the account_admin or security_admin role.

#### SQL 
To edit an existing user using SQL, use the [`ALTER USER`] statement. For example:

```
ALTER USER "john" rename to "john_new";
```

#### UI
To edit a user via the UI:
1. Click **Govern** to open the govern space, then choose **Users** from the menu:

< screenshot >

2. Search for the relevant user using the top search filters or by scrolling through the users' list. Hover over the right-most column to make the user menu appear,then choose **Edit user**.
3. Edit the desired fields and choose **Save**.


### Deleting an existing user

{: .note}
Deleting a user requires the account_admin or security_admin role.

#### SQL 
To delete an existing user using SQL, use the [`DROP USER`] statement. For example:

```
DROP USER "john";
```

#### UI
To delete a user via the UI:
1. Click **Govern** to open the govern space, then choose **Users** from the menu:

< screenshot >

2. Search for the relevant user using the top search filters or by scrolling through the users list. Hover over the right-most column to make the user menu appear, then choose **Delete user**.
3. Choose **Confirm**.
