---
layout: default
title: dbt
description: Learn how to connect dbt to Firebolt.
nav_order: 4
parent: Integrate with Firebolt
---

# Overview

![DBT](../../assets/images/dbt-logo.png)

[DBT](https://www.getdbt.com), or Data Build Tool, is a framework designed for managing and executing data transformations within modern data warehousing architectures. It facilitates the development and deployment of SQL-based transformations in a version-controlled environment, enabling collaboration and ensuring reproducibility of data pipelines. DBT streamlines the process of transforming raw data into analytics-ready datasets, accelerating the delivery of insights.

The Firebolt adapter for dbt brings together dbt's state-of-the-art development tools and Firebolt's next-generation analytics performance. On top of dbt's core features, the adapter offers native support for all of Firebolt's index types and has been specifically enhanced to support ingestion from S3 using Firebolt's external tables mechanics.


# Prerequisites

There are two ways to deploy DBT: self-hosted [DBT Core](https://docs.getdbt.com/docs/introduction#dbt-core) and managed [DBT Cloud](https://docs.getdbt.com/docs/cloud/about-cloud/dbt-cloud-features).

This guide shows how to set up a local installation of [DBT Core](https://docs.getdbt.com/docs/introduction#dbt-core). This guide uses Python's `pip` package manager, but you can use the following ways to install DBT: [Homebrew](https://docs.getdbt.com/docs/core/homebrew-install), [Docker](https://docs.getdbt.com/docs/core/docker-install), and from [source](https://docs.getdbt.com/docs/core/source-install).

You will need the following:

* A GitHub account.
* Python 3.8+.

# Quickstart

This guide shows you how to set up DBT with Firebolt and run your first DBT [model](https://docs.getdbt.com/docs/build/models).

### Setup DBT Core

1. Create a new Python [virtual environment](https://docs.python.org/3/library/venv.html), as shown in the following script example:
    ```shell
    python3 -m venv dbt-env
    ```
2. Activate your venv, as shown in the following script example:
    ```shell
    source dbt-env/bin/activate
    ```
3. Install Firebolt's [adapter](https://github.com/firebolt-db/dbt-firebolt) for DBT, as shown in the following script example:
    ```shell
    python -m pip install dbt-firebolt
    ```
4. (Optional) Check that both dbt packages are installed.
    ```shell
    python -m pip list | grep dbt
    ```
    This command should return `dbt-core` and `dbt-firebolt` and their respective versions.


### Setup connection to Firebolt

DBT uses a `profiles.yml` file to store the connection information. This file generally lives outside of your dbt project to avoid checking in sensitive information in to version control.

The usual place to create this file on Mac and Linux is `~/.dbt/profiles.yml`.

1. Open `~/.dbt/profiles.yml` with your preferred text editor.
2. Paste the following sample configuration:
    ```yaml
    jaffle-shop:
    target: dev
    outputs:
        dev:
        type: firebolt
        client_id: "<client-id>"
        client_secret: "<client-secret>"
        database: "<database-name>"
        engine_name: "<engine-name>"
        account_name: "<account-name>"
    ```
3. Replace the placeholders with your account's information.

    `<client-id>` and `<client-secret>` are key and secret of your service account. If you don't have one, follow the steps in the [Manage service accounts](../managing-your-organization/service-accounts.md) page to learn how to set one up.

    `<database-name>` and `<engine-name>` are the Firebolt's database and engine that you want your queries to run.

    `<account-name>` is a Firebolt account that you're connected to. Learn more [here](../managing-your-organization/managing-accounts.md).

### Setup Jaffle Shop, a sample dbt project

`jaffle_shop` is a fictional ecommerce store. This dbt project transforms raw data from an app database into a customers and orders model ready for analytics. [This version](https://github.com/firebolt-db/jaffle_shop_firebolt) is designed to showcase Firebolt's integration with DBT.

1. Clone `jaffle-shop-firebolt` repository and change to the newly created directory.
    ```shell
    git clone https://github.com/firebolt-db/jaffle_shop_firebolt.git
    cd jaffle_shop_firebolt
    ```

2. Ensure your profile is setup correctly.
    ```shell
    dbt debug
    ```

    If you're seeing an error here, check that your `profiles.yml` is [set up correctly](#setup-connection-to-firebolt), is in the right directory on your system, and that the [engine](../operate-engines/operate-engines.md). is running.
    Also check that you're still in `dbt-env` virtual Python environment that we've [setup earlier](#setup-dbt-core) and that both packages are present.


3. Install dependent packages.
    ```shell
    dbt deps
    ```

4. Run the external table model. If your database is not in `us-east-1` AWS region then refer to the [Readme](https://github.com/firebolt-db/jaffle_shop_firebolt) on how to copy the files.
    ```shell
    dbt run-operation stage_external_sources
    ```

5. Load sample CSV in your database.
    ```shell
    dbt seed
    ```

6. Run the models.
    ```shell
    dbt run
    ```

You should now see the `customers` and `orders` tables in your database, created using dbt models. From here you can explore more of DBT's capabilities, including incremental models, documentation generation, and more, by following the official guides in the section below.

# Limitations

Not every feature of DBT is supported in Firebolt. You can find an up-to-date list of features in the [adapter documentation](https://github.com/firebolt-db/dbt-firebolt?tab=readme-ov-file#feature-support).


# External table loading strategy


In the previous Jaffle Shop example we used a public S3 bucket to load data. If your bucket contains sensitive data, you will want to restrict access. Follow our [guide](../loading-data/creating-access-keys-aws.md) to set up AWS authentication using an ID and secret key.

Now in your `dbt_project.yml`, you can specify the credentials for your external table in fields `aws_key_id` and `aws_secret_key`, as shown in the following code example:
```yaml
sources:
  - name: firebolt_external
    schema: "{{ target.schema }}"
    loader: S3

    tables:
      - name: <table-name>
        external:
          url: 's3://<bucket_name>/'
          object_pattern: '<regex>'
          type: '<type>'
          credentials:
            aws_key_id: <aws-id>
            aws_secret_key: <aws-secret-key>
          object_pattern: '<regex>'
          compression: '<compression-type>'
          partitions:
            - name: <partition-name>
              data_type: <partition-type>
              regex: '<partition-definition-regex>'
          columns:
            - name: <column-name>
              data_type: <type>
```

To use external tables, you must define a table as external in your dbt_project.yml file. Every external table must contain the fields: `url`, `type`, and `object_pattern`. The Firebolt external table [specification](../../sql_reference/commands/data-definition/create-external-table.md) requires fewer fields than those specified in the dbt documentation.

# "Copy" loading strategy

An alternative method of loading data from S3 into Firebolt is using [COPY FROM](../../sql_reference/commands/data-management/copy-from.md). It has a simple syntax and doesn't require an exact match with your source data. This command does not create an intermediate table and writes your data straight into Firebolt so you can start working with it right away.

The copy syntax in dbt closely adheres to the [specification](../../sql_reference/commands/data-management/copy-from.md#syntax), allowing you to define the necessary fields for data ingestion into Firebolt.

To use `COPY FROM` instead of creating an external table, set `strategy: copy` in your external source definition. For backwards compatibility, if no strategy is specified, the external table strategy is used by default.

```yaml

sources:
  - name: s3
    tables:
      - name: <table-name>
        external:
          strategy: copy
          url: 's3://<bucket_name>/'
          credentials:
            aws_key_id: <aws-id>
            aws_secret_key: <aws-secret-key>
          options:
            object_pattern: '<regex>'
            type: 'CSV'
            auto_create: true
```

You can also include the following options:
```yaml
options:
    object_pattern: '<regex>'
    type: 'CSV'
    auto_create: true
    allow_column_mismatch: false
    max_errors_per_file: 10
    csv_options:
        header: true
        delimiter: ','
        quote: DOUBLE_QUOTE
        escape: '\'
        null_string: '\\N'
        empty_field_as_null: true
        skip_blank_lines: true
        date_format: 'YYYY-MM-DD'
        timestamp_format: 'YYYY-MM-DD HH24:MI:SS'
```
Please note that `csv_options` are indented. For detailed descriptions of these options and their allowed values, refer to the [parameter specification](../../sql_reference/commands/data-management/copy-from.md#parameters).

# Further reading

* [Configuring Firebolt-specific features](https://docs.getdbt.com/reference/resource-configs/firebolt-configs).
* [Incremental models](https://docs.getdbt.com/docs/build/incremental-models).
* [Data tests](https://docs.getdbt.com/docs/build/data-tests).
* [Documenting your models](https://docs.getdbt.com/docs/collaborate/documentation).
