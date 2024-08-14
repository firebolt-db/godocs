---
layout: default
title: Load data
description: Understand options for loading data into Firebolt from your data lake.
parent: Guides
nav_order: 3
has_children: true
has_toc: false
---

# Load data

You can load data into Firebolt from an Amazon S3 bucket using two different workflows.

If you want to get started quickly, load data using a Load data wizard in the Firebolt workspace. If you want a more customized experience, you can write SQL scripts to handle each part of your workflow. This guide shows you how to load data using both the wizard and SQL, and some common data loading workflows and errors.

Before you can load data, you must first register with Firebolt, then create a database and an engine. For information about how to register, see [Get Started](../getting-started.md). To create a database and engine, the following apply:
- If you use the Load data wizard, the user interface (UI) guides you through creating an engine and database.
- If you want to use the Firebolt SQL UI, you can select buttons to create a database and engine. See [Get Started](../getting-started.md) for more information.
- If you want to write your own SQL script, you must use `CREATE DATABASE` and `CREATE ENGINE` before you can load data.

Use the previous guidance to select the best workflow for your use case, as shown in the following diagram:
<img src="../../assets/images/load_data_workflow.png" alt="The load data workflow includes using the load data wizard or SQL to create a database, engine, and then load data." width="700"/>

Firebolt saves metadata including virtual columns, and the source file’s name, size and timestamp when mapping data from an Amazon S3 bucket to a Firebolt database. You can query this metadata directly for troubleshooting and analysis. For more information, see [Work with external tables](working-with-external-tables.md).

Optimizing your workflow for Firebolt starts when you load your data. Your data should load into tables that have primary indexes. You should also use other optimization strategies including aggregating indexes and warm tables. This guide shows you basic instructions for loading data into tables. For an introduction on optimization, see [Get Started](../getting-started.md). For more advanced information about primary and aggregating indexes, see [Work with indexes](../../Guides/working-with-indexes/index.md).

After you load your data, you can start running and optimizing your queries. A typical workflow has the previous steps followed by data and resource cleanup as shown in the following diagram:

<img src="../../assets/images/get_started_workflow.png" alt="The load data workflow includes using the load data wizard or SQL to create a database, engine, and then load data." width="700"/>

For more information on how to register, create a database and an engine, or the other steps in a typical workflow, see [Get Started](../getting-started.md).