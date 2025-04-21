## Firebolt Release Notes - Version 4.18

### New Features

<!-- Auto Generated Markdown for FIR-44312 - Owned by Tal Zelig -->
**Users can now ALTER their corresponding USER object without administrative or RBAC permissions**<br>
Users can now [ALTER]({% link sql_reference/commands/access-control/alter-user.md %}) their corresponding [USER]({% link Overview/organizations-accounts.md %}#users) object and change its properties without needing role-based access control permissions ([RBAC]({% link Overview/Security/Role-Based Access Control/index.md %})). This enhancement simplifies user self-management by reducing the dependency on administrative permissions. Restrictions remain for sensitive properties including [logins or service accounts]({% link Overview/organizations-accounts.md %}#organizations), which require higher-level permissions.

**Use a LOCATION object to store credentials for authentication**<br>
You can now use [CREATE LOCATION]({% link sql_reference/commands/data-definition/create-location.md %}) to create a `LOCATION` object in your Firebolt account. Use `LOCATION` to store credentials and authenticate to external systems without needing to provide static credentials each time you run a query or create a table. `LOCATION` works with ([RBAC]({% link Overview/Security/Role-Based Access Control/index.md %})) so you can manage permissions securely. You can view detailed information about your locations including source type, URL, description, owner, and creation time in [information_schema.locations]({% link sql_reference/information-schema/locations.md %}).

<!-- Auto Generated Markdown for FIR-43325 - Owned by Amit Schreiber -->
**Added creation timestamps for tables, views, indexes, and locations**<br>
Use creation timestamps in `information_schema` views for [tables]({% link sql_reference/information-schema/tables.md %}), [views]({% link sql_reference/information-schema/views.md %}), [indexes]({% link sql_reference/information-schema/indexes.md %}), and [locations]({% link sql_reference/information-schema/locations.md %}) to help track objects for data management.

**Added support for SQL pipe syntax**  
Firebolt now supports [SQL Pipe syntax]({% link sql_reference/commands/queries/pipe.md %}), an alternative way to structure SQL queries using the `|>` operator. This syntax allows for a linear, step-by-step flow of query transformations, improving readability and simplifying query composition. It supports all standard SQL operations and can be combined with traditional SQL syntax.

<!-- Auto Generated Markdown for FIR-44425 - Owned by Artem Grachev -->
**Added wildcard character functionality to `READ_PARQUET` and `READ_CSV` to simultaneously read multiple files**<br>
You can use wildcard characters such as `*` or `?` to specify a file URL as a [glob pattern](https://en.wikipedia.org/wiki/Glob_(programming)) in the [READ_PARQUET]({% link sql_reference/functions-reference/table-valued/read_parquet.md %}) and [READ_CSV]({% link sql_reference/functions-reference/table-valued/read_csv.md %}) table-valued functions to read multiple files simultaneously. This enhancement simplifies managing large datasets by reducing the need to make multiple function calls.


<!-- Auto Generated Markdown for FIR-42972 - Owned by Eugene Fomenko -->
**Added functionality to transfer ownership of objects in the Firebolt Workspace**<br>
You can now [transfer ownership]({% link Guides/security/ownership.md %}#managing-ownership-in-the-firebolt-workspace) of Firebolt objects through the **Firebolt Workspace** user interface (UI). You can transfer ownership of individual objects or bulk transfer owned by a specific user. You can also delete individual objects or in bulk, helping to simplify the management of object ownership within the UI.


### Performance Improvements

<!-- Auto Generated Markdown for FIR-44586 - Owned by Demian Hespe -->
**Enabled result and subresult caching for queries with window functions**<br>
Enabled [result and subresult caching]({% link Overview/queries/understand-query-performance-subresult.md %}) for queries that contain [window functions]({% link sql_reference/functions-reference/window/index.md %}), which can reduce query runtimes by storing previous results and enhance overall query performance and efficiency.


### Bug Fixes

<!-- Auto Generated Markdown for FIR-44680 - Owned by Michael Freitag -->
**Fixed an issue where `CREATE VIEW` statements did not preserve the order of named function parameters**<br>
An issue was resolved where [CREATE VIEW]({% link sql_reference/commands/data-definition/create-view.md %}) statements did not maintain the correct order of named function parameters, which could lead to syntax errors when querying the view. This fix improves query reliability by ensuring the proper order of function parameters.
