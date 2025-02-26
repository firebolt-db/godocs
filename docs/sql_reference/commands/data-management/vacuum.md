---
redirect_from:
  - /sql-reference/commands/vacuum.html
layout: default
title: VACUUM
description: Reference and syntax for the VACUUM command.
great_grand_parent: SQL reference
grand_parent:  SQL commands
parent: Data management
---

# VACUUM
{: .no_toc}

Optimizes tablets, selects small or fragmented ones, and restructures them for optimal query performance. `VACUUM` optimizes both tables and aggregate indexes unless explicitly configured otherwise.  

A tablet is a physical storage unit in Firebolt that holds a subset of table data. Firebolt divides tables into tablets to optimize query execution and parallel processing. Over time, [`DELETE`]({% link sql_reference/commands/data-management/delete.md %}), [`UPDATE`]({% link sql_reference/commands/data-management/update.md %}), [`INSERT`]({% link sql_reference/commands/data-management/insert.md %}), and [`COPY FROM`]({% link sql_reference/commands/data-management/copy-from.md %}) modify data and affect tablet structure, potentially leading to **suboptimal tablets** that degrade performance.  

Use `VACUUM` to merge small tablets and remove deleted rows, improving query performance and storage efficiency, especially for frequently updated tables. Run `VACUUM` **regularly** to ensure efficient storage and fast queries.

**Topics**:

* [Syntax](#syntax)
* [Parameters](#parameters)
* [Options](#options)
* [Examples](#examples)
* [Best practices](#best-practices)

## Syntax

```text
VACUUM [ (INDEXES = ALL | NONE, MAX_CONCURRENCY = <number>) ] <table>
```

## Parameters 
 

| Parameter | Description|
| :---------| :----------|
| `<table>`| The table to optimize. |


## Options  
  

| Option               | Syntax Format                          | Description  |
|----------------------|--------------------------------------|--------------|
| **`INDEXES`**        | `INDEXES = ALL` (default)            | Optimizes both the table and all its aggregating indexes. |
|                      | `INDEXES = NONE`                     | Optimizes only the table, excluding indexes. |
| **`MAX_CONCURRENCY`** | `MAX_CONCURRENCY = <number>`        | Sets the maximum number of concurrent jobs to use for optimization. |



## Examples
{: .no_toc}

**Optimize a table including its indexes**

The following code example optimizes the `games` table, including all its aggregating indexes:

```sql
VACUUM games;
```

**Optimize a table without including its indexes**

The following code example optimizes the `players` table without affecting its aggregating indexes:

```sql
VACUUM (INDEXES = NONE) players;
```

**Optimize a table with a single concurrent stream**

The following code example optimizes the `players` table using a single concurrent stream to limit resource usage:

```sql
VACUUM (MAX_CONCURRENCY = 1) players;
```

**Measure query performance before and after `VACUUM`** 

The following example shows how `VACUUM` optimizes query execution by reducing the impact of deleted rows and improving tablet efficiency.

The first step loads a small dataset from an Amazon S3 bucket into the `tutorial_vacuum` table and scales it to 10 million rows, which may take a few minutes to complete: 

```sql
COPY tutorial_vacuum 
FROM 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv'
WITH HEADER=TRUE;

INSERT INTO tutorial_vacuum
SELECT a.* FROM tutorial_vacuum a, GENERATE_SERIES(1, 1000000);
```

Next, the following code example deletes 90% of the rows, creating approximately 900,000 deleted entries. This simulates a table with a high number of deleted rows, allowing `VACUUM` to optimize storage and improve query efficiency:

```sql
DELETE FROM tutorial_vacuum WHERE "LevelID" > 1; 
```

The following code example measures query performance before and after running `VACUUM`:

```sql
SELECT hash_agg(*) FROM tutorial_vacuum;
VACUUM tutorial_vacuum;
SELECT hash_agg(*) FROM tutorial_vacuum;
```

In the previous example, the first `SELECT` statement processes data with many deleted rows, while the second is run after `VACUUM` optimizes the table. The following query history highlights the performance improvement from `VACUUM`:

| NO  | STATEMENT                                | STATUS   | DURATION   |
|:----|:-----------------------------------------|:---------|:-----------|
| 1   | `SELECT hash_agg(*) FROM tutorial_vacuum`; | Success  | 4.43 s     |
| 2   | `VACUUM tutorial_vacuum`;                  | Success  | 17.53 s    |
| 3   | `SELECT hash_agg(*) FROM tutorial_vacuum`; | Success  | 0.82 s     |

In the previous table, the first `SELECT` query ran for over 4 seconds, while the identical `SELECT` query after `VACUUM` ran in under 1 second. After running `VACUUM`, the query runtime decreased from 4.43 seconds to 0.82 seconds.

## Best practices 

* **Avoid conflicts with mutations** &ndash; `VACUUM` is non-blocking and runs alongside other operations. If a concurrent `INSERT`, `UPDATE`, or `DELETE` commits before `VACUUM` finishes, the table structure changes, reducing `VACUUM`'s effectiveness. To minimize conflicts, schedule `VACUUM` during **low-traffic periods** or run it on a **dedicated engine**.  

* **Handle transaction conflicts** &ndash; Applications running `INSERT`, `UPDATE`, or `DELETE` in parallel with `VACUUM` should gracefully handle transaction conflicts to maintain data consistency. The first operation to commit takes precedence. You can do the following to handle transaction conflicts:
    * Use retry mechanism with exponential backoff to avoid immediate retries flooding the system.
    * Capture and log transaction errors related to `VACUUM` to diagnose conflicts. For example, the following code example checks the `query_history` view in `information_schema` for failures:

        ``` sql
        SELECT * FROM information_schema.query_history 
        WHERE status = 'FAILED' AND query LIKE 'UPDATE%';
        ```
    * Run `VACUUM` during low-traffic periods to reduce conflicts with queries and data modifications.
    * Reduce the scope of altering tables and databases by breaking changes into smaller transactions to reduce the likelihood of conflicts. The following code example uses batch updates to a table instead of a single update:

        ```sql
        UPDATE orders SET status = 'shipped' WHERE order_id BETWEEN 100 AND 200;
        UPDATE orders SET status = 'shipped' WHERE order_id BETWEEN 201 AND 300;
        ```

    * Check for stale data before modifying data to ensure that rows still exist and haven't been altered by `VACUUM`. The following code example checks that the rows meeting a condition exist before updating them:

        ```sql
        SELECT * FROM orders WHERE order_id = 100 FOR UPDATE;
        ```

* **Manage resource usage** &ndash; `VACUUM` consumes compute and storage resources, especially for large or frequently modified tables. It runs multiple concurrent streams based on CPU cores, which can improve speed but increase memory usage. Use the `MAX_CONCURRENCY` option in `VACUUM` to limit parallel processing.  

* **Monitor storage impact** &ndash; `VACUUM` creates optimized versions of tablets, but older versions remain until garbage collection, which runs periodically in the background and removes them. This temporarily increases storage usage. You can check storage usage with the following code example that retrieves storage use for all tables:

```sql
SELECT table_name, used_size, deleted_size, row_count 
FROM information_schema.tables
WHERE table_schema = 'my_schema';
```

In the previous code example, the `used_size` is the amount of storage actively used, `deleted_size` is the size of deleted rows that have not been reclaimed by garbage collection, and `row_count` is the total number of rows in the table.

* **Use a dedicated engine if needed** &ndash; Running `VACUUM` on a separate engine than the one running queries prevents conflicts and ensures efficient resource allocation.  

* **Automate scheduling** &ndash; Use external tools like Airflow or custom scripts to schedule `VACUUM` automatically. See [Integrate with Firebolt]({% link Guides/integrations/integrations.md %}) for supported tools.  


