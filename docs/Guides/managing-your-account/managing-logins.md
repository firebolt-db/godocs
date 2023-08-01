---
layout: default
title: Managing logins
description: Learn about user permissions and how to add and remove logins in a Firebolt account.
nav_order: 3
parent: Managing your organization
grand_parent: Guides
---

# Managing Firebolt users
{: .no_toc}

## Managing users

### Create a new user

{: .note}
Creating a user requires the account_admin or security_admin roles.

Creating new users in your account can be done in two ways - using SQL or the UI. To create a user using SQL, use the [`CREATE USER`] statement. For example:

```sql
CREATE USER "john";
```

To create a user via the UI:
1. Click **Govern** to open the govern space, then choose **Users** from the menu:

2. From the users management page, choose **Create user**.
3. Enter the new user's name. This user name can be any string - it can contain spaces, and non-alpha-numeric characters such as exclamation points (!), percent signs (%), at sign(@), dot sign (.), underscore sign (_), minus sign (-), and asterisks (*), but if the string contains these spaces or non-alphanumeric characters, it must be enclosed in single or double quotes. 

4. Optionally, you can:
  - Choose **Associate a login** or **Associate a service account**, then choose the relevant login/service account from the list.
  - Choose a **default database** for the user.
  - Choose a **default engine** for the user. 
  - Choose **roles** to be granted to the user. 

### Edit an existing user

{: .note}
Editing a user requires the account_admin or security_admin roles.

Editing an existing user in your account can be done in two ways - using SQL or the UI. To edit an existing user using SQL, use the [`ALTER USER`] statement. For example:

```sql
ALTER USER "john" rename to "john_new";
```


To edit a user via the UI:
1. Click **Govern** to open the govern space, then choose **Users** from the menu:

2. Search for the relevant user using the top search filters or by scrolling through the users' list. Hover over the right-most column and choose  then choose **Edit user**.
3. Edit the desired fields and choose **Save**.


### Deleting an existing user

{: .note}
Deleting a user requires the account_admin or security_admin roles.

Deleting an existing user in your account can be done in two ways - using SQL or the UI. To delete an existing user using SQL, use the [`DROP USER`] statement. For example:

```sql
DROP USER "john";
```

To delete a user via the UI:
1. Click **Govern** to open the govern space, then choose **Users** from the menu:

2. Search for the relevant user using the top search filters or by scrolling through the users list. Hover over the right-most column and choose  then choose **Delete user**.
3. Choose Confirm.


### List users

{: .note}
Listing users requires the account_admin or security admin roles. 

Listing the users in your account can be done in two ways - using SQL or the UI. To list users using SQL, query the [information_schema.users] view:

```sql
SELECT * FROM information_schema.users;
```

To list users via the UI, click **Govern** to open the govern space, then choose **Users** from the menu.