---
layout: default
title: CREATE ACCOUNT
description: Reference and syntax for the CREATE ACCOUNT command.
grand_parent:  SQL commands
parent: Data definition
---

# CREATE ACCOUNT
Creates a new account.

For more information, see [Managing accounts](../../../Guides/managing-your-organization/managing-accounts.md).

{: .note}
Organizations can have 20 accounts per organization and you can use `CREATE ACCOUNT` 25 times. If you have a need for additional account creations beyond this limit, contact [Firebolt Support](https://docs.firebolt.io/godocs/Reference/help-menu.html) for assistance. Our team can provide guidance and, if appropriate, adjust your account settings to accommodate your needs.

## Syntax

```sql
CREATE ACCOUNT [IF NOT EXISTS] <account_name>
[ WITH REGION = <region> ]
```

## Parameters 
{: .no_toc} 

| Parameter  | Description                                                                                                                                                                                                                                                            |
| :--------- |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<account_name>`                              | The name of the account, must start and end with an alphabetic character and cannot contain spaces or special characters except for hyphens (-).                                                                                                                       |
| `<region>`                      | The region in which the account is configured. Choose the same region as the Amazon S3 bucket that contains data you ingest. See [Available AWS Regions](../../../Reference/available-regions.md) If not specified, `us-east-1` (US East (N. Virginia) is the default. |                                                                                                    

## Example

The following command will create an account in the US East (N. Virginia) region.

```sql
CREATE ACCOUNT dev WITH REGION = “us-east-1”
```
