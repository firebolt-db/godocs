---
layout: default
title: Primary indexes
description: Learn about primary indexes in Firebolt and how to configure and use them.
parent: Work with indexes
grand_parent: Guides
nav_order: 7
---

# Primary indexes
{: .no_toc}

* Topic ToC
{:toc}

‌Firebolt uses primary indexes to physically sort data into the Firebolt File Format (F3). The index also colocates similar values, which allows data to be pruned at query runtime. When you query a table, rather than scanning the whole data set, Firebolt uses the table’s index to prune the data. Unnecessary ranges of data are never loaded from disk. Firebolt reads only the relevant ranges of data to produce query results.

Primary indexes in Firebolt are a type of *sparse index*. Unlike a dense index that maps every search key value in a file, a sparse index is a smaller construct that holds only one entry per data block (a compressed range of rows). By using the primary index to read a much smaller and highly compressed range of data from F3 into the engine cache at query runtime, Firebolt produces query results much faster with less disk I/O.

The video below explains sparse indexing. Eldad Farkash is the CEO of Firebolt.
<iframe width="560" height="315" src="https://www.youtube.com/embed/7XDTVB9gsFw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## How you create a primary index

To define a primary index, you use the `PRIMARY INDEX` clause within a [`CREATE TABLE`](../../sql-reference/commands/data-definition/create-fact-dimension-table.md) statement. Although they are optional, we strongly recommend them.

The basic syntax of a `PRIMARY INDEX` clause within a `CREATE TABLE` statement is shown in the example below.

```sql
CREATE [FACT|DIMENSION] TABLE <table_name> (
  <column1> <datatype>,
  <column2> <datatype>,
  <column3> <datatype>,
     ...
)
PRIMARY INDEX <column1> [, <...column2>];
```

## Primary indexes can’t be modified

After you create a table, you can’t modify the primary index. To change the index, you must drop the table and recreate it.

## How to choose primary index columns

The columns that you choose for the primary index and the order in which you specify them are important. If you have already defined a workload that you want to run in Firebolt, try out the [CALL RECOMMEND_DDL](../../sql_reference/commands/queries/recommend_ddl.html) command to find suitable primary index and partiton key configurations. You can learn more about how primary indexes should be chosen in the [Primary index examples](#primary-index-examples) section.

### Include columns used in WHERE clauses

Include all columns that are used in query `WHERE` clauses to filter query results.

### Consider including columns used in GROUP BY clauses

Consider adding columns that you use in `GROUP BY` statements with aggregate functions.

### Order columns in the index definition by cardinality

Specify columns in order of how frequently they’re used in `WHERE` clauses and in descending order of cardinality. In other words, in the first position (`<column1>` in the syntax above) specify the column that filters results the most. Then specify remaining columns in descending order of how much they filter.

Avoid specifying a column of the highest cardinality&mdash;that is, a column that has truly unique values or the primary key&mdash;unless you use that column in query `WHERE` clauses. Also avoid specifying columns of low cardinality that won’t adequately filter results.

### Include as many columns as you need

The number of columns that you specify in the index won’t negatively affect query performance. Additional columns might slow down ingestion very slightly, but the benefit for flexibility and performance of analytics queries will almost certainly outweigh any impact to ingestion performance.

### Consider how you alter values in WHERE clauses

The primary index isn’t effective if Firebolt can’t determine the values in the index column. If the `WHERE` clause in your query contains a function that transforms the column values, Firebolt can’t use the index. Consider a table with the primary index definition shown below, where `playerid` is a `INTEGER` data type in a table named `players`.

```sql
  PRIMARY INDEX playerid
```

In the example analytics query over the `players` table, Firebolt can’t use the primary index with the `WHERE` clause. This is because the function with `playerid` is on the left side of the comparison. To satisfy the conditions of comparison, Firebolt must read all values of `playerid` to apply the `UPPER` function.

![](../../assets/images/Red_X_resized.png)  

```sql
SELECT
  playerid
FROM
  players
WHERE
  UPPER(playerid) LIKE ‘AA%’;
```

In contrast, Firebolt can use the primary index in the following example:

![](../../assets/images/Green_check_resized.png)  

```sql
SELECT
  playerid
FROM
  players
WHERE
  playerid LIKE ‘AAA%’;
```

If you know that you will use a function in a predicate ahead of time, consider creating a virtual column to store the result of the function. You can then use that virtual column in your index and queries. This is particularly useful for hashing columns.

### With a star schema, include join key columns in the fact table index

If you have a star schema with a fact table referring to many dimension tables, include the join keys (the foreign key columns) in the primary index of the fact table. This helps accelerate queries because the Firebolt query planner uses join keys as a predicate.

Conversely, on the dimension table side, there is no benefit to including the join key in the dimension table primary index unless you use it as a filter on the dimension table itself.

## Using partitions with primary indexes

In most cases, partitioning isn’t necessary because of the efficiency of primary indexes (and aggregating indexes). If you use partitions, the partition column is the first stage of sorting. Firebolt divides the table data into file segments according to the `PARTITION BY` definition. Then, within each of those segments, Firebolt applies the primary index to prune and sort the data into even smaller data ranges as described above.

For more information, see [Working with partitions](../../Overview/working-with-tables/working-with-partitions.md).

## Primary index examples

This section demonstrates different primary indexes created on a fact table, `totalscore`, created with the DDL and sample values shown below.

### Example fact table
{: .no_toc}

The examples in this section are based on the fact table below. Each record stores the current level and high score of a player, identified by their `playerid` and `nickname`. 

#### Table DDL
{: .no_toc}

```sql
CREATE FACT TABLE player_information (
  registeredon DATE,
  playerid TEXT,
  nickname TEXT NOT NULL,
  currentscore BIGINT,
  level INTEGER NOT NULL
)
PRIMARY INDEX <see examples below>;
```

#### Table contents (excerpt)
{: .no_toc}

| registeredon |    level    | playerid | nickname | currentscore |
|:------|:------|:------|:-------|:-------|
| 2018-05-30 | 1 |       78152 | kennethpark      |         137 |
| 2020-11-13 | 2 |       57328 | sabrina21  |         104 |
| 2020-07-11 | 3 |       44963 | rileyjon   |         111 |
| 2019-09-06 | 4 |       70147 | ymatthews      |          49 |

#### Cardinality of columns
{: .no_toc}

A `COUNT DISTINCT` query on each column returns the following. A higher number indicates higher cardinality.

| distinct_dates | distinct_levels | distinct_currentscores | 
|:----------------|:-----------------|:--------------------|
|           1461 |             35 |              89664 |    


### Example query pattern&mdash;date-based queries

Consider the two example queries below that return values with date-based filters.

#### Query 1
{: .no_toc}

```sql
SELECT
  *
FROM
  player_registry
WHERE
  registeredon BETWEEN '2020-01-01' AND '2020-01-02'
  AND playerid = "11386"
  AND event_type = 'click'
```

#### Query 2
{: .no_toc}

```sql
SELECT
  count(*),
  registeredon
FROM
  players
WHERE
  EXTRACT(YEAR FROM registeredon) = ‘2021’
```

For both queries, the best primary index is:

```sql
PRIMARY INDEX (registeredon, playerid, event_type)
```

* With `visit_date` in the first position in the primary index, Firebolt sorts and compresses records most efficiently for these date-based queries.
* The addition of `playerid` in the second position and `event_type` in the third position further compresses data and accelerates query response.
* `playerid` is in the second position because it has higher cardinality than `event_type`, which has only three possible values.

For query 2, you can improve performance further by partitioning the table according to year as shown in the query excerpt below.

```
PRIMARY INDEX (registeredon, playerid, event_type)
PARTITION BY (EXTRACT (YEAR FROM registeredon))
```

Without the partition, Firebolt likely must scan across file segments to return results for the year 2021. With the partition, segments exist for each year, and Firebolt can read all results from a single segment. If the query runs on a multi-node engine, the benefit may be greater. Firebolt can avoid pulling data from multiple engine nodes for results.

### Example query pattern&mdash;customer-based query

Consider the example query below that returns the sum of `click` values for a particular player registry.

```sql
SELECT
  playerid,
  nickname,
  event_type,
  SUM(event_value)
FROM
  events
WHERE
  playerid = "14493"
  AND event_type = 'click'
  AND event_value > 0
GROUP BY
	1,
  2,
  3;
```

For this query, the best primary index is:

```sql
PRIMARY INDEX (playerid, asset_id, event_type)
```

* `playerid` is in the first position because it has the highest cardinality and sorts and prunes data most efficiently for this query.
* The addition of `asset_id` won’t accelerate this particular query, but adding it is not detrimental.
* Although `event_type` has low cardinality, because it’s contained in the `WHERE` clause, adding it to the primary index has some benefit.

### Example&mdash;using virtual columns

Virtual columns are most often used in a primary index to:

* Accommodate functions that alter column values.
* Calculate hash values for columns that contain long strings.

A virtual-column example for a function that transforms a column value is shown below.

#### Step 1&mdash;create the fact table with the virtual column in the index
{: .no_toc}

The example DDL below creates a fact table similar to the one earlier in this section. However, it adds the `upper_customer_id` column. The table creates this virtual column to store the result of an `UPPER` function that upper-cases `customer_id` values during the `INSERT INTO` operation.

The `PRIMARY INDEX` clause uses the `upper_customer_id` column because that column is used in analytics queries.

```sql
CREATE FACT TABLE events_log (
  visit_date DATE,
  asset_id TEXT,
  customer_id TEXT NOT NULL,
  event_type TEXT,
  event_count INTEGER NOT NULL,
  uppder_customer_id TEXT NOT NULL
)
PRIMARY INDEX visit_date, upper _customer_id;
```

#### Step 2&mdash;use the function during ingestion (`INSERT INTO` statement)
{: .no_toc}

```sql
INSERT INTO
  player_registry 
SELECT
  registeredon,
  asset_id,
  playerid,
  event_type,
  event_count,
  UPPER(playerid) AS upper_player_id
FROM
  players;
```

#### Step 3&mdash;query using the virtual column in predicates
{: .no_toc}

The example `SELECT` query below uses the virtual column to produce query results and benefits from the index.

```sql
SELECT
  playerid
FROM
  players
WHERE
  upper_player_id LIKE ‘AAA%’;
```
