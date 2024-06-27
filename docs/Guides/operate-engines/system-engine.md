---
layout: default
title: System Engine
description: System engine documentation
nav_order: 4
parent: Operate Engines
grand_parent: Guides
---

# System Engine
{: .no_toc}

Firebolt's system engine enables running various metadata-related queries without having to start an engine. The system engine is always available for you in all databases to select and use.  

The system engine supports running the following commands:
* All [access control](../../sql_reference/commands/access-control/index.md) commands
* All [engine](../../sql_reference/commands/engines/index.md) commands
* Most [data definition](../../sql_reference/commands/data-definition/index.md) commands. The following commands are not supported:
  * [ALTER TABLE DROP PARTITION](../../sql_reference/commands/data-definition/alter-table.md)
  * [CREATE AGGREGATING INDEX](../../sql_reference/commands/data-definition/create-aggregating-index.md)
  * [CREATE EXTERNAL TABLE](../../sql_reference/commands/data-definition/create-external-table.md)
  * [CREATE TABLE AS SELECT](../../sql_reference/commands/data-definition/create-fact-dimension-table-as-select.md)
* Most [metadata](../../sql_reference/commands/metadata/index.md) commands. The following commands are not supported:
  * [SHOW CACHE](../../sql_reference/commands/metadata/show-cache.md)
* Non-data-accessing [SELECT](../../sql_reference/commands/queries/select.md) queries like `SELECT CURRENT_TIMESTAMP()`
* [SELECT](../../sql_reference/commands/queries/select.md) queries on some [information_schema](../../sql_reference/information-schema/information-schema-and-usage-views.md) views:
    * [information_schema.accounts](../../sql_reference/information-schema/accounts.md)
    * [information_schema.applicable_roles](../../sql_reference/information-schema/applicable-roles.md)
    * [information_schema.columns](../../sql_reference/information-schema/columns.md)
    * [information_schema.databases](../../sql_reference/information-schema/databases.md)
    * [information_schema.engines](../../sql_reference/information-schema/engines.md)
    * [information_schema.indexes](../../sql_reference/information-schema/indexes.md)
    * [information_schema.logins](../../sql_reference/information-schema/logins.md)
    * [information_schema.network_policies](../../sql_reference/information-schema/network_policies.md)
    * [information_schema.service_accounts](../../sql_reference/information-schema/service-accounts.md)
    * [information_schema.tables](../../sql_reference/information-schema/tables.md)
    * [information_schema.users](../../sql_reference/information-schema/users.md)
    * [information_schema.views](../../sql_reference/information-schema/views.md)

## Using the system engine via the Firebolt manager 
1. In the Firebolt manager, choose the Databases icon in the navigation pane.
2. Click on the SQL Workspace icon for the desired database. In case you have no database in your account - create one first. 
3. From the engine selector in the SQL Workspace, choose System Engine, then run one of the supported queries.

## Using the system engine via SDKs
### Python SDK
Connect via the connector and specify engine_name = ‘system’ and database = ‘dummy’.

System engine does not need a database defined, but for the Python SDK - the `database` parameter is required, so any string here will work (except an empty string). If you wish to connect to an existing database and run metadata queries with the system engine, just specify the name of your database.

**Example**
```json
from firebolt.db import connect
from firebolt.client import DEFAULT_API_URL
from firebolt.client.auth import UsernamePassword
 
username = "<your_username>"
password = "<your_password>"
 
with connect(
   database="<any_db_here>", # this is a required parameter
   auth=UsernamePassword(username, password),
   api_endpoint=DEFAULT_API_URL,
   engine_name="system",
) as connection:
 
   cursor = connection.cursor()
 
   cursor.execute("SHOW DATABASES")

   print(cursor.fetchall())
```

### Other SDKs
Any other Firebolt connector can also be used similarly, as long as the engine name is specified as ‘system’ and the database is set to any name (string).

## Known limitations and future release plans

**Supported queries for system engine**

At this time, the system engine only supports running the metadata-related queries listed above. Additional queries will be supported in future versions.

System engine is currently only available for accounts that have a single region enabled.
