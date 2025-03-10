---
layout: default
title: Pricing and billing
description: How Firebolt bills for usage
parent: Overview
nav_order: 2
---

# Pricing and billing

Firebolt provides a scalable cloud data warehouse solution designed to be simple, transparent, and flexible. 

Pricing is based on two main factors:

* [Compute costs](#compute-costs) &ndash; Compute costs depend on the size and duration of the clusters you use.
* [Data storage](#data-storage) &ndash; Storage costs are based on the amount of data stored, including compressed storage. 

Firebolt offers flexible pricing options to accommodate different workloads and business needs including the following:  

* Auto-scaling &ndash; Dynamically adjust cluster resources based on workload requirements.
* Workload isolation &ndash; Run multiple clusters concurrently for optimized performance without affecting other workloads.
* Serverless capabilities &ndash; Pay only for completed queries with no charges for idle time.

When you start using Firebolt, you receive $200 in free credits to use in the first 30 days. Afterwards, you can sign up for one of Firebolt's [subscription plans](#subscription-plans).

## Compute costs

Firebolt compute costs are determined by the following:

* The number of compute nodes used to process your workload.
* The type of node selected. You can choose a small (S), medium (M), large (L) or extra-large (XL) node from either the storage-optimized or compute-optimized node family.

Usage is calculated with one-second granularity, from the time that Firebolt makes the engine available for queries until it enters a stopped state.

Compute pricing is elastic, and you pay only for the resources you consume during query processing.

Sizing is determined in FBUs (Firebolt Units) as follows:

| Node type        | Compute family    | Sizing in FBU    |
|------------------|-------------------|------------------|
| Small (S)        | Storage-optimized | 8                |
| Medium (M)       | Storage-optimized | 16               |
| Large (L)        | Storage-optimized | 32               |
| Extra Large (XL) | Storage-optimized | 64               |
| Small (S)        | Compute-optimized | 4                |
| Medium (M)       | Compute-optimized | 8                |
| Large (L)        | Compute-optimized | 16               |
| Extra Large (XL) | Compute-optimized | 32               |

The price of an FBU varies by Firebolt edition and region.

## Data storage
 
Usage is calculated based on the daily average amount of data in bytes stored under your Firebolt account name, including both indexes and raw compressed data.

Data storage costs vary by AWS region and are based on the [Amazon S3 prices](https://aws.amazon.com/s3/pricing), with no additional charges.

| Region                    | Price per TB per month in $USD |
|---------------------------|----------------------------|
| US East (N. Virginia)      | $23.00                     |
| US West (Oregon)           | $23.00                     |
| Europe (Frankfurt)         | $24.50                     |
| Europe (Ireland)           | $23.00                     |
| Asia Pacific (Singapore)   | $25.00                     |


## Subscription Plans
To continue using Firebolt’s engines for query processing after your initial $200 credit, you must set up a subscription plan. Firebolt offers two main plans:

* [Pay-as-you-go](#pay-as-you-go-plan) &ndash; A flexible plan that requires no commitment.
* [Commited-use](#committed-use-discount-plan) &ndash; A plan where you pay for usage up-front, and Firebolt loads discounted usage credits into your account.

### Pay-as-you-go plan

A pay-as-you-go plan is flexible, and provides on-demand pricing with no upfront commitment. This plan is ideal for startups or teams with unpredictable workloads. In order to use this plan, you’ll need to set up account billing through [AWS Marketplace](https://aws.amazon.com/marketplace) as follows: 

1. Login to [Firebolt's Workspace](https://go.firebolt.io/login). If you haven’t yet registered with Firebolt, see the [Get Started]({% link Guides/getting-started/index.md %}) guide.
2. In the Firebolt Workspace, select the Configure(<img src="../assets/images/configure-icon.png" width="20" alt="The Firebolt Configure Space icon">) icon from the left navigation pane.
2. Under **Configure**, select **Billing**.
3. Select **Connect to AWS Marketplace** to navigate to the Firebolt page on AWS Marketplace.
4. Select **View Purchase Options** in the top-right corner of the screen.
5. Select **Setup Your Account**.
  
You pay for your consumption through AWS Marketplace at the end of each month.

### Committed-use discount plan

In a committed-use discount plan, you receive discounted rates in exchange for committing to a specified usage volume. This plan is recommended for organizations with predictable workloads.

Contact [support@firebolt.io](mailto:support@firebolt.io) to discuss a committed-use plan, custom enterprise plans or annual pricing commitments.

## Billing dashboard

You can use Firebolt's billing dashboard to monitor resource consumption, track expenses, monitor payments, and analyze billing trends efficiently.

Billing invoices are generated on a monthly basis, and provide a detailed breakdown of resource consumption and associated costs.

To access the dashboard:
1. Login to [Firebolt's Workspace](https://go.firebolt.io/login). If you haven’t yet registered with Firebolt, see the [Get Started]({% link Guides/getting-started/index.md %}) guide.
2. In the Firebolt Workspace, select the Configure(<img src="../assets/images/configure-icon.png" width="20" alt="The Firebolt Configure Space icon">) icon from the left navigation pane.
2. Under **Configure**, select **Billing**.

## Support
For pricing or billing inquiries, contact Firebolt's support team at [support@firebolt.io](mailto:support@firebolt.io).
