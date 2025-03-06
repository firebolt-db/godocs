---
redirect_from:
  - /loading-data/configuring-aws-role-to-access-amazon-s3.html
layout: default
title: Use AWS roles to access S3
description: Learn how to use AWS IAM roles to allow Firebolt to access your data lake in Amazon S3.
parent: Load data
nav_order: 4
has_toc: false
has_children: false
---


# Use AWS roles to access Amazon S3
{: .no_toc}
Firebolt uses AWS Identity and Access Management (IAM) permissions to load data from an Amazon S3 bucket into Firebolt. This requires you to set up permissions using the AWS Management Console. You have two options to specify credentials with the appropriate `CREDENTIALS` when you create an external table:

* You can provide **Access Keys** associated with an IAM principal that has the required permissions
* You can specify an **IAM role** that Firebolt assumes for the appropriate permissions.

This guide explains how to configure an IAM role and an AWS IAM permissions policy to grant Firebolt the necessary permissions to access and read data from an Amazon S3 bucket.

1. Topic ToC
{:toc}

## Create an IAM permissions policy

1. Log in to the [AWS Identity and Access Management \(IAM\) Console](https://console.aws.amazon.com/iam/home#/home).
2. From the left navigation panel, under **Access management**, choose **Account settings**.
3. Under **Security Token Service \(STS\),** in the **Endpoints** list, find the **Region name** where your account is located. If the status is **Inactive**, choose **Activate**.
4. Choose **Policies** from the left navigation panel.
5. Select **Create Policy.**
6. Select the **JSON** tab.
7. Add a policy document that will allow Firebolt to access the S3 bucket and folder.

   The following policy in JSON format provides Firebolt with the required permissions to unload data using a single bucket and folder path. Copy and paste the text into the policy editor. Replace `<bucket>` and `<prefix>` with the actual bucket name and path prefix.

   ```javascript
   {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "s3:GetObject",
                  "s3:GetObjectVersion"
              ],
              "Resource": "arn:aws:s3:::<bucket>/<prefix>/*"
          },
          {
              "Effect": "Allow",
              "Action": "s3:GetBucketLocation",
              "Resource": "arn:aws:s3:::<bucket>"
          },
          {
              "Effect": "Allow",
              "Action": "s3:ListBucket",
              "Resource": "arn:aws:s3:::<bucket>",
              "Condition": {
                  "StringLike": {
                      "s3:prefix": [
                          "<prefix>/*"
                      ]
                  }
              }
          }
      ]
   }
   ```

   * If you encounter the following error: `Access Denied (Status Code: 403; Error Code: AccessDenied)`, remove the following condition from the IAM policy:

   ```javascript
              "Condition": {
                  "StringLike": {
                      "s3:prefix": [
                          "<prefix>/*"
                      ]
                  }
              }
   ```

8. Select **Next** in the bottom-right corner of the workspace.
9. In the **Review and create** pane, under **Policy details**, enter the **Policy name**. For example, `_firebolt-s3-access_`.
10. Enter an optional **Description**.
11. Select the **Create policy** button in the bottom-right corner of the workspace.

{: .warning}
Setting the s3:prefix condition key to * grants access to **all** prefixes in the specified bucket for the associated action.

## Create the IAM role

To integrate Firebolt with AWS Identity and Access Management (IAM), you must first obtain your Firebolt account ID and then create an IAM policy in AWS. The following steps guide you through retrieving your Firebolt account ID and setting up the necessary IAM role and policy in AWS to establish secure authentication.

### Obtain your Firebolt account ID
1. Log in to the [Firebolt Workspace](https://go.firebolt.io/login).
2. Select the plus (**+**) sign in Firebolt's **Develop Space**.
3. Select an engine for loading data.
4. Next to **Authentication method**, select the radio button for **IAM Role**.
5. In **IAM Role Setup Guidance**, select **Create an IAM role**.
6. In the **Create new IAM role** popup window, note your Firebolt account ID from ARN in the custom trust policy. An example ARN is formatted as follows: `arn:aws:iam::123456789012:role/my-firebolt-role`. In the previous example, the account ID is `123456789012`.

### Create an IAM policy in AWS
1. Log in to the [AWS Identity and Access Management \(IAM\) Console](https://console.aws.amazon.com/iam/home#/home).
2. From the left navigation panel, choose **Roles**.
3. Then, choose **Create role**.
4. In the **Select trusted entity** pane that pops up, select **AWS account** as the **Trusted entity type**.
5. Under **An AWS account**, select the radio button next to **Another AWS Account**.
5. In the **Account ID** field, enter your Firebolt **Account ID** from the last step in [Obtain your Firebolt account ID](#obtain-your-firebolt-account-id).
6. Ensure that the checkbox next to **Require external ID (Best practice when a third party will assume this role)** is checked.
6. Choose **Next**.
7. Begin entering the name of the policy you created in step 1 of [Create an IAM permissions policy](#create-an-iam-permissions-policy) in the search box, and then select it from the list.
8. Select **Next**.
9. In the **Role details** pane, enter a **Role name** and optional **Description** for the role.
10. Select **Create role**.
11. Record the **Role ARN** listed on the role summary page.

Once you've created your IAM policy and associated it with your IAM role, you're ready to load data into Firebolt using IAM roles. Firebolt assumes the IAM role to securely access and read data from your Amazon S3 bucket.

## Specifying the IAM Role for Data Loading

When loading data into Firebolt, specify the IAM role ARN from the previous step to grant the necessary permissions. If you configured an external ID, ensure it is included along with the role ARN. Below are a few references for how to Load Data into Firebolt using AWS IAM Roles to access your storage bucket.

### Specify the IAM role in COPY FROM

Use the role ARN from the previous step when you specify the role ARN in the [CREDENTIALS]({% link sql_reference/commands/data-management/copy-from.md %}) of the `COPY FROM` statement. If you specified an external ID, make sure to specify it in addition to the role ARN. When you use the `COPY FROM` statement to load data from your source, Firebolt assumes the IAM role to obtain permissions to read from the location specified in the `COPY FROM` statement. 

Use the IAM role ARN when specifying the [CREDENTIALS]({% link sql_reference/commands/data-management/copy-from.md %}) in the COPY FROM statement. If you specified an external ID, include it with the role ARN. Firebolt assumes this role to access the specified data source.

For a step-by-step guide, see [Loading Data Wizard](../loading-data/loading-data-sql.md#the-simplest-copy-from-workflow)

#### Example: 

```sql
COPY INTO tutorial 
FROM 's3://your_s3_bucket/your_file.csv'
WITH
CREDENTIALS = (
    AWS_ROLE_ARN='arn:aws:iam::123456789012:role/my-firebolt-role'
    AWS_EXTERNAL_ID='ca4f5690-4fdf-4684-9d1c-2d5f9fabc4c9'
)
HEADER=TRUE AUTO_CREATE=TRUE;
```

### Using IAM Role in the Firebolt UI Wizard 

You can use the role ARN from the previous step when loading data via the Loading Data Wizard in the Firebolt UI. For a step-by-step guide, see [Loading Data Wizard](../loading-data/loading-data-wizard.md). 


### Using IAM Role in External Table Definitions

Specify the IAM role ARN and optional external_id in the [`CREDENTIALS`]({% link sql_reference/commands/data-definition/create-external-table.md %}) of the `CREATE EXTERNAL TABLE` statement. Firebolt assumes this IAM role when using an `INSERT INTO` statement to load data into a fact or dimension table.

#### Example:

```sql
CREATE EXTERNAL TABLE my_ext_table (
  c_id    INTEGER,
  c_name  TEXT,
  c_type  TEXT PARTITION('[^/]+/c_type=([^/]+)/[^/]+/[^/]+')
)
CREDENTIALS = (AWS_ROLE_ARN='arn:aws:iam::123456789012:role/my-firebolt-role' AWS_ROLE_EXTERNAL_ID='ca4f5690-4fdf-4684-9d1c-2d5f9fabc4c9')
URL = 's3://my_bucket/'
OBJECT_PATTERN= '*.parquet'
TYPE = (PARQUET)
```