## Firebolt Release Notes - Version 4.19

### New Features

<!-- Manually added by Mosha for FIR-42774 -->
**Added support for [GROUPING SETS](../../../sql_reference/commands/queries/select.html#group-by-grouping-sets), [ROLLUP](../../../sql_reference/commands/queries/select.html#group-by-rollup) and [CUBE](../../../sql_reference/commands/queries/select.html#group-by-cube) clauses**  
Expanded SQL support with the addition of `GROUPING SETS`, `ROLLUP` and `CUBE` clauses for `GROUP BY` operations. These clauses enable more flexible and efficient multi-level aggregations in a single query, simplifying complex reporting and analytics workflows.
* `GROUPING SETS`: Specify multiple groupings in a single query.
* `ROLLUP`: Create subtotals that roll up from the most detailed level to a grand total.
* `CUBE`: Generate subtotals for all combinations of a set of columns.
These enhancements unlock more powerful data summarization directly within SQL.

<!-- Manually added by Mosha for FIR-24769 -->
**Added `COVAR_POP`, `COVAR_SAMP` and `CORR` functions**  
Added support for advanced statistical analysis directly in SQL with the introduction of the following aggregate functions:  
* [COVAR_POP]({% link sql_reference/functions-reference/aggregation/covar-pop.md %}) : Calculates the population covariance between two sets of values. 
* [COVAR_SAMP]({% link sql_reference/functions-reference/aggregation/covar-samp.md %}) : Computes the sample covariance. 
* [CORR]({% link sql_reference/functions-reference/aggregation/corr.md %}) : Returns the Pearson correlation coefficient. 
These functions enable deeper insight into relationships between variables, making it easier to perform in-database analytics without external tools.

<!-- Auto Generated Markdown for FIR-37933 - Owned by David Gichev -->
**Added [ARRAY_INTERSECT]({%link sql_reference/functions-reference/array/array-intersect.md %}) function to find common elements in arrays**          
Added a new function `ARRAY_INTERSECT`, which finds common elements across given arrays. This functionality simplifies operations that require comparing multiple arrays to identify shared items, enhancing data analysis capabilities.


**Added the ability to attach a certificate's public key to a service account using ALTER SERVICE ACCOUNT.**

<!-- Manually added by mshneer for FIR-44433 -->
**Added the ability to control an engine's Auto VACUUM behavior**  
`CREATE ENGINE` and `ALTER ENGINE` statements now support an `AUTO_VACUUM` parameter.

<!-- Manually added by Mariia Kaplun for FIR-42321 -->
**Added the ability to revoke a privilege for a specific object, even if the privilege is inherited via an ANY-privilege from its parent object.**     
We've added the ability to revoke a privilege for a specific object, even when that privilege is inherited through an ANY-privilege granted to the parent object. For example, if a `SELECT ANY` privilege is granted on a schema, it is now possible to revoke the `SELECT` privilege for a specific table within that schema.


### Performance Improvements

<!-- Auto Generated Markdown for FIR-44201 - Owned by jingtao.huang -->
**Reduced memory usage for the `COPY TO` function with `SINGLE_FILE=true`**          
Memory usage was reduced when using the `COPY TO` function with `SINGLE_FILE=true`. This change optimizes performance and resource efficiency, especially for users dealing with large datasets.


<!-- Auto Generated Markdown for FIR-44870 - Owned by Demian Hespe -->
**Enabled `RESULT` and `SUBRESULT` cache to reuse query results between user interface and JDBC connector**          
The `RESULT` and `SUBRESULT` cache now reuses query results between those sent from the user interface and those sent from the JDBC connector. This improves performance by reducing redundant computations.


<!-- Auto Generated Markdown for FIR-44352 - Owned by Lorenz Hübschle -->
**Rearchitected the Parquet reader for more predictable memory usage with external tables and the `READ_PARQUET` function**          
We have significantly rearchitected our parquet reader. This should lead to more predictable memory usage when reading from external tables or using the `READ_PARQUET` function and improve performance for many parquet workloads. More improvements, including bringing these changes to `COPY FROM`, will follow in upcoming releases.


<!-- Auto Generated Markdown for FIR-44191 - Owned by Lorenz Hübschle -->
**Improved join pruning to support more join types and pruning through window operators**          
Join pruning now supports almost any join between the table scan being pruned and the probe side of the join where pruning is applied. It now also supports pruning through window operators when the column used for pruning is included in all windows' `PARTITION BY` clause. This enhancement improves query performance by reducing unnecessary data processing.


### Behavior Changes

<!-- FIR-42938 - Owned by Mariia Kaplun -->
**Updated how ANY privileges are displayed in [information_schema.object_privileges]({%link sql_reference/information-schema/object-privileges.md %})**          
The representation of privileges in the `information_schema.object_privileges` has been updated so that all objects privileges granted to the user are explicitly enumerated.
So `usage any database on account` privilege will be expanded to:
- usage any database on account
- usage database db1
- usage database db2 ...

