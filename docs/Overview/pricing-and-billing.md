---
layout: default
title: Pricing and billing
description: How Firebolt bills for usage
parent: Overview
nav_order: 2
---

# Firebolt pricing and deployment models
{: .no_toc}
Firebolt offers flexible deployment models that provide scalability and cost efficiency, to meet diverse business needs. Choose between fully managed or self-managed solutions tailored to your infrastructure and workload requirements. 

## Choose your deployment model
Firebolt offers two deployment models: [Fully managed](#fully-managed-editions-and-pricing) and [Self-managed](#self-managed-editions-and-pricing). Each model includes specific editions and pricing options. Fully managed has Standard, Enterprise, and Dedicated editions with Pay-As-You-Go or Committed-Use discount pricing. Self-managed includes Firebolt Core (free) and Private Cloud, with pricing based on your infrastructure setup.

This section outlines the available deployment models, their editions, and associated pricing options.

### Fully managed editions and pricing  
Firebolt’s fully managed service ensures high performance and reliability with Firebolt handling the infrastructure, scaling, maintenance, and performance optimizations. There are three editions available:

**Standard edition**       
The Standard edition is best for teams seeking a low-cost entry point without the need to manage compute infrastructure. You receive high performance with sub-second query latency, multi-dimensional compute elasticity, and security features such as Role-Based Access Control (RBAC), single sign-on (SSO), multi-factor authentication (MFA), and audit logging.

**Enterprise edition**              
The Enterprise edition is designed for organizations that need advanced security, compliance, and scalability. It includes all the features in the Standard edition, plus multi-cluster scaling, auto-scaling for concurrency, AWS PrivateLink and HIPAA compliance support.

**Dedicated edition**               
The Dedicated edition is ideal for enterprises with strict security and isolation needs (e.g., government clouds). It includes all the features in the Enterprise edition, plus complete data isolation on a single-tenant infrastructure, offering the highest level of security.

### Fully managed pricing:       
Firebolt offers two pricing options for the Standard and Enterprise editions:

* **Pay-as-you-go**: A pay-as-you-go plan is flexible, and provides on-demand pricing with no upfront cost or commitment. This plan is ideal for startups or teams with unpredictable workloads. Customers get billed monthly based on actual usage and only pay for what they use with per-second billing

* **Committed-use discounts**: A committed-use discount prepaid consumption model that provides discounted rates against a prepaid usage commitment. This plan is ideal for organizations with consistent, high-volume workloads and results in lower total costs compared to the pay-as-you-go plan. Once all prepaid FBU credits are consumed, your plan  switches to the pay-as-you-go pricing model. Customers can always continue using Firebolt, with consumption either drawing from prepaid credits or transitioning to the pay-as-you-go model when credits run out.

Contact [support@firebolt.io](mailto:support@firebolt.io) to discuss a committed-use plan, annual pricing commitments, dedicated edition pricing. 

### Compute and storage pricing
Firebolt pricing is based on compute usage and data storage. 

**Compute usage pricing**         
Compute costs are measured in Firebolt Units (FBUs) and vary based on [engine]({% link Overview/engine-fundamentals.md %}) node type, number of nodes (cluster size), the number of clusters and usage duration. Costs are only billed for the time Firebolt engines are running. Firebolt offers two compute family options:
* **Storage-optimized** (default): High SSD capacity for caching and production workloads.
* **Compute-optimized**: About 2x cheaper; ideal for development and test environments or workloads with smaller active datasets.

**Storage-optimized pricing for compute usage**

| Node Type       | Sizing in FBU | US Region Pricing |                 | Non-US Region Pricing |                   |
|----------------|--------------|-------------------|-------------------|---------------------|---------------------|
|               |              | **Standard ($0.23/FBU/hr)** | **Enterprise ($0.35/FBU/hr)** | **Standard ($0.28/FBU/hr)** | **Enterprise ($0.42/FBU/hr)** |
| **Small (S)**  | 8            | $1.84            | $2.80            | $2.24              | $3.36              |
| **Medium (M)** | 16           | $3.68            | $5.60            | $4.48              | $6.72              |
| **Large (L)**  | 32           | $7.36            | $11.20           | $8.96              | $13.44             |
| **Extra Large (XL)** | 64      | $14.72           | $22.40           | $17.92             | $26.88            |                   

**Compute-optimized pricing for compute usage**

| Node Type       | Sizing in FBU | US Region Pricing |                 | Non-US Region Pricing|                    |
|----------------|--------------|-------------------|-------------------|---------------------|---------------------|
|               |              | **Standard ($0.23/FBU/hr)** | **Enterprise ($0.35/FBU/hr)** | **Standard ($0.28/FBU/hr)** | **Enterprise ($0.42/FBU/hr)** |
| **Small (S)**  | 4            | $0.92            | $1.40            | $1.12              | $1.68              |
| **Medium (M)** | 8            | $1.84            | $2.80            | $2.24              | $3.36              |
| **Large (L)**  | 16           | $3.68            | $5.60            | $4.48              | $6.72              |
| **Extra Large (XL)** | 32      | $7.36            | $11.20           | $8.96              | $13.44            |                                          

**Data storage pricing**:     
Data storage costs are based on the compressed data stored, including indexes and raw data. Pricing is based on Amazon S3 costs in your selected AWS region. There are no additional storage charges beyond S3 costs.

  | Available AWS Regions           | Price per TB/month ($USD)     |
  |---------------------------------|-------------------------------|
  | US East (N. Virginia)           | $23.00                        |
  | US West (Oregon)                | $23.00                        |
  | Europe (Frankfurt)              | $24.50                        |
  | Europe (Ireland)                | $23.00                        |
  | Asia Pacific (Singapore)        | $25.00                        |

### Self-managed editions and pricing
Firebolt offers two self-managed options, where you run Firebolt on your own infrastructure. 
   
**Firebolt Core**             
Firebolt Core is a free downloadable version that can be deployed on cloud, on-prem, or a local machine. This option is best for teams needing full control over deployment with a lightweight Firebolt engine. Customers manage infrastructure (compute and storage), hosting, all software upgrades, and maintenance.

**Private Cloud (BYOC)**                 
The Private Cloud is a BYOC (Bring your own cloud) offering for organizations that want Firebolt’s software but prefer to use their own cloud infrastructure. Customers manage their own infrastructure for both compute and storage, whereas Firebolt manages hosting, Firebolt upgrades and maintenance. For BYOC pricing, contact [support@firebolt.io](mailto:support@firebolt.io)

## Support plans and service level agreements
Firebolt offers support options based on your selected edition. 

Response Time Commitments (TFR = Time to First Response)

| Severity Level    | Issue Type                                    | Standard Edition TFR         | Enterprise Edition TFR     |
|------------------|----------------------------------------------|------------------------------|----------------------------|
| Critical (Sev1) | Service outage or major disruption          | Response within 4 hours      | Response within 30 minutes |
| High (Sev2)   | Significant performance degradation         | Response within 8 business hours | Response within 2 hours   |
| Medium (Sev3) | Minor impact or feature issue               | Response within 24 business hours | Response within 6 business hours |
| Low (Sev4)    | General inquiries or documentation questions | Response within 48 business hours | Response within 24 business hours |


**Premium support features**            
Premium customers receive additional support benefits beyond response time commitments:
* **Proactive monitoring**: Alerts for issues and potential optimizations available to Premium customers
* **Enhanced support channels**: All customers can access support via email and the in-app form. Premium customers also have access to Slack, with in-app chat under consideration for the future. 
* **Dedicated support engineer**: Premium customers are assigned a designated support engineer who has a deep understanding of their use and care for personalized support. Standard customers receive assistance from the general support pool. 
* **Critical event management (Upcoming feature)**: Premium customers will have the option to pay for dedicated support engineers during specific timeframes, such as major product launches or key business events. 

Contact [support@firebolt.io](mailto:support@firebolt.io) to learn more about Premium Support offerings. 


## Billing setup and monitoring

You can use Firebolt's billing dashboard to monitor resource consumption, track expenses, monitor payments, and analyze billing trends efficiently.
Billing invoices are generated on a monthly basis, and provide a detailed breakdown of resource consumption and associated costs.

**Pay-As-You-Go setup via AWS Marketplace:**
1. Login to [Firebolt's Workspace](https://go.firebolt.io/login). If you haven’t yet registered with Firebolt, see the [Get Started]({% link Guides/getting-started/index.md %}) guide.
2. In the Firebolt Workspace, select the Configure(<img src="../assets/images/configure-icon.png" width="20" alt="The Firebolt Configure Space icon">) icon from the left navigation pane.
3. Under **Configure**, select **Billing**. This page allows you to view invoices and consumption details.
4. Select **Connect to AWS Marketplace**.
5. On AWS Marketplace, click **View Purchase Options** > **Setup Your Account**.

Firebolt will bill you monthly through **AWS Marketplace** based on usage. 
