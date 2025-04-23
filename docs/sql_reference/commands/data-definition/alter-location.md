---
layout: default
title: ALTER LOCATION
description: Reference and syntax for the ALTER LOCATION statement.
parent: Data definition
---

# ALTER LOCATION
{: .no_toc}

Modifies an existing location object in your Firebolt account. You can use ALTER LOCATION to rename a location, update its URL, or modify its credentials while maintaining all dependent objects.

**Topics:**
* [Notes](#notes)
* [Syntax](#syntax)
* [Parameters](#parameters)
* [Examples](#examples)
* [Error handling](#error-handling)

## Notes

- All identifiers are case-insensitive unless enclosed in double-quotes
- Location modifications maintain all dependent object relationships
- External tables using the location remain valid after modifications
- For more information about object identifiers, see [Object identifiers]({% link Reference/object-identifiers.md %})

## Syntax

```sql
-- Rename a location
ALTER LOCATION [IF EXISTS] <location_name> RENAME TO <new_location_name>

-- Update location URL
ALTER LOCATION [IF EXISTS] <location_name> 
SET URL { = | TO } '<new_url>'

-- Update location credentials
ALTER LOCATION [IF EXISTS] <location_name>
SET CREDENTIALS { = | TO } (
    AWS_ACCESS_KEY_ID = '<aws_access_key_id>' 
    AWS_SECRET_ACCESS_KEY = '<aws_secret_access_key>' 
    [ AWS_SESSION_TOKEN = '<aws_session_token>' ] 
    | 
    AWS_ROLE_ARN = '<aws_role_arn>' 
    [ AWS_ROLE_EXTERNAL_ID = '<aws_role_external_id>' ]
)
```

## Parameters

| Parameter | Description |
| :-------- | :---------- |
| `<location_name>` | The identifier of the location to modify. |
| `<new_location_name>` | The new identifier for the location. Must be a valid identifier, see [Object identifiers]({% link Reference/object-identifiers.md %}). |
| `<new_url>` | The new Amazon S3 URL in the format: `s3://{bucket_name}/{path}` |
| `<aws_access_key_id>` | The AWS access key ID. |
| `<aws_secret_access_key>` | The AWS secret access key. |
| `<aws_session_token>` | The AWS session token. |
| `<aws_role_arn>` | The AWS role ARN. |
| `<aws_role_external_id>` | The AWS role external ID. |
| `IF EXISTS` | Optional parameter that suppresses the error if the location doesn't exist. |

## Examples

### Rename a location

```sql
ALTER LOCATION my_location RENAME TO my_new_location;
```

### Update location URL

```sql
-- Basic URL update
ALTER LOCATION my_location 
SET URL = 's3://new-bucket/new-path/';

-- Update URL using TO syntax
ALTER LOCATION my_location 
SET URL TO 's3://new-bucket/different-path/';
```

### Update credentials

```sql
-- Update to use access keys
ALTER LOCATION my_location 
SET CREDENTIALS = (
    AWS_ACCESS_KEY_ID = 'new_key' 
    AWS_SECRET_ACCESS_KEY = 'new_secret'
);

-- Update to use role-based authentication
ALTER LOCATION my_location 
SET CREDENTIALS TO (
    AWS_ROLE_ARN = 'arn:aws:iam::123456789012:role/S3Access'
);
```

## Error handling

The following table lists common errors and their resolutions:

| Error | Cause | Resolution |
|:-----------|:------|:-----------|
| **Invalid Identifier** | New location name contains invalid characters or is a reserved keyword. | Use a valid identifier that starts with a letter and contains only letters, numbers, and underscores. |
| **Location Not Found** | The specified location doesn't exist or you lack permission to modify it. | Verify the location name and your permissions. Use `IF EXISTS` to handle non-existent locations. |
| **Name Conflict** | The new location name is already in use. | Choose a different name or drop the existing location first. |
| **Invalid URL** | The new URL is not a valid S3 URL. | Use the correct format: `s3://{bucket_name}/{path}` |
| **Invalid Credentials** | Missing required credential parameters or invalid format. | Ensure all required credentials are provided and properly formatted. |