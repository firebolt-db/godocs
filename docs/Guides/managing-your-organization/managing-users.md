---
redirect_from:
  - /managing-your-account/managing-users.html
layout: default
title: Manage users and roles
description: Learn about user permissions and how to add and remove users in a Firebolt account.
nav_order: 8
parent: Manage organization
---

# Manage users and roles
{: .no_toc}

In Firebolt, an **organization** can have multiple **accounts**, each serving as a separate workspace for managing resources and data. Within each account, users are created to control access, with their identities defined through logins or service accounts. **Logins** are associated with individual human users, each authenticated by unique credentials, allowing them to interact directly with Firebolt's resources according to assigned roles. **Service accounts** provide programmatic access for applications and automated processes within the account, such as data pipelines or monitoring tools. Each login and service account is linked to specific **roles**, which define their permissions, ensuring that access is managed efficiently and securely across the organization.

## <img src="../../assets/images/icon-login.png" alt="Icon for a Firebolt login for human access." width="30"/> Logins

A **login** in Firebolt represents a **human user** and is associated with an individual’s credentials, identified by an **email address**. Logins are tied to user roles, which define what the individual can access or modify. A login is primarily used for human authentication and allows a user to access the platform, run queries, and interact with databases and other resources. For instance, a login object might be created for a specific person such as `kate@acme.com`, and this login is linked to roles that control permissions.

## <img src="../../assets/images/icon-service-account.png" alt="Icon for a Firebolt service account for programmatic access." width="30"/> Service accounts

A **service account** represents a **machine or application** rather than a human user. It allows automated processes to authenticate and interact with Firebolt resources. A service account is used for programmatic access, such as in pipelines, monitoring systems, application data access, and scheduled queries. Service accounts are associated with roles just like logins but are designed to operate without human intervention. For example, a service account might be used for a data pipeline that regularly ingests data into Firebolt. Each service account must be associated with a user. For more information about how to create and manage service accounts, see [Manage programmatic access to Firebolt]({% link Guides/managing-your-organization/service-accounts.md %}).

## <img src="../../assets/images/icon-user-bangs.png" alt="Icon for a Firebolt user." width="30"/> Users

 A **user** is a distinct identity that interacts with the Firebolt platform. Each user is assigned specific **roles**, which determine what actions they can perform and which resources they can access. Users are essential for controlling access in Firebolt and are managed through **role-based access control (RBAC)**. Users authenticate via **logins** or **service accounts**, depending on whether they are human users or machine-based processes.

 A user must be associated with **either** a login or a service account, as follows:

<img src="../../assets/images/user_login_service-account.png" alt="A user must be associated with either a login or a service account." width="500">


There can be multiple users per login or service account. Users are managed at the account level, as shown in the following diagram:

<img src="../../assets/images/multiple-users-per-login-or-sa.png" alt="There can be multiple users per login, for human access, or per service account, for programmatic access" width="500">

You can [add](#set-up-a-new-user), [edit](#edit-an-existing-user) or [delete](#deleting-an-existing-user) users using SQL in the **Develop Space** or using the user interface (UI) in the **Configure Space**.

{: .note}
Managing roles requires the account_admin role. For more information about roles, see the [Roles]({% link Overview/organizations-accounts.md %}#roles) section in [Organizations and accounts]({% link Overview/organizations-accounts.md %}), and the [Account permissions]({% link Overview/Security/Role-Based Access Control/account-permissions.md %})  section of [Role-based access control]({% link Overview/Security/Role-Based Access Control/index.md %}) that specifies permissions for **CREATE USER**.

**Topics**
- [Manage users and roles](#manage-users-and-roles)
  - [ Logins](#-logins)
  - [ Service accounts](#-service-accounts)
  - [ Users](#-users)
  - [Set up a new user](#set-up-a-new-user)
    - [Set up a new user for programmatic access](#set-up-a-new-user-for-programmatic-access)
    - [Set up a new user for human access](#set-up-a-new-user-for-human-access)
      - [Create a login](#create-a-login)
        - [Create a login using the UI](#create-a-login-using-the-ui)
        - [Create a login using SQL](#create-a-login-using-sql)
      - [Create a user](#create-a-user)
        - [Create a user using the UI](#create-a-user-using-the-ui)
        - [Create a user using SQL](#create-a-user-using-sql)
      - [Link the user to the login or service account](#link-the-user-to-the-login-or-service-account)
        - [Link a user using the UI](#link-a-user-using-the-ui)
        - [Link a user using SQL](#link-a-user-using-sql)
      - [Create a role](#create-a-role)
        - [Create a role using the UI](#create-a-role-using-the-ui)
        - [Create a role using SQL](#create-a-role-using-sql)
      - [Assign a role to a user](#assign-a-role-to-a-user)
        - [Assign a role using the UI](#assign-a-role-using-the-ui)
        - [Assign a role using SQL](#assign-a-role-using-sql)
  - [Edit an existing user](#edit-an-existing-user)
    - [Edit a user using the UI](#edit-a-user-using-the-ui)
    - [Edit a user using SQL](#edit-a-user-using-sql)
  - [Deleting an existing user](#deleting-an-existing-user)
    - [Delete a user using the UI](#delete-a-user-using-the-ui)
    - [Delete a user using SQL](#delete-a-user-using-sql)


## Set up a new user

To set up a new user, complete the following steps:

1.  Create a new login or service account. The following section provides information about creating a new login, for human access to Firebolt. If you want to set up a new user for programmatic access, see [Create a service account]({% link Guides/managing-your-organization/service-accounts.md %}#create-a-service-account).
2. Create a new user.
3. Link the user with a login or a service account.
4. Create a role.
5. Assign the role to the user.

The following sections guide you through the previous steps.

### Set up a new user for programmatic access

<img src="../../assets/images/workflow-new-user-sa.png" alt="To set up a new user for programmatic access, first set up a service account." width="700" >

To set up a user for programmatic access, [create a service account]({% link Guides/managing-your-organization/service-accounts.md %}#create-a-service-account), and then complete the steps in the following sections to [create a user](#create-a-user), [link the user](#link-the-user-to-the-login-or-service-account) to a service account, [create a role](#create-a-role), and [assign the role](#assign-a-role-to-a-user) to the user.

### Set up a new user for human access

#### Create a login
<img src="../../assets/images/workflow-new-user-create-login.png" alt="To set up a user for human access, first create a login." width="700">

A login is an **email** that is used for authentication. A login can be associated with multiple accounts. When you set up a new user, you must create either a login or service account for them. Create a login if you want to associate a user with human access to Firebolt. [Create a service account]({% link Guides/managing-your-organization/service-accounts.md %}#create-a-service-account) for programmatic access. You will link the user to **either** a login or a service account.

##### Create a login using the UI

Login to [Firebolt’s Workspace](https://go.firebolt.io/login). If you haven’t yet registered with Firebolt, see the [Get Started]({% link Guides/getting-started/index.md %}) guide. If you encounter any issues, reach out to [support@firebolt.io](mailto:support@firebolt.io) for help. Then, do the following:

1. Select the Configure icon (<img src="../../assets/images/configure-icon.png" alt="The Firebolt Configure Space icon." width="12"/>) in the left navigation pane to open the **Configure Space**.
2. Select **Logins**.
3. Select **Create Login**.
4. In the **Create login** window that pops up, enter the following:
  
    1. First Name - The first name of the user.
    2. Last Name - The last name of the user.
    3. Login Name - The email address of the user.

5. Select a network policy from the drop-down list. You can choose **Default** or create your own. The default network policy accepts traffic from any IP address. For more about network policies, including how to create a new policy, see [Manage network policies]({% link Guides/security/network-policies.md %}).
6. Toggle the following options on or off to select the following:

    1. Is password enabled - Toggle **on** to require authentication using a password.
    2. Is MFA enabled - Toggle **on** to require authentication using multi-factor authentication (MFA).
    3. Is organization admin - Toggle **on** to grant that login permissions associated with an **Organization Admin**. A user must have organization administrative privileges to manage logins and service accounts. For more information about organization administrative privileges and other roles, see the [Roles]({% link Overview/organizations-accounts.md %}#roles) section in [Organizations and accounts]({% link Overview/organizations-accounts.md %}).

7. Select **Create**.

##### Create a login using SQL

Login to [Firebolt’s Workspace](https://go.firebolt.io/login). If you haven’t yet registered with Firebolt, see the [Get Started]({% link Guides/getting-started/index.md %}) guide. If you encounter any issues, reach out to [support@firebolt.io](mailto:support@firebolt.io) for help. Then, do the following:

1. Select the **Develop** icon (<img src="../../assets/images/develop-icon.png" alt="The Firebolt Develop Space icon" width="12"/>).

    By default, when you login to **Firebolt’s Workspace** for the first time, Firebolt creates a tab in the **Develop Space** called **Script 1**. The following apply:

    * The database that **Script 1** will use is located directly below the tab name. If you want to change the database, select another database from the drop-down list.

    * An engine must be running to process the script in a selected tab. The name and status of the engine that **Script 1** uses for computation is located to the right of the current selected database. If the engine has auto-start set to `TRUE`, it will start from a stopped state. For more information about auto-start, see [Immediately Starting or Automatically Stopping an Engine]({% link Guides/operate-engines/working-with-engines-using-ddl.md %}#automatically-start-or-stop-an-engine). 

3. Select **system** from the drop-down arrow next to the engine name. The system engine is always running, and you can use it to create a login. You can also use an engine that you create.
4. Use the syntax in the following example code to create a login in the SQL Script Editor:

    ```sql
    CREATE LOGIN "<login_name>"
    WITH FIRST_NAME = <first_name> 
    LAST_NAME = <last_name>;
    ```

#### Create a user

<img src="../../assets/images/workflow-new-user-create-user.png" alt="To set up a new user, after you create a login, create a user." width="700">

After you create a login, the next step is to create a user.

##### Create a user using the UI

1. Select the **Govern** icon (<img src="../../assets/images/govern-icon.png" alt="The Firebolt Govern Space icon." width="12"/>) in the left navigation pane to open the **Govern Space**.
2. Select **Users** from the left sub-menu bar.
3. Select the **+ Create User** button at the top right of the **Govern Space**.
4. In the **Create User** window, enter the following:

   1. **User name** - The name of the user to associate with the login. This name can be any string, excluding spaces, and special characters such as exclamation points (!), percent signs (%), at sign(@), dot sign (.), underscore sign (_), minus sign (-), and asterisks (*).

   2. **Assign to** - Use the dropdown to assign the user to one of the following:  
      i. **Unassigned** - No specific assignment.

      ii. **Login** - Associates the user with a login name or email address. After selecting this option, you will be prompted to choose the login name or email address.

      iii. **Service Account** - Associates the user with a service account. After selecting this option, you will be prompted to choose a service account name.
   1. **Role** - Select the role you want to assign to the user. If no role is specified, the user is automatically granted a [public role]({% link Overview/organizations-accounts.md %}#public-role). For more information about roles, see the [Roles]({% link Overview/organizations-accounts.md %}#roles) section in [Organization and accounts]({% link Overview/organizations-accounts.md %}).

   2. **Default Database** - Choose a database to associate with the user, setting it as their default for access.

   3. **Default Engine** - Choose a default processing engine to associate with the user.

5. Select **Create new user** to save the configuration. 


##### Create a user using SQL

Use the syntax in the following example code and the [CREATE USER]({% link sql_reference/commands/access-control/create-user.md %}) statement to create a user in the **SQL Script Editor** in the **Develop Space**:

```sql
CREATE USER <my_user>;
```

You can also create a user and link it to a login simultaneously as shown in the following code example:
```sql
CREATE USER <my_user> WITH LOGIN = "<my_login>";
```

Create a user and link it to a service account at the same time as shown in the following code example:

```sql
CREATE USER <my_user> WITH SERVICE_ACCOUNT=<my_service_account>
```

#### Link the user to the login or service account

<img src="../../assets/images/workflow-new-user-link-login.png" alt="To set up a new user, after you create a user, link it to the login or service account." width="700">

If the user wasn’t associated with a login or service account when they were created, you must link them.

##### Link a user using the UI

1. Select the Govern icon (<img src="../../assets/images/govern-icon.png" alt="The Firebolt Govern Space icon" width="12"/>) in the left navigation pane to open the **Govern Space**.
2. Select **Users** from the left sub-menu bar.
3. Select the three horizontal dots (…) to the right of the user that you need to link to a login.
4. Select **Edit user details**.
5. If you want to link the user to a login for human access, select **Login** from the drop-down list next to **Assign to**. If you want to link the user to a service account for programmatic access, select **Service Account** from the drop-down list next to **Assign to**.
6. If you want to link the user to a login for human access, select the name of the login to associate with the user from the drop-down list under **Login name**.  If you want to link the user to a service account for programmatic access, select a name from the drop-down list next to **Service account name**. This drop-down list contains only login accounts that are not already assigned to a user in the current account.
7. Select **Save**.

##### Link a user using SQL

Use the syntax in the following example code and the [ALTER_USER]({% link sql_reference/commands/access-control/alter-user.md %}) statement to link a user to a login in the **SQL Script Editor** in the **Develop Space**:

```sql
ALTER USER <my_user> SET LOGIN = "<login_name>";
```

The following code links a user to a service account:

```sql
ALTER USER <user_name> SET SERVICE_ACCOUNT = <service_account_name>
```

#### Create a role
<img src="../../assets/images/workflow-new-user-create-role.png" alt="To set up a new user, after you link the user, create a role." width="700">

If you don’t already have a role that you want to assign to a user, you can create a role to define what actions users can perform. For more information, see [Roles]({% link Overview/organizations-accounts.md %}#roles).

##### Create a role using the UI

1. Select the Govern icon (<img src="../../assets/images/govern-icon.png" alt="The Firebolt Govern Space icon." width="12"/>) in the left navigation pane to open the **Govern Space**.
2. Select **Roles** from the left sub-menu bar.
3. Select the **+ New Role** button at the top right of the **Govern Space**.
4. In the left sub-menu bar, enter the following:

    1. Role name - The name of the role that you want to create. You can use this role to grant privileges for more than one user.

5. Select **Databases** in the left sub-menu bar, and select the following in **Database privileges**:

    1. **Create database** - Toggle **on** to allow the user to create any database in the account.
    2. **Modify any database** - Toggle **on** to allow the user to modify any database in the account, or keep the option **off** to select the specific database the user can modify.
    3. **Usage any database** - Toggle **on** to allow the user to use any database in the account, or keep the option **off** to select the specific database the user can use.
    4. If you didn’t specify using or modifying all databases, select the checkbox next to the specific database that you want to grant the user access to modify or use.

6. Select **Engines** in the left sub-menu bar, and select the following in **Engine privileges**:

    1. **Create engine** - Toggle **on** to allow the user to create any engine in the account.
    2. **Modify any engine** - Toggle **on** to allow the user to modify any engine in the account, or keep the option **off** to select the specific engine the user can modify.
    3. **Operate any engine** - Toggle **on** to allow the user to stop or start any engine in the account, or keep the option **off** to select the specific engine the user can start or stop. Any running engine that is not the system engine accumulates usage costs.
    4. **Usage any engine** - Toggle **on** to allow the user to use any engine in the account, or keep the option **off** to select the specific engine the user can use.

7. Select **Create**.

##### Create a role using SQL

Use the syntax in the following example code and the [CREATE ROLE]({% link sql_reference/commands/access-control/create-role.md %}) and [GRANT]({% link sql_reference/commands/access-control/grant.md %}) statements to create a role in the **SQL Script Editor** in the **Develop Space**:

```sql
CREATE ROLE <my_role>;
```

Use the following code to grant engine **access to a role**:

```sql
GRANT USAGE ON ENGINE <engine_name> TO <role_name>
```

Use the following code example to grant a role permission to **modify a database**:

```sql
GRANT MODIFY ON DATABASE <database_name> TO <role_name>
```

Use the following code example to grant a role permission to **create objects inside the public schema**:

```sql
GRANT CREATE ON SCHEMA public TO <role_name>
```

Use the following code to grant a role permission to **access the public schema** in a database:

```sql
GRANT USAGE ON SCHEMA public TO <role_name>
```

Use the following code example to grant a role permission to **read data from a specified table**:

```sql
GRANT SELECT ON TABLE <table_name> TO <role_name>
```

For more information about role-based access, see [Manage role-based access control]({% link Guides/security/rbac.md %}).

#### Assign a role to a user
<img src="../../assets/images/workflow-new-user-assign.png" alt="To set up a new user, after creating a role, assign it to a user." width="700">

You can assign a new role to the user or change the role assigned to the user from the default **public** role to grant them specific permissions. A user can have multiple roles.

##### Assign a role using the UI

1. Select the Govern icon (<img src="../../assets/images/govern-icon.png" alt="The Firebolt Govern Space icon." width="12"/>) in the left navigation pane to open the **Govern Space**. 
2. Select **Users** from the left sub-menu bar.
3. Select the three horizontal dots (…) to the right of the user that you need to link to a login.
4. Select **Edit user details**.
5. Select the checkbox next to the role that you want to assign to the user from the list under **Assign Roles**.
6. Select **Save**.


##### Assign a role using SQL

Use the syntax in the following example code and the [GRANT]({% link sql_reference/commands/access-control/grant.md %}) statement to assign a role in the **SQL Script Editor** in the **Develop Space**:

```sql
GRANT <my_role> TO USER <my_user>;
```

You can use `GRANT` to assign a role to another role as follows:

```sql
GRANT <some_role> TO ROLE <another_role>
```

## Edit an existing user

You can alter a user's name, login or service account that they are associated with, their default database, and engine.

### Edit a user using the UI

1. Select the Govern icon (<img src="../../assets/images/govern-icon.png" alt="The Firebolt Govern Space icon." width="12"/>) in the left navigation pane to open the **Govern Space**. 
2. Select **Users** from the left sub-menu bar.
3. Select the three horizontal dots (…) to the right of the user that you need to edit.
4. Select **Edit user details**.
5. Edit the desired fields.
6. Select **Save**.

### Edit a user using SQL 

Use the [ALTER USER]({% link sql_reference/commands/access-control/alter-user.md %}) statement to change a user's information in the **SQL Script Editor** in the **Develop Space**. 

The following code example changes a user's name:

```sql
ALTER USER "alex" RENAME TO "alexs";
```

The following code example changes a user's login:

```sql
ALTER USER alex SET LOGIN="alexs@acme.com";
```

{: .note}
Users can modify most of their own account settings without requiring [RBAC]({% link Overview/Security/Role-Based Access Control/index.md %}#role-based-access-control-rbac) permissions, except when altering [LOGIN]({% link Guides/managing-your-organization/managing-logins.md %}) configurations or a [SERVICE ACCOUNT]({% link Guides/managing-your-organization/service-accounts.md %}).

## Deleting an existing user

You can delete a user using either the UI or with SQL. The delete operation is irreversible.

### Delete a user using the UI

1. Select **Users** from the left sub-menu bar.
2. Select the three horizontal dots (…) to the right of the user that you need to delete.
3. Select **Delete user**.
4. Select **Confirm** to delete the user. This operation is irreversible.


### Delete a user using SQL

Use the syntax in the following example code and the the [DROP USER]({% link sql_reference/commands/access-control/drop-user.md %}) statement to delete an existing user in the **SQL Script Editor** in the **Develop Space**:

```sql
DROP USER "alex";
```
