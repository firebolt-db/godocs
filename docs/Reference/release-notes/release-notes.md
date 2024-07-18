---
layout: default
title: Release notes
description: Latest release notes for the Firebolt data warehouse.
parent: General reference
nav_order: 1
has_toc: false
has_children: false
---

# Release notes

Firebolt continuously releases updates so that you can benefit from the latest and most stable service. These updates might happen daily, but we aggregate release notes to cover a longer time period for easier reference. The most recent release notes from the latest version are below. 

- See the [Release notes archive](../release-notes/release-notes-archive.md) for earlier-version release notes.

{: .note}
Firebolt might roll out releases in phases. New features and changes may not yet be available to all accounts on the release date shown.

## DB version 4.2
**July 2024**

- [Release notes](#release-notes)
  - [DB version 4.2](#db-version-42)
    - [New features](#new-features)
    - [Breaking Changes](#breaking-changes)
    - [Enhancements, changes and new integrations](#enhancements-changes-and-new-integrations)

### New features

<!--- FIR-32118---> **New `ntile` window function**

Firebolt now supports the `ntile` window function. Refer to our [NTILE](../sql_reference/../../sql_reference/functions-reference/window/ntile.md) documentation for examples and usage. 

### Breaking Changes 

<!--- FIR-33028 --->**Improved rounding precision for floating point to integer casting**
{: style="color:red;"}

Casting from floating point to integers now uses Banker's Rounding, matching PostgreSQL's behavior. This means that numbers that are equidistant from the two nearest integers are rounded to the nearest even integer:  

Examples:
```sql
SELECT 0.5::real::int
``` 
This returns 0. 

```sql
SELECT 1.5::real::int
``` 
This returns 2. 

 Rounding behavior has not changed for numbers that are strictly closer to one integer than to all others.
 
<!--- FIR-33869---> **JSON functions update**
{: style="color:red;"}

Removed support for `json_extract_raw`, `json_extract_array_raw`, `json_extract_values`, and `json_extract_keys`. Updated `json_extract` function: the third argument is now `path_syntax`, which is a JSON pointer expression. See [JSON_EXTRACT](../sql_reference/../../sql_reference/functions-reference/JSON/json-extract.md) for examples and usage. 

<!--- FIR-32486---> **Cluster ordinal update**
{: style="color:red;"}

Replaced `engine_cluster` with [`cluster_ordinal`](../sql_reference/../../sql_reference/information-schema/engine-metrics-history.md) in `information_schema.engine_metrics_history`. The new column is an integer representing the cluster number.

<!--- FIR-34090 ---> **Configurable cancellation behavior on connection drop**
{: style="color:red;"}

Introduced the `cancel_query_on_connection_drop` setting, allowing clients to control query cancellation on HTTP connection drop. Options include `NONE`, `ALL`, and `TYPE_DEPENDENT`. Refer to [system settings](../system-settings.md#query-cancellation-mode-on-connection-drop) for examples and usage. 

<!--- FIR-33925 ---> **JSON format as default for error output**
{: style="color:red;"}

The HTTP API now returns query execution errors in JSON format by default. This change allows for the inclusion of meta information such as error codes and the location of failing expressions in SQL scripts.

<!--- FIR-33925 ---> **STOP ENGINE will drain currently running queries first**
{: style="color:red;"}

`STOP ENGINE` command now supports graceful drain, meaning any currently running queries will be run to completion. Once all the queries are completed, the engine will be fully stopped and terminated. If you want to stop the engine immediately, you can issue a STOP ENGINE command use the TERMINATE option. For example, to immediately stop an engine, my_engine, you can use:

```sql
 STOP ENGINE myEngine WITH TERMINATE = TRUE
```

<!--- FIR-33925 ---> **Scaling engines will not terminate currently running queries**
{: style="color:red;"}

`ALTER ENGINE` command now supports graceful drain, meaning when you scale an engine (vertically or horizontally), any currently running queries will not be terminated. New queries after the scaling operation will be directed to a new cluster, while queries running on the old cluster will be run to completion.

<!--- FIR-33857---> **Updated ownership management**
{: style="color:red;"}

We have introduced several updates to role and privilege management: 
  * The `security_admin` role will be removed temporarily and re-introduced in a later release.
  * `Information_object_privileges` includes more privileges. Switching to to a specific user database (e.g by executing `use database db`) will only show privileges relevant for that database. Account-level privileges no longer show up when attached to a specific database. 
  * Every newly created user is granted with a `public` role. This grant can be revoked.

### Enhancements, changes and new integrations

<!--- FIR-33699---> **Improved query performance**

Queries with "`SELECT [project_list] FROM [table] LIMIT [limit]`" on large tables are now significantly faster.

<!--- FIR-33857---> **Updated table level RBAC**

Table level RBAC is now supported by Firebolt. This means that RBAC checks also cover schemas, tables, views and aggregating indexes. Refer to our [RBAC](./../../Guides/security/rbac.md) docs for a detailed overview of this new feature. The new Firebolt version inhibits the following change:
   * System built-in roles are promoted to contain table level RBAC information. This means that new privileges are added to `account_admin`, `system_admin` and `public` roles. The effect is transparent— any user assigned with those roles will not be affected.

<!--- FIR-33857---> **Removal of Deprecated Columns from `INFORMATION_SCHEMA.ENGINES`**

We removed the following columns from `INFORMATION_SCHEMA.ENGINES` that were only for FB 1.0 compatibility: `region`, `spec`, `scale`, `warmup`, and `attached_to`. These columns were always empty. (These columns are hidden and do not appear in `SELECT *` queries, but they will still work if referenced explicitly.)
