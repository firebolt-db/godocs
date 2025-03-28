---
layout: default
title: Explore compute cost
description: How Firebolt bills for compute usage
parent: Pricing and billing
nav_order: 1
---

# Explore compute cost

You can use data from the `information_schema.engines_billing` and `information_schema.engine_history` views, to analyze and optimize compute costs related to engine usage, scaling, and auto-stop events. The following queries will guide you in tracking engine costs, identifying cost patterns, and understanding the impact of different configurations on your compute expenses.

Topics:
* [How to track hourly average costs over time](#how-to-track-hourly-average-costs-over-time) &ndash; Learn how to track hourly patterns in engine costs.
* [How to find top users by cost](#how-to-find-top-users-by-cost) &ndash; Learn how to identify the users that are responsible for the highest compute costs.
* [Find the cost impact of auto-stop events](#find-the-cost-impact-of-auto-stop-events) &ndash; Learn how to compare engine costs before and after an auto-stop event.

## How to track hourly average costs over time

You can analyze daily trends to identify peak load hours and better understand the times when engine usage and associated costs are the highest. The following code example calculates the average billed cost per hour over the past 7 days, grouping the results by hour of the day:

```sql
SELECT EXTRACT(HOUR FROM usage_date) AS usage_hour, 
       AVG(billed_cost) AS avg_hourly_cost
FROM information_schema.engines_billing
WHERE usage_date >= CURRENT_DATE - INTERVAL '7 days'
GROUP BY EXTRACT(HOUR FROM usage_date)
ORDER BY usage_hour;
```

## How to find top users by cost

You can analyze engine billing data to identify the users who are responsible for the highest engine costs over a specific period. Use this information to hold teams or individuals accountable for their resource usage.

The following code example calculates the total billed cost for each engine owner between the specified dates, sorting the results in descending order to show the highest spenders first:

```sql
SELECT eh.engine_owner, SUM(eb.billed_cost) AS total_cost
FROM information_schema.engines_billing eb
JOIN information_schema.engine_history eh USING (engine_name)
WHERE eb.usage_date BETWEEN DATE '2025-02-24' AND DATE '2025-03-26'
GROUP BY eh.engine_owner
ORDER BY total_cost DESC;
```

## Find the cost impact of auto-stop events

When you [create an engine]({% link sql_reference/commands/engines/create-engine.md %}), you can set the `AUTO_STOP` parameter to automatically stop an engine after it has been idle for a specified number of minutes. You can query the engine history before and after an auto-stop event to see if auto-stop functionality results in cost savings.

The following code example calculates the billed cost for engines both before and after an auto-stop event, showing how the cost changes once the engine is stopped automatically:

```sql
SELECT eb.engine_name,
       CAST(eh.event_start_time AS DATE) AS auto_stop_date,
       SUM(CASE WHEN eb.usage_date < CAST(eh.event_start_time AS DATE) THEN eb.billed_cost ELSE 0 END) AS cost_before,
       SUM(CASE WHEN eb.usage_date >= CAST(eh.event_start_time AS DATE) THEN eb.billed_cost ELSE 0 END) AS cost_after
FROM information_schema.engine_history eh
JOIN information_schema.engines_billing eb ON eh.engine_name = eb.engine_name
WHERE eh.event_type = 'AUTO_STOP'
GROUP BY eb.engine_name, CAST(eh.event_start_time AS DATE);
```