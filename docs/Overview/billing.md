---
layout: default
title: Billing
description: How Firebolt bills for usage
parent: Overview
nav_order: 2
---

# Billing

Firebolt provides a scalable cloud data warehouse solution designed to be simple, transparent, and flexible. Pricing is based on two main factors:

* **Compute resources** &ndash; Compute costs depend on the size and duration of the clusters you use.
* **Data storage** &ndash; Storage costs are based on the amount of data stored, including compressed storage. 

Firebolt offers flexible pricing options to accommodate different workloads and business needs including the following:  

* Auto-scaling &ndash; Dynamically adjust cluster resources based on workload requirements.
* Workload isolation &ndash; Run multiple clusters concurrently for optimized performance without affecting other workloads.
* Serverless capabilities &ndash; Pay only for completed queries with no charges for idle time.

Start using Firebolt and receive $200 in free credits for the first 30 days.

## Usage-based compute costs

Firebolt compute costs are determined by the following:
* The number of compute nodes used to process your workload.
* The type of node selected. You can choose a small (S), medium (M), large (L) or extra-large (XL) node.

Usage is calculated with one-second granularity, from the time that Firebolt makes the engine available for queries until it enters a stopped state.

## Cluster size

Compute pricing is elastic, and you pay only for the resources you consume during query processing.

Sizing is determined in FBUs (Firebolt Units) as follows:

1 FBU = $0.35 /hr

| Node type        | Sizing in FBU | Pricing in $USD |
|------------------|---------------|--------------|
| Small (S)        | 8             | $2.80 / hr    |
| Medium (M)       | 16            | $5.60 / hr    |
| Large (L)        | 32            | $11.20 / hr   |
| Extra Large (XL) | 64            | $22.40 / hr   |


## Storage
 
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
Firebolt offers two main subscription plans:

* **Pay-as-you-go** &ndash; Flexible, on-demand pricing with no upfront commitment. This plan is ideal for startups or teams with unpredictable workloads.

* **Committed use discounts** &ndash; Receive discounted rates in exchange for committing to a specified usage volume. This plan is recommended for organizations with predictable workloads.

Contact [support@firebolt.io](mailto:support@firebolt.io) to discuss custom enterprise plans or annual pricing commitments.

## Set-up account billing through AWS Marketplace
To continue using Firebolt’s engines for query processing after your initial $200 credit, you’ll need to set up a billing account by connecting your account to the [AWS Marketplace](https://aws.amazon.com/marketplace), as follows: 

1. Login to [Firebolt's Workspace](https://go.firebolt.io/login). If you haven’t yet registered with Firebolt, see the [Get Started]({% link Guides/getting-started/index.md %}) guide.
2. In the Firebolt Workspace, select the Configure(<img src="../assets/images/configure-icon.png" width="20" alt="The Firebolt Configure Space icon">) icon from the left navigation pane.
2. Under **Organization settings**, select **Billing**.
3. Select **Connect to AWS Marketplace** to navigate to the Firebolt page on AWS Marketplace.
4. Select **View Purchase Options** in the top-right corner of the screen.
5. Select **Setup Your Account**.
  
Your account should now be associated with AWS Marketplace.

## Cost estimates

Firebolt provides a usage dashboard to help you monitor resource consumption. Billing invoices are generated on a monthly basis, and provide a detailed breakdown of resource consumption and associated costs.

## Support
For pricing or billing inquiries, contact Firebolt's support team at [support@firebolt.io](mailto:support@firebolt.io).
