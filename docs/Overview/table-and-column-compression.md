---
layout: default
title: Table and Column Compression
description: Learn about custom compression for managed tables
parent: Overview
nav_order: 7
has_children: true

---

# Custom column and table compression
{: .no_toc}

## Overview

Firebolt allows users to specify a custom compression algorithm at both the table level and the column level when creating a table. Compression helps you reduce storage costs and improve query performance by decreasing disk usage and I/O.

## Supported compression algorithms

Firebolt supports the following compression algorithms:

- `lz4`&ndash; Default option; fast compression and decompression, ideal for general workloads. 
- `zstd`&ndash; Higher compression ratios at the cost of increased CPU usage; useful for large datasets. 

{: .note}
Disabling compression with `NONE` is not supported. Firebolt always compresses data using one of the supported algorithms. 

## Specify compression settings

You can specify compression settings for a table, columns, or a combination of both when creating tables: 
* [Table-level compression](#table-level-compression) sets a default compression method for all columns. 
* [Column-level compression](#column-level-compression) overrides the table-level default for individual columns. 
  
### Table-level compression

You specify table-level compression using the `WITH` clause in the `CREATE TABLE` statement. This compression applies to all columns unless explicitly overriden at the column level. 

##### Syntax:
{: .no_toc}

Use the following syntax to set table-level and/or column-level compression. 

```sql
CREATE TABLE table_name (
    column1 data_type COMPRESSION algorithm COMPRESSION_LEVEL level, 
    column2 data_type COMPRESSION algorithm,
    column3 data_type 
) 
WITH (COMPRESSION = algorithm, COMPRESSION_LEVEL =level);
```
##### Compression level
{: .no_toc}

* The optional `COMPRESSION_LEVEL` parameter lets you fine-tune the balance between compression efficiency and CPU usage. 
* Higher values provide greater comparison but increase CPU overhead. 
* Firebolt uses algorithm-specific default levels if no level is specified. 

##### Default behavior
{: .no_toc}

* If you don't specify column-level compression. Firebolt applies the table-level setting. 
* If no table-level setting is provided, Firebolt defaults to `lz4` . 


##### Example:
{: .no_toc}

The following code creates a table with ZTSD compression:

```sql
CREATE TABLE sales (
    a INT
) WITH (compression=zstd, compression_level=15);
```

### Column-level compression

Column-level compression allows you to override table-level compression settings for specific columns. This approach is useful for columns that have different compression requirements, such as large text fields or numerical columns. 

##### Syntax:
{: .no_toc}

```sql
CREATE TABLE table_name (
    column1 data_type COMPRESSION algorithm COMPRESSION_LEVEL level,
    column2 data_type COMPRESSION algorithm,
    column3 data_type
);
```

##### Compression level
{: .no_toc}

* The `compression_level` parameter fine-tunes compression efficiency versus CPU usage.
* Higher compresson levels reduce storage but consume more CPU resources during compression and decompression.
* If not specified, Firebolt applies a default compression level appropriate for the selected algorithm. 

##### Default behavior
{: .no_toc}

* If you do not specify compression explicitly, Firebolt applies the default `lz4` compression algorithm. 
* When you define table-level compression, all columns inherit this setting unless overriden with column-level compression. 

## Step-by-step examples of compression
The following examples show how to use table-level and column-level compression in Firebolt.

**Step 1: Create and populate an uncompressed table**                     
Create a base table without custom compression and populate it with data using `GENERATE_SERIES`

```sql
-- create the target table
CREATE TABLE origin_no_compression (a int, b int, c string, d string);
-- insert 10000 rows
INSERT INTO origin_no_compression SELECT 1, 2, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 'In dapibus metus quis velit mattis dignissim.' FROM GENERATE_SERIES(1,10000) ;
```

**Step 2: Apply table-level compression**                                               
Create a new table using ZTSD compression and compression level 15, applying the setting to all columns:

```sql
CREATE TABLE table_a_column_level_zstd(a int COMPRESSION zstd COMPRESSION_LEVEL 15, b int, c string, d string);
CREATE TABLE table_a_b_column_level_zstd(a int COMPRESSION zstd COMPRESSION_LEVEL 15, b int COMPRESSION zstd COMPRESSION_LEVEL 15, c string, d string);
CREATE TABLE table_c_column_level_zstd(a int , b int, c string COMPRESSION zstd COMPRESSION_LEVEL 15, d string);
CREATE TABLE table_c_d_column_level_zstd(a int , b int, c string COMPRESSION zstd COMPRESSION_LEVEL 15, d string COMPRESSION zstd COMPRESSION_LEVEL 15);
```

Insert data into these tables from the `origin_no_compression` table: 

```sql
INSERT INTO table_a_column_level_zstd SELECT * FROM origin_no_compression;
INSERT INTO table_a_b_column_level_zstd SELECT * FROM origin_no_compression;
INSERT INTO table_c_column_level_zstd SELECT * FROM origin_no_compression;
INSERT INTO table_c_d_column_level_zstd SELECT * FROM origin_no_compression;
```

**Step 3: Apply column-level compression**                                              
Next, create tables demonstrating column-level compression configuration: 

```sql
CREATE TABLE table_a_b_column_level_zstd (
    a INT COMPRESSION zstd COMPRESSION_LEVEL 15,
    b INT COMPRESSION zstd COMPRESSION_LEVEL 15,
    c STRING,
    d STRING
);
```

**Step 4: Compare compression results**                                             
Check the `compressed_byte` value of the tables to evaluate the effectiveness of compression settings:

```sql
SELECT compressed_bytes,table_name
FROM information_schema.tables
WHERE table_name = 'origin_no_compression'
   OR table_name = 'table_a_column_level_zstd'
   OR table_name = 'table_a_b_column_level_zstd'
   OR table_name = 'table_c_column_level_zstd'
   OR table_name = 'table_c_d_column_level_zstd'
ORDER BY table_name;
```

### Example results                                          
These are typical results from a single-node engine, showing how different compression methods and column-level settings affect table sizes: 

| compressed_bytes | table_name                      |
|-----------------|---------------------------------|
| 4772            | origin_no_compression          |
| 4396            | table_a_b_column_level_zstd    |
| 4584            | table_a_column_level_zstd      |
| 2558            | table_c_column_level_zstd      |
| 763             | table_c_d_column_level_zstd    |

Column-level expression significantly reduces storage for specific columns, as demonstrated in these examples, and ZSTD typically offers higher compression efficiency compared to the default LZ4. 