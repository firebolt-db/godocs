---
layout: default
title: Synchronous queries
description: Learn how to submit sync queries and get their status. 
parent: API reference
nav_order: 1
---

# Synchronous queries

Synchronous queries in Firebolt allow users to send a sql statement and wait for an immediate response before proceeding with other operations. These queries are best suited for interactive analytics, dashboards, and data retrieval where low-latency performance is essential. Synchronous queries complete within a single request-response cycle.

Synchronous queries are the default query mode for submitting queries in Firebolt. All of the statements in the [SQL reference]({% link sql_reference/index.md %}) guide can be used inside a synchronous query. 

## How to submit a synchronous query

You can submit a synchronous query using either the user interface (UI) in the Firebolt **Develop Space**. Every query submitted using the UI is a synchronous query. For more information about how to submit a query using the UI, see [Get started using SQL]({% link Guides/getting-started/get-started-sql.md %}). 

You can also submit a synchronous query programmatically using the Firebolt API. The following are required prerequisites to submit a query programmatically:

- **Firebolt account** &ndash; You need an active Firebolt account. If you do not have one, you can [sign up](https://go.firebolt.io/signup) for one.
- **Firebolt database and engine** &ndash; You must have access to a Firebolt database. If you do not have access, you can [create a database]({% link Guides/getting-started/get-started-sql.md %}#create-a-database) and then [create an engine]({% link Guides/getting-started/get-started-sql.md %}#create-an-engine).
- **Firebolt service account** &ndash; You must have an active Firebolt [service account]({% link Guides/managing-your-organization/service-accounts.md %}) for programmatic access, along with its ID and secret.
- **Sufficient permissions** You will need to have [USAGE permission]({% link Overview/Security/Role-Based Access Control/engine-permissions.md %}#engine-permissions) on the engine that runs the query. A user always has permission to view their own queries. To see another user's queries, you must have `MONITOR ENGINE` or `MONITOR ALL` privileges.

To submit a synchronous query programatically, use a Firebolt Driver to send an HTTP request with the SQL query to Firebolt's API endpoint. 

### Use a Firebolt Driver

Use a Firebolt driver to connect to a Firebolt database, authenticate securely, and run queries with minimal setup. The driver provides built-in methods for running queries, handling responses, and managing connections. All Firebolt drivers support synchronous queries. See the documentation for each driver for specific details on how to submit synchronous queries programmatically:

* [Node.js SDK]({% link Guides/developing-with-firebolt/connecting-with-nodejs.md %}) &ndash; Firebolt Node.js SDK
* [Python SDK]({% link Guides/developing-with-firebolt/connecting-with-Python.md %}) &ndash; Firebolt Python SDK
* [JDBC Driver]({% link Guides/developing-with-firebolt/connecting-with-jdbc.md %}) &ndash; Firebolt JDBC Driver
* [SQLAlchemy]({% link Guides/developing-with-firebolt/connecting-with-sqlalchemy.md %}) &ndash; Firebolt SQLAlchemy adapter
* [.NET SDK]({% link Guides/developing-with-firebolt/connecting-with-net-sdk.md %}) &ndash; Firebolt .NET SDK
* [Go SDK]({% link Guides/developing-with-firebolt/connecting-with-go.md %}) &ndash; Firebolt Go SDK

### Python example API call

The following code example establishes a connection to a Firebolt database using a service account's credentials, runs a simple `SELECT` query, retrieves and prints the result:

```python
from firebolt.db import connect
from firebolt.client.auth import ClientCredentials

id = "service_account_id"
secret = "service_account_secret"
engine_name = "your_engine_name"
database_name = "your_test_db"
account_name = "your_account_name"

query = """
    SELECT 42;
    """

with connect(
    engine_name=engine_name,
    database=database_name,
    account_name=account_name,
    auth=ClientCredentials(id, secret),
) as connection:
    cursor = connection.cursor()

    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)
```

## Handling long-running synchronous queries

Synchronous queries maintain an open HTTP connection for the duration of the query, and stream results back as they become available. While there is no strict time limit, queries running longer than one hour may experience connectivity interruptions. If the HTTP connection is lost, some queries, including `INSERT`, continue to run by default, while `SELECT` queries are cancelled. You can modify this behavior using the [cancel_query_on_connection_drop](../../Reference/system-settings.md#query-cancellation-mode-on-connection-drop) setting. 

To avoid connection issues, consider submitting long-running queries as [asynchronous](using-async-queries.md) queries. 

## Error handling

Common errors and solutions when using synchronous queries:

| Error Type         | Cause                                    | Solution |
|--------------------|-----------------------------------------|----------|
| **Timeout**       | The query runs longer than expected.        | Submit as an [asynchronous query](using-async-queries.md). |
| **Connection loss** | The HTTP connection is interrupted.        | Use the `cancel_query_on_connection_drop` setting to modify behavior. |
| **Permission denied** | The user lacks required permissions.     | Ensure the user has `USAGE` permission on the engine. |


### How to check the status of a sync query

The queries running on an engine are available in the [engine_running_queries]({% link sql_reference/information-schema/engine-running-queries.md %}) view. 


### Query cancelation 

A running synchronous query can be cancelled using the [cancel]({% link sql_reference/commands/queries/cancel.md %}) statement as follows:

```sql
CANCEL QUERY '<query_id>';
```

Use the query ID retrieved from the [engine_running_queries]({% link sql_reference/information-schema/engine-running-queries.md %}) view to cancel a specific query.

