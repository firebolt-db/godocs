---
redirect_from:
  - /general-reference/information-schema/locations.html
layout: default
title: Locations
description: Use this reference to learn about the metadata available for Firebolt locations using the information schema.
parent: Information schema
grand_parent: SQL reference
---

# Information schema for locations

You can use the `information_schema.locations` view to return information about each location in your Firebolt [account]({% link Overview/organizations-accounts.md %}#accounts). The view contains one row for each location. Use a `SELECT` query to return information about each location as shown in the example below.

To view location information, you must have `LIST LOCATION` or `LIST ANY LOCATION` privileges. For more information about location permissions, see [CREATE LOCATION]({% link sql_reference/commands/data-definition/create-location.md %}).

```sql
SELECT
  *
FROM
  information_schema.locations;
```

## Columns in information_schema.locations

Each row has the following columns with information about each location:

| Column Name      | Data Type   | Description |
| :---------------| :-----------| :-----------|
| location_name   | TEXT        | The name of the location. |
| source          | TEXT        | The type of the external data source. Firebolt currently supports only `AMAZON_S3`. |
| url             | TEXT        | The data source URL. For Amazon S3, the format is `s3://{bucket_name}/{path}`. |
| description     | TEXT        | Optional metadata describing the location's purpose. |
| location_owner  | TEXT        | The owner of the location. |
| created         | TIMESTAMPTZ | The timestamp when the location was created. |

## Example

The following query returns information about all locations in your account:

```sql
SELECT 
  location_name,
  source,
  url,
  description,
  location_owner,
  created
FROM 
  information_schema.locations;
```

## Notes

- All identifiers are case-insensitive unless enclosed in double-quotes.
- For more information about object identifiers, see [Object identifiers]({% link Reference/object-identifiers.md %}).
