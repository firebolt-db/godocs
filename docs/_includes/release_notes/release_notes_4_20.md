## Firebolt Release Notes - Version 4.20

### New Features

<!-- Auto Generated Markdown for FIR-42182  -->
**Introduced the [ARRAYS_OVERLAP]({% link sql_reference/functions-reference/array/arrays-overlap.md %}) function to identify shared elements in input arrays**  
Introduced the `ARRAYS_OVERLAP` function to determine if two or more input arrays share common elements. This enhancement enables users to identify overlapping array elements, improving data analysis capabilities.

<!-- Auto Generated Markdown for FIR-44728  -->
**Added the [NGRAM]({% link sql_reference/functions-reference/string/ngram.md %}) function to generate overlapping n-grams from text**  
Added a new scalar function: `NGRAM`. The function `NGRAM(n, text)` generates a sequence of overlapping n-grams from the given text. Each n-gram is a contiguous substring of n characters. It returns the result as an SQL array of text. This function is useful for text analysis and can help in search queries. 

**Example**:
```sql
SELECT ngram(4, 'abc😊def');
```
**Results**:
```
{abc😊,bc😊d,c😊de,😊def}
```

<!-- Manually added for FIR-27429 -->
**Added support for [VALUES]({% link sql_reference/commands/queries/select.md %}#values-lists) lists to create constant tables**  
Added support for `VALUES` lists to create an in-memory constant table with one or multiple rows for use in queries.
For example:
```
SELECT * FROM (VALUES (1, 'one'), (2, 'two'), (3, 'three')) AS t (num, letter);
```
is effectively equivalent to:
```
SELECT 1 AS num, 'one' AS letter
UNION ALL
SELECT 2, 'two'
UNION ALL
SELECT 3, 'three';
```
Syntactically, `VALUES` can be used anywhere a `SELECT` is allowed.

<!-- Auto Generated Markdown for FIR-45478  -->
**Added support for `$$` to quote multiline string literals containing newlines and single quotes**  
Added support for `$$` to quote string literals that contain newlines and single quotes. This enhancement helps users create multiline strings without needing to escape special characters, making SQL scripts easier to read and maintain. For example:

```sql
SELECT $$
That's a 
   multi-line
     string
       literal
$$
```


### Performance Improvements

<!-- Auto Generated Markdown for FIR-35306 -->
**Improved Aggregating index scan performance by eliminating unnecessary re-aggregation**  
The Aggregating index scan now detects when data is already fully aggregated. It directly projects results without re-aggregating. This improvement reduces query latency and increases performance for applicable workloads.


<!-- Auto Generated Markdown for FIR-44559 -->
**Enhanced schema discovery performance for Parquet files in `COPY FROM` and `READ_PARQUET()` functions**  
Enhanced the performance of [Automatic Schema Discovery](/sql_reference/commands/data-management/copy-from/#automatic-schema-discovery) for Parquet files in the `COPY FROM` command and the `READ_PARQUET()` function. This improvement accelerates data loading and processing for users.


### Bug Fixes

<!-- Auto Generated Markdown for FIR-45223  -->
**Fixed the `information_schema.tables.ddl` output for tables using `TO_...` family of functions in the partition expression**  
Fixed the `information_schema.tables.ddl` output for tables with a partition expression such as `TO_YYYYMMDD`. This update ensures that the expression no longer incorrectly results in the `TO_YEARMONTHDAY` function.
