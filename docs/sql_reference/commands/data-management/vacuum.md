---
layout: default
title: VACUUM
description: Reference and syntax for the VACUUM command.
grand_parent:  SQL commands
parent: Data management
---

# VACUUM
Optimizes tablets for query performance.

`VACUUM` optimizes tablets for query performance. DML operations (such as [`DELETE`](delete.md), [`UPDATE`](update.md), [`INSERT`](insert.md) and [`COPY FROM`](copy-from.md)) might create tablets that are not optimally sized. Suboptimal tablets occur because DML efficiently utilizes resources in proportion to the cardinality of the data being inserted. In addition to standard SQL operations, tuples that are deleted by an update are not always physically removed from their table; they remain present until a `VACUUM` is done. In other words, tablets are not necessarily optimal for running queries; therefore, it’s necessary to do `VACUUM` periodically, especially on frequently updated tables.

## Syntax

```sql
VACUUM <table>
```

## Parameters
{: .no_toc}

| Parameter | Description                         |Supported input types |
| :--------- | :----------------------------------- | :---------------------|
| `<table>` | The name of the table to be optimized | FACT, DIMENSION table or AGGREGATE INDEX |

## Example
{: .no_toc}

Optimize table named `games`.

```sql
VACUUM games;
```

### Usage Notes

Here are considerations related to running the `VACUUM` command.

* **What happens during VACUUM**<br>
`VACUUM` analyzes the tablets, selects the ones that are too small or have too many deleted rows, and produces new versions that are optimized for query execution for both tablets and Aggregate Indexes.<br>
`VACUUM` is a non-blocking process and runs alongside other operations executed by the user. Consequently, some changes performed by `VACUUM` may conflict with mutations run by the user. The operation that commits first wins (see Transaction and concurrency for details) . This means that applications that execute mutations in parallel with `VACUUM` should gracefully handle transaction conflicts. It also means that benefits of the `VACUUM` may be diminished by a mutation that committed data first.<br>

* **Space and performance considerations**<br>
Users must be aware that `VACUUM` consumes both compute and storage resources.<br>
`VACUUM` can consume a considerable amount of compute resources depending on the table size, number of tablets, and number of mutations in the table.<br>
`VACUUM` produces optimized versions of the data, while leaving behind older versions subject to the garbage collection (GC) process. These older tablets will continue to consume storage space until the GC process completes the clean-up.<br>
If users would like to have precise control over `VACUUM`, it may be preferable to execute on a dedicated engine that could be sized and run just for `VACUUM` operations. With `VACUUM` running on a dedicated engine, it would not conflict with other queries' execution and cache resources, and would provide operational separation from other scenarios.<br>
`VACUUM` may introduce a performance penalty as the newly created optimized tablets need to be synchronized with other engines operating on the same table(s).<br>

* **Automatic scheduling**<br>
You can enable automatic scheduling of processes such as `VACUUM` by integrating with external tools. Please see section [Integrate with Firebolt](../../../Guides/integrations/integrations.md) for more detail on our current support for these tools.

### Example of running VACUUM to improve query performance. 

This example demonstrates a use case for running `VACUUM` and its performance impact. Let’s create a large table with 10 million rows: 

```sql
COPY tutorial_vacuum 
FROM 's3://firebolt-publishing-public/help_center_assets/firebolt_sample_dataset/levels.csv'
WITH HEADER=TRUE;

INSERT INTO tutorial_vacuum
SELECT a.* FROM tutorial_vacuum a, GENERATE_SERIES(1, 1000000); -- This may run a couple of minutes
```

Script above loads 10 rows from S3 csv file; after that it inserts into the same table the cross product of the 10 inserted rows with 1 million integers.
Next we will delete about 90% of rows from the table, that would result in about 900,000 deleted rows.

```sql
DELETE FROM tutorial_vacuum WHERE "LevelID" > 1; 
```

Let’s run a simple select from the tutorial_vacuum table; VACUUM it, and repeat the same select.

```sql
SELECT checksum(*) FROM tutorial_vacuum;
VACUUM tutorial_vacuum;
SELECT checksum(*) FROM tutorial_vacuum;
```

The first select is executed on data with a lot of deleted rows, while the second is run after `VACUUM` and benefits from it. Let’s examine query history and see the performance benefit of the `VACUUM` operation:

| NO  | STATEMENT                                | STATUS   | DURATION   |
|:----|:-----------------------------------------|:---------|:-----------|
| 3   | SELECT checksum(*) FROM tutorial_vacuum; | Success  | 0.82 s     |
| 2   | VACUUM tutorial_vacuum;                  | Success  | 17.53 s    |
| 1   | SELECT checksum(*) FROM tutorial_vacuum; | Success  | 4.43 s     |


Note that the first select was running for more than 4 seconds while exactly the same select after VACUUM completes in less than a second. 
