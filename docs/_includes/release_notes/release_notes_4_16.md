## Firebolt Release Notes - Version 4.16

### New Features

<!-- Auto Generated Markdown for FIR-43599 - Owned by Misha Shneerson -->
**Added `MAX_CONCURRENCY` option to the `VACUUM` statement for enhanced concurrency control**         
The [VACUUM]({% link sql_reference/commands/data-management/vacuum.md %}) statement now includes the `MAX_CONCURRENCY` option, allowing users to limit the number of concurrent streams. This improves control over resource usage during `VACUUM` operation.

<!-- Auto Generated Markdown for FIR-43506 - Owned by Misha Shneerson -->
**Introduced the `INDEXES = ALL | NONE` for the `VACUUM` statement**         
The [VACUUM]({% link sql_reference/commands/data-management/vacuum.md %}) statement now supports the `INDEXES = ALL | NONE` option, giving users control over whether indexes are optimized during vacuum operations.

<!-- Auto Generated Markdown for FIR-43695 - Owned by Tobias Humig -->
**Added support for casting text literals to interval literals with expressions like `'1 month'::INTERVAL`**         
Interval literals are now supported as casts from text literals, such as `'1 month'::INTERVAL`. This makes it easier to represent time intervals in SQL queries.

<!-- Auto Generated Markdown for FIR-42736 - Owned by Demian Hespe -->
**Added default value support for `GEOGRAPHY` columns**         
Default value support was added for `GEOGRAPHY` columns. Users can now specify a default value when creating a `GEOGRAPHY` column. For example, use `CREATE TABLE geo_table (geo_column GEOGRAPHY DEFAULT 'GEOMETRYCOLLECTION EMPTY')`. This simplifies table setup and ensures consistency across database entries when no explicit value is provided.

<!-- Auto Generated Markdown for FIR-43706 - Owned by Anton Perkov -->
**Added `MIN_CLUSTERS` and `MAX_CLUSTERS` columns to `INFORMATION_SCHEMA.ENGINES`**            
Added two new columns, `MIN_CLUSTERS` and `MAX_CLUSTERS`, to the `INFORMATION_SCHEMA.ENGINES` table. This enhancement provides users with additional details about cluster configurations, facilitating improved database management and analysis.

<!-- Auto Generated Markdown for FIR-41942 - Owned by Mosha Pasumansky -->
**Added support for `STATEMENT_TIMEOUT` to manage query execution time limits**              
Added support for `STATEMENT_TIMEOUT`. This feature specifies the number of milliseconds a statement is allowed to run. Any statement or query exceeding the specified time is canceled. A value of zero disables the timeout by default. This addition helps prevent excessively long-running queries, improving system efficiency and resource use.

<!-- Auto Generated Markdown for FIR-43693 - Owned by Tobias Humig -->
**Added the PostgreSQL function `DATE(<arg>)` as an alternative to `<arg>::DATE` for improved query readability and usability**        
The PostgreSQL function `DATE(<arg>)` was added as an alternative syntax to `<arg>::DATE`. This addition provides users with a more intuitive way to convert data to dates, enhancing readability and ease of use in SQL queries.

<!-- Auto Generated Markdown for FIR-36879 - Owned by Mosha Pasumansky -->
**Supported the `FROM` first syntax for enhanced query flexibility and readability**           
The SQL data warehouse now supports the `FROM` first syntax. This change permits placing the `FROM` clause before the `SELECT` clause, enhancing query flexibility. For instance, it allows queries like `FROM t SELECT a, SUM(b) GROUP BY a` or even just `FROM t` by omitting the `SELECT` clause. Users can experience improved readability and ordering of SQL queries.

<!-- Markdown for FIR-35591 - Owned by Adam Bouhmad -->
**Support for AWS PrivateLink is now in public preview**      
Firebolt Enterprise customers can now securely access Firebolt APIs over AWS’s backbone network through AWS PrivateLink integration.

**Added concurrency auto-scaling**        
Engines can now be created with concurrency auto-scaling enabled, or modified to enable concurrency auto-scaling. Setting the `MIN_CLUSTERS` and `MAX_CLUSTERS` parameters on CREATE ENGINE and ALTER ENGINE commands turns on concurrency auto-scaling: the engine will dynamically resize between the specified `MIN_CLUSTERS` and `MAX_CLUSTERS` values to match demand.

**Firebolt introduces three fully managed editions**
Firebolt now offers **Standard, Enterprise, and Dedicated editions**, each designed for different performance, security, and scalability needs.
* **Standard**: High-performance, elastic scaling for cost-efficient, fully managed analytics.
* **Enterprise & Dedicated**: Includes **multi-cluster scaling, AWS PrivateLink**, and **advanced security features**.
* **Dedicated**: Built for regulated industries (finance, healthcare) with **single-tenant infrastructure** and compliance with **HIPAA, SOC 2, ISO**.
  
Enterprise and Dedicated customers also get **faster support response times**, **Slack-based support**, and a **designated support engineer**. For more information on Firebolt's editions, refer to the [Pricing and billing]({% link Overview/billing.md %}) page. 

### Behavior Changes

### Performance Improvements

<!-- Auto Generated Markdown for FIR-43659 - Owned by Demian Hespe -->
**Introduced pruning for `GEOGRAPHY` columns at the tablet level to enhance query performance**           
Introduced pruning at the tablet level for `GEOGRAPHY` columns, improving query performance. For tables created before this release, running `VACUUM` is necessary to activate spatial pruning. For more information as well as tips for improving pruning potential, read our [blog post](https://www.firebolt.io/blog/architecture-and-internal-representation-of-the-geography-data-type).

<!-- Auto Generated Markdown for FIR-42544 - Owned by Judson Wilson -->
**Introduced the `INDEX_GRANULARITY` storage parameter in `CREATE TABLE` to optimize table storage for specific query patterns**          
Added the `INDEX_GRANULARITY` storage parameter to `CREATE TABLE` to control the internal tablet range size for new tables. This setting optimizes table storage for specific query patterns, enhancing performance.

### Bug Fixes

<!-- Auto Generated Markdown for FIR-38200 - Owned by Jonathan Doron -->  
**Removed a planner rule that transform aggregations on a case statement**
The dedicated planner rule, which transformed aggregations like `agg(CASE WHEN P THEN V ELSE NULL END)` into `AGGIF(V, P)`, has been removed. This change simplifies query structures by removing unused internal plan representation.

<!-- Auto Generated Markdown for FIR-43485 - Owned by Tal Zelig -->
**Fixed conflicts when granting identical permissions on public schemas in different databases**            
Resolved an issue where granting the same permissions on public schemas across different databases caused conflicts. This fix ensures that permissions are applied correctly, improving database management and security.
