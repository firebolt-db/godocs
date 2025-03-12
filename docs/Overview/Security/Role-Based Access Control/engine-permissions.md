---
redirect_from:
  - /Overview/Role-Based Access Control/engine-permissions.html
layout: default
title: Engine Permissions
description: Learn about engine-level permissions in Firebolt.
parent: Role-Based Access Control
nav_order: 6
---

# Engine permissions

In Firebolt, an **engine** is a compute resource that processes data and serves queries. Engines provide **full workload isolation**, allowing multiple workloads to run independently while sharing access to the same data. Engines are also **decoupled from databases**, which means:
* An engine can connect to multiple databases.
* A database can be accessed by multiple engines.

The following table outlines the privileges that can be granted for engines within a particular account:

| Privilege             | Description                                                                 | GRANT Syntax                                                     | REVOKE Syntax                                                    |
|---------------------------|---------------------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|
| USAGE                 | Allows using an engine to run queries.                                   | `GRANT USAGE ON ENGINE <engine_name> TO <role>;`                       | `REVOKE USAGE ON ENGINE <engine_name> FROM <role>;`                    |
| OPERATE                | Allows stopping and starting an engine.                                      | `GRANT OPERATE ON ENGINE <engine_name> TO <role>;`                      | `REVOKE OPERATE ON ENGINE <engine_name> FROM <role>;`                   |
| MODIFY                 | Allows altering engine properties or dropping the engine.                       | `GRANT MODIFY ON ENGINE <engine_name> TO <role>;`                       | `REVOKE MODIFY ON ENGINE <engine_name> FROM <role>;`                    |
| MONITOR [USAGE]    | Enables the tracking of engine queries through the `engine_running_queries` view for active queries and the `engine_query_history` view for past queries in `information_schema`. | `GRANT MONITOR USAGE ON ENGINE <engine_name> TO <role>;` | `REVOKE MONITOR USAGE ON ENGINE <engine_name> FROM <role>;`  |
| ALL [PRIVILEGES]    | Grants all privileges over the engine to a role. | `GRANT ALL ON ENGINE <engine_name> TO <role>;` | `REVOKE ALL ON ENGINE <engine_name> FROM <role>;`  |


{: .note}
If a user lacks **USAGE** and **OPERATE** privileges for an engine, they will not be able to select or interact with the engine via the Firebolt UI.

## Examples of granting engine permissions

### USAGE permission
The following code example grants the role `developer_role` permission to use the `myEngine` engine for executing queries:

```sql
GRANT USAGE ON ENGINE "myEngine" TO developer_role;
```

### OPERATE permission
The following code example gives the role `developer_role` permission to start and stop the `myEngine` engine:

```sql
GRANT OPERATE ON ENGINE "myEngine" TO developer_role;
```

### MODIFY permission
The following code example grants the role `developer_role` permission to alter properties or drop the `myEngine` engine:

```sql
GRANT MODIFY ON ENGINE "myEngine" TO developer_role;
```

### MONITOR [USAGE] permission
The following code example grants the role `developer_role` permission to see the query history and currently running queries for the engine `myEngine`:

```sql
GRANT MONITOR USAGE ON ENGINE "myEngine" TO developer_role;
```

### ALL permissions
The following code example grants the role `developer_role` with all engine permissions on `myEngine`:

```sql
GRANT ALL ON ENGINE "myEngine" TO developer_role;
```