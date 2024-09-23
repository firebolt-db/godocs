# Firebolt Release Notes - Version 4.6

## Breaking Changes

<!-- Auto Generated Markdown for FIR-35643 - Owned by Pascal Schulze -->
**Introduced `SHOW CATALOGS` statement and aliased `SHOW DATABASES` to it while deprecating `SHOW DATABASE X`**
{: style="color:red;"}

A new statement `SHOW CATALOGS` now acts as an alias for `SHOW DATABASES`. The statement `SHOW DATABASE X` is no longer supported.

<!-- Auto Generated Markdown for FIR-31001 - Owned by Asya Shneerson -->
**`COPY FROM` now unzips Parquet files with gzip extensions**
{: style="color:red;"}

Before version 4.6, the `COPY FROM` command did not apply file-level decompression to Parquet files with a `.gzip` or `.gz` extension. The command treated these files as standard Parquet files, assuming that any compression existed only within the internal Parquet format structure.

With the release of version 4.6, `COPY FROM` now processes Parquet files similarly to other formats. When a Parquet file has a `.gz` or `.gzip` extension, the command will first decompress the file before reading it as a Parquet format file. Hence, it will now fail while reading internally compressed Parquet files with gzip extensions. Users experiencing issues with loading files after this change should contact the support team at support@firebolt.io for assistance.

## Performance Improvements

<!-- Auto Generated Markdown for FIR-31001 - Owned by Asya Shneerson -->
**`COPY FROM` support for filtering by source file metadata**<BR>
[COPY FROM](https://docs.firebolt.io/sql_reference/commands/data-management/copy-from.html) now supports filtering by source file metadata using the `WHERE` clause.

## New Features

<!-- Auto Generated Markdown for FIR-34445 - Owned by Pascal Schulze -->
**Added support for vector distance calculations with new functions**
Firebolt has added support for vector distance and similarity calculations with the following new functions: [VECTOR_COSINE_DISTANCE](https://docs.firebolt.io/sql_reference/functions-reference/array/vector-cosine-distance.html), [VECTOR_MANHATTAN_DISTANCE](https://docs.firebolt.io/sql_reference/functions-reference/array/vector-manhattan-distance.html), [VECTOR_EUCLIDEAN_DISTANCE](https://docs.firebolt.io/sql_reference/functions-reference/array/vector-euclidean-distance.html), [VECTOR_SQUARED_EUCLIDEAN_DISTANCE](https://docs.firebolt.io/sql_reference/functions-reference/array/vector-squared-euclidean-distance.html), [VECTOR_COSINE_SIMILARITY](https://docs.firebolt.io/sql_reference/functions-reference/array/vector-cosine-similarity.html), and [VECTOR_INNER_PRODUCT](https://docs.firebolt.io/sql_reference/functions-reference/array/vector-inner-product.html).


## Bug Fixes

<!-- Auto Generated Markdown for FIR-35653 - Owned by Alex Hall -->
**Fixed a rare bug that caused some query failures from incorrect computation of cacheable subresults**
Fixed a rare bug impacting the logic that determined which subresults could be cached and reused. This issue could have caused query failures in certain patterns, but it did not impact the accuracy of the query outcomes.

<!-- Auto Generated Markdown for FIR-36315 - Owned by Jonathan Doron -->
**Updated name of aggregatefunction2 to aggregatefunction in explain output**
The name `aggregatefunction2` has been updated to `aggregatefunction` in the [EXPLAIN](https://docs.firebolt.io/sql_reference/commands/queries/explain.html) output.

<!-- Auto Generated Markdown for FIR-35760 - Owned by Andres Senac -->
**Fixed incorrect results in `ARRAY_AGG` expressions by excluding `NULL` values for false conditions in aggregating indexes**
Aggregate expressions like `ARRAY_AGG(CASE WHEN <cond> THEN <column> ELSE NULL END)` previously returned incorrect results by excluding `NULL` values for rows when the condition was `FALSE`. As a result, any aggregating index that used this expression aggregate expression had to be removed and recreated after upgrading an engine version to ensure correct behavior.
