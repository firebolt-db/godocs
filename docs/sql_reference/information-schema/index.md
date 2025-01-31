---
redirect_from:
    - /general-reference/information-schema/databases.html
layout: default
title: Information schema
description: Reference for Information Schema views
nav_order: 2
parent: SQL reference
has_toc: true 
has_children: true
---

## Information Schema Views

The Firebolt information schema consists of a set of system views that contain metadata information on the objects defined in the current account, as well as database usage views.
Firebolt supports `information_schema` schema based on ANSI SQL standard, but extended with Firebolt specific information, both as additional columns in standard views, and as additional views.
For better compatibility with applications that rely on Postgres specific system views, Firebolt also supports `pg_catalog` schema and subset of Postgres compatible views in it.

Not all information schema views are available on Firebolt's system engine or within the **Firebolt Workspace**. The following views are unavailable:
* `engine_metrics_history`
* `engine_running_queries`
* `engine_query_history`
* `engine_user_query_history`
