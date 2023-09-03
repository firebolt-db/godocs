---
layout: default
title: Use the API
description: Learn about using the Firebolt API to interact with Firebolt.
nav_order: 1
parent: Query data
grand_parent: Guides
---

# Firebolt REST API - Work in progress!!

Use the Firebolt REST API to execute queries on engines programmatically. This topic provides commands for common tasks using the REST API, including authentication, working with engines, and executing queries. A service account is required to access the API - learn about managing service accounts [here](../managing-your-organization/service-accounts.md). 

## In this topic

* [Use tokens for authentication](#use-tokens-for-authentication)
* [Start, stop, and restart engines](#start-stop-and-restart-engines)
* [Get the URL of an engine](#get-the-url-of-an-engine)
* [Ingest data](#ingest-data)
* [Run queries](#run-queries)

## Use tokens for authentication

To authenticate Firebolt using service accounts via Firebolt’s REST API, send the following request to receive an authentication token:

```json
    curl --location --request POST 'https://api.app.firebolt.io/auth/v1/token' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'client_id=<id>' \
    --data-urlencode 'client_secret=<secret>' \
    --data-urlencode 'grant_type=client_credentials'
```

Where:

| Property                          | Data type | Description |
| :------------------------------   | :-------- | :---------- |
| id                                | TEXT      | The user’s ID ([created here](#create-a-service-account-user)). |
| secret                            | TEXT      | The user’s secret ([generated here](#generate-a-secret-for-the-service-account-user)). |


**Response**

```json
{  
  "access_token": "YOUR_ACCESS_TOKEN_VALUE",  
  "expires_in": 43200,  
  "refresh_token": "YOUR_REFRESH_TOKEN_VALUE",  
  "scope": "offline_access",  
  "token_type": "Bearer"  
}
```

Use the returned access_token to authenticate with Firebolt.


## Start, stop, and restart engines

An engine in Firebolt is a cluster of nodes that do the work when you run SQL queries. You can use the REST API to start, stop, and restart engines. To perform these operations on an engine, you must have the unique engine ID and the engine must be stopped. The operation to get this ID is shown first, followed by start, stop, and restart operations. For more information about engines, see [Working with engines](../../Overview/understanding-engine-fundamentals.md).

### Get the System Engine URL

The endpoint returns the engine URL for accountName. It requires authentication with a bearer token. 

**Request**

```bash
curl http://api.{env}.firebolt.io/web/v3/account/{accountName}/engineUrl 
-H "Accept: application/json" 
-H "Authorization: Bearer {token}"
```

**Response**

```json
{
    "engine_id": {
        "account_id": "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "engine_id": "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

### Start an engine

Replace `ENGINE_ID` in the example below with the value you retrieved for `engine_id`.

**Request**

```bash
curl --request POST 'https://api.app.firebolt.io/core/v1/account/engines/ENGINE_ID:start' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN_VALUE'
```

**Response**

```json
{
    "engine": {
        "id": {
            "account_id": "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "engine_id": "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        },
        "name": "YOUR_ENGINE_NAME",
        "description": "",
        "emoji": "1F3A5",
        "compute_region_id": {
            "provider_id": "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "region_id": "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        },
        "settings": {
            "preset": "ENGINE_SETTINGS_PRESET_GENERAL_PURPOSE",
            "auto_stop_delay_duration": "1200s",
            "minimum_logging_level": "ENGINE_SETTINGS_LOGGING_LEVEL_INFO",
            "is_read_only": false,
            "warm_up": "ENGINE_SETTINGS_WARM_UP_INDEXES"
        },
        "current_status": "ENGINE_STATUS_RUNNING_IDLE",
        "current_status_summary": "ENGINE_STATUS_SUMMARY_STOPPED",
        "latest_revision_id": {
            "account_id": "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "engine_id": "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "engine_revision_id": "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        },
        "endpoint": "YOUR_ENGINE_NAME.YOUR_ACCOUNT_NAME.YOUR_REGION.app.firebolt.io",
        "endpoint_serving_revision_id": null,
        "create_time": "2021-05-03T20:40:43.024856Z",
        "create_actor": "/users/xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "last_update_time": "2021-05-21T23:54:15.841494Z",
        "last_update_actor": "",
        "last_use_time": null,
        "desired_status": "ENGINE_STATUS_UNSPECIFIED",
        "health_status": "ENGINE_HEALTH_STATUS_UNSPECIFIED",
        "endpoint_desired_revision_id": null
    },
    "desired_engine_revision": null
}
```

### Stop an engine

Replace `ENGINE_ID` in the example below with the value you retrieved for `engine_id`.

**Request**

```bash
curl --request POST 'https://api.app.firebolt.io/core/v1/account/engines/ENGINE_ID:stop' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN_VALUE'
```

**Response**

```json
{
    "engine": {
        "id": {
            "account_id": "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "engine_id": "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        },
        "name": "YOUR_ENGINE_NAME",
        "description": "",
        "emoji": "1F3A5",
        "compute_region_id": {
            "provider_id": "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "region_id": "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        },
        "settings": {
            "preset": "ENGINE_SETTINGS_PRESET_GENERAL_PURPOSE",
            "auto_stop_delay_duration": "1200s",
            "minimum_logging_level": "ENGINE_SETTINGS_LOGGING_LEVEL_INFO",
            "is_read_only": false,
            "warm_up": "ENGINE_SETTINGS_WARM_UP_INDEXES"
        },
        "current_status": "ENGINE_STATUS_RUNNING_REVISION_SERVING",
        "current_status_summary": "ENGINE_STATUS_SUMMARY_RUNNING",
        "latest_revision_id": {
            "account_id": "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "engine_id": "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "engine_revision_id": "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        },
        "endpoint": "YOUR_ENGINE_NAME.YOUR_ACCOUNT_NAME.YOUR_REGION.app.firebolt.io",
        "endpoint_serving_revision_id": null,
        "create_time": "2021-05-03T20:40:43.024856Z",
        "create_actor": "/users/xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "last_update_time": "2021-05-24T21:05:59.388381Z",
        "last_update_actor": "",
        "last_use_time": null,
        "desired_status": "ENGINE_STATUS_UNSPECIFIED",
        "health_status": "ENGINE_HEALTH_STATUS_UNSPECIFIED",
        "endpoint_desired_revision_id": null
    },
    "desired_engine_revision": null
}
```

### Restart an engine

Replace `ENGINE_ID` with the value you retrieved for `engine_id`.

**Request**

```bash
curl --request POST 'https://api.app.firebolt.io/core/v1/account/engines/ENGINE_ID:restart' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN_VALUE'
```

**Response**

```json
{
    "engine": {
        "id": {
            "account_id": "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "engine_id": "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        },
        "name": "YOUR_ENGINE_NAME",
        "description": "",
        "emoji": "1F3A5",
        "compute_region_id": {
            "provider_id": "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "region_id": "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        },
        "settings": {
            "preset": "ENGINE_SETTINGS_PRESET_GENERAL_PURPOSE",
            "auto_stop_delay_duration": "1200s",
            "minimum_logging_level": "ENGINE_SETTINGS_LOGGING_LEVEL_INFO",
            "is_read_only": false,
            "warm_up": "ENGINE_SETTINGS_WARM_UP_INDEXES"
        },
        "current_status": "ENGINE_STATUS_RUNNING_REVISION_SERVING",
        "current_status_summary": "ENGINE_STATUS_SUMMARY_RUNNING",
        "latest_revision_id": {
            "account_id": "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "engine_id": "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "engine_revision_id": "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        },
        "endpoint": "YOUR_ENGINE_NAME.YOUR_ACCOUNT_NAME.YOUR_REGION.app.firebolt.io",
        "endpoint_serving_revision_id": null,
        "create_time": "2021-05-03T20:40:43.024856Z",
        "create_actor": "/users/xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "last_update_time": "2021-05-24T21:15:00.522042Z",
        "last_update_actor": "",
        "last_use_time": null,
        "desired_status": "ENGINE_STATUS_UNSPECIFIED",
        "health_status": "ENGINE_HEALTH_STATUS_UNSPECIFIED",
        "endpoint_desired_revision_id": null
  },
    "desired_engine_revision": null
}
```

## Get the URL of an engine

Some Firebolt REST API operations require the URL of the engine to run the request. You can get the URL of an engine in any state, but the engine must be running to accept requests at its URL. Commands to start, stop, and restart and engine use the engine ID instead of the URL. For more information about starting, stopping, and restarting engines using the Firebolt REST API, see [Start, stop, and restart engines](#start-stop-and-restart-engines) above.

The examples below show you how to get the URL of the default engine by providing the database name, and how to get it using the engine name.

**Get the URL of the default engine in your database**

Use the following request to get the URL of the default engine in your database.

```bash
curl --request GET 'https://api.app.firebolt.io/core/v1/account/engines:getURLByDatabaseName?database_name=YOUR_DATABASE_NAME' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN_VALUE'
```

This returns:

```json
{"engine_url": "YOUR_DATABASES_DEFAULT_ENGINE_URL"}
```

**Get the URL of an engine by providing the engine name**

Use the following request to get the URL of an engine by using the engine name,

```bash
curl --request GET 'https://api.app.firebolt.io/core/v1/account/engines?filter.name_contains=YOUR_ENGINE_NAME' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN_VALUE'
```

This returns (`...` indicates areas of JSON omitted from this example):

```json
{
  "page": {
    ...
  },
  "edges": [
    {
      ...
        "endpoint": "YOUR_ENGINE_URL",
      ...
      }
    }
  ]
}
```

## Ingest data

Ingesting data using the Firebolt REST API requires the following steps:

1. [Create an external table](./firebolt-rest-api.html/#create-an-external-table)
2. [Create a fact table and import data](./firebolt-rest-api.html/#create-a-fact-table-and-import-data)

### Create an external table

Use a request similar to the example below to create an external table.

```bash
echo "CREATE_EXTERNAL_TABLE_SCRIPT" | curl \
--request POST 'https://YOUR_ENGINE_URL/?database=YOUR_DATABASE_NAME' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN_VALUE' \
--data-binary @-
```

Provide values for placeholders according to the following guidance.

* `YOUR_ENGINE_URL` is the value of `engine_url` returned by the command shown in Get the URL of an engine.
* `YOUR_DATABASE_NAME` is the name of the database.
* `CREATE_EXTERNAL_TABLE_SCRIPT` is a SQL script using the `CREATE EXTERNAL TABLE` statement similar to the following example:

```sql
CREATE EXTERNAL TABLE [ IF NOT EXISTS ] <external_table>
  ( <col_name> <col_type> [ , ... ])
  URL = 's3://<path_to_s3_objects>'
  [ CREDENTIALS = ( AWS_KEY_ID = '******' AWS_SECRET_KEY = '******' ) ]
  OBJECT_PATTERN = <pattern_regex>
  TYPE = ( { CSV | JSON | PARQUET } );
```

In the above script, replace the following placeholders:

* `<external_table>` is the name of the external table to create.
* `<col_name> <col_type>` are columns and corresponding data type specifications.
* `<path_to_s3_objects>` is the path to your data store in Amazon S3.
* `<pattern_regex>` is a pattern that identifies the files inside the S3 location. For example, to specify all files of `<filename>.parquet` in the bucket, use `'*.parquet'` in place of `<pattern_regex>`.

### Create a fact table and import data

Use the following request to create a fact table:

```bash
echo "CREATE_FACT_TABLE_SCRIPT" | curl \
--request POST 'https://YOUR_ENGINE_URL/?database=YOUR_DATABASE_NAME' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN_VALUE' \
--data-binary @-
```

Provide values for placeholders according to the following guidance.

* `YOUR_ENGINE_URL` is the value returned by the command shown in [Get the URL of an engine](#get-the-url-of-an-engine).
* `YOUR_DATABASE_NAME` is the name of the database.
* `CREATE_FACT_TABLE_SCRIPT` is a SQL script similar to the following:

```sql
CREATE FACT TABLE [IF NOT EXISTS] <fact_table>
(
    <column_name> <column_type>
    [ , ... ]  
)
PRIMARY INDEX <column_list>
```

In the above script, replace the following:

* `<fact_table>` is the name of the fact table to create.
* `<column_name> <column_type>` are columns and corresponding data type specifications.
* `<column_list>` is a list of column names separated by commas (for example, `column1, column2`) to be used for the primary index. For more information, see [How to choose primary index columns](../working-with-indexes/using-primary-indexes.md#how-to-choose-primary-index-columns).

{: .note}
Before importing the data to the fact table, consider creating an aggregating index to boost performance even further. You can also create the aggregating index later. For more information, see [Aggregating indexes](../working-with-indexes/using-aggregating-indexes.md).


**Import data into the fact table**

Use the following request to import data into your fact table:

```bash
echo "IMPORT_SCRIPT" | curl \
--request POST 'https://YOUR_ENGINE_URL/?database=YOUR_DATABASE_NAME' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN_VALUE' --data-binary @-
```

Provide values for placeholders according to the following guidance.

* `YOUR_ENGINE_URL` is the value of `your_engine_url` returned by the command shown in [Get the URL of an engine](#get-the-url-of-an-engine).
* `YOUR_DATABASE_NAME` is the name of the database.
* `IMPORT_SCRIPT` is a SQL script similar to the following:

```sql
INSERT INTO <fact_table> SELECT * FROM <external_table>
```

* `<fact_table>` is your Firebolt table name.
* `<external_table>` is the name of the external table to use for ingestion.

## Run queries

Use the following syntax to submit a query to run to a running engine. You can specify multiple queries separated by a semicolon (;).

### Request

```bash
echo "SELECT_QUERY" | curl \
--request POST 'https://YOUR_ENGINE_ENDPOINT/?database=YOUR_DATABASE_NAME' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN_VALUE' \
--data-binary @-
```

Provide values for placeholders according to the following guidance.

* `YOUR_ENGINE_URL` is the value of `engine_url` returned by the command shown in [Get the URL of an engine](#get-the-url-of-an-engine).
* `YOUR_DATABASE_NAME` is the name of the database.
* `SELECT_QUERY` is the query to run. You can separate multiple queries using a semicolon (`;`) as shown in the example below.

```sql
SELECT_QUERY_1;  
SELECT_QUERY_2;  
--more queries...  
SELECT_QUERY_N;
```

{: .note}
Queries are per request. To run multiple statement queries, separate queries each into one request. 

### Cancel a running query

Use the following request to cancel a running query:

```bash
curl --request POST 'https://YOUR_ENGINE_URL/cancel?query_id=YOUR_QUERY_ID' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN_VALUE'
```

Provide values for placeholders according to the following guidance.

* `YOUR_ENGINE_URL` is the value of `engine_url` returned by the command shown in [Get the URL of an engine](#get-the-url-of-an-engine).
* `YOUR_QUERY_ID` is the ID of the query you need to cancel. You can get a query ID using the [running queries view](../../Reference//information-schema/running-queries.md).
