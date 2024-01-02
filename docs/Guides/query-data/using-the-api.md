---
layout: default
title: Use the API
description: Learn about using the Firebolt API to interact with Firebolt.
nav_order: 2
parent: Query data
grand_parent: Guides
---

# Firebolt API

Use the Firebolt REST API to execute queries on engines programmatically. Learn how to use the API, including authentication, working with engines and executing queries. A service account is required to access the API - learn about [managing service accounts here](../managing-your-organization/service-accounts.md). 

* Topic toC
{:toc}

## Create a service account and associate it with a user
Create a service account with organization administrator privilege, 
i.e., the service account property_is_organization_admin_ must be _true_.
Next, create a user with role privileges you would like to have the service account
and associate the service account with the user.

## Use tokens for authentication


To authenticate Firebolt using the service accounts with the properties
as described above via Firebolt’s REST API, send the following request 
to receive an authentication token:


```bash
    curl --location --request POST 'https://id.app.firebolt.io/oauth/token' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'client_id=<id>' \
    --data-urlencode 'client_secret=<secret>' \
    --data-urlencode 'grant_type=client_credentials'
    --data-urlencode 'audience=https://api.firebolt.io'
```

where:

| Property                          | Data type | Description                                                                                                                                        |
| :------------------------------   | :-------- |:---------------------------------------------------------------------------------------------------------------------------------------------------|
| id                                | TEXT      | The service account ID ([created here](../managing-your-organization/service-accounts.md#creating-a-service-account)).                             |
| secret                            | TEXT      | The service account secret ([generated here](../managing-your-organization/service-accounts.md#generating-a-secret-for-a-service-account)). |


**Response**

```json
{
  "access_token":"access_token_value",
  "token_type":"Bearer",
  "expires_in":86400
}
```

Use the returned access_token to authenticate with Firebolt.

To run a query using the API, you must first obtain the url of the engine you want to run on. Queries can be run against any engine in the account, including the system engine. 

## Get the system engine URL

Use the following endpoint to return the system engine URL for `<account name>`. 

```bash
curl http://api.app.firebolt.io/web/v3/account/<account name>/engineUrl 
-H 'Accept: application/json' 
-H 'Authorization: Bearer <access token>'
```

**Example:** `https://api.app.firebolt.io/web/v3/account/my-account/engineUrl`

**Response**

```json
{
    "engineUrl": "https://api.us-east-1.dev.firebolt.io"
}
```

## Get ID of your account

Use the following endpoint to retrieve the ID of your account:

```bash
curl http://api.app.firebolt.io/web/v3/account/<account name>/resolve \
-H 'Accept: application/json' \
-H 'Authorization: Bearer <access token>'
```

**Example:** `https://api.app.firebolt.io/web/v3/account/my-account/resolve`   

**Response**

```json
{
    "id":"<account_id>",
    "region":"us-east-1"
}
```

## Execute a query on the system engine

Use the following endpoint to run a query on the system engine:  

```bash
curl --location '<system engine URL>/query?account_id=<account id>' \
--header 'Authorization: Bearer <access token>' \
--data '<SQL query>'
```

where:

| Property                          | Data type | Description |
| :------------------------------   | :-------- | :---------- |
| system engine URL                 | TEXT      | The system engine URL ([retrieved here](#get-the-system-engine-url)) |
| account id                        | TEXT      | The account id |
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
curl --location 'https://<system_engine_URL>/query?account_id=<account id>' \
--header 'Authorization: Bearer <access token>' \
--data 'SELECT * FROM information_schema.engines WHERE engine_name=my_engine'
```

## Execute a query on a user engine

Use the following endpoint to run a query on a user engine:

```bash
curl --location 'https://{user engine URL}/query?database={database name}' \
--header 'Authorization: Bearer <access token>' \
--data '<SQL query>'
```

where:

| Property                          | Data type | Description |
| :------------------------------   | :-------- | :---------- |
| user engine URL                   | TEXT      | The user engine URL ([retrieved here](#get-a-user-engine-url)) |
| database name                     | TEXT      | The database to run the query |
| SQL query                         | TEXT      | Any valid SQL query |                 

{: .note}
Queries are per request. To run multiple statement queries, separate queries each into one request. 
