---
layout: default
title: Pricing and billing
description: How Firebolt bills for usage
parent: Overview
nav_order: 2
---

# Firebolt pricing and deployment models

Firebolt offers flexible deployment models to meet diverse business needs, providing scalability and cost efficiency. When you start using Firebolt, you receive $200 in free credits to use in the first 30 days. Afterwards, you can sign up for one of Firebolt's fully managed or self-managed solutions tailored to your infrastructure and workload requirements. 

## Choose your deployment model
Firebolt offers two deployment models: [Fully managed](#fully-managed-editions-firebolt-managed-infrastructure) and [Self-managed](#self-managed-editions-customer-managed-infrastructure). Each model includes specific editions and pricing options. Fully Managed has Standard, Enterprise, and Dedicated editions with Pay-As-You-Go or Committed-Use Discount pricing. Self-Managed includes Firebolt Core (free) and Private Cloud editions, with pricing based on your infrastructure setup.

This section outlines the available deployment models, their editions, and associated pricing options.

### Fully managed editions (Firebolt-managed infrastructure)    
Firebolt’s fully managed service ensures performance and reliability with auto-scaling and workload isolation.

* **Standard edition**: Best for teams seeking high performance and scalability without managing infrastructure.
  * Features include: 
    * Fully-managed cloud data warehouse
    * High-performance query execution
    * Role-Based Access Control
    * Network policies
    * Single sign-on (SSO)
    * Multi-factor authentication (MFA)
    * Audit logging
    * SOC2 compliance attestation
    * AWS S3-backed storage

* **Enterprise edition**: Designed for organizations needing advanced security, compliance, and scalability.
  * Features include:
    * All features included in the **Standard** edition
    * Auto-scaling for concurrency
    * AWS PrivateLink
    * HIPAA compliance support
    * Multi-cluster scaling

* **Dedicated edition**: Single-tenant environment offering the highest level of security and isolation.
  * Features include:
    * All features included in the **Standard** and **Enterprise editions**
    * Complete data isolation on single-tenant infrastructure

**Pricing:**       
Firebolt offers flexible pricing options to accommodate different workloads and business needs including the following:  

* **Pay-as-you-go**: Flexible, no commitment billed monthly based on actual usage. 
  * No upfront cost&mdash; billed monthly based on actual usage. 
  * Per-second billing&mdash; only pay for what you use. 
  * Set-up billing through AWS Marketplace: 
    1. Login to [Firebolt's Workspace](https://go.firebolt.io/login). If you haven’t yet registered with Firebolt, see the [Get Started]({% link Guides/getting-started/index.md %}) guide.
    2. In the Firebolt Workspace, select the Configure(<img src="../assets/images/configure-icon.png" width="20" alt="The Firebolt Configure Space icon">) icon from the left navigation pane.
    3. Under **Configure**, select **Billing**.
    4. Select **Connect to AWS Marketplace** to navigate to the Firebolt page on AWS Marketplace.
    5. Select **View Purchase Options** in the top-right corner of the screen.
    6. Select **Setup Your Account**.

* **Committed-use discounts**: Lower-rate plan for organizations with consistent, high-volume workloads through prepaid usage commitments. 
  * Prepaid usage commitment for discounted rates.
  * Lower total cost compared to Pay-as-You-Go.
  * Compute costs are measured in Firebolt Units (FBUs) and vary on node type, cluster size, and usage duration. Billing occurs only when Firebolt engines are running. Firebolt offers two compute skews:
    * **Compute optimized**&mdash; About 2x cheaper, ideal for development and test environments or workloads with smaller active datasets.
      * |                      | Regional Pricing within the US |                          | Regional Pricing outside the US |                          |
    |----------------------|-------------------------------|--------------------------|---------------------------------|--------------------------|
    |                      | **Standard**                  | **Enterprise**           | **Standard**                    | **Enterprise**           |
    | **$/FBU/hr**         | 0.23                          | 0.35                     | 0.28                            | 0.42                     |
    | **FBU's**            | 4                             | 4                        | 4                               | 4                        |
    | **Small**            | 0.92                         | 1.4                      | 1.12                             | 1.68                     |
    | **Medium**           | 1.84                          | 2.8                      | 2.24                             | 3.36                     |
    | **Large**            | 3.68                          | 5.6                     | 4.48                            | 6.72                    |
    | **X-Large**          | 7.36                         | 11.2                     | 8.96                            | 13.44                    |

    * **Storage optimized**&mdash; Default option; High SSD capacity for caching and production workloads.
      * |                      | Regional Pricing within the US |                          | Regional Pricing outside the US |                          |
    |----------------------|-------------------------------|--------------------------|---------------------------------|--------------------------|
    |                      | **Standard**                  | **Enterprise**           | **Standard**                    | **Enterprise**           |
    | **$/FBU/hr**         | 0.23                          | 0.35                     | 0.28                            | 0.42                     |
    | **FBU's**            | 8                             | 8                        | 8                               | 8                        |
    | **Small**            | 1.84                          | 2.8                      | 2.24                            | 3.36                     |
    | **Medium**           | 3.68                          | 5.6                      | 4.48                            | 6.72                     |
    | **Large**            | 7.36                          | 11.2                     | 8.96                            | 13.44                    |
    | **X-Large**          | 14.72                         | 22.4                     | 17.92                           | 26.88                    |
    
        Note that there are no additional storage charges beyond S3 costs. Contact [support@firebolt.io](mailto:support@firebolt.io) to discuss enterprise pricing and annual contracts.

Available AWS regions pricing:

| **Available AWS Regions**       | **Price per TB/month ($USD)** |
|---------------------------------|-------------------------------|
| US East (N. Virginia)           | $23.00                        |
| US West (Oregon)                | $23.00                        |
| Europe (Frankfurt)              | $24.50                        |
| Europe (Ireland)                | $23.00                        |
| Asia Pacific (Singapore)        | $25.00                        |

### Self-managed editions (Customer-managed infrastructure)

Firebolt offers two self-managed editions: Firebolt Core and Private Cloud. 

* Editions:     
  * **Firebolt Core** A free, downloadable version offering complete control over deployment on any infrastructure. Runs on cloud, on-prem, or local machine. 
    * You manage: Hosting, upgrades, and maintenance

  * **Private Cloud (BYOC)** For organizations wanting Firebolt software on their own cloud infrastructure. 
    * You manage: infrastructure, compute, and storage costs
    * We provide: software and updates
    * For BYOC pricing, contact [support@firebolt.io](mailto:support@firebolt.io)

* Platforms supported:
  * Google Cloud Platform (GCP)
  * Amazon Web Services (AWS)
* Compute & storage:
  * Both editions use the storage optimized compute exclusively

## Billing dashboard

You can use Firebolt's billing dashboard to monitor resource consumption, track expenses, monitor payments, and analyze billing trends efficiently.

Billing invoices are generated on a monthly basis, and provide a detailed breakdown of resource consumption and associated costs.

To access the dashboard:
1. Login to [Firebolt's Workspace](https://go.firebolt.io/login). If you haven’t yet registered with Firebolt, see the [Get Started]({% link Guides/getting-started/index.md %}) guide.
2. In the Firebolt Workspace, select the Configure(<img src="../assets/images/configure-icon.png" width="20" alt="The Firebolt Configure Space icon">) icon from the left navigation pane.
2. Under **Configure**, select **Billing**.

## Support
For pricing or billing inquiries, contact Firebolt's support team at [support@firebolt.io](mailto:support@firebolt.io).
