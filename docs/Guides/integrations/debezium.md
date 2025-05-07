---
layout: default
title: Kafka CDC with Debezium
description: CDC events with Kafka and Debezium
nav_order: 12
nav_exclude: true
search_exclude: true
sitemap: false
parent: Integrate with Firebolt
---

# Integrate with Debezium
{: .no_toc}

<img src="../../assets/images/debeziumicon.png" alt="Debezium logo" width="450"/>

Debezium is a distributed platform that captures changes from your databases so that your analytics are always consistent between systems. Debezium uses CDC (Change Data Capture) events to record all row-level changes within each database table in a change event. Applications read these events to see the changes in the same order in which they occurred. Firebolt integrates with Debezium via its JDBC driver, allowing you to ingest CDC events directly into Firebolt for further analysis.

Debezium uses Apache Kafka as the backbone for handling and delivering CDC events. Kafka Connect allows for data transfer between Kafka and other systems. Kafka topics organize and store captured events. In Firebolt's integration with Debezium, any database supported by Debezium can act as a source for capturing database changes, while Firebolt serves as the sink for storing and analyzing these changes via Debezium's JDBC sink connector. If a native Debezium source connector is unavailable for a specific database, as long as the messages conform to Debezium’s message format, they can still be consumed by the sink connector and loaded into Firebolt.

Topics:
* [Prerequisites](#prerequisites) &ndash; Set up your environment to use Debezium.
* [Quickstart](#quickstart) &ndash; Learn how to quickly set up a CDC pipeline with Kafka and Kafka Connect.
* [Firebolt connector configuration](#firebolt-connector-configuration) &ndash; Configure the Firebolt JDBC driver and define the necessary connection properties.
* [Using Docker Compose](#using-the-docker-compose) &ndash; Deploy the setup using Docker Compose.
* [Manual installation](#manual-installation) &ndash; Set up Kafka and Kafka Connect manually.
* [Sample Event](#sample-event) &ndash; Learn how to send a sample JSON message through Kafka’s console producer and write the event to a Firebolt database.
* [Configuration](#configuration) &ndash; Configure Firebolt sink for your specific use case.
* [Limitations](#limitations) &ndash; Firebolt does not support some operations in data loading.
* [Additional resources](#additional-resources) &ndash; Learn more about Debezium source connectors, custom configurations for Kafka Connect, and Debezium sink connectors.

## Prerequisites
You must have the following prerequisites before connecting Firebolt to Debezium:
* **Firebolt account** &ndash; You need an active Firebolt account. If you do not have one, you can [sign up](https://go.firebolt.io/signup) for one. 
* **Firebolt service account** &ndash; You must have access to an active Firebolt service account, which facilitates programmatic access to Firebolt, its ID and secret. 
* **Firebolt User**: You need a separate user [associated](../managing-your-organization/service-accounts.md#create-a-user) with your service account. The user should have [USAGE](../../Overview/Security/Role-Based%20Access%20Control/database-permissions/) permission to query your database, and [OPERATE](../../Overview/Security/Role-Based%20Access%20Control/engine-permissions.html) permission to start and stop an engine if it is not already started. It should also have at least USAGE, SELECT and INSERT [permissions](../../Overview/Security/Role-Based%20Access%20Control/database-permissions/schema-permissions.html) on the schema you are planning to query.


# Quickstart

There are two ways to deploy this setup: using Docker Compose or starting each service manually on the local machine. Docker Compose simplifies deployment by managing all required services in containers, while manual deployment provides more flexibility for configuring individual components.

## Firebolt connector configuration

Before using Kafka Connect to register the Firebolt connector, you need to configure it properly. This step involves setting up Debezium’s Kafka Connect so it can communicate with Firebolt. Specifically, you must configure the Firebolt JDBC driver and define the necessary connection properties. These settings establish the connection and will be used later when Kafka Connect is set up.

1. Create a `sink-connector.json` file in a directory of your choice.
2. Copy and paste the following JSON into this file, replacing the placeholders as described below

    ```json
    {
    "name": "firebolt-sink-connector",
    "config": {
        "connector.class": "io.debezium.connector.jdbc.JdbcSinkConnector",
        "topics": "cdc.public.demo",
        "connection.url": "jdbc:firebolt:database?account=<account_name>&engine=<engine_name>&merge_prepared_statement_batches=true",
        "connection.username": "<client_id>",
        "connection.password": "<client_secret>",
        "hibernate.dialect": "org.hibernate.dialect.PostgreSQLDialect",
        "primary.key.mode": "none",
        "primary.key.fields": "",
        "insert.mode": "insert",  
        "schema.evolution": "basic",
        "delete.enabled": "false",
        "quote.identifiers": true
      }
    }
    ```
    
    Use the following configuration parameters for your sink connector:

    | Parameter               | Description                                                                                                       |
    |-------------------------|-------------------------------------------------------------------------------------------------------------------|
    | `name`                 | A name for this connector.                                                                                         |
    | `connector.class`      | Set the connector class to Debezium's sink connector `io.debezium.connector.jdbc.JdbcSinkConnector`.                                                                                                            |
    | `topics`               | The list of Kafka topics that this connector will be listening to, separated by commas. If Debezium source connector is used to create events then the topics would have a specific [naming scheme](https://debezium.io/documentation/reference/stable/connectors/postgresql.html#postgresql-topic-names). For this example you can use `cdc.public.demo` (see `topic.prefix` and `topic.include.list` fields in [Create a Postgres connector configuration](#create-a-postgres-connector-configuration) for reference)                                             |
    | `connection.url`       | The Firebolt JDBC [connection string]({% link Guides/developing-with-firebolt/connecting-with-jdbc.md %}#connecting-to-firebolt-with-the-jdbc-driver). `merge_prepared_statement_batches` here is important to improve the insert performance, see the [note below](#merge-prepared-statement-batches) for more information. |
    | `connection.username`  | The client ID of your Firebolt [service account]({% link Guides/managing-your-organization/service-accounts.md %}).                   |
    | `connection.password`  | THe secret of your Firebolt [service account]({% link Guides/managing-your-organization/service-accounts.md %}).                      |
    | `hibernate.dialect`    | Specifies the SQL dialect for the target database. Set to `org.hibernate.dialect.PostgreSQLDialect`.                                       |
    | `insert.mode`          | A Kafka Connect property that defines how data is written to a target system. You can use either `insert` for new rows, or `update` to modify existing rows in your Firebolt database. `upsert` allows combining both insert and update operations.        |
    | `primary.key.mode`     | Specifies how the connector resolves [primary key](https://debezium.io/documentation/reference/stable/connectors/jdbc.html#jdbc-property-primary-key-mode), which is required for `"insert.mode": "update"` or when `"delete.enabled"` is set to `true`. Otherwise set to `"none"`
    | `primary.key.fields`   | Specify which fields to use as primary key columns, separated by commas. This parameter is only used when `insert.mode` is set to update. |
    | `schema.evolution`     | Controls how the connector handles schema changes. Use `basic` for basic schema evolution (adding columns if a new one is encountered or if the name is changed) or `none` to disable schema evolution entirely. For more information see [Schema evolution](https://debezium.io/documentation/reference/stable/connectors/jdbc.html#jdbc-schema-evolution) in Debezium's documentation. |
    | `delete.enabled`       | A boolean value that determines whether delete operations from the source database should be propagated to Firebolt. Set to `true` to enable deletion of rows in Firebolt when they are deleted in the source database. Requires `primary.key.mode` set to other than `none`. |
    | `quote.identifiers`   | A boolean value that determines whether to quote database identifiers (e.g., table and column names). Set to `true` to ensure compatibility with case-sensitive or reserved keywords in Firebolt. |

    For more information, see [Apache Kafka's sink connector configs](https://kafka.apache.org/documentation.html#sinkconnectconfigs) and [Debezium's connector for JDBC](https://debezium.io/documentation/reference/stable/connectors/jdbc.html)

    <a id="merge-prepared-statement-batches"></a>
    `merge_prepared_statement_batches` JDBC connection flag is designed to improve performance when multiple rows are updated in the source database either at the same time or in quick succession. It optimizes the INSERT queries by allowing the JDBC driver to combine multiple rows into a single statement that's executed in one request to Firebolt, eliminating additional network round trips to the server. 

## Using the Docker Compose

This tutorial showcases how to quickly create a CDC pipeline with Kafka, Postgres database and Kafka connect cluster running in their own containers. In order to follow it you need to have docker [installed](https://docs.docker.com/get-started/get-docker/). Modern docker versions come with `docker compose` by default.

We'll be using debezium's [docker images](https://hub.docker.com/u/debezium) in order to simplify the installation. You can use your own images or non-debezium images, but there might be some additional setup required. Refer to the docker hub [READMEs](https://hub.docker.com/u/debezium) for more information.

### Download and set up the JDBC driver

1. Download the latest Firebolt's JDBC driver (.jar) from [Firebolt's JDBC repository](https://github.com/firebolt-db/jdbc/releases).
2. Place it in a directory that will be [mounted](https://docs.docker.com/engine/storage/bind-mounts/) in docker and note its path.


### Create a docker compose file and start the services

1. Create a `docker-compose.yml` file with the following contents:

    ```yaml
    services:
      zookeeper:
        image: quay.io/debezium/zookeeper:3.0
        environment:
          ZOOKEEPER_CLIENT_PORT: 2181
          ZOOKEEPER_TICK_TIME: 2000
        ports:
          - "2181:2181"
          - "2888:2888"
          - "3888:3888"
        networks:
          - kafka-net


      kafka:
        image: quay.io/debezium/kafka:3.0
        depends_on:
          - zookeeper
        environment:
          ZOOKEEPER_CONNECT: zookeeper:2181
        ports:
          - "9092:9092"
          - "29092:29092"
        networks:
          - kafka-net

      postgres:
        image: quay.io/debezium/postgres:16
        environment:
          POSTGRES_USER: <pg_user>
          POSTGRES_PASSWORD: <pg_password>
          POSTGRES_DB: postgres
        ports:
          - "5432:5432"
        networks:
          - kafka-net

      connect:
        image: quay.io/debezium/connect:3.0
        depends_on:
          - kafka
          - postgres
        environment:
          BOOTSTRAP_SERVERS: kafka:9092
          GROUP_ID: 1
          CONFIG_STORAGE_TOPIC: my_connect_configs
          OFFSET_STORAGE_TOPIC: my_connect_offsets
          KEY_CONVERTER_SCHEMAS_ENABLE: "true"
          VALUE_CONVERTER_SCHEMAS_ENABLE: "true"
          KEY_CONVERTER: org.apache.kafka.connect.json.JsonConverter
          VALUE_CONVERTER: org.apache.kafka.connect.json.JsonConverter
          CONNECT_CONSUMER_MAX_POLL_RECORDS: 2000 # increase to improve throughput
        volumes:
          - /path/to/your/jdbc/directory/firebolt-jdbc-<version>.jar:/kafka/libs/firebolt-jdbc-<version>.jar
        ports:
          - "8083:8083"
        networks:
          - kafka-net

    networks:
      kafka-net:
        driver: bridge
      
    ```
2. Replace palceholders `/path/to/your/jdbc/directory/` with the directory where you have placed the JDBC driver and `firebolt-jdbc-<version>.jar` with the name of the driver in that directory.
3. Replace placeholders `<pg_user>` and `<pg_password>` with the credentials of your choice. Note them down for later.
4. Run `docker compose up` in the directory containing `docker-compose.yml` file.


### Create a Postgres connector configuration

1. Create a postgres connector settings `source-connector.json` file in a directory of your choice.
2. Copy and paste the following JSON into this file, replacing the placeholders as described below

    ```json
    {
      "name": "postgres-source-connector",
      "config": {
        "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
        "database.hostname": "postgres",
        "database.port": "5432",
        "database.user": "<pg_user>",
        "database.password": "<pg_password>",
        "database.dbname" : "postgres",
        "topic.prefix": "cdc",
        "table.include.list": "public.demo"
      }
    }
    ```

    | Parameter               | Description                                                                                                       |
    |-------------------------|-------------------------------------------------------------------------------------------------------------------|
    | `name`                 | A name for this connector.                                                                                         |
    | `connector.class`                 | Connector to use, for Posgres should be `io.debezium.connector.postgresql.PostgresConnector`                                                                                         |
    | `database.hostname`                 | Host name where your database is set up. For this demo `postgres` specifies that we're using a postgres docker compose service for connection.                                                                                         |
    | `database.port`                 | Port to access the database. Standard Postgres port is `5432`.                                                                                         |
    | `database.user`                 | Postgres username specified earlier in `docker-compose.yml`                                                                                          |
    | `database.password`                 | Postgres password specified earlier in `docker-compose.yml`                                                                                         |
    | `database.dbname`                 | Database name specified earlier. For this example we can use `postgres`.                                                                                         |
    | `topic.prefix`                 | A unique topic prefix for topics created. Should be unique across connectors.                                                                                          |
    | `table.include.list`                 | A list of Postgres tables to monitor for changes.                                                                                         |


### Use the Conect API to add source and sink connectors

1. Make a POST request to set up a source connector with the config file `source-connector.json` set up earlier:

    ```shell
    curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d @source-connector.json
    ```

2. Make a POST request to set up a sink connector with the config file `sink-connector.json` set up earlier:

    ```shell
    curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d @sink-connector.json
    ```

3. Verify the status of the connectors:

    ```shell
    curl -X GET http://localhost:8083/connectors/postgres-source-connector/status
    curl -X GET http://localhost:8083/connectors/firebolt-sink-connector/status
    ```

To get more information if something went wrong fetch Kafka Conenct logs via `docker logs kafka-connect-1`.

### Write data and see it propagated

If everything succeeded you're now ready to send CDC data throught the Kafka pipeline.
1. Connect to Postgres or use the connection established before `docker compose exec postgres psql -U <pg_user> -d postgres`. Use `pg_user` and `pg_password` specified earlier in `docker-compose.yml`
2. Create a demo table:

    ```sql
    CREATE TABLE demo (id INT, data VARCHAR(255));
    ```
3. Write data to the table that's being monitored:

    ```sql
    INSERT INTO demo VALUES (1, 'my data');
    ```
4. You should shortly see a table created in Firebolt with the name `<topic_name>_<postgres_schema>_<posgres_table_name>` (for our demo it will be `cdc_public_demo`) and the above data written.

## Manual installation 

### Connect to Apache Kafka
To connect to Apache Kafka, you must download and start a Kafka service, create a Kafka topic, and configure and start Kafka Connect. 
This guide walks you through setting up Kafka locally. If you're setting it up in production or in a distributed mode refer to the Kafka [documentation](https://kafka.apache.org/documentation).

1. **[Download](https://www.apache.org/dyn/closer.cgi?path=/kafka/3.9.0/kafka_2.13-3.9.0.tgz) the latest Kafka release and extract it:**

    ```shell
    $ tar -xzf kafka_2.13-3.9.0.tgz
    $ cd kafka_2.13-3.9.0
    ```
2. **Start Kafka**    
    a. Start ZooKeeper, a centralized service that coordinates distributed systems and manages Kafka's metadata, before starting Kafka to ensure proper coordination and cluster integrity, as follows:
 
      ```shell
      $ bin/zookeeper-server-start.sh config/zookeeper.properties
      ```

    b. Next, start a Kafka broker service using the configuration settings in config/server.properties as follows:

      ```shell
      $ bin/kafka-server-start.sh config/server.properties
      ```
  The configuration in config/server.properties contains default settings that come with the Kafka installation package. 
  Once all services have successfully launched, you will have a basic Kafka environment running and ready to use. 

3. **Create a Kafka Topic**    
Kafka topics store captured events. The following code example creates a topic named firebolt-cdc-events:

   ```shell
   $ bin/kafka-topics.sh --create --topic firebolt-cdc-events --bootstrap-server localhost:9092
   ```

   In the previous example, `firebolt-cdc-events` is the desired topic name and `localhost:9092` is the URL for the default Kafka server. If you're running on a different URL or port, replace `localhost:9092`.

   (Optional) Use the `--describe` option to verify that the Kafka topic has been created as follows:

   ```shell
   $ bin/kafka-topics.sh --describe --topic firebolt-cdc-events --bootstrap-server localhost:9092
   ```

4. **Configure and start Kafka Connect**      
Kafka Connect is a framework that helps integrate Kafka with systems that are external to Kafka. To use Kafka Connect with Firebolt, you need to modify the Kafka connect properties, install the Debezium and Firebolt JDBC drivers, and create a sink connector for a Debezium sink connector.    
   1.  **Modify connector properties**      
    Kafka Connect operates with both standalone mode as a single process, and distributed mode. The following code shows how to set up Kafka Connect for standalone mode. For information about distributed mode, see [Apache’s documentation for Kafka Connect](https://kafka.apache.org/documentation.html#connect_running). 
    Set the following properties in `config/connect-standalone.properties` file to use JSON converters and specify the plugin path:

        ```shell
        key.converter=org.apache.kafka.connect.json.JsonConverter
        value.converter=org.apache.kafka.connect.json.JsonConverter
        key.converter.schemas.enable=true
        value.converter.schemas.enable=true
        plugin.path=/usr/local/share/kafka/plugins 
        ```
        If your event messages use a different format than JSON, refer to the [Connect configuration API](https://kafka.apache.org/documentation.html#connectconfigs). 

        In the previous code example, ensure that `plugin.path` points to the [location](https://kafka.apache.org/documentation/#connectconfigs_plugin.path) that will contain the Debezium plugin, which we'll download in the next step. 

   2. **Install the Debezium and Firebolt JDBC drivers**   
    Extract the following files into your Kafka Connect environment: 
      1. Download the Debezium [JDBC connector](https://www.apache.org/dyn/closer.cgi?path=/kafka/3.9.0/kafka_2.13-3.9.0.tgz)
      1. Copy the driver to the directory you've specified in `plugin.path` in the previous step.
      1. Download the latest Firebolt's JDBC driver (.jar) from [Firebolt's JDBC repository](https://github.com/firebolt-db/jdbc/releases).
      1. Copy the JDBC driver into `libs` folder within your kafka installation.

   3. **Configure a sink connector**    
    Use the sink-connector-config.json configuration file for the sink connector [created earlier](#firebolt-connector-configuration). Copy it into `config` directory of your Kafka installtion or note its path for the next step.

   4. **Start Kafka Connect**
    Start Kafka Connect in standalone mode by running the following command from your kafka installation folder:
    
    ```shell
    $ bin/connect-standalone.sh config/connect-standalone.properties config/sink-connector-config.json
    ```
    * The `connect-standalone.properties` file contains Kafka Connect properties including `plugin.path`.
    * The `sink-connector-config.json` file contains the Debezium sink configuration from the previous step. 
  
### Sample Event
This section shows you how to send custom events through a Kafka console producer, which is a command-line tool that allows users to manually send messages to a Kafka topic. If you want to set up a connector for capturing database events, use Debezium's [source connector](https://debezium.io/documentation/reference/stable/connectors/index.html), which continuously monitors a database for changes. If you have a database that's not supported by Debezium, you can use any method that conforms to the following structure, and Firebolt's sink connector will be able to consume it. For more information about the expected Kafka message structure, see Debezium's [Data change events documentation](https://debezium.io/documentation/reference/stable/connectors/postgresql.html#postgresql-events). 

The following code example starts a Kafka console producer that sends messages to the firebolt-cdc-events topic on a Kafka broker running at localhost:9092:

  ```shell
  $ bin/kafka-console-producer.sh --topic firebolt-cdc-events --bootstrap-server localhost:9092
  ```

After running this command, the console producer will display a prompt where you can paste a payload or message. Paste the following example of a Kafka message that defines a single integer field "id" with a value 1.
  
```json
    {
      "schema": {
        "type": "struct",
        "name": "connector-name.database-name.table-name.Key",
        "optional": false,
        "fields": [
              {
                  "name": "id",
                  "index": "0",
                  "schema": {
                      "type": "INT32",
                      "optional": "false"
                  }
              }
          ]
      },
      "payload": {
          "id": "1"
      },
    }
```

You must paste the message without newlines as a single line as follows:

```json
{"schema":{"type":"struct","name":"connector-name.database-name.table-name.Key","optional":false,"fields":[{"name":"id","index":"0","schema":{"type":"INT32","optional":"false"}}]},"payload":{"id":"1"}}
```

Sending this message to Kafka routes it to the Debezium sink connector, which creates a table called `firebolt_cdc_events` from the topic name after replacing dashes with underscores. Kafka creates a table with a single column `id` of type `INT`. You can customize table names in your Debezium [configuration](https://debezium.io/documentation/reference/stable/connectors/jdbc.html#jdbc-property-collection-name-format). Debezium writes the row from the message into this newly created table, and all subsequent messages to this topic must conform to the same schema to be written to the same table.

## Configuration

### Change Data Capture (CDC)

Debezium is highly effective at capturing and processing CDC (Change Data Capture) events from source databases. When configuring the Firebolt sink connector, you can tailor the setup to handle specific CDC operation types based on your use case.

#### Append-Only Ingestion

This configuration is ideal for scenarios where you only need to append new records to your Firebolt table. No updates or deletions from the source database will be processed.

**Configuration:**
Add or modify the following keys in the [sink configuration](#firebolt-connector-configuration):

```json
"insert.mode": "insert",
"primary.key.mode": "none",
"schema.evolution": "basic"
```

**How it works:**
- Processes only `INSERT` operations from the source database.
- Ignores `UPDATE` and `DELETE` operations.
- Automatically adapts to new columns in the source schema (basic schema evolution).
- Does not require a primary key.

**Use cases:**
- Historical logging or audit trails.
- Time-series data ingestion.
- Event streams where updates and deletions are not needed.

#### Append-Only Ingestion with Deletes

This configuration appends new records to Firebolt tables and also propagates deletions from the source database.

**Configuration:**
Add or modify the following keys in the [sink configuration](#firebolt-connector-configuration):

```json
"insert.mode": "insert",
"primary.key.mode": "record_key",
"primary.key.fields": "<pk_col>",
"schema.evolution": "basic",
"delete.enabled": "true"
```

**How it works:**
- Processes `INSERT` and `DELETE` operations.
- Ignores `UPDATE` operations.
- Automatically adapts to new columns in the source schema (basic schema evolution).
- Requires a primary key to identify records for deletion. This should be set in the source database.

**Use cases:**
- Event streams where deletions must be reflected in the analytics layer.
- Data warehousing scenarios requiring clean datasets by removing obsolete records.

#### Append + Update Scenarios

**Note:** This scenario is currently <ins>not supported</ins>.

This configuration is used when both new records and updates to existing records need to be processed.

**Configuration:**
Add or modify the following keys in the [sink configuration](#firebolt-connector-configuration):

```json
"insert.mode": "upsert",
"primary.key.mode": "record_key",
"primary.key.fields": "<pk_col>"
```

**How it works:**
- Updates existing records based on the primary key.
- Inserts new records if no matching primary key exists.
- Requires a primary key to uniquely identify records.

**Use cases:**
- Customer records that need to reflect the latest state.
- Inventory systems requiring updates and new product additions.

#### Complete CDC Pipeline with Deletes

**Note:** This scenario is currently <ins>not supported</ins>.

This configuration handles full CDC operations, including inserts, updates, and deletions.

**Configuration:**
Add or modify the following keys in the [sink configuration](#firebolt-connector-configuration):

```json
"insert.mode": "upsert",
"primary.key.mode": "record_key",
"primary.key.fields": "<pk_col>",
"delete.enabled": "true"
```

**How it works:**
- Processes `INSERT`, `UPDATE`, and `DELETE` operations.
- Requires a primary key to uniquely identify records.
- Deletes records in Firebolt when they are deleted in the source database.

**Use cases:**
- Full data synchronization between systems.
- Master data management requiring referential integrity.

### Throughput Optimization

For high-throughput use cases, such as IoT metrics ingestion, you can optimize the connector configuration to improve performance.

**Configuration:**
Add or modify the following key in the [sink configuration](#firebolt-connector-configuration):

```json
"batch.size": 5000
```

**Additional Kafka Connect settings:**
To align with the batch size, adjust the Kafka Connect worker's `consumer.max.poll.records` property. For example, set it to `5000`:

- In Docker Compose: Override the `CONNECT_CONSUMER_MAX_POLL_RECORDS` environment variable.
- In manual installations: Update the `consumer.max.poll.records` property in the `connect-standalone.properties` file.

**Note:** Ensure other Kafka settings, such as `fetch.max.bytes` and `max.partition.fetch.bytes`, are configured to handle the expected payload size.

For more details, refer to Debezium's [batch support optimization guide](https://debezium.io/blog/2023/12/20/JDBC-sink-connector-batch-support/).

## Limitations

The following limitations apply when integrating Firebolt with Apache Kafka: 
* You can only insert or update data in your table using either `insert` or `update` mode. The `"insert.mode":"upsert"` [setting](https://debezium.io/documentation/reference/stable/connectors/jdbc.html#jdbc-property-insert-mode) is not yet supported.
* [Append+Update](#append--update-scenarios) and [CDC](#complete-cdc-pipeline-with-deletes) scenarios are not yet supported due to the limitation above.

## Additional resources

* Learn how to setup a database source you can use with Debezium's [source connectors](https://debezium.io/documentation/reference/stable/connectors/index.html).
* Learn more about [Kafka Connect](https://kafka.apache.org/documentation/#connect).
* Learn how to [customize a Kafka Connect configuration](https://kafka.apache.org/documentation/#connectconfigs). 
* Learn how a [Debezium sink](https://debezium.io/documentation/reference/stable/connectors/jdbc.html#how-the-jdbc-connector-works) works and about its limitations.
