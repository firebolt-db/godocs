---
layout: default
title: Engine metrics history
description: Use this reference to learn about the resource consumption of your engine
parent: Information schema
grand_parent: SQL reference
---

# Information schema for engine metrics history

You can use the `information_schema.engine_metrics_history` view to return information about the resource consumption of your engine. As engines can have 1 or more engine clusters that are transient, this provides visibilty into the utilization of each engine cluster. Each rows represents the aggregate resource metrics for a single engine cluster at the given event time. Per default, we collect 2 metric snapshots per minute for the last 30 days. You can use a `SELECT` query to return the metrics for each engine cluster at a given point in time as shown in the example below.

```sql
SELECT
  *
FROM
  information_schema.engine_metrics_history
WHERE
  event_time > now() - INTERVAL '2 hours'
LIMIT 100;
```

## Columns in information_schema.engine_metrics_history

Each row has the following columns with information about each query in query history.

| Column Name       | Data Type   | Description                                                                                |
|:------------------|:------------|:-------------------------------------------------------------------------------------------|
| engine_ordinal    | BIGINT      | the cluster number
| event_time        | TIMESTAMPTZ | timestamp at which the metrics where collected                                             |
| cpu_used          | DECIMAL     | current CPU utilization (percentage)                                                       |
| memory_used       | DECIMAL     | current memory used (percentage)                                                           |
| disk_used         | DECIMAL     | currently used disk space which encompasses space used for cache and spilling (percentage) |
| cache_hit_ratio   | DECIMAL     | current SSD cache hit ratio                                                                |
| spilled_bytes     | BIGINT      | amount of spilled data to disk in bytes                                                    |
| running_queries   | BIGINT      | number of currently running queries in the system                                          |
| suspended_queries | BIGINT      | number of queries that have been suspended (not-running and awaiting to be executed)       |
