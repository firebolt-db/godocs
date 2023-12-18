---
layout: default
title: Apache Superset
description: Learn about connecting Apache Superset to Firebolt.
nav_order: 5
parent: Integrate with Firebolt
grand_parent: Guides
---

# Connecting to Apache Superset

[Apache Superset](https://superset.apache.org) is a business intelligence web application that makes it easy for users of all skill sets to explore and visualize their data, from simple pie charts to highly detailed deck.gl geospatial charts.&#x20;

## To get started

### Install the driver

If you self-host Superset, you must install the Firebolt driver.

To install the driver, see [Adding New Database Drivers in Docker](https://superset.apache.org/docs/databases/docker-add-drivers) in Superset documentation. Use `firebolt-sqlalchemy` as the driver name in `requirements-local.txt`.

### Set up the connection

In the Superset UI, go to **Data** > **Databases** > **Add Database**.&#x20;

The connection expects a SQLAlchemy connection string of the form:

```
firebolt://{client_id}:{client_secret}@{database}/{engine_name}
```

To authenticate, use a service account ID and secret.
A service account is identified by a `client_id` and a `client_secret`.
Learn how to generate an ID and secret [here](../managing-your-organization/service-accounts.md).

This is currently available in the latest `master` branch in Superset and will also be included in the Superset v1.4 stable release when it is available.
