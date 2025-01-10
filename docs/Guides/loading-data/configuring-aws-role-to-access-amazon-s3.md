---
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
2. From the left navigation panel, choose **Account settings**.
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

8. Select **Review policy**.
9. Enter the policy **Name**. For example, `_firebolt-s3-access_`.
10. Enter an optional **Description**.
11. Then, choose **Create policy**.

{: .warning}
Setting the `s3:prefix` condition key to `*` grants access to all  prefixes in the specified bucket for the associated action.

## Create the IAM role

In the AWS Management Console, create an AWS IAM role. The IAM role will assume the permissions you defined in step 1 to access the Amazon S3 buckets where your data files are saved.

1. Log in to the [AWS Identity and Access Management \(IAM\) Console](https://console.aws.amazon.com/iam/home#/home).
2. From the left navigation panel, choose **Roles**.
3. Then, choose **Create role**.
4. Select **Another AWS account** as the trusted entity type.
5. In the **Account ID** field, enter the **AWS Account ID** that you want to use with Firebolt. Users with appropriate privileges can view this value by doing the following:
 
    1) Select the plus (**+**) sign in Firebolt's **Develop Space**.
    2) Choose **Load Data**.
    3) Select an engine for loading data.
    4) Select **Next**.
    5) Select an IAM Role as an authentication method.
    6) Select **Create an IAM role**.
    7) Copy the Firebolt **AWS Principal ID** defined in the **Trust Policy**.
6. Choose **Next**.
7. Begin entering the name of the policy you created in step 1 of [Create an IAM permissions policy](#create-an-iam-permissions-policy) in the search box, and then select it from the list.
8. Select **Next**.
9. Enter a **Name** and optional **Description** for the role.
10. Select **Create role**.
    
    You have now created an IAM permissions policy, an IAM role for Firebolt access, and attached the permissions policy to the role.
11. Record the **Role ARN** listed on the role summary page.

## Specify the IAM role in the external table definition
Specify the role ARN in the [CREDENTIALS]({% link sql_reference/commands/data-definition/create-external-table.md %}) of the `CREATE EXTERNAL TABLE` statement. If you specified an external ID, make sure to specify it in addition to the role ARN. When you use an `INSERT INTO` statement to load data from your source to a fact or dimension table, Firebolt assumes the IAM role to obtain permission to read from the location specified in the external table definition.
