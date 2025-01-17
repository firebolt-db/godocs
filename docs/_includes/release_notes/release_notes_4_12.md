## Firebolt Release Notes - Version 4.12

### New Features

<!-- Auto Generated Markdown for FIR-42126 - Owned by Pascal Schulze -->
**Added `ST_S2CELLIDFROMPOINT` to retrieve the [S2 Cell ID](http://s2geometry.io/devguide/s2cell_hierarchy) of a `GEOGRAPHY` Point**

You can now use [ST_S2CELLIDFROMPOINT]({% link sql_reference/functions-reference/geospatial/st_s2cellidfrompoint.md %}) to retrieve the S2 cell ID, which identifies the region on Earth that fully contains, or covers, a single Point `GEOGRAPHY` object. You can also specify a cell resolution level.

**Added keyboard shortcuts to the Firebolt Develop Space**

The Firebolt **Develop Space** user interface added the following Windows/Mac [keyboard shortcuts]({% link Guides/query-data/using-the-develop-workspace.md %}#keyboard-shortcuts-for-the-develop-space):

* Ctrl + Alt + E / Ctrl + ⌘ + E &ndash; Toggle expanding or collapsing query results.
* Ctrl + Alt + N / Ctrl + ⌘ + N &ndash; Create a new script.
* Ctrl + Alt + [ / Ctrl + ⌘ + [ &ndash; Jump to the previous script.
* Ctrl + Alt + ] / Ctrl + ⌘ + ] &ndash; Jump to the next script.

<!-- Auto Generated Markdown for FIR-42147 - Owned by Mosha Pasumansky -->
**Introduced the `INFORMATION_SCHEMA.ROUTINES` view for built-in functions and operators**

Added the [INFORMATION_SCHEMA.ROUTINES]({% link sql_reference/information-schema/routines.md %}) view to return information about all of Firebolt's built-in functions and operators including their database, schema, name, type, return data type, parameter data types, and whether they are deterministic.


<!-- Auto Generated Markdown for FIR-41816 - Owned by Kfir Yehuda -->
**Added support for the `GEOGRAPHY` data type in external tables using CSV and JSON formats**

Firebolt can now read columns of type `GEOGRAPHY` from external tables in CSV or JSON format, which allows the querying of geospatial data including Points and Polygons.

<!-- FIR-37266 - Owned by Mariia Kaplun -->
**Added a new `MONITOR USAGE` privilege**

You can use the `MONITOR USAGE` privilege to view all queries running on an engine using [information_schema.engine_query_history]({% link sql_reference/information-schema/engine-query-history.md %}) or [information_schema.engine_running_queries]({% link sql_reference/information-schema/engine-running-queries.md %}) views.

<!-- FIR-38440 - Owned by Ivan Koptiev -->
**Introduced support for network policy `ADD`/`REMOVE` commands**  
Admins can now append or remove specific IP addresses in `ALLOW` or `BLOCK` lists without overriding existing values. This update simplifies network policy management when handling large IP lists and reduces the risk of concurrent updates overwriting each other.

### Performance Improvements

<!-- Auto Generated Markdown for FIR-38755 - Owned by Demian Hespe -->
**Improved performance of the `ST_COVERS`, `ST_CONTAINS`, and `ST_INTERSECTS` functions**

Optimized the [ST_COVERS]({% link sql_reference/functions-reference/geospatial/st_covers.md %}), [ST_CONTAINS]({% link sql_reference/functions-reference/geospatial/st_contains.md %}), and [ST_INTERSECTS]({% link sql_reference/functions-reference/geospatial/st_intersects.md %}) functions to improve performance when processing LineStrings and Points with non-intersecting inputs, and Polygons with inputs that do not intersect their boundaries.


<!-- Auto Generated Markdown for FIR-42003 - Owned by Michael Freitag -->
**Improved performance of the `REGEXP_LIKE_ANY` function**

The [REGEXP_LIKE_ANY]({% link sql_reference/functions-reference/string/regexp-like-any.md %}) function now performs more efficiently when matching against multiple patterns by compiling a single combined [RE2](https://github.com/google/re2/) regular expression object instead of evaluating each pattern separately.

### Behavior Changes

<!-- Auto Generated Markdown for FIR-37317 - Owned by Tal Zelig -->
**Updated user name rules to improve consistency and validation**

The following changes affect the use of user names in [CREATE USER]({% link sql_reference/commands/access-control/create-user.md %}) AND [ALTER USER]({% link sql_reference/commands/access-control/alter-user.md %}):
* The `@` character is no longer allowed in user names.
* The range of permissible characters in user names is expanded. For more information, see [CREATE USER]({% link sql_reference/commands/access-control/create-user.md %}).
* When renaming a user with  [ALTER USER]({% link sql_reference/commands/access-control/alter-user.md %}) `old_name RENAME TO new_name`, the `new_name` must now comply with the updated user name rules.
* Any new names created with [CREATE USER]({% link sql_reference/commands/access-control/create-user.md %}) must now comply with the updated user name rules.

### Bug Fixes

<!-- Auto Generated Markdown for FIR-42149 - Owned by Demian Hespe -->
**Fixed an error where `APACHE_DATASKETCHES_HLL_ESTIMATE` failed for `NULL` inputs**

Resolved an error in the [APACHE_DATASKETCHES_HLL_ESTIMATE]({% link sql_reference/functions-reference/datasketches/apache-datasketches-hll-estimate.md %}) function that occurred if any of its input values were `NULL`. The function can now process `NULL` inputs.

<!-- Auto Generated Markdown for FIR-36604 - Owned by Tal Zelig -->
**Resolved issue that allowed account lockout on last login**

Fixed an issue where the `ALTER USER SET LOGIN/SERVICE_ACCOUNT=...` statement could lock out the only active login in an account, rendering the account inaccessible. The operation now fails with an explicit error message in such cases.

<!-- Auto Generated Markdown for FIR-35894 - Owned by Tal Zelig -->
**Fixed incorrect ownership modification for `information_schema`**

The statement `ALTER SCHEMA information_schema SET OWNER owner_name;` previously succeeded, which was incorrect, because `information_schema` cannot be modified. The operation now fails with an explicit error message.

<!-- Auto Generated Markdown for FIR-38817 - Owned by jingtao.huang -->
**Fixed an out-of-memory error during large CSV imports**

Updated the ingestion pipeline for [COPY FROM]({% link sql_reference/commands/data-management/copy-from.md %}) to ensure that large CSV files without a predefined schema can load into new tables without causing memory errors. This error did not affect external tables.

<!-- Markdown for FIR-42447 - Owned by Gil Cizer -->
**Prevent running queries when using a dropped database**

When the current database does not exist, such as when it has been dropped, most queries fail as expected. We fixed a bug where some queries against specific `information_schema` views, such as `engines`, `catalogs`, `applicable_roles`, would still succeed in such cases. These queries now fail consistently, like all other queries against a non-existent database.
For example, running `SELECT * FROM information_schema.engines` when the database is dropped previously worked, but now fails.
