## DB version 4.7

### Behavior Changes

<!-- Auto Generated Markdown for FIR-36501 - Owned by Leonard von Merzljak -->
**Updated sorting method for array columns with `NULL` values to align with PostgreSQL behavior**
{: style="color:red;"}

The sorting method for array columns containing `NULL` values has been updated to ensure that `ASC NULLS FIRST` places `NULL` values before arrays, and `DESC NULLS LAST` places `NULL` values after arrays, which aligns with PostgreSQL behavior.

The following code example creates a temporary table `tbl` which contains three rows: a `NULL` array, an array with the value `1`, and an array with a `NULL` element. Then, a `SELECT` statement sorts all rows in ascending order:
```sql
WITH tbl(i) AS (
  SELECT NULL::INT[]
  UNION ALL
  SELECT ARRAY[1]::INT[]
  UNION ALL
  SELECT ARRAY[NULL]::INT[]
)
SELECT * FROM tbl ORDER BY i ASC NULLS FIRST;
```

The query previously returned `{NULL}, {1}, NULL`, but now returns `NULL, {1}, {NULL}`.

`NULLS FIRST` and `NULLS LAST` apply to the array itself, not to its elements. By default, ascending order (`ASC`) assumes `NULLS LAST`, while descending order (`DESC`) assumes `NULLS FIRST` when sorting arrays.

<!-- Auto Generated Markdown for FIR-37163 - Owned by Mosha Pasumansky -->
**Allowed use of the SESSION_USER function without parentheses**
{: style="color:red;"}

The `SESSION_USER` function can now be used without parentheses, like this: `SELECT SESSION_USER`. As a result, any column named `session_user` now needs to be enclosed in double quotes as follows: `SELECT 1 as "session_user"` or `SELECT "session_user" FROM table`.


### New Features

<!-- Auto Generated Markdown for FIR-35515 - Owned by Judson Wilson -->
**Added Snappy compression support to the COPY TO command for PARQUET output format**<br/>
You can now apply Snappy compression, which is faster than GZIP, when using `COPY TO` with `TYPE=PARQUET`. Specify `COMPRESSION=SNAPPY` within `COPY TO` to enable this.


<!-- Auto Generated Markdown for FIR-36415 - Owned by Pascal Schulze -->
**Added `information_schema.engine_user_query_history` view to log only user-initiated queries**<br/>
Added a new query history view, `information_schema.engine_user_query_history` that shows all queries initiated by users. This view filters information from `information_schema.engine_query_history` view, which logs all engine queries including system-generated ones like UI updates and page-load requests.


<!-- Markdown for FIR-35689 - Owned by Mariia Kaplun -->
**Added support for `information_schema.enabled_roles`**<br/>
Added a new view `information_schema.enabled_roles` which lists the roles available in the account.


<!-- Auto Generated Markdown for FIR-36502 - Owned by Demian Hespe -->
**Added a system setting `enable_subresult_cache` for controlling subresult reuse**<br/>
A new system setting `enable_subresult_cache` allows users to enable or disable caching of query subresults for subsequent reuse.
Caching remains enabled by default. This setting allows users to temporarily disabling caching, e.g. for benchmarking purposes.


<!-- Auto Generated Markdown for FIR-36879 - Owned by Mosha Pasumansky -->
**Added "FROM first" syntax allowing the `FROM` clause to precede the `SELECT` clause**<br/>
Added support for the "FROM first" syntax, which allows placing the `FROM` clause before the `SELECT` clause, for example `FROM t SELECT a, SUM(b) GROUP BY a`. You can now also omit the `SELECT` clause, as in `FROM t`.


<!-- Auto Generated Markdown for FIR-36609 - Owned by Mosha Pasumansky -->
**Introduced `~` and `!~` operators as aliases for `REGEXP_LIKE` and `NOT REGEXP_LIKE`**<br/>
Added the `~` operator as an alias for `REGEXP_LIKE`, and the `!~` operator, which serves as an alias for `NOT REGEXP_LIKE`.


<!-- Auto Generated Markdown for FIR-35669 and FIR-36800 - Owned by Kfir Yehuda -->
**Introduced JSON functions `JSON_POINTER_EXTRACT_KEYS`, `JSON_POINTER_EXTRACT_VALUES`, `JSON_POINTER_EXTRACT_TEXT`**<br/>
The following new JSON functions are now supported:
- `JSON_POINTER_EXTRACT_KEYS` extracts keys from a JSON object
- `JSON_POINTER_EXTRACT_VALUES` extracts values from a JSON object
- `JSON_POINTER_EXTRACT_TEXT` extracts the JSON string value as SQL TEXT


<!-- FIR-35717, FIR-36590, FIR-36591 -- Owned by Demian Hespe -->
**Introduced trigonometric functions `RADIANS`, `SIN`, `ATAN2`**<br/>
The following trigonometric functions are now supported:
- `RADIANS` to convert degrees into radians
- `SIN` to compute the sine in radians
- `ATAN2` to calculate the arctangent with two arguments. `ATAN2(y,x)` is the angle between the positive x-axis and the line from the origin to the point `(x,y)`, expressed in radians.


<!-- Auto Generated Markdown for FIR-35708 - Owned by Christoph Anneser -->
**Introduced new functions to calculate standard deviation and variance for both samples and populations**<br/>
New functions that accept `REAL` and `DOUBLE` inputs and return standard deviations and variances:
- `STDDEV_SAMP` - Returns the sample standard deviation of all non-`NULL` numeric values produced by an expression, which measures how spread out values are in a sample.
- `STDDEV_POP` - Returns the population standard deviation of all non-`NULL` numeric values produced by an expression, which measures how spread out values are in an entire population.
- `VAR_SAMP` - Returns the sample variance of all non-`NULL` numeric values produced by an expression, which measures the average of the squared differences from the sample mean, indicating how spread out the values are within a sample.
- `VAR_POP` - Returns the population variance of all non-`NULL` numeric values produced by an expression. The population variance measures the average of the squared differences from the population mean, indicating how spread out the values are within the entire population.


<!-- Auto Generated Markdown for FIR-36430, FIR-35462 - Owned by Christoph Anneser -->
**Introduced new array functions `ARRAY_ALL_MATCH` and `ARRAY_ANY_MATCH`**<br/>
The new functions `ARRAY_ALL_MATCH` and `ARRAY_ANY_MATCH` accept an (optional) lambda function and an array and return `TRUE` if all elements (`ARRAY_ALL_MATCH`) or any element (`ARRAY_ANY_MATCH`) satisfy the lambda condition, and `FALSE` otherwise.  When no lambda is passed, the array has to be of type `BOOLEAN`, and the identity lambda `x -> x` is used.

### Performance Improvements

<!-- Auto Generated Markdown for FIR-36691 - Owned by Timo Kersten -->
**Improved performance of `JSON_EXTRACT`, `JSON_EXTRACT_ARRAY`, and `JSON_VALUE` functions**<br/>
Enhanced the performance of the `JSON_EXTRACT`, `JSON_EXTRACT_ARRAY`, and `JSON_VALUE` functions.


### Bug Fixes

<!-- Auto Generated Markdown for FIR-36881 - Owned by Mosha Pasumansky -->
**Corrected JSON output format to display NaN values consistently as `nan`**<br/>
The JSON output format previously showed some NaN values as `-nan`. This was corrected to consistently display NaN values as `nan` in the JSON output.


<!-- Auto Generated Markdown for FIR-36752 - Owned by Demian Hespe -->
**Resolved an issue with `CHECKSUM` and `HASH_AGG` failing when combining literals and table columns**<br/>
Fixed an issue where the `CHECKSUM` and `HASH_AGG` functions failed when used with a combination of literals and table columns.


<!-- Auto Generated Markdown for FIR-36849 - Owned by Lorenz Hübschle -->
**Fixed a rare inaccuracy that could cause incorrect results on multi-node engines when performing certain `UNION ALL` operations**<br/>
Fixed a rare inaccuracy when performing certain `UNION ALL` operations on subqueries that are the result of aggregations or joins on overlapping but distinct keys, followed by an aggregation or join on the common keys of the subqueries' aggregations or joins.


<!-- Auto Generated Markdown for FIR-36783 - Owned by Lorenz Hübschle -->
**Fixed a rare inaccuracy that could cause incorrect results with CTEs using `RANDOM()` in specific join scenarios**<br/>
Fixed a rare inaccuracy that caused incorrect results when a common table expression using the `RANDOM()` function was used multiple times, and at least one of these uses was on the probe side of a join involving a primary index key of the underlying table.
