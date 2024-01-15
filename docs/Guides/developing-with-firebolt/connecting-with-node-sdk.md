# Firebolt Node SDK

## Overview
The Firebolt Node SDK is a software development kit designed to facilitate the integration of Firebolt's high-performance database capabilities into Node.js applications. This SDK provides a set of tools and interfaces for developers to interact with Firebolt databases, enabling efficient data manipulation and query execution.


## Installation
To install the Firebolt Node SDK, run the following command in your project directory:
```bash
npm install firebolt-node-sdk
```

## Quick Start
To get started with the Firebolt Node SDK, here's a simple example:

```javascript
import { Firebolt } from 'firebolt-sdk'

const firebolt = Firebolt();

const connection = await firebolt.connect({
  auth: {
    client_id: process.env.FIREBOLT_CLIENT_ID,
    client_secret: process.env.FIREBOLT_CLIENT_SECRET,
  },
  account: process.env.FIREBOLT_ACCOUNT,
  database: process.env.FIREBOLT_DATABASE,
  engineName: process.env.FIREBOLT_ENGINE_NAME
});

const statement = await connection.execute("SELECT 1");

// fetch statement result
const { data, meta } = await statement.fetchResult();

// or stream result
const { data } = await statement.streamResult();

data.on("metadata", metadata => {
  console.log(metadata);
});

data.on("error", error => {
  console.log(error);
});

const rows = []

for await (const row of data) {
  rows.push(row);
}

console.log(rows)

```
## Documentation
For more detailed documentation, including API references and advanced usage, please refer to the [README](https://github.com/firebolt-db/firebolt-node-sdk/blob/main/README.md) file in the repository.

## Contribution
For support, issues, or contributing, please refer to the repository's issue tracker and contributing guidelines.

## License
This SDK is released under **Apache License 2.0**. Please see the [LICENSE](https://github.com/firebolt-db/firebolt-node-sdk/blob/main/LICENSE) file for more details.