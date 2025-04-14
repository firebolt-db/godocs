---
redirect_from:
  - /sql-reference/commands/create-fact-dimension-table.html
layout: default
title: CREATE TABLE
description: Reference and syntax for the CREATE TABLE statement.
parent: Data definition
---

# CREATE TABLE

Creates a new table in the current database.

* Topic ToC
{:toc}


## Syntax
{: .no_toc}

```sql
CREATE [FACT|DIMENSION] TABLE [IF NOT EXISTS] <table_name>
(
    <column_name> <column_type> [constraints]
    [, <column_name> <column_type> [constraints]
    [, ...n]]
)
[PRIMARY INDEX <column_name>[, <column_name>[, ...k]]]
[PARTITION BY <column_name>[, <column_name>[, ...m]]]
[WITH ( <storage_parameter> = <storage_parameter_value>[, <storage_parameter> = <storage_parameter_value>[, ...p]] ) ]
```

## Parameters 
{: .no_toc} 

| Parameter                   | Description                                                                                                      |
| :-------------------------- | :--------------------------------------------------------------------------------------------------------------- |
| `<table_name>`              | An identifier that specifies the name of the table. This name should be unique within the database.              |
| `<column_name>`             | An identifier that specifies the name of the column. This name should be unique within the table.                |
| `<column_type>`             | Specifies the data type for the column.                                                                          |
| `<storage_parameter>`       | The name of a [storage parameter](#storage-parameters) for controlling behaviors related to storage and indexes. |
| `<storage_parameter_value>` | The value assigned to a `<storage_parameter>`.                                                                   |

All identifiers are case-insensitive unless enclosed in double-quotes. For more information, see [Object identifiers]({% link Reference/object-identifiers.md %}).

## Column constraints and the default expression

Firebolt supports the following column constraints:

```sql
<column_name> <column_type> [NULL | NOT NULL] [DEFAULT <expression>]
```


| Constraint           | Description                                                                                                                                                                                                                | Default value |
| :-------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------- |
| `DEFAULT <expression>`     | Determines the default value used when no value is provided, instead of inserting a `NULL` value.                                                                                                                                               |               |
| `NULL` \| `NOT NULL` | Determines if the column may or may not contain `NULL` values.                                                                                                                                                                     | `NULL`    |

{: .note}
Only literals and the following functions are supported in default expressions: [CURRENT_DATE]({% link sql_reference/functions-reference/date-and-time/current-date.md %}), [LOCALTIMESTAMP]({% link sql_reference/functions-reference/date-and-time/localtimestamp.md %}), [CURRENT_TIMESTAMP]({% link sql_reference/functions-reference/date-and-time/current-timestamptz.md %}), and NOW, which is an alias for CURRENT_TIMESTAMP.

### Example: Creating a table with `NULL` and `NOT NULL` values

The following example illustrates different use cases for column definitions and `INSERT` statements:

* An **Explicit** `NULL` insert &ndash; a direct insertion of a `NULL` value into a particular column.
* An **Implicit** `NULL` insert &ndash; an `INSERT` statement with missing values for a particular column.

The following example creates a fact table `t1` with five columns, specifying if each column can contain `NULL` values, their default values, and a primary index on `col2`:

```sql
CREATE FACT TABLE t1
(
    col1 INTEGER  NULL,
    col2 INTEGER  NOT NULL,
    col3 INTEGER  NULL DEFAULT 1,
    col4 INTEGER  NOT NULL DEFAULT 1,
    col5 TEXT
)
PRIMARY INDEX col2;
```

After creating a table, you can manipulate the values using different `INSERT` statements, as shown in the following examples:

| INSERT statement | Results and explanation  |
| :--------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `INSERT INTO t1 VALUES (1,1,1,1,1)`                                                                                               | This code example inserts `1` into each column.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `INSERT INTO t1 VALUES (NULL,1,1,1,1)`                                                                                            | This code example explicitly inserts a `NULL` value into `col1`. Because `col1` can contain `NULL` values, this operation is successful.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `INSERT INTO t1 (col2,col3,col4,col5) VALUES (1,1,1,1)`                                                                           | This code example shows both explicit and implicit `INSERT` statements. Because `col1` has no value specified, and lacks a default expression, it is implicitly set to `NULL`.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `INSERT INTO t1 VALUES (1,NULL,1,1,1)`<br> <br>`INSERT INTO t1 (col1,col3,col4,col5) VALUES (1,1,1,1)` | This code example shows how a **null mismatch** error is generated. Because `col2` is defined as `NOT NULL` with no default expression, both `INSERT` statements implicitly try to insert `NULL` values into `col2`, and generate “null mismatch” events. |
| `INSERT INTO t1 VALUES (1,1,NULL,1,1)`                                                                                            | This code example explicitly inserts a `NULL` value into `col3`. Because `col3` is defined as `NULL DEFAULT 1`, the operation is successful.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `INSERT INTO t1 (col1,col2,col4,col5) VALUES (1,1,1,1)`                                                                           | By not specifying a value for `col3`, this code example implicitly inserts the default value `1` into `col3`, which is defined as `NULL DEFAULT 1`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `INSERT INTO t1 VALUES (1,1,1,NULL,1)`                                                                                            | This code example shows how another **null mismatch** error is generated. Because `col4` is defined as `NOT NULL DEFAULT 1`, the explicit insertion of a `NULL` value violates the `NOT NULL` constraint, and results in a null mismatch event.                                                                                                                                                                                                                                                                                                                                                                                                    |
| `INSERT INTO t1 (col1,col2,col3,col5) VALUES (1,1,1,1)`                                                                           | This code example shows how omitting a value in an implicit insert invokes the default value `1` for `col4`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `INSERT INTO t1 VALUES (1,1,1,1,NULL)`<br><br>`INSERT INTO t1 (col1,col2,col3,col4) VALUES (1,1,1,1)` | This code example shows how explicit and implicit inserts cause a **null mismatch** error. Because `col5` was neither defined with a default expression nor allowed to contain `NULL` values, Firebolt treats `col5` as `NOT NULL DEFAULT NULL`. Both `INSERT` statements attempt to insert a `NULL` value into a `NOT NULL TEXT` column, invoking in a null mismatch event.                                                                                                                                                                                                                        |

### PRIMARY INDEX

The `PRIMARY INDEX` is an optional sparse index that sorts and organizes data based on the indexed field as it is ingested, without affecting data scan performance. For more information, see [Primary index]({% link Overview/indexes/primary-index.md %}).

#### Syntax
{: .no_toc}

```sql
PRIMARY INDEX <column_name>[, <column_name>[, ...n]]
```

The following table describes the primary index parameters:

| Parameter.      | Description                                                                                                                                  | Mandatory? |
| :--------------- | :-------------------------------------------------------------------------------------------------------------------------------------------- | :---------- |
| `<column_name>` | Specifies the name of the column in the Firebolt table which composes the index. At least one column is required. | Y          |

### PARTITION BY

The `PARTITION BY` clause defines one or more columns that determine how the table is divided into physical parts. These columns serve as the partition key and cannot allow `NULL` values. When multiple columns are used as the partition key, the combination of all of these columns define the partition boundaries.

```sql
PARTITION BY <column_name>[, <column_name>[, ...n]]
```

The following subset of SQL functions can be used in `PARTITION BY` expressions:

* [TO_YYYYMM]({% link sql_reference/functions-reference/date-and-time/to-yyyymm.md %})
* [TO_YYYYMMDD]({% link sql_reference/functions-reference/date-and-time/to-yyyymmdd.md %})
* [EXTRACT]({% link sql_reference/functions-reference/date-and-time/extract.md %})`(year|month|day|hour from <column_name>)`
* [DATE_TRUNC]({% link sql_reference/functions-reference/date-and-time/date-trunc.md %})

For more information, see [Working with partitions]({% link Overview/indexes/using-indexes.md %}#partitions-in-tables).

### Table type

Firebolt supports two types of [tables]({% link Overview/indexes/using-indexes.md %}#tables):
    
* `FACT` table - the data is distributed across all nodes of the engine.
* `DIMENSION` table - the entire table is replicated in every node of the engine.

The [CREATE TABLE]({% link sql_reference/commands/data-definition/create-fact-dimension-table.md %}) command defaults to a `FACT` table. `DIMENSION` tables are ideal for relatively small tables, up to tens of gigabytes, that are used in joins with `FACT` tables.

## Storage Parameters
{: .no_toc} 

Storage parameters are specified in the optional `WITH (...)` clause as comma separated `<storage_parameter> = <storage_parameter_value>` assignments.

| Storage Parameter     | Description                                                                                                                                                                                                                                                                          |
| :-------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<index_granularity>` | The maximum number of rows in each granule. `<storage_parameter_value>` must be a power of 2 between 128 and 8192. The default value is 8192. For more information, see [Index granularity]({% link Overview/indexes/primary-index.md %}#advanced-option-index-granularity). |
| `<compression>` | The compression to use at the table level. The default value is `LZ4`. For more information, see [Custom Compression]({% link Overview/table-and-column-compression.md %}). |
| `<compression_level>` | The compression level to use  for the specidfied compression. This parameter cannot be set without `compression`. For more information, see [Custom Compression]({% link Overview/table-and-column-compression.md %}). |

All identifiers are case-insensitive unless enclosed in double-quotes. For more information, see [Object identifiers]({% link Reference/object-identifiers.md %}).

## Related functions

Firebolt also supports the following related functions:
* [CREATE TABLE AS SELECT (CTAS)]({% link sql_reference/commands/data-definition/create-fact-dimension-table-as-select.md %}) &ndash; - Creates a table and loads data into it based on a `SELECT` query. 
* [CREATE TABLE CLONE]({% link sql_reference/commands/data-definition/index.md %}) &ndash; Creates a table that is a copy of an existing table in the database.
