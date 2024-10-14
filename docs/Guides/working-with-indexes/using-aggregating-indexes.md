---
layout: default
title: Aggregating indexes
description: Learn about aggregating indexes in Firebolt and how to configure and use them.
parent: Work with indexes
nav_order: 8
---

# Aggregating indexes
{: .no_toc}

* Topic ToC
{:toc}

Aggregating indexes accelerate queries that include aggregate functions that you perform repeatedly on large tables with millions or billions of rows. Aggregating indexes greatly reduce the compute resources required at query runtime to process functions. This can improve performance and save cost by allowing you to use less costly engines. Dashboards and repetitive reports are common use cases for aggregating indexes. It’s less common to create aggregating indexes for ad hoc queries.

## How aggregating indexes work

Firebolt uses an aggregating index to pre-calculate and store the results of aggregate functions that you define. An aggregating index is like a materialized view in many ways, with technology proprietary to Firebolt that works together with the F3 storage format to make them more efficient.

At query runtime, Firebolt determines the aggregating indexes that provide the best query performance. To return query results, Firebolt uses the indexes rather than scanning the table.

Firebolt automatically updates aggregating indexes as you ingest new data, or mutate existing data. The precalculated results of aggregate functions are stateful and consistent with the underlying table data on the engine.

Firebolt shards aggregating indexes across engine nodes in multi-node engines as it does with the underlying tables.

The video below is a technical discussion of some issues with traditional materialized views and how Firebolt addresses the problem with unique technology. Eldad Farkash is the CEO of Firebolt.
<iframe width="560" height="315" src="https://www.youtube.com/embed/Hniv9u4w7lI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Aggregating index tradeoffs

Effective aggregating indexes are relatively small compared to the underlying table.

For very large tables, an aggregating index may still be quite large. If the index is effective, the savings at query runtime will outweigh the cost of storage. Aggregating indexes also increase compute requirements during data ingestion because Firebolt performs pre-calculations at that time. As with storage, savings at query runtime usually outweigh the ingestion cost.

If your application favors speed of ingestion over speed of analytics queries, be sure to test ingestion with aggregating indexes before production.

## How to define an aggregating index

To create an aggregating index, use the [CREATE AGGREGATING INDEX](../../sql_reference/commands/data-definition/create-aggregating-index.md) statement. This statement specifies a table, a subset of columns from the table, and a list of the aggregate functions that commonly run over that table. You can create as many aggregating indexes per table as you need. Each aggregating index is associated with a single table.

The syntax for the `CREATE AGGREGATING INDEX` is shown below.

```sql
CREATE AGGREGATING INDEX <agg_index_name> ON <fact_table_name>
  (
    <fact_table_column_1> [,<fact_table_column_2>][,...]
    <aggregate_expression> [,...]
  );
```

### Aggregating indexes can’t be modified

You can’t modify aggregating indexes after you create them. To modify an aggregating index, use the `DROP AGGREGATING INDEX` command, and then use `CREATE AGGREGATING INDEX` to specify a new index for the same table.

### How to choose aggregating index columns

Firebolt uses the columns that you specify for an aggregating index in much the same way as the columns for a primary index.

Follow the same guidelines as those outlined for primary index columns. Most importantly, specify columns in ascending order of cardinality (number of distinct values), i.e. lowest cardinality first.

All columns that are used in aggregations at query runtime must appear in the index definition, either in the primary index or the function definitions, for the optimizer to use the index at query runtime. This includes columns that are part of the aggregate functions, any columns used in `GROUP BY` and `WHERE` clauses, and any columns in the table that are used as join keys. If a column is missing, Firebolt must scan the table instead, and the aggregating index thus won't improve performance.

### How to choose aggregate expressions

You can specify as many aggregate expressions as required in an aggregating index definition. At query runtime, the number of aggregate expressions does not affect query performance. However, because Firebolt pre-processes each aggregate expression during ingestion, each additional aggregate expression increases compute requirements during ingestion.

Aggregate expressions that you specify must correspond precisely to the aggregate expressions used at query runtime, including specified columns. You also can specify complex functions in the index definition, but make sure to specify them precisely as you use them in queries.

## Aggregating indexes and partitions

Aggregating indexes inherit the partitions from the underlying table. When you drop a partition from the underlying table, the partition is dropped from the aggregating index.

## Aggregating index examples

The example in this section are based on a table, `game_information`, created with the DDL shown below. 

```sql
CREATE TABLE game_information (
  gameid INTEGER,
  playerid INTEGER,
  playerid_total DOUBLE PRECISION,
  gameid_count INTEGER
);
```

From this table, let's assume we typically run queries that use these aggregations:

```sql
SUM(playerid_total)
SUM(gameid count)
AVG(gameid_count)
```

And they are grouped by different combinations of the `gameid` and `playerid` columns.

‌The DDL below creates an aggregating index to accelerate these aggregations.

```sql
CREATE AGGREGATING INDEX id_information ON game_information (
  gameid,
  playerid,
  SUM(playerid_total),
  SUM(gameid_count),
  AVG(gameid_count)
);
```

As with a primary index, the order of the columns specified is important. Firebolt creates a primary index for the aggregating index. In our example, the primary index is in the order of `gameid`, `playerid`.
