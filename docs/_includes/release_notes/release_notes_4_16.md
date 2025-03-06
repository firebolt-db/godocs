## Firebolt Release Notes - Version 4.16

### New Features

<!-- Auto Generated Markdown for FIR-43599 - Owned by Misha Shneerson -->
**Added `MAX_CONCURRENCY` option to the `VACUUM` statement for enhanced concurrency control**         
The [VACUUM]({% link sql_reference/commands/data-management/vacuum.md %}) statement now includes the `MAX_CONCURRENCY` option, allowing users to limit the number of concurrent streams. This improves control over resource usage during `VACUUM` operation.

<!-- Auto Generated Markdown for FIR-43506 - Owned by Misha Shneerson -->
**Introduced the `INDEXES = ALL | NONE` for the `VACUUM` statement**         
The [VACUUM]({% link sql_reference/commands/data-management/vacuum.md %}) statement now supports the `INDEXES = ALL | NONE` option, giving users control over whether indexes are optimized during vacuum operations.

<!-- Auto Generated Markdown for FIR-43695 - Owned by Tobias Humig -->
**Added support for casting text literals to interval literals**         
Firebolt now supports casting text literals to interval literals using expressions like `'1 month'::INTERVAL`, making it easier to define time intervals in queries.

<!-- Auto Generated Markdown for FIR-42736 - Owned by Demian Hespe -->
**Added default value support for `GEOGRAPHY` columns**         
Firebolt now supports default values for columns with the [GEOGRAPHY]({% link sql_reference/geography-data-type.md %}#geography-data-type) data type. For example, `CREATE TABLE geo_table (geo_column GEOGRAPHY DEFAULT 'GEOMETRYCOLLECTION EMPTY')` ensures consistency across database entries when no explicit value is provided.

<!-- Auto Generated Markdown for FIR-43706 - Owned by Anton Perkov -->
**Added `MIN_CLUSTERS` and `MAX_CLUSTERS` columns to `INFORMATION_SCHEMA.ENGINES`**            
Added two new columns, `MIN_CLUSTERS` and `MAX_CLUSTERS`, to the `INFORMATION_SCHEMA.ENGINES` table. This enhancement provides users with additional details about cluster configurations, facilitating improved database management and analysis.

<!-- Auto Generated Markdown for FIR-41942 - Owned by Mosha Pasumansky -->
**Added support for `STATEMENT_TIMEOUT` to manage query execution time limits**              
Added support for `STATEMENT_TIMEOUT`. This feature specifies the number of milliseconds a statement is allowed to run. Any statement or query exceeding the specified time is canceled. A value of zero disables the timeout by default. This addition helps prevent excessively long-running queries, improving system efficiency and resource use.

<!-- Auto Generated Markdown for FIR-43693 - Owned by Tobias Humig -->
**Added the PostgreSQL function `DATE(<arg>)` as an alternative to `<arg>::DATE`**        
Firebolt now supports the `DATE(<arg>)` function, offering an alternative to the `<arg>::DATE` syntax for improved readability and usability in SQL queries.

<!-- Auto Generated Markdown for FIR-36879 - Owned by Mosha Pasumansky -->
**Supported the `FROM` first syntax for enhanced query flexibility and readability**           
SQL queries can now use `FROM` before `SELECT`, allowing for more flexible query structures such as `FROM t SELECT a, SUM(b) GROUP BY a` or even `FROM t` without a `SELECT` clause.

<!-- Markdown for FIR-35591 - Owned by Adam Bouhmad -->
**Support for AWS PrivateLink is now in public preview**      
[Firebolt now supports AWS PrivateLink]({% link Guides/security/privatelink.md %}), allowing Firebolt Enterprise customers to securely access the Firebolt API without exposing traffic to the public internet. AWS PrivateLink enhances security, minimizes data exposure, and improves network reliability by keeping traffic within AWS.

**Added concurrency auto-scaling**        
Engines can now be created with concurrency auto-scaling enabled, or modified to enable concurrency auto-scaling. Setting the `MIN_CLUSTERS` and `MAX_CLUSTERS` parameters on CREATE ENGINE and ALTER ENGINE commands turns on concurrency auto-scaling: the engine will dynamically resize between the specified `MIN_CLUSTERS` and `MAX_CLUSTERS` values to match demand.

**Firebolt introduces three fully managed editions**
Firebolt now offers **Standard, Enterprise, and Dedicated editions**, each designed for different performance, security, and scalability needs.
* **Standard**: High-performance, elastic scaling for cost-efficient, fully managed analytics.
* **Enterprise & Dedicated**: Includes **multi-cluster scaling, AWS PrivateLink**, and **advanced security features**.
* **Dedicated**: Built for regulated industries (finance, healthcare) with **single-tenant infrastructure** and compliance with **HIPAA, SOC 2, ISO**.
  
Enterprise and Dedicated customers also get **faster support response times**, **Slack-based support**, and a **designated support engineer**. For more information on Firebolt's editions, refer to the [Pricing and billing]({% link Overview/billing.md %}) page. 

### Behavior Changes

<!-- Auto Generated Markdown for FIR-38200 - Owned by Jonathan Doron -->  
**Removed a planner rule that transform aggregations on a case statement**
The planner rule that converted `AGG(CASE WHEN P THEN V ELSE NULL END)` into `AGGIF(V, P)` has been removed to simplify query processing.

### Performance Improvements

<!-- Auto Generated Markdown for FIR-43659 - Owned by Demian Hespe -->
**Introduced pruning for `GEOGRAPHY` columns at the tablet level to enhance query performance**           
Firebolt now prunes [GEOGRAPHY]({% link sql_reference/geography-data-type.md %}#geography-data-type) data at the tablet level to enhance query performance. To activate spatial pruning on tables created before this release, run `VACUUM`. For additional details, see our [blog post](https://www.firebolt.io/blog/architecture-and-internal-representation-of-the-geography-data-type).

<!-- Auto Generated Markdown for FIR-42544 - Owned by Judson Wilson -->
**Added `INDEX_GRANULARITY` storage parameter to optimize table storage**          
The `CREATE TABLE` statement now supports the `INDEX_GRANULARITY` storage parameter, allowing users to configure internal tablet range sizes for better performance based on query patterns. 

### Bug Fixes

<!-- Auto Generated Markdown for FIR-43485 - Owned by Tal Zelig -->
**Fixed permission conflicts on public schemas across multiple databases**            
Resolved an issue where granting identical permissions on public schemas in different databases caused conflicts. This fix ensures correct permission application for improved database security.
