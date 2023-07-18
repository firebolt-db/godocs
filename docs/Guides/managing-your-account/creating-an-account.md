---
layout: default
title: Registering to Firebolt
description: Learn how to create an organization. 
nav_order: 2
parent: Account and user management
grand_parent: Guides
---

# Registration to Firebolt 

To start working with Firebolt, you first need to register and create your organization and first account. Read more about organization and accounts and their benefits [here](../../Overview/organizations-accounts.md).

An organization provides a logical structure for managing accounts, billing, and authentication. When registering to Firebolt, the organization name is the same as the organizational domain name you use in your email. Organization names are globally unique—no two organizations can have the same name. If you need two organizations under the same organization domain - contact the Firebolt support team for further assistance.

## Create an organization
To register to Firebolt and create an organization:
1. Go to Firebolt’s registration page: [go.firebolt.io/signup](go.firebolt.io/signup)
2. Enter the following information in the form:
First name
Last name
Email - make sure you use a business email address. Based on that, we infer the name of your company and organization.
Region in which to create your first account (you can create additional accounts in additional regions later).
3. Click on Register.
An email is sent to the email address provided in step 2 above to verify the organization. When this email is received, click on Activate. 
4. To move on to the next step, Firebolt needs to approve your registration request and validate your information. This step could take a couple of minutes to complete. Once approved - you will get a welcome email. 5. Click on Go to Firebolt in this email.
A page for choosing a password will be presented. Enter your password as instructed and choose Set password. 
6. Choose Log in
Enter your login information (email address and password) and click Log in.

Congratulations - you have successfully set up your organization. Welcome to Firebolt! 

Next steps:
- Choose a name for your first account (you can also keep the default name).
- Add users to your account (create logins, users, and manage roles ).
- Create databases, engines, and load your data. Follow our [getting started tutorial](../getting-started.md) to try this out with sample data.

## Managing accounts
Your organization comes prepared with one account for your convenience. To add more accounts or edit existing ones: 
Create new account
Creating an account requires the OrgAdmin role.

Creating new accounts in your organization can be done in two ways - using SQL or the UI. To create an account using SQL, use the CREATE ACCOUNT statement. For example:
CREATE ACCOUNT my_account WITH REGION = “us-east-1”;


To create an account via the UI:
Click on the Configure button to open the configure space, then choose Accounts from the menu:

From the accounts management page, choose Create Account.
Type a name for the account and choose a region for it. You can’t change the region later.

Choose Create. 

Firebolt adds the account to the account management page.
Edit an existing account
Edit an account requires the AccountAdmin or OrgAdmin roles.

Editing an existing account in your organization can be done in two ways - using SQL or the UI. To edit an existing account using SQL, use the ALTER ACCOUNT statement. For example:
ALTER ACCOUNT my_account RENAME TO my_dev_account;


To edit an account via the UI:
Click on the Configure button to open the configure space, then choose Accounts from the menu:

Search for the relevant account using the top search filters or by scrolling through the accounts list. Hover over the right-most column and choose  then choose Edit account.
Edit the name of the account:

You can also see additional details on the accounts, such as region, account ID, and URL. These details are read-only.
Choose Save. 
Delete an existing account
Deleting an account requires the AccountAdmin or OrgAdmin roles.

Deleting an existing account in your organization can be done in two ways - using SQL or the UI. To delete an existing account using SQL, use the DROP ACCOUNT statement. For example:
DROP ACCOUNT my_account;


To delete an account via the UI:
Click on the Configure button to open the configure space, then choose Accounts from the menu:

Search for the relevant account using the top search filters or by scrolling through the accounts list. Hover over the right-most column and choose  then choose Delete account. 
If your account is not empty (contains other objects such as users/databases/engines/etc.), you will need to confirm that you will also delete the sub-objects by selecting Delete account sub-objects permanently.

Choose Confirm.

The account will be removed from the accounts management page (with all the sub-objects it contained).
