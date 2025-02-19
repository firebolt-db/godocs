---
layout: default
title: Synchronous queries
description: Learn how to submit sync queries and get their status. 
parent: API reference
nav_order: 1
---

# Synchronous queries

Synchronous queries in Firebolt allow users to send a query and wait for an immediate response before proceeding with other operations. These queries are best suited for interactive analytics, dashboards, and data retrieval where low-latency performance is essential. Unlike asynchronous queries, which run in the background and return results later, synchronous queries complete within a single request-response cycle.

Synchronous queries are the default query mode for submitting queries in Firebolt. All of the statements in the [SQL reference](../../sql_reference/index.md) guide can be used inside a synchronous query. 

## Handling long-running synchronous queries

Synchronous queries maintain an open HTTP connection for the duration of the query, and stream results back as they become available. While there is no strict time limit, queries running longer than one hour may experience connectivity interruptions. If the HTTP connection is lost, some queries, including `INSERT`, continue to run by default, while `SELECT` queries are cancelled. You can modify this behavior using the [cancel_query_on_connection_drop](../../Reference/system-settings.md#query-cancellation-mode-on-connection-drop) setting. 

To avoid connection issues, consider submitting long-running queries as [asynchronous](using-async-queries.md) queries. 

## How to submit a synchronous query

## Using the firebolt UI
Every query submitted via the UI is a syncronous query. 

## Using a firebolt SDK
Every firebolt SDKs supports syncronous queries. See the docs for each SDK or driver for details on submitting sync queries.

## Python Example
```python
from time import sleep

from firebolt.db import connect
from firebolt.client.auth import ClientCredentials

id = "service_account_id"
secret = "service_account_secret"
engine_name = "your_engine_name"
database_name = "your_test_db"
account_name = "your_account_name"

# Example query
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

# How to check the status of an sync query
## List running queries
The queries running on an engine are available via the [engine_running_queries](../../sql_reference/information-schema/engine-running-queries.md) view. 

### Example queries
```sql
SELECT query_id, user_name, query_text 
FROM information_schema.engine_running_queries
LIMIT 100;
```

# Cancelation 
A query can be cancelled via the [cancel](../../sql_reference/commands/queries/cancel.md) statement.

# Permissions
Submitting an sync query requires the USAGE permission on that engine. A user always has permission to view their own queries. To see another user's queries, they must have MONITOR ENGINE or MONITOR ALL privileges.