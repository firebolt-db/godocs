## Firebolt Release Notes - Version 4.10

### New Features

**Added `CREATE TABLE CLONE` to clone an existing table in a database**

You can create a clone of an existing table in a database using `CREATE TABLE CLONE`, which is extremely fast because it copies the table structure and references without duplicating the data. The clone functions independently of the original table. Any changes to the data or schema of either table will not affect the other.

<!-- Auto Generated Markdown for FIR-35649 - Owned by Amit Schreiber -->
**Added 3-part identifier support for specifying databases in queries**

You can now reference a database other than the current one in queries by using 3-part identifiers, which specify the database, schema, and object. For example, even if you previously selected a database `db`
by using `USE DATABASE db`, you can still query a different database by using a query such as
`SELECT * FROM other_db.public.t`. The limitation still exists that every query only addresses a single database.

**Added `ALTER TABLE ADD COLUMN` to add a column to an existing table**

You can now use `ALTER TABLE ADD COLUMN` to add columns to Firebolt-managed tables.
This functionality is temporarily limited to tables that were created on Firebolt version 4.10 or higher.

<!-- Auto Generated Markdown for FIR-38051 - Owned by chen.burshtein -->**Added support of `ALTER TABLE RENAME` command**
You can use `ALTER TABLE RENAME` to change the name of Firebolt-managed tables.
This functionality is temporarily limited to tables created on Firebolt version 4.10 or higher.

<!-- FIR-38051 - Owned by Asya Shneerson --> 
**Added support for external file access using AWS session tokens**          

You can now use `<AWS_SESSION_TOKEN>` with access keys to securely authenticate and access external files on AWS with the following features: 

* The [COPY TO]({% link sql_reference/commands/data-management/copy-to.md %}) and [COPY FROM]({% link sql_reference/commands/data-management/copy-from.md %}) commands.
* [External tables]({% link Guides/loading-data/working-with-external-tables.md %}) located in an Amazon S3 bucket.
* The following table-valued functions: `read_parquet`, `read_csv`, and `list_objects`.

### Behavior Changes

<!-- Auto Generated Markdown for FIR-25824 - Owned by Kfir Yehuda -->
**Enhanced PostgreSQL compliance for casting data types from text to float**

Cast from text to floating-point types is now compliant with PostgreSQL with the following improvements: 

1. **The correct parsing of positive floats** &ndash; A plus sign (`+`) preceding a float is now handled correctly. Example: `'+3.4'`.
2. **Exponent-only input** &ndash; Float values starting with an exponent `'e'` or `'E'` are rejected. Example: `'E4'`.
3. **Incomplete exponents** &ndash; Float values ending with an exponent without a subsequent exponent value are rejected. Example: `'4e+'`.

<!--FIR-38448 - Owned by Dan Englund -->
**Account-level rate limits implemented for the system engine**

Firebolt has implemented account-level rate limits to ensure equitable resource usage among all users of the system engine. When these limits are exceeded, requests will be rejected with the following error message: `429: Account system engine resources usage limit exceeded`. This rate limit targets accounts with exceptionally high resource consumption. Accounts with typical resource usage should not be affected and require no further action.

### Bug Fixes

<!-- Auto Generated Markdown for FIR-37817 - Owned by Demian Hespe -->
**Corrected runtime reporting**

Resolved an issue where the runtime displayed in Firebolt's user interface and JSON responses omitted including processing times for some query steps. 

<!-- Auto Generated Markdown for FIR-38001 - Owned by Zhen Li -->
**Resolved "Invalid Input Aggregate State Type" error with aggregating indexes**

Fixed an issue where the "invalid input aggregate state type" error could occur when queries read from aggregating indexes that defined a `COUNT(*)` aggregate function before other aggregate functions. After this fix, such aggregating indexes can now be queried correctly without needing to be rebuilt.

<!-- Auto Generated Markdown for FIR-35653 - Owned by Alex Hall -->
**Fixed a rare bug in subresult caching logic**

Addressed a rare issue in the logic for caching and reusing subresults that could cause query failures with specific query patterns. This issue did not impact the correctness of query results.

<!-- Markdown for FIR-38446 - Owned by Vitaliy Liudvichenko -->
**Resolved issue preventing schema owners from granting "ANY" privileges**

Fixed an issue where schema owners were unable to grant "ANY" privileges on their schema to other users.      
For example:

```sql
GRANT SELECT ANY ON SCHEMA public TO ...
```
Schema owners can now execute this command which allows the specified user or role to perform SELECT operations on any table. 