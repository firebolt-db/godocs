---
redirect_from:
  - /developing-with-firebolt/connecting-with-go.html
layout: default
title: Go
description: Learn about using the Go SDK for Firebolt.
nav_order: 7
parent: Develop with Firebolt
has_toc: true
---

# Firebolt Go SDK Documentation

## Overview

The Firebolt Go SDK is an implementation of Go's `database/sql/driver` interface, enabling Go developers to connect to and interact with Firebolt databases seamlessly.

## Prerequisites

You must have the following prerequisites before you can connect your Firebolt account to Go:
* **Go installed and configured** on your system. The minimum supported version is 1.18 or higher. If you do not have Go installed, you can download the [latest version](https://go.dev/dl/). After installing, if you don't have a Go module yet, you'll need to initialize one. See the [Go documentation on modules](https://go.dev/doc/tutorial/create-module) for detailed instructions on how to create and initialize a Go module.
* **Firebolt account** &ndash; You need an active Firebolt account. If you do not have one, you can [sign up](https://go.firebolt.io/signup) for one.
* **Firebolt service account** &ndash; You must have access to an active Firebolt [service account]({% link Guides/managing-your-organization/service-accounts.md %}), which facilitates programmatic access to Firebolt, its ID and secret.
* **Firebolt user** &ndash; You must have a user that is [associated]({% link Guides/managing-your-organization/service-accounts.md %}#create-a-user) with your service account. The user should have [USAGE]({% link Overview/Security/Role-Based Access Control/database-permissions/index.md %}) permission to query your database, and [OPERATE]({% link Overview/Security/Role-Based Access Control/engine-permissions.md %}) permission to start and stop an engine if it is not already started.
* **Firebolt database and engine (optional)** &ndash; You can optionally connect to a Firebolt database and/or engine. If you do not have one yet, you can [create a database]({% link Guides/getting-started/get-started-sql.md %}#create-a-database) and also [create an engine]({% link Guides/getting-started/get-started-sql.md %}#create-an-engine). You would need a database if want to access stored data in Firebolt and an engine if you want to load and query stored data.
   
## Installation

To install the Firebolt Go SDK, run the following `go get` command from inside your Go module:

```bash
go get github.com/firebolt-db/firebolt-go-sdk
```

## DSN Parameters

Go passes a data source name (DSN) to Firebolt's Go SDK to connect to Firebolt. The SDK parses the DSN string for parameters to authenticate and connect to a Firebolt account, database, and engine.

The DSN string supports the following parameters:

- `client_id`: client ID of your [service account]({% link Guides/managing-your-organization/service-accounts.md %}).
- `client_secret`: client secret of your [service account]({% link Guides/managing-your-organization/service-accounts.md %}).
- `account_name`: The name of your Firebolt [account]({% link Guides/managing-your-organization/managing-accounts.md %}).
- `database`: (Optional) The name of the [database]({% link Overview/Security/Role-Based Access Control/database-permissions/index.md %}) to connect to.
- `engine`: (Optional) The name of the [engine]({% link Overview/Security/Role-Based Access Control/engine-permissions.md %}) to run SQL queries on.

The following is an example DSN string:

```text
firebolt://[/<database>]?account_name=<account_name>&client_id=<client_id>&client_secret=<client_secret>&engine=<engine>
```

## Connect to Firebolt

To establish a connection to a Firebolt database, construct a DSN string with your credentials and database details. The following example contains a script to connect to Firebolt that you can place in a file (e.g `main.go`) and run using `go run main.go` inside your Go module:

```go
package main

import (
    "database/sql"
    "fmt"
    // Import the Firebolt Go SDK
    _ "github.com/firebolt-db/firebolt-go-sdk"
)

func main() {
    // Replace with your Firebolt credentials and database details
    clientId := "your_client_id"
    clientSecret := "your_client_secret"
    accountName := "your_account_name"
    databaseName := "your_database_name" // Optional parameter
    engineName := "your_engine_name" // Optional parameter
    dsn := fmt.Sprintf("firebolt:///%s?account_name=%s&client_id=%s&client_secret=%s&engine=%s", databaseName, accountName, clientId, clientSecret, engineName)

    // Open a connection to the Firebolt database
    db, err := sql.Open("firebolt", dsn)
    if err != nil {
        log.Fatalf("Error opening database connection: %v\n", err)
        return
    }
    defer db.Close()

    // Your database operations go here
}
```

## Run queries

Once connected, you can run SQL queries. The following examples show you how to create a table, insert data, and retrieve data. You can place them inside the previous script under `// Your database operations go here``:

```go
// Create a table
_, err = db.Exec("CREATE TABLE IF NOT EXISTS test_table (id INT, value TEXT)")
if err != nil {
    log.Fatalf("Error creating table: %v\n", err)
    return
}

// Insert data into the table
_, err = db.Exec("INSERT INTO test_table (id, value) VALUES (?, ?)", 1, "sample value")
if err != nil {
    log.Fatalf("Error inserting data: %v\n", err)
    return
}

// Query data from the table
rows, err := db.Query("SELECT id, value FROM test_table")
if err != nil {
    log.Fatalf("Error querying data: %v\n", err)
    return
}
defer rows.Close()

// Iterate over the result set
for rows.Next() {
    var id int
    var value string
    if err := rows.Scan(&id, &value); err != nil {
        log.Fatalf("Error scanning row: %v\n", err)
        return
    }
    log.Print("Row: id=%d, value=%s\n", id, value)
}
```

## Streaming Queries

Firebolt supports streaming large query results using `rows.Next()`, allowing efficient processing of large datasets.

If you enable result streaming, the query execution might finish successfully, but the actual error might be returned while iterating the rows.
{: .note}

To enable streaming, use the `firebolt-go-sdk/context` package to create a context with streaming enabled:

```go
package main

import (
    "context"
    "database/sql"
    "fmt"
    "log"
    
    "github.com/firebolt-db/firebolt-go-sdk"
    fireboltContext "github.com/firebolt-db/firebolt-go-sdk/context"
    
)

func main() {
    dsn := "firebolt:///your_database_name?account_name=your_account_name&client_id=your_client_id&client_secret=your_client_secret"
    db, err := sql.Open("firebolt", dsn)
    if err != nil {
        log.Fatalf("Failed to open database: %v", err)
    }
    defer db.Close()
    
    streamingCtx := fireboltContext.WithStreaming(context.Background())
    
    // Execute a query with streaming enabled. Imitate large query result
    rows, err := db.QueryContext(ctx, "SELECT 123, 'data' FROM generate_series(1, 100000000)")
    if err != nil {
        log.Fatalf("Query execution failed: %v", err)
    }
    defer rows.Close()

    for rows.Next() {
        var col1 string
        var col2 int
        if err := rows.Scan(&col1, &col2); err != nil {
            log.Fatalf("Error scanning row: %v", err)
        }
        log.Print("Row: col1=%s, col2=%d\n", col1, col2)
    }
    if err := rows.Err(); err != nil {
        log.Fatalf("Row iteration error: %v", err)
    }
}
```

Streaming queries are particularly useful when dealing with large datasets, as they avoid loading the entire result set into memory at once.

## Troubleshooting
When building a DSN to connect with Firebolt using the Go SDK, follow these best practices to ensure correct connection string formatting and avoid parsing errors. The DSN must follow this structure:
```text
firebolt:///<database_name>?account_name=<account_name>&client_id=<client_id>&client_secret=<client_secret>&engine=<engine_name>
```

**Guidelines**

* Place the database name in the URI path after `firebolt:///`.
* Use only letters, numbers, and underscores (_) in the database name. Avoid hyphens (-), as they may cause parsing errors.
* Ensure the `account_name` matches the name shown in the Firebolt Console URL, which is usually lowercase with no special characters.
* Use the exact engine name as shown in the Firebolt Workspace.
* Do not pass the database name as a query parameter. The SDK does not support `&database=` in the DSN.

### Common errors and solutions

| Error message                               | Likely cause                                              | Solution                                                 |
|---------------------------------------------|-----------------------------------------------------------|----------------------------------------------------------|
| `invalid connection string format`          | URI format is invalid or it contains illegal characters (like `-`)       | Double check the URI format and remove illegal characters.  |
| `unknown parameter name database`           | Attempted to pass `database` as a query parameter.         | Move the database name into the URI path.                |
| `error opening database connection`         | Incorrect connection credentials.                      | Verify connection parameters values in the Firebolt UI and use exact values.    |

## Additional Resources

- [Firebolt Go SDK GitHub Repository](https://github.com/firebolt-db/firebolt-go-sdk)
- [Firebolt Documentation: Connecting with Go]({% link Guides/developing-with-firebolt/connecting-with-go.md %})