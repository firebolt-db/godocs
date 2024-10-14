---
layout: default
title: Subresult Reuse
description: How to understand subresult reuse.
parent: Optimize query performance
nav_order: 1
has_toc: false
has_children: false
---

# Subresult Reuse in Firebolt

*Learn about subresult reuse in Firebolt in more detail in our blog post [Caching & Reuse of Subresults across Queries](https://www.firebolt.io/blog/caching-reuse-of-subresults-across-queries).*

Workloads using repetitive query patterns can benefit tremendously from reuse and caching. Firebolt can cache subresults from various operators within the query plan, including hash tables from hash-joins.
These subresults are placed in an in-memory FireCache, which can use up to 20% of the available RAM. If a sub-plan is reused in a different query, Firebolt's caching system detects it and can retrieve cached subresults, even if the rest of the query differs. Firebolt uses the following guidelines to determine which subresults to cache:
- Firebolts optimizer may insert a `MaybeCache` operator above any node in the query plan, which may cache a subresult if it isn't too large. The `MaybeCache` operator may later retrieve and reuse the cached subresult if the same subplan, with the same underlying data, is evaluated again.
Currently, the optimizer places a `MaybeCache` operator in the following places:
  - At the top of the query plan to cache the full result.
  - At nodes where “sideways information passing” occurs, optimizing joins where the probe-side has an indexed key.

  The `MaybeCache` operator is versatile, and it can be placed anywhere in the plan. 
- Firebolt stores subresult hash-tables created for `Join` operators in the FireCache, provided they are not too large. These hash tables are costly to compute, so reusing them when similar consecutive queries run offers significant performance advantages.

Subresult reuse in Firebolt is fully transactional. When any changes occur in a base table (such as through an `INSERT`, `UPDATE`, or `DELETE`), outdated cache entries are no longer used.

# Example 

The following query, based on the [TPC-H benchmark](https://www.tpc.org/tpch/) schema, calculates the total order price and the number of orders for each nation by joining the `orders`, `customer`, and `nation` tables:

```SQL
SELECT n_name as nation, SUM(o_totalprice), COUNT(*)
  FROM orders, customer, nation
 WHERE o_custkey = c_custkey AND c_nationkey = n_nationkey
 GROUP BY ALL;
```

The simplified plan for this example query would look like the following:

<img src="../../assets/images/subresult_reuse.png" alt="A query plan using subresult reuse." width="700"/>

In this example, a `MaybeCache` operator positioned at the top of the plan caches the subresult from the first run into the FireCache. Additionally, both `Join` operators store their respective hash tables in the cache.
On a subsequent run of exactly the same query (over unchanged data), the `MaybeCache` operator fetches the subresult from the cache, allowing the entire evaluation to be skipped. As a result, query latency is reduced to mere milliseconds. In this example, it leads to a speed improvement of over 100x on a single node, medium engine running TPC-H with scale factor of 100.

If the `WHERE` condition is changed to add `... AND o_orderdate >= '1998-01-01'::Date ...`, the subresult cached by the `MaybeCache` operator cannot be used because the query plan below it has changed. However, the subplan below the upper `Join` remains unchanged, allowing the previously cached hash table to be reused in that `JOIN` operator. This eliminates the need to re-evaluate the subplan and rebuild the hash table.
This results in more than 5x speed improvement on subsequent queries, even when each query has a different date restriction.

# Recognizing Subresult Reuse in Query Telemetry

Firebolt transparently leverages subresult reuse. If you want to see whether subresult reuse helped to speed up your query, look for `Nothing was executed` in the [EXPLAIN (ANALYZE)](../../sql_reference/commands/queries/explain.md) output. This shows that an operator was skipped because a higher level operator retrieved the subresult from the FireCache. For example, in the following `EXPLAIN (ANALYZE)` output, the `MaybeCache` operator retrieved the result from the cache, bypassing the need to run the entire query:

```
[0] [MaybeCache]
|   [RowType]: date not null, text not null, bigint not null, double precision null
|   [Execution Metrics]: output cardinality = 10000, thread time = 0ms, cpu time = 0ms
 \_[1] [Projection] ref_2, ref_1, ref_0, ref_3
   |   [RowType]: date not null, text not null, bigint not null, double precision null
   |   [Execution Metrics]: Optimized out
    \_[2] [SortMerge] OrderBy: [ref_2 Ascending Last, ref_1 Ascending Last, ref_0 Ascending Last, ref_3 Ascending Last] Limit: [10000]
      |   [RowType]: bigint not null, text not null, date not null, double precision null
      |   [Execution Metrics]: Nothing was executed
[...]
```

# Disabling Subresult Reuse

While testing, you might want to disable the subresult cache using the `enable_subresult_cache` [system setting](../../Reference/system-settings.md) in order to measure the performance of your query without caching:

```sql
-- Disable the subresult cache
SET enable_subresult_cache = false;
-- This query does not use the subresult cache
SELECT checksum(*) FROM production_table;
```

Setting `enable_subresult_cache` to `FALSE` disables the use of all cached subresults. In particular, it deactivates two caching mechanisms that normally speed up query runtimes: the use of the `MaybeCache` operator, which includes the full result cache, and the hash-table cache used by the `Join` operator.
