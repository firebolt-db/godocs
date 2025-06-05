---
redirect_from:
  - /sql-reference/commands/create-location.html
layout: default
title: CREATE LOCATION
description: Reference and syntax for the CREATE LOCATION statement.
parent: Data definition
---

# CREATE LOCATION
{: .no_toc}

Creates a new location object in your Firebolt account, which is a secure, reusable object that stores the connection details and credentials for external data sources. Instead of entering these details each time you run a query or create a table, you can use a location object.

The location object stores the following:
* The source type specification
* Authentication credentials
* The data source URL
* Optional descriptive metadata

This makes it easier to manage data access, keeps your credentials safe, and saves you from having to repeat the same information across multiple queries. 

You can use `LOCATION` to centralize credential storage with managed access with Role-Based Access Control ([RBAC]({% link Overview/Security/Role-Based Access Control/index.md %})) for `CREATE`, `MODIFY`, and `USAGE` permissions for different users, use a single location definition for multiple tables and queries, and control access to sensitive data. `LOCATION` is version control-friendly because no sensitive credentials are stored in source code.

After you create a `LOCATION`, you can use the `information_schema.locations` view to see [details about all the locations]({% link sql_reference/information-schema/locations.md %}) in your account including source type, URL, description, owner and creation time.

 **Related:**

This document covers `LOCATION` objects in general. For more information about specific types of `LOCATION` objects, including more in-depth examples, please see:
 * [CREATE LOCATION (Amazon S3)]({% link sql_reference/commands/data-definition/create-location-s3.md %})
 * [CREATE LOCATION (Iceberg)]({% link sql_reference/commands/data-definition/create-location-iceberg.md %})

 **Topics:**
 * [Syntax](#syntax)
 * [Parameters](#parameters)
 * [Permissions](#permissions)
 * [Examples](#examples)
 * [Notes](#notes)
 * [Error Handling](#error-handling)
 * [Best Practices](#best-practices)
 * [Limitations](#limitations)

## Syntax

```sql
CREATE LOCATION [ IF NOT EXISTS ] <location_name> WITH
  SOURCE = { 'AMAZON_S3' | 'ICEBERG' }
  [ , ... ]

-- Amazon S3 Location
CREATE LOCATION [ IF NOT EXISTS ] <location_name> WITH
  SOURCE = 'AMAZON_S3'
  CREDENTIALS = {
    ( AWS_ACCESS_KEY_ID = '<aws_access_key_id>'
      AWS_SECRET_ACCESS_KEY = '<aws_secret_access_key>'
      [ AWS_SESSION_TOKEN = '<aws_session_token>' ] )
    |
    ( AWS_ROLE_ARN = '<aws_role_arn>'
      [ AWS_ROLE_EXTERNAL_ID = '<aws_role_external_id>' ] )
  }
  URL = '<url>'
  [ DESCRIPTION = '<description>' ]

-- Iceberg Location
CREATE LOCATION [ IF NOT EXISTS ] <location_name> WITH
  SOURCE = 'ICEBERG'
  CATALOG = { 'FILE_BASED' | 'REST' | 'DATABRICKS_UNITY' }
  CATALOG_OPTIONS = {
    -- FILE_BASED
    ( URL = '<file_based_catalog_url>' )
    |
    -- REST
    ( URL = '<rest_catalog_url>'
      WAREHOUSE = '<warehouse>'
      NAMESPACE = '<namespace>'
      TABLE = '<table_name>' )
    |
    -- DATABRICKS_UNITY
    ( WORKSPACE_INSTANCE = '<workspace_instance>'
      CATALOG = '<uc_catalog_name>'
      SCHEMA = '<uc_schema_name>'
      TABLE = '<uc_table_name>' )
  }
  CREDENTIALS = {
    -- AWS Authentication
    ( AWS_ACCESS_KEY_ID = '<aws_access_key_id>'
      AWS_SECRET_ACCESS_KEY = '<aws_secret_access_key>'
      [ AWS_SESSION_TOKEN = '<aws_session_token>' ] )
    |
    ( AWS_ROLE_ARN = '<aws_role_arn>'
      [ AWS_ROLE_EXTERNAL_ID = '<aws_role_external_id>' ] )
    |
    -- OAuth Authentication
    ( OAUTH_CLIENT_ID = '<oauth_client_id>'
      OAUTH_CLIENT_SECRET = '<oauth_client_secret>'
      [ OAUTH_SCOPE = '<oauth_scope>' ]
      [ OAUTH_SERVER_URL = '<oauth_server_url>' ] )
  }
  [ DESCRIPTION = '<description>' ]
```

## Parameters

### Common Parameters

| Parameter | Description |
| :-------- | :---------- |
| `<location_name>` | A unique identifier for the location within your account. |
| `SOURCE` | The external data source type. Currently, `AMAZON_S3` (See [CREATE LOCATION (Amazon S3)]({% link sql_reference/commands/data-definition/create-location-s3.md %})) and `ICEBERG` (See [CREATE LOCATION (Iceberg)]({% link sql_reference/commands/data-definition/create-location-iceberg.md %})) are supported. |
| `DESCRIPTION` | Optional metadata describing the location's purpose. |

### Amazon S3 Parameters

| Parameter | Description |
| :-------- | :---------- |
| `CREDENTIALS` | Authentication credentials for Amazon S3 access. |
| `URL` | The data source URL in the format: `s3://{bucket_name}/{path}`. This must be a valid S3 URL. |

### Iceberg Parameters

| Parameter | Description |
| :-------- | :---------- |
| `CATALOG` | The type of Iceberg catalog. Supported values: `FILE_BASED`, `REST`, or `DATABRICKS_UNITY`. |
| `CATALOG_OPTIONS` | Configuration options specific to the chosen catalog type. |
| `CREDENTIALS` | Authentication credentials for accessing the Iceberg catalog. Depending on the type of catalog, either AWS or OAuth credentials are used. |

#### AWS Authentication Parameters

| Parameter | Description |
| :-------- | :---------- |
| `AWS_ACCESS_KEY_ID` | Your AWS access key ID for key-based authentication. |
| `AWS_SECRET_ACCESS_KEY` | Your AWS secret access key for key-based authentication. |
| `AWS_SESSION_TOKEN` | Optional temporary session token for temporary credentials. |
| `AWS_ROLE_ARN` | The ARN of the IAM role to assume for role-based authentication. |
| `AWS_ROLE_EXTERNAL_ID` | Optional external ID for role assumption. |

#### OAuth Authentication Parameters

| Parameter | Description |
| :-------- | :---------- |
| `OAUTH_CLIENT_ID` | The OAuth client ID for authentication. |
| `OAUTH_CLIENT_SECRET` | The OAuth client secret for authentication. |
| `OAUTH_SCOPE` | Optional OAuth scope for authentication. |
| `OAUTH_SERVER_URL` | Optional OAuth server URL for authentication. |

#### Iceberg Catalog-Specific Parameters

##### FILE_BASED Catalog
| Parameter | Description |
| :-------- | :---------- |
| `URL` | The URL for the file-based catalog. |

##### REST Catalog
| Parameter | Description |
| :-------- | :---------- |
| `URL` | The REST catalog URL. |
| `WAREHOUSE` | The warehouse identifier. |
| `NAMESPACE` | The namespace identifier. |
| `TABLE` | The table name. |

##### DATABRICKS_UNITY Catalog
| Parameter | Description |
| :-------- | :---------- |
| `WORKSPACE_INSTANCE` | The Databricks workspace instance. |
| `CATALOG` | The Unity Catalog name. |
| `SCHEMA` | The Unity Catalog schema name. |
| `TABLE` | The Unity Catalog table name. |

## Permissions

`LOCATION` objects are managed using [RBAC]({% link Overview/Security/Role-Based Access Control/index.md %}) with the following permission levels:

| Permission | Description |
| :--------- | :---------- |
| CREATE LOCATION | Create a new location object. |
| MODIFY LOCATION | Modify existing location objects. |
| MODIFY ANY LOCATION | Modify any location object in the account. |
| LIST LOCATION | View location object details. |
| LIST ANY LOCATION | View any location object in the account. |
| USAGE LOCATION | Use a location object. |
| USAGE ANY LOCATION | Use any location object in the account. |

## Examples

* [Create a location](#create-a-location)
* [Create a location with a description](#create-a-location-with-a-description)
* [Create a location only if it doesn't exist](#create-a-location-only-if-it-doesnt-exist)
* [Use a location to load data into an external table](#use-a-location-to-load-data-into-an-external-table)
* [Use a location to load data using COPY statements](#use-a-location-to-load-data-using-copy-statements)
* [Use a location to load data with a TVF](#use-a-location-to-load-data-with-a-tvf)
* [Alter a location](#alter-a-location)
* [Delete a location](#delete-a-location)

### Create a location

The following code example creates a location that uses keys to authenticate to AWS:

```sql
CREATE LOCATION my_location WITH
  SOURCE = 'AMAZON_S3'
  CREDENTIALS = ( AWS_ACCESS_KEY_ID = '1231' AWS_SECRET_ACCESS_KEY = '567' )
  URL = 's3://my-bucket/path/to/data'
```

### Create a location with a description

The following code example creates a location object named `my_location`, for an Amazon S3 data source with the specified URL and description:

```sql
CREATE LOCATION my_location WITH
  SOURCE = 'AMAZON_S3'
  CREDENTIALS = ( AWS_ACCESS_KEY_ID = '1231' AWS_SECRET_ACCESS_KEY = '567' )
  URL = 's3://my-bucket/path/to/data'
  DESCRIPTION = 'Main data storage location'
```

### Create a location only if it doesn't exist

The following code example uses an access key to authenticate to AWS using a location only if it doesn't already exist:

```sql
CREATE LOCATION IF NOT EXISTS my_location WITH
  SOURCE = 'AMAZON_S3'
  CREDENTIALS = ( AWS_ACCESS_KEY_ID = '1231' AWS_SECRET_ACCESS_KEY = '567' )
  URL = 's3://my-bucket/path/to/data'
```

### Use a location to load data into an external table

The following code example creates an external table `my_ext_table` that uses a previously created location `my_location` to load Parquet data files matching the *.parquet pattern from Amazon S3:

```sql
CREATE EXTERNAL TABLE my_ext_table (
  c_id    INT,
  c_name  TEXT
)
LOCATION = my_location
OBJECT_PATTERN = '*.parquet'
TYPE = PARQUET
```

For more information about using locations in external tables, see [CREATE EXTERNAL TABLE]({% link sql_reference/commands/data-definition/create-external-table.md %}).

### Use a location to load data using COPY statements

The following code example uses `COPY FROM` to load Parquet data files matching the *.parquet pattern from `my_location` into `my_table`:

```sql
COPY INTO my_table
FROM my_location
WITH
  OBJECT_PATTERN = '*.parquet'
  TYPE = PARQUET
```

For more information, see [COPY TO]({% link sql_reference/commands/data-management/copy-to.md %}) and [COPY FROM]({% link sql_reference/commands/data-management/copy-from.md %}).

### Use a `LOCATION` to load data with a TVF

You can use `LOCATION` to load data using table-valued functions (TVFs) such as [READ_CSV]({% link sql_reference/functions-reference/table-valued/read_csv.md %}), [READ_PARQUET]({% link sql_reference/functions-reference/table-valued/read_parquet.md %}), and [LIST_OBJECTS]({% link sql_reference/functions-reference/table-valued/list-objects.md %}).

The following code example uses `READ_CSV` to query data from a CSV file stored in `my_location`, using the first row as headers for column names:

```sql
SELECT * FROM READ_CSV(
  location => my_location,
  header => TRUE
)
```

### Alter a location

Firebolt does not yet support altering a location that has been created. This feature will be available in a future release.

### Delete a location

You can use [DROP LOCATION]({% link sql_reference/commands/data-definition/drop-location.md %}) to remove a location from your Firebolt account. 

The following code example deletes a `LOCATION` from your Firbolt account:

```sql
DROP LOCATION [IF EXISTS] <location_name> [WITH FORCE]
```

{: .note} Deleting a location will affect all objects that depend on the `LOCATION` that you are dropping.

## Notes

- All identifiers are case-insensitive unless enclosed in double-quotes
- Locations cannot be created on the system engine
- For more information about object identifiers, see [Object identifiers]({% link Reference/object-identifiers.md %})

## Error Handling

The system uses secure error handling for location objects:
* Generic error messages ensure security by not exposing sensitive information.
* Detailed error information is only available to users with the necessary permissions.
* Users without the required permissions are provided with instructions to contact an administrator.

## Best Practices

1. Use location objects instead of embedding credentials directly in queries or table definitions.
2. Regularly rotate credentials stored in location objects.
3. Follow the principle of least privilege when assigning permissions.
4. Use clear and descriptive names and descriptions for location objects.
5. Keep a record of dependencies before removing any location objects.

## Limitations

- The `DROP CASCADE` functionality is not supported.
- The source type cannot be modified for existing location objects.
- Location objects cannot be used alongside inline credentials in the same statement.
- Historical versions of credentials are not maintained.
