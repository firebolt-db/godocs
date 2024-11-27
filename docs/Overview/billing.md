## Overview
Get started with Firebolt and get $200 in free credits for your first 30 days.

## Firebolt Pricing 
Firebolt provides a scalable and efficient cloud data warehouse solution tailored to the needs of modern analytics. Firebolt pricing model is designed to offer simplicity, transparency, and scalability to support a wide range of workloads.
Firebolt charges for the following:
1. Compute Resources: Based on the compute clusters you use (by their size and duration).
2. Data Storage: Charges apply for the storage used on Firebolt, including compressed storage.

## Pricing Components
### 1. Compute (Usage-Based)
Firebolt compute costs are determined by:
#of Nodes: Number of nodes used to process your workload.
Type of Nodes: Type of node selected (S, M, L, XL)
Usage is calculated with one-second granularity between the time Firebolt makes the engine available for queries and when the the engine moves to the stopped state.

### Cluster Sizes and Pricing:
Compute pricing is elastic—you only pay for the resources you consume during query execution.
Sizing is determined in FBU's (Firebolt Units).
1 FBU = $0.35 /hr
Node Type |  Sizing in FBU |  Pricing in $ |
|-----|-----|-----|
|Small (S)           |8   |$2.80 /hr  |
|Medium (M)          |16  |$5.60 /hr  |
|Large (L)           |32  |$11.20 /hr | 
|Extra Large (XL)    |64  |$22.40 /hr |

### 2. Storage
Usage is calculated on the daily average amount of data (in bytes) stored under your Firebolt account name for indexes and raw compressed data. 
Data storage cost varies by the region. Storage is AWS S3 list price with no additional charges.
Region | Price /TB /month ($)* |
|-----|------|
|US East (N. Virginia)    |$23.0 |
|US West (Oregon)         |$23.0 |
|Europe (Frankfurt)       |$24.5 |
|Europe (Ireland)         |$23.0 |
|Asia Pacific (Singapore) |$25.0 |

### 3. Additional Features
Firebolt offers:
Auto-Scaling: Dynamically adjust cluster resources based on workload requirements.
Workload Isolation: Run multiple clusters concurrently for optimized performance without affecting other workloads.
Serverless Capabilities: Pay only for executed queries with no idle time costs.

## Subscription Plans
Firebolt offers two main engagement models:
### Pay-As-You-Go:
Flexible, on-demand pricing with no upfront commitment.
Ideal for startups or teams with unpredictable workloads.
### Committed Use Discounts:
Receive discounted rates in exchange for a pre-committed usage volume.
Recommended for organizations with predictable workloads.
Contact support@firebolt.io to discuss custom enterprise plans or annual pricing commitments.

## Payment Options

# Set-up account billing through AWS Marketplace
To continue using Firebolt’s engines for query execution after your initial $200 credit, you’ll need to set-up a billing account by connecting your account to the AWS Marketplace. 

Steps for registration: 
1. On the Firebolt Workspace page, select the Configure(AggIndex) icon from the left navigation pane.
2. Under Organization settings, select Billing.
3. Click Connect to AWS Marketplace to take you to the Firebolt page on AWS Marketplace.
4. On the AWS Marketplace page, click the View Purchase Options in the top right hand corner of the screen.
5. Click Setup Your Account.
  
Your account should now be associated with AWS Marketplace.

## Estimation and Billing
Firebolt provides a usage dashboard to help you monitor resource consumption.
Invoices are generated monthly, with resource consumption and cost breakdowns.

## Support
For pricing or billing inquiries:
Contact: support@firebolt.io
