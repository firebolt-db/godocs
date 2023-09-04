---
layout: default
title: Use the API
description: Learn about using the Firebolt API to interact with Firebolt.
nav_order: 1
parent: Query data
grand_parent: Guides
---

# Firebolt API

Use the Firebolt REST API to execute queries on engines programmatically. Learn how to use the API, including authentication, working with engines and executing queries. A service account is required to access the API - learn about managing service accounts [here](../managing-your-organization/service-accounts.md). 

* Topic toC
{:toc}

## Use tokens for authentication

To authenticate Firebolt using service accounts via Firebolt’s REST API, send the following request to receive an authentication token:

```bash
    curl --location --request POST 'https://api.app.firebolt.io/auth/v1/token' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'client_id=<id>' \
    --data-urlencode 'client_secret=<secret>' \
    --data-urlencode 'grant_type=client_credentials'
```

where:

| Property                          | Data type | Description |
| :------------------------------   | :-------- | :---------- |
| id                                | TEXT      | The user’s ID ([created here](../managing-your-organization/service-accounts.md#creating-a-service-account)). |
| secret                            | TEXT      | The user’s secret ([generated here](../managing-your-organization/service-accounts.md#generating-a-secret-for-the-service-account-user)). |


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

To run a query using the API, you must first obtain the url of the engine you want to run on. Queries can be run against any engine in the account, including the system engine. 

## Get the system engine URL

Use the following endpoint to return the system engine URL for `<account_name>`. 

```bash
curl http://api.app.firebolt.io/web/v3/account/<account_name>/engineUrl 
-H 'Accept: application/json' 
-H 'Authorization: Bearer <access token>'
```

**Example:** `https://api.app.firebolt.io/web/v3/account/my_account/engineUrl`

## Execute a query on the system engine

Use the following endpoint to run a query on the system engine:  

```bash
curl --location '<system_engine_URL>/query?account_id=<account_id>' \
--header 'Authorization: Bearer <access token>' \
--data '<SQL query>'
```

where:

| Property                          | Data type | Description |
| :------------------------------   | :-------- | :---------- |
| system_engine_URL                 | TEXT      | The system engine URL ([retrieved here](#get-the-system-engine-url)) |
| account_id                        | TEXT      | The account id |
| SQL query                         | TEXT      | Any valid SQL query |                 


## Get a user engine URL

Get a user engine url by running the following query against the `information_schema.engines` table: 

```sql
SELECT url 
FROM information_schema.engines 
WHERE engine_name=<engine_name>
```

You can run the query on the system engine using the API with the following request: 

```bash
curl --location 'https://<system_engine_URL>/query?account_id=<account_id>' \
--header 'Authorization: Bearer <access token>' \
--data 'SELECT * FROM information_schema.engines WHERE engine_name=my_engine'
```

## Execute a query on a user engine

Use the following endpoint to run a query on a user engine:

```bash
curl --location 'https://{user_engine_URL}/query?database={database_name}' \
--header 'Authorization: Bearer <access token>' \
--data '<SQL query>'
```

where:

| Property                          | Data type | Description |
| :------------------------------   | :-------- | :---------- |
| user_engine_URL                   | TEXT      | The user engine URL ([retrieved here](#get-a-user-engine-url)) |
| database_name                     | TEXT      | The database to run the query |
| SQL query                         | TEXT      | Any valid SQL query |                 

{: .note}
Queries are per request. To run multiple statement queries, separate queries each into one request. 
