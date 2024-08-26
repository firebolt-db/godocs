## DB version 4.4
**August 2024**

## Breaking Changes

<!-- Auto Generated Markdown for FIR-35240 - Owned by Kfir Yehuda -->**Reserved the keyword GEOGRAPHY, requiring double quotes for use as an identifier**
{: style="color:red;"}

The word GEOGRAPHY is now a reserved keyword and must be quoted using double quotes for use as an identifier. For example, `create table geography(geography int);` will now fail, but `create table "geography" ("geography" int);` will succeed.

<!-- Auto Generated Markdown for FIR-34196 - Owned by Pascal Schulze -->**Deprecated the legacy HTTP ClickHouse headers**
{: style="color:red;"}

We no longer accept or return the legacy HTTP ClickHouse header format `X-ClickHouse-*`.

<!-- Auto Generated Markdown for FIR-35190 - Owned by Kfir Yehuda -->**Fixed `json_value` zero-byte handling**
{: style="color:red;"}

The `json_value` function no longer returns null characters (0x00), as the TEXT datatype does not support them. For example, `select json_value('"\u0000"');` now results in an error.

<!-- Manually Generated Markdown for FIR-36032 - Owned by Paul Edgington -->**Change default values for NODES and TYPE during CREATE ENGINE**
{: style="color:red;"}

When performing a CREATE ENGINE, the default values for NODES and TYPE parameters have changed. NODES defaults to `2` (previously `1`) and TYPE defaults to `M` (previously `S`). To create an engine with the previous default values, run the following command:

```sql
CREATE ENGINE my_engine WITH NODES=1 TYPE=S
```

## New Features

<!-- Auto Generated Markdown for FIR-24598 - Owned by Leonard von Merzljak -->**Extended support for date arithmetic**

Now you can subtract two dates to get the number of elapsed days. For example, `DATE '2023-03-03' - DATE '1996-09-03'` produces `9677`.

<!-- Auto Generated Markdown for FIR-32335 - Owned by Krishna Thotapalli -->**Role-based permissions for COPY FROM and external tables**

Added support for role-based permissions (ARNs) to the COPY FROM command and external table operations.

<!-- Auto Generated Markdown for FIR-35164 - Owned by Ivan Koptiev -->**Added `trust_policy_role` column to `information_schema.accounts` view for S3 access**

Added a new column `trust_policy_role` to the `information_schema.accounts` view. This column shows the role used by Firebolt to access customer S3 buckets.

<!-- Auto Generated Markdown for FIR-24797 - Owned by Tali Magidson -->**Enabled selection of external tables' pseudo columns without adding data columns**

Users can now select an external table's pseudo columns (source file name, timestamp, size, and etag) without adding any data columns. For example, `select $source_file_timestamp from t_external` returns the file timestamps for each row. The query `select count($source_file_timestamp) from t_external` returns the total number of rows in the external table, similar to `count(*)`. The query `select count(distinct $source_file_name) from t_external` returns the number of distinct objects containing at least one row in the source S3 location.
Regarding `count(*)` performance, formats like CSV or JSON still require reading the data fully to determine an external file's row count. However, Parquet files provide the row count as part of the file header, and this is now used instead of reading the full data.

<!-- Auto Generated Markdown for FIR-33707 - Owned by Zhen Li -->**Extended support for arbitrary join conditions, including multiple inequality predicates**

We now support more join conditions. As long as there is one equality predicate comparing a left column to a right column of the join (not part of an OR expression), the remaining join condition can now be an arbitrary expression. The limitation on the number of inequality predicates was removed.

<!-- Auto Generated Markdown for FIR-35507 - Owned by Benjamin Wagner -->**New functions `URL_ENCODE` and `URL_DECODE`**

We added support for the `URL_ENCODE` and `URL_DECODE` functions.

<!-- Auto Generated Markdown for FIR-35480 - Owned by Mosha Pasumansky -->**New function `SQRT**

Added support for the `SQRT` function to compute the square root.

<!-- Auto Generated Markdown for FIR-33990 - Owned by Kfir Yehuda -->
<!-- Auto Generated Markdown for FIR-35214 - Owned by Kfir Yehuda -->**New functions `JSON_VALUE`, `JSON_VALUE_ARRAY`, `JSON_EXTRACT_ARRAY`**

Added support for the functions `JSON_VALUE`, `JSON_VALUE_ARRAY`, and `JSON_EXTRACT_ARRAY`.

<!-- Auto Generated Markdown for FIR-34266 - Owned by Mariia Kaplun -->**New function `SESSION_USER`**

Support has been added for the `SESSION_USER` function, which retrieves the current user name.
<!-- also added documentation for the following functions: CURRENT_DATABASE, CURRENT_ENGINE, CURRENT_ACCOUNT -->

<!-- Auto Generated Markdown for FIR-34678 - Owned by Pascal Schulze -->**New columns in `information_schema.engine_query_history`**

Added two new columns to `information_schema.engine_query_history`: `query_text_normalized_hash` and `query_text_normalized`.


## Bug Fixes

<!-- Auto Generated Markdown for FIR-35343 - Owned by Judson Wilson -->**Fixed directory structure duplication in the S3 path when using the COPY TO statement with SINGLE_FILE set to FALSE**

Fixed an issue in `COPY TO` when `SINGLE_FILE=FALSE`. Previously, the specified directory structure in the location was repeated twice in the S3 path. For example, files were output to "s3://my-bucket/out/path/out/path/" instead of "s3://my-bucket/out/path/".

<!-- Manually Generated Markdown for FIR-32830 - Owned by Judson Wilson -->**Fixed the file extension in the S3 path when using the COPY TO statement with GZIP-Parquet format**

Fixed an issue in `COPY TO` when `TYPE=PARQUET` and `COMPRESSION=GZIP`, which uses the Parquet file format with internal GZIP compression for the columns. Previously, the output files would have the extension ".parquet.gz". Now, the extension is ".gz.parquet".
