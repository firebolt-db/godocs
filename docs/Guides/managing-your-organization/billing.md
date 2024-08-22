---
layout: default
title: Billing
description: Understand how Firebolt bills for compute and storage through the AWS Marketplace and your AWS account.
nav_order: 11
parent: Manage organization
---

# Billing

Firebolt bills are based on the consumption of resources within each account in your organization. This includes the total amount of data stored and engine usage.

* **Data storage** usage is calculated on the daily average amount of data (in bytes) stored under your Firebolt account name for indexes and raw compressed data.

* **Engine resources** usage is calculated with **one-second granularity** between the time Firebolt starts to provision the engine and when the request to terminate the engine is submitted. Warmup time for caching indexes and raw data is counted in engine usage time.

## Invoices

Invoices for Firebolt engines and data are submitted through the AWS Marketplace. The final monthly invoice is available on the third day of each month through the AWS Marketplace. A billing cycle starts on the first day of the month and finishes on the last day of the same month.

## Viewing billing information

Users with the **Org Admin** role can monitor the cost history of each account in the organization.

**To view cost information for your organization**
Organization cost details are captured in two information_schema tables. Query those two tables and retrieve any information about the organization's cost   
1) [Engines billing](../../sql_reference/information-schema/engines-billing.md)
2) [Storage billing](../../sql_reference/information-schema/storage-billing.md)

{: .note}
Firebolt billing is reported to the AWS Marketplace at the beginning of the next day. By default, the **Accounts & Billing** page displays the engine usage breakdown based on billing time. If you prefer to see the engine usage by actual usage day, you can click the **Engines breakdown** selector under the **Usage cost by engine** table and click **Actual running time**. 