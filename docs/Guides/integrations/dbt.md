---
layout: default
title: dbt
description: Learn how to connect dbt to Firebolt.
nav_order: 4
parent: Integrate with Firebolt
grand_parent: Guides
---

# Connect with dbt

[dbt](https://www.getdbt.com) (data build tool) is a modern development framework that enables data analysts and data engineers to transform data by writing SELECT statements. dbt handles turning these SELECT statements into tables and views.

The Firebolt adapter for dbt brings together dbt's state-of-the-art development tools and Firebolt's next-generation analytics performance. On top of dbt's core features, the adapter offers native support for all of Firebolt's index types and has been specifically enhanced to support ingestion from S3 using Firebolt's external tables mechanics.

## Get started

We recommend you follow the guidelines for dbt integration in our [Github repository](https://github.com/firebolt-db/dbt-firebolt).

## Authentication

To authenticate, use a service account ID and secret.
A service account is identified by a `client_id` and a `client_secret`.
Learn how to generate an ID and secret [here](../managing-your-organization/service-accounts.md).
