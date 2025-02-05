---
redirect_from:
  - /working-with-engines/system-engine.html
layout: default
title: System Engine
description: System engine documentation
nav_order: 4
parent: Operate Engines
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
* [SELECT](../../sql_reference/commands/queries/select.md) queries on some [information_schema](../../sql_reference/information-schema/index.md) views:
    * [information_schema.accounts](../../sql_reference/information-schema/accounts.md)
    * [information_schema.applicable_roles](../../sql_reference/information-schema/applicable-roles.md)
    * [information_schema.transitive_applicable_roles](../../sql_reference/information-schema/transitive-applicable-roles.md)
    * [information_schema.columns](../../sql_reference/information-schema/columns.md)
    * [information_schema.catalogs](../../sql_reference/information-schema/catalogs.md)
    * [information_schema.enabled_roles](../../sql_reference/information-schema/enabled-roles.md)
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
Connect via the connector without specifying the engine_name. Database parameter is optional.

System engine does not need a database defined. If you wish to connect to an existing database and run metadata queries with the system engine, just specify the name of your database.

**Example**
```json
from firebolt.db import connect
from firebolt.client import DEFAULT_API_URL
from firebolt.client.auth import ClientCredentials

client_id = "<service_account_id>"
client_secret = "<service_account_secret>"
account_name = "<your_account_name>"

with connect(
   database="<any_db_here>", # Omit this parameter if you don't need db-specific operations
   auth=ClientCredentials(client_id, client_secret),
   account_name=account_name,
   api_endpoint=DEFAULT_API_URL,
) as connection:

   cursor = connection.cursor()

   cursor.execute("SHOW CATALOGS")

   print(cursor.fetchall())
```

Guidance on creating service accounts can be found in the [service account](../managing-your-organization/service-accounts.md) section.

### Other SDKs
Any other Firebolt connector can also be used similarly, as long as the engine name is omitted.

## System Engine Limitations

### Supported queries for system engine

System engine only supports running the metadata-related queries listed above. Additional queries will be supported in future versions.

### Rate Limits for System Engines

To ensure fair and consistent access to the System Engine for all users, we have introduced rate limits that govern resource usage per account. These limits are designed to prevent resource contention and ensure optimal performance for everyone.

When the rate limits are exceeded on the system engine, the system will return the following error: `429: Account system engine resources usage limit exceeded`.
This error typically occurs when an account submits an excessive number of queries or executes highly complex queries that surpass the allocated resource thresholds.

**What to Do If You Encounter Rate Limits**

If you receive the 429 error, consider these steps to resolve the issue:

* Switch to a User Engine: Offload your workloads to a dedicated User Engine if possible. User Engines do not have the same rate limits, making them better suited for higher workloads or complex operations.
* Review your query patterns and ensure they are not unnecessarily complex or resource-intensive. Use best practices to write efficient queries that minimize resource consumption.
* Contact Support: If you believe your account has been rate-limited unfairly or you anticipate requiring higher limits, reach out to our support team to discuss adjusting your account's thresholds.

**Best Practices to Avoid Rate Limits**

* Avoid running multiple concurrent queries that heavily use system resources.
* Leverage Firebolt's indexing and other optimization features to streamline your queries.
* Regularly audit your workloads and usage patterns to align with the system's best practices.

**Why This Matters**

These rate limits are critical for maintaining a fair and robust environment where all users can achieve reliable performance without disruption from resource-heavy neighbors. This measure aligns with our commitment to delivering consistent and high-quality service across all accounts.

For additional support or questions, please contact our support team or refer to our documentation on optimizing query performance.