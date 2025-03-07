---
redirect_from:
  - /developing-with-firebolt/connecting-with-nodejs.html
layout: default
title: Node.js
description: Learn about using the Node.js SDK for Firebolt.
nav_order: 1
parent: Develop with Firebolt
has_toc: true
---

# Node.js
{:.no_toc}

* Topic ToC
{:toc}

## Overview
The Firebolt Node SDK is a software development kit designed to facilitate the integration of Firebolt's high-performance database capabilities into Node.js applications. This SDK provides a set of tools and interfaces for developers to interact with Firebolt databases, enabling efficient data manipulation and query execution. For more detailed documentation, including API references and advanced usage, refer to the [README](https://github.com/firebolt-db/firebolt-node-sdk/blob/main/README.md) file in the Firebolt Node SDK repository.

## Installation
To install the Firebolt Node SDK, run the following command in your project directory:
```bash
npm install firebolt-sdk
```

## Authentication

After installation, you must authenticate before you can use the SDK to establish connections, run queries, and manage database resources. The following code example sets up a connection using your Firebolt [service account]({% link Guides/managing-your-organization/service-accounts.md %}) credentials:

```typescript
const connection = await firebolt.connect({
  auth: {
    client_id: '12345678-90123-4567-8901-234567890123',
    client_secret: 'secret',
  },
  engineName: 'engine_name',
  account: 'account_name',
  database: 'database',
});
```
In the previous code example, the following details apply:

* `client_id` and `client_secret`: These are your service account credentials. Refer to Firebolt's guide to learn how to [create a service account]({% link Guides/managing-your-organization/service-accounts.md %}#create-a-service-account) and obtain its [ID]({% link Guides/managing-your-organization/service-accounts.md %}#get-a-service-account-id) and [secret]({% link Guides/managing-your-organization/service-accounts.md %}#generate-a-secret). 
* `engineName`: The name of the engine used to run your queries on.
* `database`: The target database where your tables will be stored.
* `account`: The object within your organization that encapsulates resources for storing, querying, and managing data. In the Node.js SDK, the [account]({% link Overview/organizations-accounts.md %}#accounts) parameter specifies which organizational environment the connection will use. 

## Quick start
In the following code example, credentials are stored in environment variables.

```javascript
import { Firebolt } from 'firebolt-sdk'

// Initialize client
const firebolt = Firebolt();

// Establish connection to Firebolt using environment variables for credentials and configuration
const connection = await firebolt.connect({
  auth: {
    client_id: process.env.FIREBOLT_CLIENT_ID,
    client_secret: process.env.FIREBOLT_CLIENT_SECRET,
  },
  account: process.env.FIREBOLT_ACCOUNT,
  database: process.env.FIREBOLT_DATABASE,
  engineName: process.env.FIREBOLT_ENGINE_NAME
});

// Create a "users" table
await connection.execute(`
  CREATE TABLE IF NOT EXISTS users (
    id INT,
    name STRING,
    age INT
  )
`);

// Insert sample data
await connection.execute(`
  INSERT INTO users (id, name, age) VALUES
  (1, 'Alice', 30),
  (2, 'Bob', 25)
`);

// Update rows
await connection.execute(`
  UPDATE users SET age = 31 WHERE id = 1
`);

// Fetch data with a query
const statement = await connection.execute("SELECT * FROM users");

// Fetch the complete result set
const { data, meta } = await statement.fetchResult();

// Log metadata describing the columns of the result set
console.log(meta)
// Outputs:
// [
//   Meta { type: 'int null', name: 'id' },
//   Meta { type: 'text null', name: 'name' },
//   Meta { type: 'int null', name: 'age' }
// ]

// Alternatively, stream the result set row by row
const { data } = await statement.streamResult();

data.on("metadata", metadata => {
  console.log(metadata);
});

// Handle metadata event
data.on("error", error => {
  console.log(error);
});

const rows = []

for await (const row of data) {
  rows.push(row);
}

// Log the collected rows
console.log(rows)
// Outputs:
// [ [ 1, 'Alice', 31 ], [ 2, 'Bob', 25 ] ]
```

## Contribution
To receive support, report issues, or contribute, please refer to the Firebolt Node SDK repository [issue tracker](https://github.com/firebolt-db/firebolt-node-sdk/issues). 

## License
This SDK is released under **Apache License 2.0**. See the [LICENSE](https://github.com/firebolt-db/firebolt-node-sdk/blob/main/LICENSE) file for more details.
