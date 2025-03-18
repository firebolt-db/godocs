---
layout: default
title: DBeaver
description: Configure DBeaver to connect to Firebolt using the JDBC driver.
nav_order: 15
parent: Integrate with Firebolt
---

# Integrate with DBeaver
{: .no_toc}

<img src="../../assets/images/DBeaver-logo.png" alt="DBeaver logo" width="100"/>

DBeaver is a free, open-source database administration tool that supports multiple database types. It provides a graphical interface for managing databases, running queries, and analyzing data. DBeaver is widely used for database development, troubleshooting, and administration, making it a versatile choice for both developers and database administrators. You can connect DBeaver to Firebolt using the [Firebolt JDBC driver]({% link Guides/developing-with-firebolt/connecting-with-jdbc.md %}).

* Topic ToC
{:toc}

## Prerequisites
You must have the following prerequisites before you can connect your Firebolt account to DBeaver:

- **Firebolt account** &ndash; You need an active Firebolt account. If you do not have one, you can [sign up](https://go.firebolt.io/signup) for one.
- **Firebolt database and engine** &ndash; You must have access to a Firebolt database. If you do not have access, you can [create a database]({% link Guides/getting-started/get-started-sql.md %}#create-a-database) and then [create an engine]({% link Guides/getting-started/get-started-sql.md %}#create-an-engine).
- **Firebolt service account** &ndash; You must have an active Firebolt [service account]({% link Guides/managing-your-organization/service-accounts.md %}) for programmatic access, along with its ID and secret.
- **Sufficient permissions** &ndash; Your service account must be [associated]({% link Guides/managing-your-organization/service-accounts.md %}#create-a-user) with a user. The user should have [USAGE]({% link Overview/Security/Role-Based Access Control/database-permissions/index.md %}) permission to query your database, and [OPERATE]({% link Overview/Security/Role-Based Access Control/engine-permissions.md %}) permission to start and stop an engine if it is not already started. It should also have at least USAGE and SELECT [permissions]({% link Overview/Security/Role-Based Access Control/database-permissions/schema-permissions.md %}) on the schema you are planning to query.
- **DBeaver installed** &ndash; You must have downloaded and installed [DBeaver](https://dbeaver.io/download/).

## Add the Firebolt JDBC Driver in DBeaver
To connect to Firebolt, you must add the Firebolt JDBC driver to DBeaver as follows:

1. Download the [Firebolt JDBC driver]({% link Guides/developing-with-firebolt/connecting-with-jdbc.md %}#download-the-jar-file).
2. In the DBeaver user interface (UI), under **Database**, select **Driver Manager**.
3. In **Driver Manager**, select **New** and enter the following parameters:
   - **Driver Name**: `Firebolt`
   - **Class Name**: `com.firebolt.FireboltDriver`
4. Select the **Libraries** tab.
5. Select **Add File**, and then select the JDBC driver you downloaded in the first step.
6. Select **Close**.

## Connect to Firebolt in DBeaver
To connect to Firebolt, you must configure a new database connection in DBeaver as follows:

1. In DBeaver, select **Database**, then **New Database Connection**.
2. Enter `Firebolt` in the search box, then select it from the list.
3. Select **Next>**.
4. Enter the connection parameters in the **Main** tab as follows:

   | Parameter    | Description |
   |-------------|-------------|
   | **JDBC URL** | Use `jdbc:firebolt:<db_name>?engine=<engine_name>&account=<account_name>` replacing `<db_name>` with your Firebolt [database name]({% link Overview/indexes/using-indexes.md %}#databases), `<engine_name>` with your [engine name]({% link Guides/getting-started/get-started-sql.md %}#create-an-engine) and `<account_name>` with your [account name]({% link Guides/managing-your-organization/managing-accounts.md %}). |
   | **Username** | Your Firebolt [service account]({% link Guides/managing-your-organization/service-accounts.md %}#get-a-service-account-id) ID. |
   | **Password** | Your Firebolt [service account]({% link Guides/managing-your-organization/service-accounts.md %}#generate-a-secret) secret. |
5. Select **Test Connection** to verify the connection. Ensure your Firebolt database is running before testing.
6. If the connection is successful, select **Finish**.

## Query Firebolt in DBeaver
1. In the database navigator, right-click or open the context menu of your Firebolt connection, select **SQL Editor**, then select **New SQL Script**.
2. Enter SQL queries into the SQL editor to interact with your Firebolt database.

## Additional Resources
* Learn more about the [Firebolt JDBC driver]({% link Guides/developing-with-firebolt/connecting-with-jdbc.md %}).
* Explore [DBeaver's documentation](https://dbeaver.io/documentation/) for details on its UI, integrations, tools, and features.
* Discover other tools that [Firebolt integrates]({% link Guides/integrations/integrations.md %}) with.
