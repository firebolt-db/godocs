`code`

~~~ go
more code
```
~~~
    dumb code
    more dumb code
things
<p>
some things<p>
here are some more things<br><br>
<a href="abc" target="_blank">
<img src="abc" alt="abc" width="500"/>
</a>

some more text

abc  xyz

# h1
## h2
### h3

h1
==

h2
--

#### h4
abc

* itemA
* itemB
  * item B.A
  * item B.B<br/><br/>list paragraph
  * item B.C

    more paragraph
* itemC
  1. item C.1
  2. item C.2

     paragraph
  3. item C.3
1. item1
2. item2


> This is a blockquote
>> This is a nested blockquote
> > Again, this is a blockquote
> 
>And here
> 
> Here too
># heading
> ```go
> package main
> ```
And now for something different


# Preset

[Preset](https://preset.io/) is a cloud-hosted data exploration and visualization platform built on top of the popular open-source project, [Apache Superset](https://superset.apache.org/). This fully managed service makes it easy to run Superset at scale with enterprise-ready security, reliability, and governance.

Boasting exceptional speed and scalability, Firebolt enables users to adeptly manage substantial data volumes with minimal query latency. The integration with Preset establishes a strong partnership for data professionals, presenting them with a streamlined and efficient workflow. This collaboration ensures prompt loading of Preset dashboards and visualizations, even when confronted with extensive datasets, thereby facilitating the extraction of maximum value from their data.

# Prerequisites

Preset is a managed service so most of the deployment requirements are handled by them.

You will only need:
* To [register](https://manage.app.preset.io/starter-registration/) a Preset account.
* To have a Firebolt account and service account [credentials](../managing-your-organization/service-accounts.md).
* [Load data](../loading-data/loading-data.md) you want to visualise.

{: .note}
  Make sure that your [service account's network policy](https://docs.firebolt.io/Guides/managing-your-organization/service-accounts.html#edit-your-service-account-using-the-ui) allows connections from [Preset IPs](https://docs.preset.io/docs/connecting-your-data).

# Quickstart

### Create a workspace

A workspace is an organizational unit, accessible by team members, that is created for a specific purpose. You can read Preset's [guidance](https://docs.preset.io/docs/about-workspaces) on workspaces to learn more.

1. To Create a Workspace, navigate to the empty card and select + Workspace.

    <img src="../../assets/images/preset-create-workspace-click.png" alt="Create Workspace" width="10%">

2. Define Workspace name and settings

    <img src="../../assets/images/preset-add-new-workspace.png" alt="Add new Workspace" width="30%">

3. Save the workspace and enter it by clicking the card.

### Setup Firebolt connection


After the initial setup in Preset User Inteface head to the `Settings -> Database connections` in the top right corner.

<img src="../../assets/images/preset-settings.png" alt="Database Connections" width="30%">

On the next screen, press the `+ Database` button and select Firebolt from the dropdown.

<img src="../../assets/images/superset-connect-a-database.png" alt="Connect database" width="30%">


The connection expects a SQLAlchemy connection string of the form:

```
firebolt://{client_id}:{client_secret}@{database}/{engine_name}?account_name={account_name}
```

To authenticate, use a service account ID and secret.
A service account is identified by a `client_id` and a `client_secret`.
Learn how to generate an ID and secret [here](../managing-your-organization/service-accounts.md).

Account name must be provided, you can learn about accounts in [Manage accounts](../managing-your-organization/managing-accounts.md) section.

<img src="../../assets/images/superset-firebolt-uri.png" alt="Credentials" width="30%">

Click the Test Connection button to confirm things work end to end. If the connection looks good, save the configuration by clicking the Connect button in the bottom right corner of the modal window.
Now you're ready to start using Preset!

### Build your first chart

To build a chart you can follow our guide in the [Superset section](connecting-to-apache-superset.md#build-your-first-chart), as the Preset works identically.

# Further reading

* [Creating a chart](https://docs.preset.io/docs/creating-a-chart) walkthrough.
* [Creating a Dashboard](https://docs.preset.io/docs/creating-a-dashboard).
* [Collaboration features of Preset](https://docs.preset.io/docs/sharing-and-collaboration).
* [Storytelling in charts](https://docs.preset.io/docs/storytelling-with-charts-and-dashboards-mini-guide).

# Get started using a wizard
{:.no_toc}

The **Load data** wizard guides you through creating a database and engine, and loading data from an Amazon S3 bucket. You can specify basic configurations, including what character to use as a file delimiter, which columns to import and their schema. After loading your data, continue working in the **Develop Space** to run and optimize a query, and export to an external table, as shown in the following diagram:

<img src="../../assets/images/get_started_wizard_workflow.png" alt="A simple workflow using the load data wizard starts with registering, using the wizard, running a query, optimizing your workflow, and cleaning up. " width="700"/>

## Register with Firebolt

<img src="../../assets/images/get_started_wizard_register.png" alt="The first step in getting started is to register with Firebolt." width="700"/>

Use the following steps to register with Firebolt:
<BR>

1. [Sign up](https://go.firebolt.io/signup) on Firebolt's registration page. Fill in your email, name, choose a password, and select **Get Started**.

2. Firebolt will send a confirmation to the address that you provided. To complete your registration, select **Verify** in the email to take you to Firebolt’s [login page](https://go.firebolt.io/login).

3. Type in your email and password and select **Log In**.

{: .note}
New accounts receive credits ($200) to get started exploring Firebolt’s capabilities. Credits must be used within 30 days of account creation.

Firebolt’s billing is based on engine runtime, measured in seconds. AWS S3 storage costs are passed through at rates that vary by region. Your cost depends primarily on which engines you use and how long those engines are running.

You can view your total cost in FBU up to the latest second and in $USD up to the latest day. For more information, see the following **Create a Database** section. For more information about costs, see [Fully-managed pricing model](/overview/billing#fully-managed-pricing-model). If you need to buy additional credits, connect Firebolt with your AWS Marketplace account. For more information about AWS Marketplace, see the following section: [Registering through AWS Marketplace section](./get-started-next.md#register-through-the-aws-marketplace).

## Use the Load data wizard

<img src="../../assets/images/get_started_wizard_wizard.png" alt="After registering, use the load data wizard to create a database, engine, and load data." width="700"/>
<BR>

You can use the **Load data** wizard to load data in either CSV or Parquet form.

 To start the **Load data** wizard, select the plus (+) icon in the **Develop Space** next to **Databases** in the left navigation pane and select **Load data**. The wizard will guide you through creating a database, an engine, and loading data. See [Load data using a wizard](../loading-data/loading-data-wizard.md#load-data-using-a-wizard) for detailed information about the workflow and the available options in the wizard.
 
 Even though the **Load data** wizard creates a database and engine for you, the [**Create a Database**](./get-started-sql.md#create-a-database) and [**Create an Engine**](./get-started-sql.md#create-an-engine) sections in the [Use SQL to load data](./get-started-sql.md) guide contain useful information about billing for engine runtime and schema.

To use the **Load data** wizard, select the plus (+) icon. For detailed information about how to use the **Load data** wizard, see the [Load data](../loading-data/loading-data.md) guide.

## Run query, optimize, clean up, and export

<img src="../../assets/images/get_started_wizard_next.png" alt="After using the load data wizard, a simple workflow continues with running a query, optimization, cleaning up, and optionally exporting a dataset." width="700"/>
<BR>

After you have loaded your data in the wizard, the rest of the steps in getting started are the same as if you ran your workflow in SQL. You can use either the **Develop Space** in the **Firebolt Workspace** to enter SQL, or use the [Firebolt API](../query-data/using-the-api.md).

* For information about how to get started running a query, see [Run query](./get-started-sql.md#run-query).

* For information about how to get started optimizing your workflow, see [Optimize your workflow](get-started-sql#optimize-your-workflow).

* For information about how to get started cleaning up resources and data, see [Clean up resources](./get-started-sql#clean-up).
  
* For information on how to export your data, see [Export data](get-started-sql.md#export-data).

## Next steps

To continue learning about Firebolt's architecture, capabilities, using Firebolt after your trial period, and setting up your organization, see [Resources beyond getting started](./get-started-next.md).
