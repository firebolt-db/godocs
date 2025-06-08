---
layout: default
title: Connect With JDBC
nav_order: 2
parent: Connect
---

# JDBC

The [official Firebolt JDBC driver](https://github.com/firebolt-db/jdbc) supports Firebolt Core from version 3.6.3 and can be downloaded from the [GitHub JDBC release page](https://github.com/firebolt-db/jdbc/releases). A detailed description can be found on the [JDBC documentation page](../Guides/developing-with-firebolt/connecting-with-jdbc.md) and the corresponding [API reference](https://jdbc.docs.firebolt.io/javadoc/). The remainder of this page provides some explanations and examples specific to Firebolt Core.

## Connection String

In order to connect to a Firebolt Core cluster with JDBC, you need to specify the address of the HTTP endpoint in the `url` connection parameter. For example, if you followed the [Get Started](./firebolt-core-get-started.md) guide to start a single-node Firebolt Core cluster on your local machine, its HTTP endpoint is exposed at `localhost:3473` and you can use the following connection string to connect to the default database.

```
jdbc:firebolt:?url=http://localhost:3473
```

More generally, the form of the connection string should be as follows.

```
jdbc:firebolt:<database>?url=<http_endpoint_url>&<other_connection_params>
```

Recall that Firebolt Core [does not support authentication](./firebolt-core-connect.md#security), so the respective instructions outlined in the dedicated [JDBC documentation page](../Guides/developing-with-firebolt/connecting-with-jdbc.md#authentication) do not apply.

## Examples

The Firebolt Core GitHub repository contains a sample [Java application](https://github.com/firebolt-db/firebolt-core/tree/main/examples/jdbc) which demonstrates how to use the Firebolt JDBC driver to send queries to Firebolt Core.
