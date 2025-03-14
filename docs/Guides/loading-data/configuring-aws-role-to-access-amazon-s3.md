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


# Use AWS IAM roles to access Amazon S3
{: .no_toc}
Firebolt uses AWS Identity and Access Management (IAM) permissions to load data from an Amazon S3 bucket into Firebolt. This requires you to set up permissions using the AWS Management Console. Specify credentials when you create an external table using one of the following options:

* You can provide **Access Keys** associated with an IAM principal that has the required permissions.
* You can specify an **IAM role** that Firebolt assumes for the appropriate permissions.

This guide explains how to create an AWS IAM permissions policy and an IAM role to grant Firebolt the necessary permissions to access and read data from an Amazon S3 bucket.

1. Topic ToC
{:toc}

## Create an IAM permissions policy in AWS

1. Log in to the [AWS Identity and Access Management \(IAM\) Console](https://console.aws.amazon.com/iam/home#/home).
2. From the left navigation panel, under **Access management**, choose **Account settings**.
3. Under **Security Token Service \(STS\),** in the **Endpoints** list, find the **Region name** where your account is located. If the status is **Inactive**, choose **Activate**.
4. Choose **Policies** from the left navigation panel.
5. Select **Create Policy**.
6. Select the **JSON** tab.
7. Add a policy document that grants Firebolt access to the Amazon S3 bucket and folder.

   The following policy in JSON format provides Firebolt with the required permissions to unload data using a single bucket and folder path. Copy and paste the text into the policy editor. Replace `<bucket>` and `<prefix>` with the actual bucket name and path prefix.

   ```json
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

   * If you encounter the following error: `Access Denied (Status Code: 403; Error Code: AccessDenied)`, one possible fix may be to remove the following condition from the IAM policy:

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

## Create the IAM role in AWS

To integrate Firebolt with AWS, you must create an IAM role and associate it with the permission policy that you created in the previous [Create an IAM permissions policy in AWS](#create-an-iam-permissions-policy-in-aws) section. The following steps guide you through creating an IAM role, configuring the required trust policy from the Firebolt Workspace, and associating it with your IAM permissions policy. Once completed, you can use the role's Amazon Resource Name (ARN) in Firebolt's `CREDENTIALS` clause to enable secure data ingestion.

1. Log in to the [AWS Identity and Access Management \(IAM\) Console](https://console.aws.amazon.com/iam/home#/home).
2. Select **Roles** from the left navigation panel.
3. Select the **Create role** button in the top right part of the main window.
4. In the **Select trusted entity** window, select the radio button next to **Custom trust policy**.
5. A **Custom trust policy** window opens. Leave this window open until you obtain a custom trust policy from the Firebolt **Workspace** as follows:
    1. Log in to the [Firebolt Workspace](https://go.firebolt.io/login).
    2. Select the plus (**+**) sign in Firebolt's **Develop Space**.
    3. Select **Load data** from the drop-down list.
    4. Select an engine from the drop-down list next to **Select engine for ingestion**. If you do not have an engine, select **Create new engine** to create one.
    5. Select the **Next step** button.
    6. Select the radio button next to **IAM Role** in the **Authentication method** row.
    7. Select the **Create an IAM role** button.
    8. In the **Create new IAM role** window that pops up, select the copy icon under **Trust policy** to copy the entire trust policy to your clipboard.
    9. Return to the AWS **Custom trust policy** window from step 5.
6. Replace the entire contents of the **Custom trust policy** with the contents of your clipboard from the Firebolt **Workspace**.
7. Select the **Next** button in the bottom right part of the main window.
8. Under **Permissions policies** enter the name of and select the checkbox next to the policy you created in step 9 of the previous section [create an IAM permissions policy in AWS](#create-an-iam-permissions-policy-in-aws).
9. Select the **Next** button in the bottom right part of the main window.
10. Under **Role name**, enter a name that you can use to identify it.
11. Select the **Create role** button in the bottom right part of the main window.
12. Under **Role name**, select the name of the role you created in step 10.
13. Copy the value under **ARN**. This value has the following format: `arn:aws:iam::123456789012:role/your_role_name`. Use the ARN value in the Firebolt `CREDENTIALS` clause as the `AWS_ROLE_ARN`, as shown in the following sections.

Once you've created your IAM policy and associated it with your IAM role, you're ready to load data into Firebolt using IAM roles. Firebolt assumes the IAM role to securely access and read data from your Amazon S3 bucket.

## How to specify the IAM role

Firebolt supports AWS IAM roles for secure access to Amazon S3 when loading data. You can specify an IAM role in different ways, including in the `COPY FROM` statement, the Firebolt **Load Data** wizard, or an external table definition. The following sections explain how to configure IAM roles for each method.

### Specify the IAM role for data loading

When loading data into Firebolt, specify the IAM role ARN from the previous step to grant the necessary permissions. If you configured an external ID, ensure it is included along with the role ARN. The following sections show you how to load data into Firebolt using AWS IAM roles to access your storage bucket.

### Specify the IAM role in `COPY FROM`

Use the IAM role ARN from the previous step in the [CREDENTIALS]({% link sql_reference/commands/data-management/copy-from.md %}) of the `COPY FROM` statement. If you specified an external ID, make sure to specify it in addition to the role ARN. When you use the `COPY FROM` statement to load data from your source, Firebolt assumes the IAM role to obtain permissions to read from the location specified in the `COPY FROM` statement. 

For a step-by-step guide, see [The simplest COPY FROM workflow]({% link Guides/loading-data/loading-data-sql.md %}#the-simplest-copy-from-workflow).

**Example**

The following code example loads data from a CSV file in an Amazon S3 bucket into the `tutorial` table in Firebolt, using an AWS IAM role for authentication, treating the first row as a header, and automatically creating the table if it does not exist:

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

### Using IAM role in the Firebolt load data wizard 

You can use the role ARN from the previous step when loading data using the **Load data** wizard in the **Firebolt Workspace**. For a step-by-step guide, see [Load data using a wizard]({% link Guides/loading-data/loading-data-wizard.md %}). 

### Using IAM role in external table definitions

Specify the IAM role ARN and the optional `external_id` in the [`CREDENTIALS`]({% link sql_reference/commands/data-definition/create-external-table.md %}) of the `CREATE EXTERNAL TABLE` statement. Firebolt assumes this IAM role when using an `INSERT INTO` statement to load data into a fact or dimension table.

**Example**

The following code example creates an external table which maps to Parquet files stored in an Amazon S3 bucket, using an AWS IAM role for access, and extracts partition values for `c_type` from the file path based on a specified regex pattern:

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