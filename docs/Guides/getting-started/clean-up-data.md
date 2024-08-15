---
layout: default
title: Cleaning up data
nav_order: 4
parent: Get started
grand_parent: Guides
---

### Cleaning up data

<img src="../assets/images/../../../assets/images/GS-cleanup.png" alt="New DB +" width="700"/>

After you’ve completed the steps in this guide, avoid incurring costs associated with the exercises by doing the following:
- [Cleaning up data](#cleaning-up-data)
  - [Stop any running engines](#stop-any-running-engines)
  - [Remove data from storage](#remove-data-from-storage)
- [Export data](#export-data)

#### Stop any running engines

Firebolt shows you the status of your current engine next to the engines icon (<img src="../assets/images/../../../assets/images/engine-icon.png" alt="AggIndex" width="12"/>) under your script tab as either **Stopped** or **Running**. To shut down your engine, select your engine from the drop-down list next to the name of the engine, and then select one of the following:
* Stop engine - Allow all of the currently running queries to finish running and then shut down the engine. Selecting this option will allow the engine to run for as long as it takes to complete all queries running on the selected engine.
* Terminate all queries and stop - Stop the engine and stop running any queries. Selecting this option stops the engine in about 20-30 seconds.  

#### Remove data from storage

To remove a table and all of its data, enter [DROP TABLE](../sql_reference/../../sql_reference/commands/data-definition/drop-table.md) into a script tab, as shown in the following code example:

`DROP TABLE levels`

To remove a database and all of its associated data, do the following:
1.  Select the database from the left navigation bar. 
2. Select the more options (<img src="../assets/images/../../../assets/images/more options icon.png" alt="AggIndex" width="10"/>) icon.
3. Select **Delete database**. Deleting your database will permanently remove your database from Firebolt. You cannot undo this action.
4. Select **Delete**.

### Export data 

If you want to save your data outside of Firebolt, you can use [COPY TO](../sql_reference/../../sql_reference/commands/data-management/copy-to.md) to export data to an external table. This section shows how to set the minimal AWS permissions and use a COPY TO to export data to an [AWS S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html). You may have to reach out to your administrator to obtain or change AWS permissions.

1. **Set permissions to write to an AWS S3 bucket**
  
  Firebolt must have the following permissions to write to an AWS S3 bucket:

  i. AWS access key credentials. The credentials must be associated with a user with permissions to write objects to the bucket. Specify access key credentials using the following syntax: 
    
  ```sql
  CREDENTIALS = (AWS_KEY_ID = '<aws_key_id>'  AWS_SECRET_KEY = '<aws_secret_key>')
  ```
      
  In the previous credentials example, `<aws_key_id>` is the AWS access key id associated with a user or role. An access key has the following form: `AKIAIOSFODNN7EXAMPLE`.
    
  `<aws_secret_key>` is the AWS secret key. A secret key has the following form: `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`.

  ii. An AWS IAM policy statement attached to a user role. Firebolt requires the following minimum permissions in the IAM policy: 

  ```sql
    {
        "Version": "2012-10-17",
        "Statement": [
            {
            "Effect": "Allow",
            "Action": [
              "s3:Get*",
              "s3:List*",
              "s3:PutObject",
              "s3:DeleteObject"
            ],
            "Resource": [
      "arn:aws:s3:::my_s3_bucket",
      "arn:aws:s3:::my_s3_bucket/*"
                  ]
              }
          ]
      }
  ```

For more information about AWS access keys and roles, see [Creating Access Key and Secret ID in AWS](../loading-data/creating-access-keys-aws.md)

i. **Export to an AWS S3 bucket**
Use [COPY TO](../sql_reference/../../sql_reference/commands/data-management/copy-to.md) select all the columns from a table and export to an AWS S3 bucket as shown in the following code example:
```sql
COPY (SELECT * FROM test_table)
  TO 's3://my_bucket/my_fb_queries'
  CREDENTIALS = (AWS_ROLE_ARN='arn:aws:iam::123456789012:role/my-firebolt-role');
```
In the previous code example, the role ARN [(Amazon Resource Name)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) identifies the AWS IAM role that specifies the access for users or services. An ARN follows the following structure: arn:aws:iam::account-id:role/role-name. Because TYPE is omitted from COPY TO, the file or files will be written in the default CSV format. Because `COMPRESSION` is also omitted, the output data is compressed using GZIP (`*.csv.gz`) format.

Firebolt assigns a query ID, that has the following example format `16B903C4206098FD`, to the query at runtime. If the size of the compressed output exceeds the default of 16 MB, Firebolt writes multiple GZIP files. In the following example, the size of the output is 40 MB, so Firebolt writes 4 files.

```sql
s3://my_bucket/my_fb_queries/
  16B903C4206098FD_0.csv.gz
  16B903C4206098FD_1.csv.gz
  16B903C4206098FD_2.csv.gz
  16B903C4206098FD_3.csv.gz
```

See [COPY TO](../sql_reference/../../sql_reference/commands/data-management/copy-to.md) for more information. 