---
layout: default
title: Data modeling
description: Understand how to organize data from efficient retrieval in Firebolt
parent: Overview
nav_order: 6
---

# Data modeling

Firebolt employs advanced indexing techniques and partitioning strategies to optimize query performance and compute efficiency. By minimizing the amount of data scanned, Firebolt indexes retrieve only the specific data ranges needed to satisfy a query. These indexes are automatically maintained during data loading, where Firebolt sorts, compresses, and incrementally updates them. Data and indexes are committed as tablets, which are automatically merged and optimized as the data evolves. This guide provides best practices for organizing tables, indexes, and data to achieve fast query results and peak performance.

## How it works

Firebolt’s indexing and partitioning strategies are designed to take advantage of a cloud-based architecture that scales to handle very large data sets. Data is queried using multiple nodes for parallel processing. Data is also stored by columns, which allows for:

* Optimized read operations. 
* Less disk space for storage.
* Vectorized processing.

Firebolt also separates compute resources from storage resources so you can scale either up or down depending on your use case. Optimize your resources based on your changing workloads, and pay only for what you use.

Firebolt’s data modeling strategies work best with **Firebolt’s managed tables**, which leverage Firebolt’s performance optimizations. External tables, which allow users to access data without loading it into Firebolt, provide flexibility for querying external data sources like Amazon S3, but they do not offer the same performance benefits as managed tables. 

This guide contains the following sections:

* [Select a primary index](#select-a-primary-index) &ndash; Select the most efficient primary index for your tables based on your query patterns and data characteristics.
* [Select an aggregating index](#select-an-aggregating-index) &ndash; Precompute and update aggregation results for fast calculations and to save compute resources.
* Find the [best partition strategy] &ndash; Find the best keys, criteria and schemes to partition your data. Base your partitioning strategy to optimize accessing data that is accessed most often and attributes that are used most frequently.
* Use Firebolt’s RECOMMEND_DDL tool to recommend the best primary index, partition keys, and schema configurations based on your query history.

The following sections show you how to use the previous data modeling strategies to decrease the number of bytes scanned to improve query performance, reduce storage costs, and optimize compute resources.

Topics:
* [Databases](#databases)
    * [Database best practices](#database-best-practices)
    * [Evaluate your query performance](#evaluate-your-query-performance)
* [Schema](#schemas)
    * [Schema best practices](#schema-best-practices)
* [Tables](#tables)
    * [Select a primary index](#select-a-primary-index)
    * [Select an aggregating index](#select-an-aggregating-index)
    * [Select indexes and partitions for me](#use-recommend_ddl-to-select-indexes-and-partitions)

### Databases

In Firebolt, a database is a logical structure that organizes and stores data for efficient querying and management. Databases are created using the `CREATE DATABASE` statement, and users can modify or delete them as needed using `ALTER` and `DROP`. Firebolt separates the compute and storage layers, ensuring that databases are efficiently managed without directly impacting processing power. Firebolt databases also integrate with data security layers, enforcing access controls and user permissions to protect sensitive information. They support real-time analytics, allowing users to run queries on large datasets quickly, and can be easily integrated with third-party tools through APIs and drivers for programming languages like Python and .NET.

**Create a database**

Use [CREATE DATABASE]({% link sql_reference/commands/data-definition/create-database.md %}), which requires only the name of the database, and an **engine** to create a database.

Firebolt provides two types of engines:
* **System engines** handle administrative tasks like creating and managing databases and tables without any need for configuration. They are always available but cannot process user data.
**User engines** perform both administrative tasks and handle queries that access and process user data. User engines provide the flexibility needed for data processing and analysis.

The following code example creates a `test_library` database with an optional description:

```sql
CREATE DATABASE IF NOT EXISTS test_library 
    WITH DESCRIPTION = 'database about library';
```

**Manage a database**

After you create a database, you can create additional objects and run queries within it. You can also modify the database parameters. 

The following code example modifies the description of a database:

```sql
ALTER DATABASE library SET DESCRIPTION = 'database about library';
```

You can delete a database with [DROP DATABASE]({% link sql_reference/commands/data-definition/drop-database.md %}), which permanently deletes the database and all its contents. Since this action cannot be undone, use it carefully. Create a backup before dropping the database to prevent data loss. 

The following code example uses the optional `IF EXISTS` clause to see if the `test_library` database exists, and then deletes it:

```sql
DROP DATABASE IF EXISTS test_library;
```

Active queries will continue using the latest version of the database, but new queries submitted after the database is dropped will fail. To minimize disruptions, monitor active queries and notify users in advance.

#### Database best practices

Efficient database design in Firebolt is key to optimizing query performance, managing scalability, and ensuring workload isolation. By using databases to logically separate data, workloads from each other. you can reduce the impact of schema changes, minimize query latency, and enhance access control through role-based policies. For example, when managing data for applications that operate across multiple regions, understanding when to use a single database versus separate databases can significantly affect performance and operational efficiency. The following best practices outline how to structure databases in Firebolt to achieve these goals:

* **Use databases to logically separate workloads** &ndash; Organize data into separate databases to isolate workloads and reduce the impact of schema changes on unrelated queries.
* **Group related tables in the same database** &ndash; Only include related tables within the same database to minimize the overhead caused by metadata synchronization during schema changes.
* **Separate data for different regions or use cases** &ndash; For multi-region applications, create separate databases for each region to avoid conflicts such as overlapping primary keys, and to prevent schema changes in one region from affecting query performance in another.
* **Minimize the number of tables in a single database** &ndash; Avoid adding too many unique tables to a single database, as schema changes require the metadata service to synchronize all associated schemas, potentially increasing query latency.
* **Leverage logical separation for access control** &ndash; Use separate databases to enforce role-based access control policies, ensuring users can only access data relevant to their roles and restricting queries across databases.
* **Consider metadata sync impacts on query latency** &ndash; Metadata synchronization can introduce slight query latencies after schema changes, especially as the number of tables in a database grows.

##### Example

The maker of the [UltraFast game](https://help.firebolt.io/t/ultra-fast-gaming-firebolt-sample-dataset/250) plans to expand into a second region, where the game will generate data with the same structure and format as the first region but potentially overlapping primary keys.

The developer has two options:

1. Store the new region's data in the existing database.
2. Create a separate database specifically for the new region.

**Recommended solution** 
Create a separate database for the new region for the following reasons:
* Optimal Query Performance &ndash; Firebolt's decoupled architecture requires metadata synchronization for schema changes. As the number of tables in a database grows, this synchronization can introduce slight query latency. Storing data for each region in separate databases eliminates this risk and ensures efficient query performance.
* Improved data isolation &ndash; Queries for one region are not impacted by schema changes in another. Separate databases allow role-based access control, restricting access to data by region, which enhances security and operational control.

By creating a dedicated database for each region, the developer ensures optimal performance, scalability, and data management tailored to the needs of the UltraFast game expansion.

#### Evaluate your query performance

You can use the code in the [Firebolt DDL Performance GitHub repository](https://github.com/wagjamin/firebolt-ddl-performance/tree/main) to measure the efficiency of your database design. Use the code to generate a set of pdf plots for latency to evaluate your choices including the following:

* How increasing the number of tables impacts schema synchronization times.
* Analyze whether separating unrelated tables into different databases improves performance.
* Validate the benefits of isolating data for different use cases or regions in separate databases.
* Understand the trade-offs of schema changes on query latency and how to mitigate them through better database organization.

### Schemas

A schema serves as a blueprint for how data is organized within a database, acting as a logical framework that groups tables, views, and indexes. Understanding how to structure and manage schemas is crucial for maintaining an organized database environment, making it easier to optimize queries and manage access. While schemas don’t directly improve query performance, the way you organize your data within them can significantly impact how efficiently queries run, especially as your data grows.

#### Schema best practices

To enhance query performance, simplify access control, and ensure scalability as your data grows, use the following best practices:

* **Logical Organization** &ndash; Grouping related tables, views, and indexes within a schema, to create a logical structure that makes it easier to navigate and optimize your queries. Well-organized data allows for clearer queries, reducing complexity and improving readability.
* **Simplified Access Control** &ndash; Using schemas to manage access to certain tables or views ensures that only relevant data is queried by specific users or roles. This prevents unnecessary data scans or joins, which can improve query execution time.
* **Scalability** &ndash; As your database grows, a well-structured schema becomes even more important. Organizing data in a way that scales efficiently prevents bottlenecks, ensuring that queries can continue to run quickly even with larger datasets.

### Tables
In Firebolt, tables are the key components for organizing and storing data. They consist of rows (records) and columns (attributes), making them an integral tool in data modeling. Firebolt supports two main types of tables:

* **Managed tables** &ndash; tables that are fully controlled by Firebolt, and make the best use of Firebolt’s optimization strategies. There are two types of managed tables, which serve different but complementary purposes:
    * **Fact tables** &ndash; store large volumes of quantitative data, such as sales metrics or user interactions, and are used for analysis and reporting.
    * **Dimension tables** &ndash; which hold descriptive data for enriching analyses, such as customer details or product categories. These tables are often duplicated across all nodes, and can dramatically improve query performance by providing fast access to frequently referenced information.

    By designing tables with both fact and dimension roles, users can optimize data management for reporting and analytics.
* **External tables** - tables that are external to Firebolt that allow you to query external data sources like Amazon S3. 

**Fact tables**

The following code example creates a **fact table**: 

```sql
CREATE TABLE borrowedbooks (
	transaction_id INT,
	book_id INT,
	member_id INT,
	checkout_date DATE,
	return_date DATE,
	late_fees NUMERIC
);
```

The internal structure of a fact table facilitates fast access to data even for very large datasets.

**Dimension tables**

Dimension tables are often replicated across all nodes, which enhances query performance and ensures quick access to frequently referenced information. 

The following code example creates a **dimension table**:

```sql
CREATE DIMENSION TABLE books (
	book_id INT,
	title TEXT,
	author TEXT,
	genre TEXT,
	publication_year INT
);
```

In the previous example, the `books` table stores details about the publication and is ideal for joining with fact tables like `borrowedbooks` to analyze borrowing patterns or book popularity.

**External tables**

External tables allow users to access and query data stored outside the database, such as in Amazon S3, without loading it into Firebolt. This capability is particularly useful when working with large datasets stored externally that don't require frequent access, enabling cost-efficient querying and avoiding data duplication. External tables generally have poorer performance compared to Firebolt managed tables because the data is not stored within Firebolt’s optimized infrastructure.

**Managing tables**

After you create a table, you can modify your table ownership, delete it including all of its dependencies. Use the following SQL commands to manage your table:

**Change table ownership**

To change the ownership of a table, use the ALTER TABLE statement with the OWNER TO clause. 

The following command assigns a new owner to the `borrowedbooks` table:

```sql
ALTER TABLE borrowedbooks OWNER TO 'new_owner';
```

**Delete a managed table**

Dropping a Firebolt managed table permanently deletes it along with all its data.

The following code checks to see if the `borrowedbooks` table exists and then deletes it:

```sql
DROP TABLE IF EXISTS borrowedbooks;
```

**Delete a managed table that has dependencies**

If the table that you want to delete has dependent objects such as views or aggregating indexes, you can use the `CASCADE` option to remove all dependencies together. 

The following code deletes the `borrowedbooks` table and all related objects:

```sql
DROP TABLE borrowedbooks CASCADE;
```

**Drop an external table**

If you drop an external table, you only remove its definition from Firebolt. The actual data remains in the external source. The following code drops the `external_books` external table:

```sql
DROP TABLE external_books;
```

#### Select a primary index

Primary indexes optimize query performance by logically organizing data for efficient access based on key columns, using sparse indexing to minimize unnecessary scans during queries. This allows Firebolt’s engine to prune unnecessary data during queries, minimizing the amount of data read from disk, and accelerating query execution. By selecting columns frequently used in filters, the primary index enables fast, efficient data retrieval, which is crucial for large-scale, data-intensive applications. Properly configuring primary indexes ensures that Firebolt can maintain high performance, even with complex queries and large datasets.

**How Firebolt uses a primary index to optimize performance**

When new data is inserted into a table, Firebolt organizes it into tablets, which are logical partitions of the table. Each tablet holds a portion of the data, sorted according to the primary index. During query processing, Firebolt uses these indexes to eliminate blocks of rows not matching query  predicate and scan only the necessary data, minimizing input and output operations, and optimizing performance.
For updates, Firebolt follows a “delete-and-insert” approach: the original row is marked for deletion, and the updated row is inserted into a new tablet. Deleted rows are not removed immediately but are flagged and later cleaned up during maintenance tasks.

**Create a primary index**

A primary index can only be defined when creating a new table, so if you need to modify the index, you'll have to create a new table. To define a primary index, use the `PRIMARY INDEX` clause to specify your columns, as shown in the following example:

```sql
CREATE TABLE borrowedbooks_pi(
  transaction_id INT,
  book_id INT,
  member_id INT,
  checkout_date DATE,
  return_date DATE,
  late_fees NUMERIC)
PRIMARY INDEX (book_id, checkout_date);
```
In the previous example, [CREATE TABLE]({% link sql_reference/commands/data-definition/create-fact-dimension-table.md %}) creates a fact table by default, and the primary index acts as a composite index of both the `book_id` and `checkout_date` columns. 

You can also create a primary index on a dimension table as shown in the following code example:

```sql
CREATE dimension TABLE books_pi(
  book_id INT,
  title TEXT,
  author TEXT,
  genre TEXT,
  publication_year INT
)
PRIMARY INDEX (book_id, title);
```

The primary index should include columns that are often used in queries that filter or aggregate data, including those that use `WHERE` and `GROUP BY` clauses, so that Firebolt can use these columns for efficient retrieval. Firebolt physically clusters the data in the table by the columns of the primary index. The primary index significantly improves query performance because it reduces the time spent scanning irrelevant rows and allows the query engine to retrieve only the necessary data.

##### Primary index best practices

To optimize query performance and maximize indexing efficiency, use the following best practices for designing composite primary indexes:

* **Column selection** &ndash; Carefully select which columns to include in a composite primary index based on query patterns, cardinality, and the specific use cases for your table. Adding unnecessary columns can negatively impact performance.
* **Column order** &ndash; The order of columns in a composite primary index is critical. Place the most selective, or highest cardinality columns first in a composite primary index. Firebolt will search based on the order of columns in the primary index. High-cardinality columns, which have many distinct values, improve index efficiency by reducing the number of rows that need to be scanned during queries.

#### Select an aggregating index
#### Select indexes and partitions for me


-----------------------old content-----------------

## Primary indexes

Firebolt uses primary indexes to physically sort data into the Firebolt File Format (F3) and colocates similar values, which allows data to be pruned at query runtime. When you query a table, rather than scanning the whole data set, Firebolt uses the table’s index to prune the data, reading only the relevant ranges of data to produce query results. Unnecessary ranges of data are never loaded from disk. 

Primary indexes in Firebolt are a type of *sparse index*. Unlike a dense index that maps every search key value in a file, a sparse index is a smaller construct that holds only one entry per data block (a compressed range of rows). By using the primary index to read a much smaller and highly compressed range of data from F3 into the engine cache at query runtime, Firebolt produces query results much faster with less disk I/O.

The video below explains sparse indexing. Eldad Farkash is the CEO of Firebolt.
<iframe width="560" height="315" src="https://www.youtube.com/embed/7XDTVB9gsFw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

For more information and examples, see [Primary indexes](../Guides/working-with-indexes/using-primary-indexes.md).

## Aggregating indexes

Aggregating indexes greatly reduce the compute resources required at query runtime in scenarios where there is a need to repeatedly execute aggregated functions on large tables with millions or billions of rows. Dashboards and repetitive reports are common use cases for aggregating indexes; it’s less common to create aggregating indexes for ad hoc queries. 

An aggregating index is like a materialized view in many ways, with technology proprietary to Firebolt that works together with the F3 storage format to make them more efficient. Firebolt uses an aggregating index to pre-calculate and store the results of aggregate functions that you define. At query runtime, Firebolt scans the aggregating indexes associated with a fact table to determine those that provide the best fit to accelerate query performance. To return query results, Firebolt uses the indexes rather than scanning the table.

Aggregating indexes are automatically updated as you ingest new data. The precalculated results of aggregate functions are stateful and consistent with the underlying fact table data on the engine. Firebolt automatically shards aggregating indexes to parallelize query execution across engine nodes.

The video below is a technical discussion of some issues with traditional materialized views and how Firebolt addresses the problem with unique technology. Eldad Farkash is the CEO of Firebolt.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Hniv9u4w7lI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

For more information and examples, see [Aggregating indexes](../Guides/working-with-indexes/using-aggregating-indexes.md).

## Join accelerators

In addition to user-managed primary and aggregated indexes, Firebolt provides built-in functionality to automatically accelerate joins between different tables. Join operations are often the most resource-intensive aspect of queries, slowing down queries and consuming engine resources. Firebolt reads the join cached in engine RAM rather than creating the join at query runtime. Join accelerators are created & held in RAM automatically for eligible queries, reducing disk I/O and compute resources at query runtime. Queries run faster and you can use engine resources more efficiently to reduce cost. 

To see how this works, let us look at an example. Say we have the following query pattern which is run hundreds of times per second with different values for l.player_id and l.date:

```sql
SELECT r.name, SUM(l.score) 
FROM   game_plays as l
JOIN   player_info as r 
ON     l.player_id = r.player_id
WHERE  l.player_id = XXX AND l.date = YYY
GROUP  BY r.name;
```

On the first run of this query, the relevant data from the right-hand side table player_info is read and stored in a specialized data structure, which is cached in RAM. This can take tens of seconds if the player_info table is large (e.g., contains millions of rows).

However, on subsequent runs of the query pattern, the cached data structure can be reused - so all subsequent queries will only take a few milliseconds (if the left-hand side with potential field restrictions is small, as here).

Not all join queries create (and use) join accelerators. Here is a set of requirements that must be met:
* The right side of the join in the query must be directly a table. Subselects or views are not supported.
* Restrictions on fields from the right side of the join need to be applied in an `OUTER SELECT`, wrapping the query.
* Since the join accelerator data structure is cached in RAM, the right side table may not be too large (by default the size of the cache is limited to 20% of the RAM).

## You can combine indexes

Each table has only one primary index, which is optional. You can have as many aggregating indexes as your workloads demand. Indexes are highly compressed. The cost of storing them is small when compared to the potential savings in engine runtime, number of nodes, and the engine spec.

## Firebolt maintains indexes automatically

After you define an index for a table, Firebolt updates the index on the general purpose engine that you use to ingest data (the engine that runs the `INSERT` statement). You don’t need to manually maintain or recreate indexes as you incrementally ingest data.


## Additional resources

* For in-depth information about index internals, see the *Firebolt Cloud Data Warehouse Whitepaper* sections on [Indexes](https://www.firebolt.io/resources/firebolt-cloud-data-warehouse-whitepaper#Indexes) and [Query Optimization](https://www.firebolt.io/resources/firebolt-cloud-data-warehouse-whitepaper#Query-optimization).
* To see examples of the application of indexes, see the Firebolt blog post, [Firebolt indexes in action](https://www.firebolt.io/blog/firebolt-indexes-in-action).

