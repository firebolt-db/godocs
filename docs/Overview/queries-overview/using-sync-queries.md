---
layout: default
title: Synchronous queries
description: Learn how to submit sync queries and get their status. 
parent: Queries overview
nav_order: 1 # FIXME
---

# Synchronous queries

Syncronous queries are the default mode of submitting queries in firebolt. All kinds of sql queries are accepted as sync queries. See the [SQL reference](../../sql_reference/index.md) for the full range of queries supported by firebolt.

## Long running sync queries

Syncronous queries keep a HTTP connection open for the duration of the query, and stream results back as they are available. While there is no enforced time limit on query run time, it is not guaranteed that the HTTP connection can survive for a very long time. This is particularly true past the 1 hour mark. If the HTTP connection is severred, some kinds of queries like `INSERT` continue to run by default. `SELECT` queries are cancelled by default. This behavior can be changed via the setting [cancel_query_on_connection_drop](../../Reference/system-settings.md#query-cancellation-mode-on-connection-drop). 

Some kinds of queries can be submitted as [async](using-async-queries.md) queries to mitigate this problem. 

# How to submit an sync query

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