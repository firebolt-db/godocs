---
layout: default
title: Explore compute cost
description: How Firebolt bills for compute usage
parent: Pricing and billing
nav_order: 1
---

# Explore compute cost

You can use data from the [`information_schema.engines_billing`]({% link sql_reference/information-schema/engines-billing.md %}) and [`information_schema.engine_history`]({% link sql_reference/information-schema/engine-history.md %}) views, to analyze and optimize compute costs related to engine usage, scaling, and auto-stop events. The following queries help track compute costs, identify cost patterns, and understand the impact of different configurations on your compute expenses.

## Examples

**Cost tracking and analysis**

* [Track hourly average costs over time](#track-hourly-average-costs-over-time) &ndash; Learn how to track hourly patterns in compute costs.
* [Find top users by cost](#find-top-users-by-cost) &ndash; Learn how to identify users that are responsible for the highest compute costs.
* [Find the cost impact of auto-stop events](#find-the-cost-impact-of-auto-stop-events) &ndash; Learn how to query engine history before and after an auto-stop event to determine if the auto-stop functionality leads to cost savings.
* [Calculate costs incurred after engine deletion](#calculate-costs-incurred-after-engine-deletion) &ndash; Learn how to track costs that continue to accumulate even an engine has stopped running.
* [Calculate costs incurred after engine creation or scaling](#calculate-costs-incurred-after-engine-creation-or-scaling) &ndash; Learn how to calculate the cost of provisioning or resizing engines to optimize resource allocation.

**Engine configuration and optimization**

* [Rank engine configurations by total cost](#rank-engine-configurations-by-total-cost) &ndash; Learn how to analyze engine billing data understand which combinations of engine type, family, and node count drive the most cost.
* [Rank efficiency by cluster count](#rank-efficiency-by-cluster-count) &ndash; Learn how to determine if single or multi-cluster setups are more efficient.
* [Calculate cost savings through auto-stop](#calculate-cost-savings-through-auto-stop) &ndash; Learn how to compare the average cost of engines with auto-stop enabled versus disabled.

### Track hourly average costs over time

You can use `information_schema.engines_billing` to track hourly average costs over time and identify peak load hours, allowing you to pinpoint when engine usage and costs are highest. Use this data to enable more efficient resource allocation and better cost optimization. Analyze daily trends to identify peak load hours and better understand the times when engine usage and associated costs are the highest. 

The following code example calculates the average billed cost per hour over the past 7 days, grouping the results by hour of the day:

```sql
SELECT EXTRACT(HOUR FROM usage_date::TIMESTAMP) AS usage_hour, 
       AVG(billed_cost) AS avg_hourly_cost
FROM information_schema.engines_billing
WHERE usage_date >= CURRENT_DATE - INTERVAL '7 days'
GROUP BY EXTRACT(HOUR FROM usage_date::TIMESTAMP)
ORDER BY usage_hour;
```

### Find top users by cost

You can use `information_schema.engines_billing` and `information_schema.engine_history` to identify the top engine owners by analyzing engine billing data. Pinpoint the individuals or teams responsible for the highest engine costs over a specific period, fostering accountability and enabling more effective resource management.

The following code example calculates the total billed cost for each engine owner between the specified dates, sorting the results in descending order to show the highest spenders first:

```sql
SELECT engine_history_table.engine_owner, SUM(engine_billing_table.billed_cost) AS total_cost
FROM information_schema.engines_billing engine_billing_table
JOIN information_schema.engine_history engine_history_table USING (engine_name)
WHERE engine_billing_table.usage_date BETWEEN DATE '2025-02-24' AND DATE '2025-03-26'
GROUP BY engine_history_table.engine_owner
ORDER BY total_cost DESC;
```

### Find the cost impact of auto-stop events

When you [create an engine]({% link sql_reference/commands/engines/create-engine.md %}), you can set the `AUTO_STOP` parameter to automatically stop an engine after it has been idle for a specified number of minutes. Query the engine history before and after an auto-stop event to see if auto-stop functionality results in cost savings.

The following code example calculates the billed cost for engines both before and after an auto-stop event, showing how the cost changes once the engine is stopped automatically:

```sql
SELECT engine_billing_table.engine_name,
       CAST(engine_history_table.event_start_time AS DATE) AS auto_stop_date,
       SUM(CASE WHEN engine_billing_table.usage_date < CAST(engine_history_table.event_start_time AS DATE) THEN engine_billing_table.billed_cost ELSE 0 END) AS cost_before,
       SUM(CASE WHEN engine_billing_table.usage_date >= CAST(engine_history_table.event_start_time AS DATE) THEN engine_billing_table.billed_cost ELSE 0 END) AS cost_after
FROM information_schema.engine_history engine_history_table
JOIN information_schema.engines_billing engine_billing_table ON engine_history_table.engine_name = engine_billing_table.engine_name
WHERE engine_history_table.event_type = 'AUTO_STOP'
GROUP BY engine_billing_table.engine_name, CAST(engine_history_table.event_start_time AS DATE);
```

### Calculate costs incurred after engine deletion

Use engine history and billing information to identify any billing discrepancies that occur after an engine has been deleted. By examining any charges that incurred after an engine was deleted, you can detect any unresolved billing issues or configuration errors.

The following code calculates the total billed cost incurred after an engine deletion event, identifying any charges that are incurred after the engine has been deleted, and grouping the results by engine name:

```sql
SELECT engine_billing_table.engine_name, MAX(engine_history_table.event_finish_time) AS deletion_time,
       SUM(engine_billing_table.billed_cost) AS post_deletion_cost
FROM information_schema.engine_history engine_history_table
JOIN information_schema.engines_billing engine_billing_table ON engine_history_table.engine_name = engine_billing_table.engine_name
WHERE engine_history_table.event_type = 'ENGINE_DELETE'
  AND engine_billing_table.usage_date > CAST(engine_history_table.event_finish_time AS DATE)
GROUP BY engine_billing_table.engine_name
HAVING SUM(engine_billing_table.billed_cost) > 0;
```

### Calculate costs incurred after engine creation or scaling

Analyze engine billing data to track the costs incurred after engine creation or scaling events to understand the immediate financial impact of provisioning or resizing engines and optimize resource allocation. Rank them to find top combinations of engine size and architecture by cost.

The following code calculates the total billed cost for each engine after an `ENGINE_CREATE` or `SCALE_UP` event, grouping the results by engine name and event type, and sorting the output by the total cost in descending order:

```sql
SELECT engine_billing_table.engine_name, engine_history_table.event_type, CAST(engine_history_table.event_start_time AS DATE) AS event_date,
       SUM(engine_billing_table.billed_cost) AS total_cost_after_event
FROM information_schema.engine_history engine_history_table
JOIN information_schema.engines_billing engine_billing_table ON engine_history_table.engine_name = engine_billing_table.engine_name
WHERE engine_history_table.event_type IN ('ENGINE_CREATE', 'SCALE_UP')
  AND engine_billing_table.usage_date > CAST(engine_history_table.event_start_time AS DATE)
GROUP BY engine_billing_table.engine_name, engine_history_table.event_type, CAST(engine_history_table.event_start_time AS DATE)
ORDER BY total_cost_after_event DESC;
```

### Rank engine configurations by total cost

Analyze engine billing data to rank engine configurations by total cost, identifying those driving the highest expenses. Optimize resource allocation and more cost-effective decisions for your engine setup.

The following code calculates the total billed cost for different engine configurations that ran of type, family, and node count, over a specified date range, and sorts the results by total cost in descending order:

```sql
SELECT engine_history_table.type, engine_history_table.family, engine_history_table.nodes, SUM(engine_billing_table.billed_cost) AS total_cost
FROM information_schema.engines_billing engine_billing_table
JOIN information_schema.engine_history engine_history_table USING (engine_name)
WHERE engine_billing_table.usage_date BETWEEN DATE '2025-02-24' AND DATE '2025-03-26'
GROUP BY engine_history_table.type, engine_history_table.family, engine_history_table.nodes
ORDER BY total_cost DESC;
```

### Rank efficiency by cluster count

Ranking efficiency by cluster count helps assess the cost-effectiveness of single versus multi-cluster setups. Analyzing engine billing data enables you to track associated costs and optimize resource allocation based on cost efficiency.

The following code example calculates the cost per [FBU]({% link Overview/engine-consumption.md %}#engine-consumption) for single or multi-cluster setups by dividing the total billed cost by the total consumed FBUs for each cluster configuration, and then sorting the results by cost per FBU in descending order:

```sql
SELECT engine_history_table.clusters, SUM(engine_billing_table.billed_cost) / NULLIF(SUM(engine_billing_table.consumed_fbu), 0) AS cost_per_fbu
FROM information_schema.engines_billing engine_billing_table
JOIN information_schema.engine_history engine_history_table USING (engine_name)
WHERE engine_billing_table.usage_date BETWEEN DATE '2025-02-24' AND DATE '2025-03-26'
GROUP BY engine_history_table.clusters
ORDER BY cost_per_fbu DESC;
```

### Calculate cost savings through auto-stop

Calculating cost savings through auto-stop allows you to compare the daily costs of engines with auto-stop enabled and disabled, helping you understand its impact on costs and optimize resource allocation.

The following code example calculates the average daily billed cost for engines with auto-stop enabled and disabled, grouping the results by the auto-stop setting to provide insights into the cost impact of having auto-stop turned on or off:

```sql
SELECT engine_history_table.auto_stop, AVG(engine_billing_table.billed_cost) AS avg_cost
FROM information_schema.engines_billing engine_billing_table
JOIN information_schema.engine_history engine_history_table USING (engine_name)
WHERE engine_billing_table.usage_date BETWEEN DATE '2025-02-24' AND DATE '2025-03-26'
GROUP BY engine_history_table.auto_stop;
```