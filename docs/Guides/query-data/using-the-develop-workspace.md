---
redirect_from:
  - /using-the-sql-workspace/using-the-sql-workspace.html
  - /using-the-sql-workspace/keyboard-shortcuts-for-sql-workspace.html
layout: default
title: Use the Develop Space
description: Learn how to navigate and use the develop space to work with your Firebolt database.
parent: Query data
has_children: true
nav_order: 1
---

# Use the Develop Space
{: .no_toc}

The **Firebolt Workspace** has a **Develop Space** that you can use to edit and run SQL scripts, as well as view query results.

* Topic ToC
{:toc}

## Get started with the Develop Space

To get started, [sign-in](https://firebolt.go.firebolt.io/) to your Firebolt account or register using the following steps: 

1. [Sign-up](https://go.firebolt.io/signup) with Firebolt. Fill in your email, name, choose a password, and select **Get started**.
2. Firebolt will send a confirmation to the address that you provided. To complete your registration, select **Verify** in the email to take you to Firebolt’s [login page](https://go.firebolt.io/login).
3. Enter in your organization name, email, and password and select **Log In**. 

### Navigating the Develop Space
{: .no_toc}
You can launch the Develop Space for a database by clicking the **Develop** icon (**</>**) from the left navigation pane. 

#### Using the UI
{: .no_toc}

The **Develop Space** is organized into three panels:

1. [Explore panel](#using-the-explore-panel): Panel on the **left** that displays available databases, engines, and security users and roles. 
2. [Document editor](#using-the-document-editor): Panel in the **center** that provides tools to edit, run, and manage your SQL scripts organized as tabs.
3. [Results panel](#using-the-results-panel): Panel at the **bottom** that shows results, execution statistics, engine monitoring information, and query history.

##### Using the Explore panel
{: .no_toc}
The Explore panel provides quick access to key tasks in Firebolt, including loading data, creating databases, and managing engines. 

**Load data**
1. Create an engine or select an existing engine for ingestion.
2. Next, set up an AWS connection by providing the Amazon S3 storage URL, selecting an authentication method, and inputting the AWS Key ID as well as the AWS Secret Key. Alternatively, you can also select the option to use the **Firebolt Playground Bucket** to load sample data. 
3. Then, specify the data you want to ingest by selecting the file name. 
4. Specify the database location for your ingested data using the dropdown menu. 
5. Create a new table by inputting a new table name. 
6. Select the file format and use the toggle to turn error handling on or off. If turned off, fill out the following fields: Error file, Authentication method, AWS Key ID, AWS Secret Key, and Max errors per file. 
7. Adjust the schema by previewing and selecting the column names you'd like to be included in the new table. 
8. Finally, review the chosen settings and configurations. 
9. Then, **Run ingestion**. 

**Create a database**
1. If this is your first time creating a database or you'd like to create a new database, select the red (**+**) icon. 
    - Select **Create new database** from the dropdown menu. 
    - Input your database name and optionally, a description. 
    - Select **Create new database**. This will add your new database to the Explore panel on the left. 

If you have previously worked with a database, the space for the database that you last worked with will open automatically and the database will be selected from the list. To switch to a different database's space, choose from the database list on the left navigation panel, below the search bar. 

**Create a new engine**
1. Enter in your new engine name. 
2. Select a node type, small or medium. 
3. Set your number of nodes between 1 and 128. 
4. Set your number of clusters up to 10. 
5. Use the advanced settings to set other preferences for your engine. 
6. Select **Create new engine**. This will add your engine to the Explore panel on the left. 

##### Using the Document editor
{: .no_toc}
The document editor uses tabs at the top of the center panel to help you organize your SQL scripts. You can switch tabs by selecting the script you'd like to work with and run them. You can store multiple query statements on the same tab. To terminate a statement, use a semi-colon (`;`). 

**Select your database and engine**                             
At the top of the Document editor, a couple dropdown menus allow you to select your database and associated engine:
* **Database selection**(<img src="../../assets/images/develop-space-database.png" alt="develop space select database image" width="20"/>): Choose the database for your SQL statements.
* **Engine selection**(<img src="../../assets/images/develop-space-select-engine.png" alt="develop space select engine image" width="25"/>): Choose the running engine or select to start an engine for running queries.

**Running scripts and generating query plans**                          
Use the red **Run** button in the top-right corner to run all queries or selected snippets.
You can use the dropdown menu next to **Run** to:
  * **Run query**: Executes the SQL statements.
  * **Generate query plan**: Generates and displays the query execution plan instead of running the query.

**Using auto-complete**                                                         
As you enter your code in a script tab, Firebolt suggests keywords and object names from the chosen database. Press the `tab` key to add the first suggestion in the list to your script, or use arrow keys to select a different item from the list and then press the `tab` key.

##### Using the Results panel
{: .no_toc}
The **Results panel** displays results in the Develop Space below the document editor, after running your SQL scripts or queries. It provides detailed information through the following tabs: 
* Results
* Statistics
* Engine monitoring
* Query history

**Results tab**                                           
The **`Results`** tab displays the data returned from your SQL query. Each executed query populates this tab with a result table showing returned values for each column defined in your query.

**Statistics tab**                                                        
The **`Statistics`** tab provides detailed statistics for each query you run. Information includes:
* No: The sequential order of executed queries.
* Statement: The SQL query that was run. 
* Status: The query status (Success, Error, or Canceled). 
* Duration: The run time of your query. 
* Rows: The number of rows returned. 
* Scanned: The amount of data scanned by your query. 
* Rows per sec: Query processing speed. 

Statements are listed with the earliest executed queries at the bottom. 

**Query Profile tab**                                               
The **`Query Profile`** tab provides a visual query plan, illustrating how Firebolt executes your query. Each step is shown in a flowchart format, enabling you to inspect query operations and data flow visually. 

**Engine monitoring tab**                                             
The **`Engine Monitoring`** tab provides real-time metrics on the resource utilization of your query execution engine, such as CPU and memory usage.

If the selected engine does not support engine monitoring (for example, the System engine), a message will indicate this, prompting you to select another engine for monitoring.

**Query history tab**                                       
The **`Query History`** tab displays past queries along with their status and run details. This helps in reviewing historical queries for debugging or optimization purposes.

If the selected engine does not provide query history (such as the System engine), a message will indicate that you should select another engine to view the query history.

**Exporting results to a local hard drive**                                                    
You can export up to 10,000 rows of query results to your local hard drive after you run a query.
1. Select the vertical ellipsis (**⋮**) in the Results panel. 
2. Choose **Export table as CSV** or **Export table as JSON** from the dropdown menu.        

Firebolt downloads the selected file type to your browser's default download location. 

## Managing scripts

* [Format a script](#format-a-script)
* [Renaming a script](#renaming-a-script)
* [Using script templates](#using-script-templates)
* [Delete a script](#delete-a-script)
* [Run a script and view results](#run-a-script-and-view-results)

Choose the vertical ellipsis (**⋮**) next to the script name in the left pane to [format](#format-a-script), [rename](#renaming-a-script),

##### Format a script
{: .no_toc}
You can format your script by selecting **Format script**. 

##### Renaming a script
{: .no_toc}
To rename your script: 
1. Choose the vertical ellipsis (**⋮**) next to the script name in the left pane.
2. Choose **Rename script**. 
3. Enter a new name.
4. Then, select **ENTER**.

##### Using script templates
{: .no_toc}                     
Script templates simplify common tasks such as importing data or creating tables. To insert a template:
1. Select the vertical ellipsis (**⋮**) next to your script tab name.
2. Select **Insert SQL template**.
3. Choose a template:
   * **Query history**: Inserts code to query historical executions.
   * **Import data**: Creates external table definitions for data ingestion.
   * **New fact table**: Inserts a template for creating a fact table.

##### Delete a script     
{: .no_toc}
If you'd like to delete a script, select **Delete script** in the dropdown menu or select the **X** icon next to the script name. 

##### Run a script and view results
{: .no_toc}
At the top of each script tab, you can choose **Run** to run your SQL statements. SQL statements can only run on running engines. If an engine isn't running, you can select it from the list and then choose the **Start** button for that engine. For more information about engines, see [Operate engines]({% link Guides/operate-engines/operate-engines.md %}).

You can run all statements in a script or select snippets of SQL to run.

**Running all SQL statements in a script**                              
Position the cursor anywhere in the script editor and then choose **Run**. All SQL statements must be terminated by a semi-colon (`;`) or an error occurs.

**Running a snippet of SQL as a statement**                                       
Select the SQL code you want to run as a statement and then choose **Run**. Behind the scenes, Firebolt automatically appends a semi-colon to the selected SQL code so it can run as a statement.

## Switching between light and dark mode
Switch themes by selecting the toggle (<img src="../../assets/images/dark-mode-toggle.png" alt="toggle button for dark and light mode" width="15"/>) at the bottom-left corner of the workspace.

## Resource center
The Resource Center provides quick access to essential Firebolt resources. Select the **Firebolt icon**(<img src="../../assets/images/firebolt-icon-transparent.png" alt="Firebolt icon transparent" width="22"/>) in the bottom-right corner of the Results panel to open the Resource Center, which includes:
* **Get started with Firebolt**: Quick-start guide for new users.
* **Knowledge Center**: Central hub for comprehensive Firebolt information.
* **Overview**: Explains core Firebolt concepts.
* **Documentation**: Provides access to detailed Firebolt documentation.
* **Release notes**: Summarizes recent updates and features.
* **Announcements**: Updates and what's new in Firebolt.
* **Search**: Enables you to search across documentation and knowledge resources.

## Keyboard shortcuts for the Develop Space

* [Query operations](#query-operations)
* [Script management](#script-management)
* [Search functionality](#search-functionality)
* [Editing text](#editing-text)

**Tip:** Use the **Keyboard shortcuts panel** (`Ctrl + Shift + ?`) to quickly view available shortcuts directly within the Develop Space.

### Query operations
{: .no_toc}

| Function                  | Windows & Linux Shortcut | Mac Shortcut      |
|:--------------------------|:-------------------------|:------------------|
| **Run** the **currently selected query**.         | Ctrl + Enter             | ⌘ + Enter         |
| **Run all** queries in the current script. | Ctrl + Shift + Enter     | ⌘ + Shift + Enter |
| **Toggle** expanding or collapsing **query results**.   | Ctrl + Alt + E           | ⌘ + Option + E    |

### Script management 
{: .no_toc}

| Function                     | Windows & Linux Shortcut | Mac Shortcut   |
|:-----------------------------|:-------------------------|:---------------|
| **Create** a new script.                   | Ctrl + Alt + N           | ⌘ + Option + N |
| **Jump** to a **previous** script.     | Ctrl + Alt + [           | ⌘ + Option + [ |
| **Jump** to the **next** script.          | Ctrl + Alt + ]           | ⌘ + Option + ] |
| **Close** the **current** script.         | Ctrl + Alt + X           | ⌘ + Option + X |
| **Close all** scripts.            | Ctrl + Alt + G           | ⌘ + Option + G |
| **Close all but** the **current** script. | Ctrl + Alt + O           | ⌘ + Option + O |

### Search functionality
{: .no_toc}

| Function          | Windows & Linux Shortcut | Mac Shortcut       |
|:------------------|:-------------------------|:-------------------|
| **Open** a **search** panel. | Ctrl + F                 | ⌘ + F              |
| **Find** the **next search result**.        | F3                       | F3                 |
| **Find** the **previous search result**.    | Shift + F3               | Shift + F3         |

### Editing text
{: .no_toc}

| Function             | Windows & Linux Shortcut  | Mac Shortcut                |
|:---------------------|:--------------------------|:----------------------------|
| **Toggle** adding or removing a **comment marker** for the current line. | Ctrl + /                  | Cmd + /                     |
| **Toggle** adding or removing a **block comment marker** around a block of code or text. | Shift + Alt + A           | Shift + Option + A          |
| **Automatically organize and indent** code for readability.          | Ctrl + Alt + F            | ⌘ + Option + F              |
| **Copy** the selected lines and paste them directly **above** the original.        | Alt + Shift + Up arrow    | Shift + Option + Up arrow   |
| **Move** the selected lines and paste them directly **above** the original without creating a duplicate.        | Alt + Up arrow            | Option + Up arrow           |
| **Copy** the selected lines and paste them directly **below** the original.      | Alt + Shift + Down arrow  | Shift + Option + Down arrow |
| **Move** the selected lines and paste them directly **below** the original without creating a duplicate.      | Alt + Down arrow          | Option + Down arrow         |
| **Select text** to the **left** of the cursor.  | Alt + Shift + Left arrow  | Ctrl + Shift + Left arrow   |
| **Select text** to the **right** of the cursor. | Alt + Shift + Right arrow | Ctrl + Shift + Right arrow  |
| **Select** the **entire line**.   | Alt + L                   | Ctrl + L                    |
| **Decrease** the **indentation level** of the current or selected lines.          | Ctrl + [                  | Cmd + [                     |
| **Increase** the **indentation level** of the current or selected lines.          | Ctrl + ]                  | Cmd + ]                     |
| **Delete** the current or selected **lines**.          | Shift + Ctrl + K          | Shift + Cmd + K             |
