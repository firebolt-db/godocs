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
    - [Breaking Changes](#breaking-changes)
    - [Enhancements, changes and new integrations](#enhancements-changes-and-new-integrations)

### Breaking Changes 

<!--- FIR-33028 --->**Improved casting precision**
{: style="color:red;"}

Casting from floating point to integers now rounds to an even number, ensuring compliance with PostgreSQL standards. 
Example: 
```sql
SELECT 0.5::real::int
``` 
This will now return 0 instead of 1. 

<!--- FIR-33869---> **JSON functions update**
{: style="color:red;"}

Removed support for `json_extract_raw`, `json_extract_array_raw`, `json_extract_values`, and `json_extract_keys`. Updated `json_extract function`: the third argument is now path_syntax, currently supporting 'JSONPointer'. See [JSON_EXTRACT](../sql_reference/../../sql_reference/functions-reference/JSON/json-extract.md) for usage examples. 

<!--- FIR-32486---> **Cluster ordinal update**
{: style="color:red;"}

Replaced `engine_cluster` with [`cluster_ordinal`](../sql_reference/../../sql_reference/information-schema/engine-metrics-history.md) in `information_schema.engine_metrics_history`. The new column has an integer representing the cluster number.

<!--- FIR-34090 ---> **Configurable Query Cancellation**

Introduced the `cancel_query_on_connection_drop` setting, allowing clients to control query cancellation on HTTP connection drop. Options include `NONE`, `ALL`, and `TYPE_DEPENDENT`. Refer to [system settings](../system-settings.md)  for usage details. 

### Enhancements, changes and new integrations

<!--- FIR-33699---> **Improved query performance**

Queries with "`SELECT` <project_list> `FROM` <table> `LIMIT` <limit>" on large tables are now significantly faster.





