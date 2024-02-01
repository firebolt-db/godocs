---
layout: default
title: EXPLAIN
parent: SQL commands
---

# EXPLAIN

The `EXPLAIN` feature in Firebolt is a powerful tool that helps you understand how the system executes a query. It provides insight into the execution plan that Firebolt will use to compute the result of your query. This information is crucial for query optimization and understanding the performance of your SQL queries.

In addition to viewing the execution plans, you can specify the `ANALYZE` option (Beta) to execute the query and receive detailed metrics about how much time is spent on each operator, and how much data it processes.

## Syntax

```sql
EXPLAIN <select_statement>

-- Beta
EXPLAIN ( <option_name> [<option_value>] [, ...] ) <select_statement>
```

| Parameter            | Description                                                                 |
| :------------------- | :-------------------------------------------------------------------------- |
| `option_name`        | The name of an option. See below for a list of all available options.       |
| `option_value`       | The value of the option. If no value is specified, it is `TRUE` by default. |
| `<select_statement>` | Any select statement.                                                       |

## Available Options (Beta)

The output of `EXPLAIN` can be augmented by specifying options. The following table lists all available options:

| Option Name | Option Values   | Description                                                                                                                                                                               |
| :---------- | :-------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `LOGICAL`   | `TRUE`, `FALSE` | Returns the optimized logical query plan. This plan is returned by default.                                                                                                               |
| `PHYSICAL`  | `TRUE`, `FALSE` | Returns the optimized physical query plan containing shuffle operators for queries on distributed engines. This gives insights how work is distributed between the nodes of an engine.    |
| `ANALYZE`   | `TRUE`, `FALSE` | Executes the query and returns the optimized physical query plan annotated with metrics from query execution. The metrics are explained in [Example with ANALYZE](#example-with-analyze). |
| `ALL`       | `TRUE`, `FALSE` | Executing `EXPLAIN (ALL) <select statement>` returns the `LOGICAL`, `PHYSICAL`, and `ANALYZE` plans.                                                                                      |

You many only specify one of the options `LOGICAL`, `PHYSICAL`, `ANALYZE`. If you need to view several plans at once, please use the `ALL` option.

## Example

The example below demonstrates an `EXPLAIN` statement for a `SELECT` query on a table named `lineitem`.

```sql
EXPLAIN
SELECT
	l_shipdate,
	l_linestatus,
	l_orderkey,
	AVG(l_discount)
FROM
	lineitem
WHERE
	l_returnflag = 'N'
	AND l_shipdate > '1996-01-01'
GROUP BY
	l_shipdate,
	l_linestatus,
	l_orderkey
ORDER BY
	1,2,3,4;
```

**Returns:**

```
[0] [Projection] lineitem.l_shipdate, lineitem.l_linestatus, lineitem.l_orderkey, avgOrNull(lineitem.l_discount)
 \_[1] [Sort] OrderBy: [lineitem.l_shipdate Ascending Last, lineitem.l_linestatus Ascending Last, lineitem.l_orderkey Ascending Last, avgOrNull(lineitem.l_discount) Ascending Last]
    \_[2] [Aggregate] GroupBy: [lineitem.l_orderkey, lineitem.l_linestatus, lineitem.l_shipdate] Aggregates: [avgOrNull(lineitem.l_discount)]
       \_[3] [Projection] lineitem.l_orderkey, lineitem.l_discount, lineitem.l_linestatus, lineitem.l_shipdate
          \_[4] [Predicate] equals(lineitem.l_returnflag, 'N'), greater(lineitem.l_shipdate, toPGDate('1996-01-01'))
             \_[5] [StoredTable] Name: 'lineitem', used 5/16 column(s) FACT
```

The `EXPLAIN` results indicate that this `SELECT` query will execute operations as follows. The Firebolt engine will:

1. Read the required columns from the `lineitem` table.
2. Filter the `lineitem` table by the `WHERE` conditions.
3. Reduce the columns that are no longer required.
4. Perform the aggregation as specified by the `GROUP BY` clause.
5. Sort results in ascending order by all columns from the `SELECT` clause.
6. Bring the columns into the order specified in the `SELECT` clause.

## Example with ANALYZE (Beta)

Now, we execute the same query on a multi-node engine, but with the `(ALL)` option specified. This is equivalent to writing `(ALL TRUE)` or `(LOGICAL, PHYSICAL, ANALYZE)`.

```sql
EXPLAIN (ALL)
SELECT
	l_shipdate,
	l_linestatus,
	l_orderkey,
	AVG(l_discount)
FROM
	lineitem
WHERE
	l_returnflag = 'N'
	AND l_shipdate > '1996-01-01'
GROUP BY
	l_shipdate,
	l_linestatus,
	l_orderkey
ORDER BY
	1,2,3,4;
```

**Returns:**

Disclaimer
: The exact format of this result is still subject to change until the full release of this feature.

```
explain_logical:

[0] [Projection] ref_2, ref_1, ref_0, ref_3
|   [RowType]: pgdate not null, text not null, bigint not null, double precision null
 \_[1] [Sort] OrderBy: [ref_2 Ascending Last, ref_1 Ascending Last, ref_0 Ascending Last, ref_3 Ascending Last]
   |   [RowType]: bigint not null, text not null, pgdate not null, double precision null
    \_[2] [Aggregate] GroupBy: [ref_0, ref_2, ref_3] Aggregates: [avgOrNull(ref_1)]
      |   [RowType]: bigint not null, text not null, pgdate not null, double precision null
       \_[3] [Projection] ref_0, ref_1, ref_3, ref_4
         |   [RowType]: bigint not null, double precision not null, text not null, pgdate not null
          \_[4] [Predicate] equals(ref_2, 'N'), greater(ref_4, toPGDate('1996-01-01'))
            |   [RowType]: bigint not null, double precision not null, text not null, text not null, pgdate not null
             \_[5] [StoredTable] Name: 'lineitem', used 5/16 column(s) FACT, ref_0: 'l_orderkey' ref_1: 'l_discount' ref_2: 'l_returnflag' ref_3: 'l_linestatus' ref_4: 'l_shipdate'
                   [RowType]: bigint not null, double precision not null, text not null, text not null, pgdate not null


explain_physical:

[0] [Projection] ref_2, ref_1, ref_0, ref_3
|   [RowType]: pgdate not null, text not null, bigint not null, double precision null
 \_[1] [SortMerge] OrderBy: [ref_2 Ascending Last, ref_1 Ascending Last, ref_0 Ascending Last, ref_3 Ascending Last]
   |   [RowType]: bigint not null, text not null, pgdate not null, double precision null
    \_[2] [Shuffle] Gather
      |   [RowType]: bigint not null, text not null, pgdate not null, double precision null
       \_[3] [Sort] OrderBy: [ref_2 Ascending Last, ref_1 Ascending Last, ref_0 Ascending Last, ref_3 Ascending Last]
         |   [RowType]: bigint not null, text not null, pgdate not null, double precision null
          \_[4] [AggregateMerge] GroupBy: [ref_0, ref_1, ref_2] Aggregates: [avgOrNullMerge(ref_3)]
            |   [RowType]: bigint not null, text not null, pgdate not null, double precision null
             \_[5] [Shuffle] Hash by [ref_0, ref_1, ref_2]
               |   [RowType]: bigint not null, text not null, pgdate not null, aggregatefunction2(avgornull, double precision not null) not null
                \_[6] [AggregatePartial] GroupBy: [ref_0, ref_2, ref_3] Aggregates: [avgOrNullState(ref_1)]
                  |   [RowType]: bigint not null, text not null, pgdate not null, aggregatefunction2(avgornull, double precision not null) not null
                   \_[7] [Projection] ref_0, ref_1, ref_3, ref_4
                     |   [RowType]: bigint not null, double precision not null, text not null, pgdate not null
                      \_[8] [Predicate] equals(ref_2, 'N'), greater(ref_4, toPGDate('1996-01-01'))
                        |   [RowType]: bigint not null, double precision not null, text not null, text not null, pgdate not null
                         \_[9] [StoredTable] Name: 'lineitem', used 5/16 column(s) FACT, ref_0: 'l_orderkey' ref_1: 'l_discount' ref_2: 'l_returnflag' ref_3: 'l_linestatus' ref_4: 'l_shipdate'
                               [RowType]: bigint not null, double precision not null, text not null, text not null, pgdate not null


explain_analyze:

[0] [Projection] ref_2, ref_1, ref_0, ref_3
|   [RowType]: pgdate not null, text not null, bigint not null, double precision null
|   [Execution Metrics]: output cardinality = 0, thread time = 0ms, cpu time = 0ms
 \_[1] [SortMerge] OrderBy: [ref_2 Ascending Last, ref_1 Ascending Last, ref_0 Ascending Last, ref_3 Ascending Last]
   |   [RowType]: bigint not null, text not null, pgdate not null, double precision null
   |   [Execution Metrics]: output cardinality = 0, thread time = 0ms, cpu time = 0ms
    \_[2] [Shuffle] Gather
      |   [RowType]: bigint not null, text not null, pgdate not null, double precision null
      |   [Execution Metrics]: output cardinality = 0, thread time = 0ms, cpu time = 0ms
       \_[3] [Sort] OrderBy: [ref_2 Ascending Last, ref_1 Ascending Last, ref_0 Ascending Last, ref_3 Ascending Last]
         |   [RowType]: bigint not null, text not null, pgdate not null, double precision null
         |   [Execution Metrics]: output cardinality = 0, thread time = 0ms, cpu time = 0ms
          \_[4] [AggregateMerge] GroupBy: [ref_0, ref_1, ref_2] Aggregates: [avgOrNullMerge(ref_3)]
            |   [RowType]: bigint not null, text not null, pgdate not null, double precision null
            |   [Execution Metrics]: output cardinality = 0, thread time = 0ms, cpu time = 0ms
             \_[5] [Shuffle] Hash by [ref_0, ref_1, ref_2]
               |   [RowType]: bigint not null, text not null, pgdate not null, aggregatefunction2(avgornull, double precision not null) not null
               |   [Execution Metrics]: output cardinality = 0, thread time = 0ms, cpu time = 0ms
                \_[6] [AggregatePartial] GroupBy: [ref_0, ref_2, ref_3] Aggregates: [avgOrNullState(ref_1)]
                  |   [RowType]: bigint not null, text not null, pgdate not null, aggregatefunction2(avgornull, double precision not null) not null
                  |   [Execution Metrics]: output cardinality = 0, thread time = 0ms, cpu time = 0ms
                   \_[7] [Projection] ref_0, ref_1, ref_3, ref_4
                     |   [RowType]: bigint not null, double precision not null, text not null, pgdate not null
                     |   [Execution Metrics]: output cardinality = 0, thread time = 0ms, cpu time = 0ms
                      \_[8] [Predicate] equals(ref_2, 'N'), greater(ref_4, toPGDate('1996-01-01'))
                        |   [RowType]: bigint not null, double precision not null, text not null, text not null, pgdate not null
                        |   [Execution Metrics]: output cardinality = 0, thread time = 0ms, cpu time = 0ms
                         \_[9] [StoredTable] Name: 'lineitem', used 5/16 column(s) FACT, ref_0: 'l_orderkey' ref_1: 'l_discount' ref_2: 'l_returnflag' ref_3: 'l_linestatus' ref_4: 'l_shipdate'
                               [RowType]: bigint not null, double precision not null, text not null, text not null, pgdate not null
                               [Execution Metrics]: output cardinality = 0, thread time = 0ms, cpu time = 0ms

```

The result has three columns `explain_logical`, `explain_physical`, and `explain_analyze`. These can be turned off individually using the corresponding option. For example, to only show `explain_logical` and `explain_analyze`, we could either specify `(LOGICAL, ANALYZE)` or `(ALL, PHYSICAL FALSE)`.

The `explain_logical` column shows the optimized logical query plan of the select statement. This is the same plan as in [Example](#example). Additionally, it shows the output row type for each operator.

The `explain_physical` column shows the more detailed optimized physical plan containing shuffle operators for distributed query execution. It allows insights into how work is distributed across the nodes of an engine.

The `explain_analyze` column contains the same query plan as the `explain_physical` column, but annotated with metrics collected during query execution. For each operator, it shows the number of rows it produced (`output_cardinality`), and how much time was spent on that operator (`thread_time` and `cpu_time`). `thread_time` is the sum of the wall-clock time that threads spent working on this operator across all nodes. `cpu_time` is the sum of the time these threads where scheduled on a CPU core. If `cpu_time` is considerably smaller than `thread_time`, this indicates that the operator is waiting a lot on IO or the engine is under multiple queries at once.
