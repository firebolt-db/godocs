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
Optimizes tablets for query performance.

`VACUUM` improves query efficiency by restructuring tablets for optimal performance. DML operations such as [DELETE](delete.md), [UPDATE](update.md), [INSERT](insert.md), and [COPY FROM](copy-from.md) might create tablets that are not optimally sized. Suboptimal tablets occur because DML efficiently utilizes resources in proportion to the cardinality of the data being inserted. In addition to standard SQL operations, tuples that are deleted by an update are not always physically removed from their table; they remain present until a `VACUUM` is finished operating. In other words, tablets are not necessarily optimal for running queries; therefore, it’s necessary to run `VACUUM` periodically, especially on frequently updated tables.

By default, any engine that processes a DML operation automatically assesses the health of tables’ data layout and runs the `VACUUM` command when necessary to maintain the underlying table health. You can disable Auto `VACUUM` for a specific engine using the 'ALTER ENGINE' statement:

```text
ALTER ENGINE <name> SET AUTO_VACUUM = OFF;
```

Firebolt recommends keeping the default setting to maintain optimal layout of your tables' underlying data.

You can also run `VACUUM` manually using the syntax and options described below.

## Syntax

```text
VACUUM [ (option_name = option_value) ] <table|aggregating index>
```
Where `<table|aggregating index>` is the name of the table or aggregating index to be optimized.

## Options
{: .no_toc}

| Option name | Option value and description         |
| :---------  | :----------------------------------- |
| `INDEXES`   | `FULL` &mdash; (Default) Specifies whether to apply optimizations to both the table and all its aggregating indexes.<br> `INCREMENTAL` &mdash; Similar to `FULL`, but will apply incremental optimizations to aggregating indexes, instead of complete reevaluation.<br> `NONE` &mdash; Optimizes only the table. |
| `MAX_CONCURRENCY`   | `<Number>` &mdash; The maximum number of concurrent jobs to use during optimization. |


## Examples
{: .no_toc}

**Optimize a table and its aggregating indexes**

Optimizing a table along with its aggregating indexes ensures that both the data and aggregating indexes remain efficient, reducing query latency and improving overall performance.
The following code example optimizes the `games` table and all its aggregating indexes:

```text
VACUUM games;
```

The example above performs a complete rebuild of related aggregating indexes. Alternatively, you can specify to apply incremental optimization, which still improves index layout while using fewer resources, though it may not achieve optimal layout:
```text
VACUUM (INDEXES = INCREMENTAL) games;
```

**Optimize a table without its indexes**

If you need to optimize a table without including its aggregating indexes to reduce resource usage, or retain efficient indexes, you can optimize only the table to prevent unnecessary computations.
The following code example optimizes the `players` table without updating its aggregating indexes:

```text
VACUUM (INDEXES = NONE) players;
```

Optimize table named `players`, using a single concurrent stream.

```text
VACUUM (MAX_CONCURRENCY = 1) players;
```

## Usage Notes

The following are considerations for running the `VACUUM` command:

### What happens during VACUUM
`VACUUM` analyzes the tablets, selects the ones that are too small or have too many deleted rows, and produces new versions that are optimized for query execution for both tablets and Aggregate Indexes.

`VACUUM` runs as a non-blocking process, alongside other user-initiated operations. Consequently, some changes performed by `VACUUM` may conflict with mutations run by the user.  If `VACUUM` and a user mutation modify the same data, the first committed operation takes precedence; see [Transactions and concurrency]({% link Overview/data-management.md %}#transactions-and-concurrency) for more details. This means that applications that run mutations in parallel with `VACUUM` should gracefully handle transaction conflicts. It also means that benefits of the `VACUUM` may be diminished by a mutation that committed data first.

### Space and performance considerations
Users must be aware that `VACUUM` consumes both compute and storage resources.
`VACUUM` can consume a considerable amount of compute resources depending on the table size, number of tablets, and number of mutations in the table.

`VACUUM` parallelizes its work into multiple concurrent streams, based on the number of CPU cores. While this can be beneficial for the speed of the operation, each stream consumes memory and CPU resources. Use the `MAX_CONCURRENCY` option to limit the number of concurrent streams.

`VACUUM` produces optimized versions of the data, while leaving behind older versions subject to the garbage collection (GC) process. These older tablets will continue to consume storage space until the GC process completes the clean-up.

If users would like to have precise control over `VACUUM`, it may be preferable to run on a dedicated engine that could be sized and run just for `VACUUM` operations. With `VACUUM` running on a dedicated engine, it would not conflict with other queries' execution and cache resources, and would provide operational separation from other scenarios.

As a general guidance, the smaller is the number of tablets the better Firebolt queries perform. Following this principle,
running `VACUUM` on a single-node engine produces less tablets.
This is because `VACUUM` can only merge tablets that are both:

* Assigned to the same node, and
* Belong to the same partition.

This principle is especially important for high-cardinality table partitions.

Finally, `VACUUM` may introduce a temporary performance penalty as the newly created optimized tablets need to be synchronized to other engines operating on the same table(s).

### VACUUM and Auto VACUUM observability

There are several aspects of `VACUUM` that you can examine using the information schema tables.

Auto VACUUM settings for an engine can be checked using the `information_schema.engines` view and looking at the column `auto_vacuum`. Engines with Auto VACUUM explicitly enabled will have the value `true` and when disabled will have the value `false`. Another possible value is `null` &ndash; this indicates default behavior of Auto `VACUUM` which is enabled.

The fragmentation ratio, defined as the ratio of rows marked for deletion to the total number of rows, can be monitored using the `information_schema.tables` view and looking at the `fragmentation` column. When a `VACUUM` operation completes for a table, you should expect to see the fragmentation ratio go down.

You can see the number of tablets for a table by querying `information_schema.tables` and looking at the column `number_of_tablets`. Typically, a `VACUUM` operation will reduce this number as tablets are merged to an optimal state to maintain the underlying health of your tables.

Additionally, both `information_schema.engine_running_queries` and `information_schema.engine_query_history` show `VACUUM` telemetry in the `telemetry` column, which contains JSON. `VACUUM` operation creates multiple jobs, each one responsible for specific portion of table or aggregating index. One can observe the progress and telemetry of both `VACUUM` operation and its jobs by inspecting the `vacuum_stats` object in the JSON.

For the `VACUUM` operation itself, the fields in `vacuum_stats` are:

|Field              |Description |
|:------------------|:------------|
|`type`             |Always set to `vacuum` |
|`objects`          |Number of tables and aggregating indexes the command operates on|
|`processed_objects`|Number of tables and aggregating indexes have been already vacuumed|
|`success_jobs`     |Number of jobs completed successfully|
|`failed_jobs`| Number of failed jobs|

For the `VACUUM` job, the fields in `vacuum_stats` are:

|Field              |Description |
|:------------------|:------------|
|`type`             |Always set to `vacuum_job` |
|`parent_query_id`  |The unique identifier of the `VACUUM` command this sub-job is part of |
|`node-ordinal`     |The ordinal number of the node the sub-job is running on |
|`tablets`     |Number of tablets that the sub-job is optimizing |
|`rows`     |Total number of rows (included deleted rows) in those `tablets` |
|`deleted_rows`     |Total number of deleted rows in those `tablets` |

Consider following example:
```sql
CREATE TABLE vacuum_example (a int, b int) PARTITION BY a;
INSERT INTO vacuum_example VALUES (1, 1);
INSERT INTO vacuum_example VALUES (1, 2);
INSERT INTO vacuum_example VALUES (2, 1), (2, 2);
DELETE FROM vacuum_example WHERE a = 2 and b = 2;
VACUUM vacuum_example;

SELECT telemetry
FROM information_schema.engine_query_history WHERE query_text LIKE 'VACUUM%'
AND STATUS = 'ENDED_SUCCESSFULLY';
```

| telemetry |
|:----|
|{"vacuum_stats":{"type":"vacuum_job", "version":"v0.0.0", "parent_query_id":"c1bf80a4-005b-4063-a271-696de6906471", "node_ordinal":1, "tablets":1, "rows":2, "deleted_rows":1}}|
|{"vacuum_stats":{"type":"vacuum_job", "version":"v0.0.0", "parent_query_id":"c1bf80a4-005b-4063-a271-696de6906471", "node_ordinal":1, "tablets":2, "rows":2, "deleted_rows":0}}|
|{"vacuum_stats":{"type":"vacuum", "version":"v0.0.0", "objects":1, "processed_objects":1, "success_jobs":2, "failed_jobs":0}}

### Example with measuring the performance impact of VACUUM

Over time, operations such as `INSERT`, `DELETE`, and `UPDATE` can create suboptimal tablets that decrease query performance. The `VACUUM` command restructures these tablets by removing deleted rows and optimizing storage, leading to faster queries.

This example demonstrates the impact of `VACUUM` by:

1. Creating a large table with 10 million rows.
2. Deleting 90% of the rows, leaving behind fragmented data.
3. Running a query before and after `VACUUM` to compare run times.

The following code example loads data from a CSV file in an Amazon S3 bucket into the `tutorial_vacuum` table with headers:

```sql
COPY tutorial_vacuum
FROM 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv'
WITH HEADER=TRUE;

INSERT INTO tutorial_vacuum
SELECT a.* FROM tutorial_vacuum a, GENERATE_SERIES(1, 1000000); -- This may run a couple of minutes
```

Script above loads 10 rows from S3 csv file; after that it inserts into the same table the cross product of the 10 inserted rows with 1 million integers.
Next, the following code example deletes all rows from the `tutorial_vacuum` table where the `LevelID` value is greater than 1, resulting in about 900,000 deleted rows:

```sql
DELETE FROM tutorial_vacuum WHERE "LevelID" > 1;
```

The following code example runs a query computing checksum of the entire `tutorial_vacuum` table before and after performing `VACUUM`, allowing a comparison of query performance and efficiency improvements after optimization.

```sql
SELECT hash_agg(*) FROM tutorial_vacuum;
VACUUM tutorial_vacuum;
SELECT hash_agg(*) FROM tutorial_vacuum;
```

In the previous code example, the first `SELECT` is run on data with many deleted rows, while the second runs after `VACUUM`, benefiting from it. The following query history shows the performance benefit of the `VACUUM` operation:

| NO  | STATEMENT                                  | STATUS   | DURATION   |
|:----|:-------------------------------------------|:---------|:-----------|
| 1   | `SELECT hash_agg(*) FROM tutorial_vacuum;` | Success  | 4.43 s     |
| 2   | `VACUUM tutorial_vacuum;`                  | Success  | 17.53 s    |
| 3   | `SELECT hash_agg(*) FROM tutorial_vacuum;` | Success  | 0.82 s     |

Note that the initial `SELECT` query ran for over 4 seconds, while the identical `SELECT` query ran for under a second, after running `VACUUM`.
