---
redirect_from:
  - /working-with-engines/working-with-engines-using-the-firebolt-manager.html
  - /working-with-engines/working-with-engines-using-ddl.html
  - /working-with-engines
layout: default
title: Work with engines
description: Learn how to create, modify and run Firebolt engines.
nav_order: 2
parent: Operate Engines
---
# Work with engines

You can create, run, modify, and scale Firebolt engines using either the **Firebolt Workspace** [user interface]({% link Guides/query-data/using-the-develop-workspace.md %}) (UI) or the [Firebolt API]({% link API-reference/index.md %}).  Learn how to perform key engine operations, including starting, stopping, resizing, and configuring auto-start/stop settings, using both the UI and SQL commands. Firebolt also allows the dynamic scaling of engines without stopping them.

{: .note}
 All the engine operations in this guide can be performed using a [system engine]({% link Guides/operate-engines/system-engine.md %}). 

Topics:

* [Create engines](#create-engines) &ndash; Learn how to create an engine.
* [Start or resume an engine](#start-or-resume-an-engine) &ndash; Learn how to start or resume an engine.
* [Stop an engine](#stop-an-engine) &ndash; Learn how to stop an engine either gracefully or immediately.
* [Resize engines](#resize-engines) &ndash; Learn how to scale engines up or down by adjusting the node type or number of nodes.
* [Concurrency auto-scaling](#concurrency-auto-scaling) &ndash; Learn how to enable auto-scaling for engines to automatically adjust the number of clusters based on workload.
* [Automatically start or stop an engine](#automatically-start-or-stop-an-engine) &ndash; Learn how to configure engines to start and stop automatically based on specific conditions.

## Create engines

You can create an engine using SQL scripts or through the UI in the **Develop Space**.

### Create an engine using the UI

1. Login to the [Firebolt Workspace](https://firebolt.go.firebolt.io/signup).
2. Select the **Develop Space** icon (</>) from the left navigation bar.
3. Select the red plus (+) button from the top of the left navigation bar.
4. Select **Create new engine**.<br>
    ![](../../assets/images/Engine_Create_Popup.png){: width="600" .centered} 
    <br /> 
5. Enter the engine name, type, and number of nodes.<br>
    ![](../../assets/images/Create_Engine_Dialog.png){: width="600" .centered}
     <br />  
6. Select **Create new engine**.

### Create an engine using the API 

To create an engine, use [CREATE ENGINE]({% link sql_reference/commands/engines/create-engine.md %}).

The following code example creates an engine with one cluster containing two nodes of type `S`:

```sql
CREATE ENGINE myengine;
```  

The following code example creates an engine with two nodes of type `M`:

```sql
CREATE ENGINE myengine WITH
TYPE="M" NODES=2 CLUSTERS=1;
```  

{: .note}
When creating an engine using the UI, Firebolt preserves the exact capitalization of the engine name. For example, an engine named **MyEngine** will retain its casing. To reference this engine in SQL commands, enclose the name in quotes: "MyEngine". For more information, visit the [Object Identifiers]({% link Reference/object-identifiers.md %}) page.

## Start or resume an engine
### Start an engine using the UI <br />
{: .fs-6}
1. In the **Engines** list, find the engine you want to start. 
2. Open the dropdown menu next to the engine and select **Start engine**. <br />
![](../../assets/images/Start_Engine.png){: width="600" .centered} <br /> 
3. The engine status changes to **Running** once started. 

### Start an engine using the API <br />
{: .fs-6}
To start your engine, use the [START ENGINE]({% link sql_reference/commands/engines/start-engine.md %}) command:

```sql
START ENGINE myengine;
```  

## Stop an engine
### Stop an engine using the UI <br />
{: .fs-6}
1. In the **Engines** list, find the engine you want to stop. 
2. Open the dropdown menu and select **Stop engine**.<br />
![](../../assets/images/Stop_Engine.png){: width="600" .centered}
 <br /> 

### Stop an engine using the API <br />
{: .fs-6}
To stop an engine, use the [STOP ENGINE]({% link sql_reference/commands/engines/stop-engine.md %}) command:

```sql
STOP ENGINE myengine;
```

To stop an engine immediately without waiting for running queries to complete, use:

```sql
STOP ENGINE myengine WITH TERMINATE=TRUE;
```

{: .note}
Stopping an engine clears its cache. Queries run after restarting will experience a cold start, potentially impacting performance until the cache is rebuilt. 

## Resize engines
### Scale engines up or down using the UI <br /> 
{: .fs-6}
1. In the **Engines** list, find the engine to modify. 
2. Open the dropdown menu and select the **More options** icon (<img src="../../assets/images/more_options_icon.png" alt="More options icon" width="7"/>). 
3. Choose **Modify engine**.<br />
![](../../assets/images/Alter_Engine_Popup.png){: width="600" .centered}<br />
4. Choose the new node type and select **Modify engine**.<br />
![](../../assets/images/Modify_Engine_Type.png){: width="600" .centered}
 <br /> 

### Scale engines up or down using the API <br />
{: .fs-6}
Use the [ALTER ENGINE]({% link sql_reference/commands/engines/alter-engine.md %}) command to change the node type:

```sql
ALTER ENGINE my_prod_engine SET TYPE = “M”;
```
The previous example updates all nodes in the engine to use the 'M' type. 

### Scale engines out or in using the UI
{: .fs-6}
1. In the **Engines** list, find the engine to modify. 
2. Open the dropdown menu, select the **More options** icon (<img src="../../assets/images/more_options_icon.png" alt="More options icon" width="7"/>), and choose **Modify engine**.<br /> 
![](../../assets/images/Alter_Engine_Popup.png){: width="600" .centered}<br /> 
3. Adjust the number of nodes using the (-) and (+) buttons. 

### Scale engines out or in using the API
 {: .fs-6}
 Use the [ALTER ENGINE]({% link sql_reference/commands/engines/alter-engine.md %}) command to change the number of nodes:

```sql
ALTER ENGINE my_prod_engine SET NODES = 3;
```

The previous example updates the engine so that it uses three nodes. 

## Concurrency auto-scaling

You can use the `MIN_CLUSTERS` and `MAX_CLUSTERS` parameters to enable auto-scaling and allow the engine to adjust the number of clusters based on workload. Firebolt scales the clusters between the defined minimum and maximum based on engine CPU usage, time in the queue, and other factors that vary with demand. Auto-scaling helps your engine adapt to fluctuating workloads, improving performance, minimizing delays during high demand, avoiding bottlenecks, ensuring consistent query response times, and optimizing resource utilization for a more cost-effective solution.

To use auto-scale, do the following:
1. Create an engine with `MIN_CLUSTERS` set to a value and `MAX_CLUSTERS` set to a value higher than `MIN_CLUSTERS` as shown in the following code example:

    ```sql   
    CREATE ENGINE your_engine with MIN_CLUSTERS = 1 MAX_CLUSTERS = 2;
    ```
In the previous code example, If `MIN_CLUSTERS` has the same value as `MAX_CLUSTERS`, auto-scaling is not enabled.

2. Check the `information_schema.engines` view to check how many clusters are being used by your engine. The following code example returns the number of `CLUSTERS`, `MIN_CLUSTERS`, and `MAX_CLUSTERS` from the specified engine:

    ```sql
    SELECT CLUSTERS, MIN_CLUSTERS, MAX_CLUSTERS 
    FROM information_schema.engines WHERE engine_name = 'your_engine'
    ```

    You can also select the **Engine monitoring** tab at the bottom of the **SQL script editor** in the **Develop Workspace** as shown in the following image:

    <img src="../../assets/images/icon-engine-monitoring.png" alt="Icon showing the engine monitoring tab selected in the Firebolt Develop Workspace." width="40%">

    The **Engine monitoring** tab displays CPU, memory, and disk use, cache reads, number of running and suspended queries, and spilled bytes. 

3. Test auto-scaling by running a query that overloads a single cluster, then check `information_schema.engines` to observe the change in the `CLUSTERS` value. You can use any query to test this functionality as long as it can overload the engine. The following example is one such query, but you can use any query that causes the engine to overload.

    1. In the **Develop Space**, run the following example query **in two separate tabs simultaneously**.  
       The following code example calculates the maximum product of `a.x` and `b.y` after casting them to `BIGINT`, and the total count of joined rows from two generated series of numbers ranging from 1 to 1,000,000:
       ```sql
       SELECT MAX(a.x::bigint * b.y::bigint), COUNT(*) 
       FROM GENERATE_SERIES(1, 1000000) AS a(x) 
       JOIN GENERATE_SERIES(1, 1000000) AS b(y) ON TRUE;
       ```
    2. After about a minute, enter the code example in step 1 in a new tab. The query should return the numbers of `CLUSTERS` as `2` as shown in the following table:

       | clusters | min_clusters | max_clusters |
       |----------|--------------|--------------|
       | 2        | 1            | 2            |

    3. Stop the engine to stop resource consumption. These queries can run for a very long time and prevent the engine from stopping automatically. The following code example stops an engine without waiting for running queries to finish:

    ```sql
    STOP ENGINE your_engine WITH TERMINATE=true
    ```


{: .note}
If you are using Firebolt in preview mode, you can only use a single cluster for your engines. If you want to try using multi-cluster engines, contact [Firebolt support](mailto:support@firebolt.io). Additionally, when scaling an engine, both the old and new compute resources may be active at the same time for a period. This simultaneous operation can result in higher consumption of Firebolt Units ([FBUs]({% link Overview/engine-consumption.md %})). 

## Automatically start or stop an engine
You can configure an engine to start automatically after creation and to stop after a set idle time. 

### Configure automatic start/stop using the UI
{: .fs-6}
1. In the **Create new engine** menu, open **Advanced Settings**. 
2. Disable **Start engine immediately** to prevent the engine from starting upon creation.<br />
![](../../assets/images/Engine_Initially_Stopped.png){: width="600" .centered}<br />
1. To configure automatic stopping, enable **Automatically stop engine** and set your idle timeout. The default is 20 minutes. Toggle the button off to disable auto-stop. <br /> 
![](../../assets/images/Engine_Auto_Stop.png){: width="600" .centered} <br /> 

### Configure automatic start/stop using the API
 {: .fs-6}
 Use the [CREATE ENGINE]({% link sql_reference/commands/engines/create-engine.md %}) command to set auto-start and auto-stop options:
 
 ```sql
CREATE ENGINE my_prod_engine WITH 
INITIALLY_STOPPED = true AUTO_STOP = 10;
```

The previous example creates an engine that remains stopped after creation and auto-stops after 10 minutes of inactivity. 

To modify the auto-stop feature later, use the [ALTER ENGINE]({% link sql_reference/commands/engines/alter-engine.md %}) command: 

```sql
ALTER ENGINE my_prod_engine SET AUTO_STOP = 30;
```

{: .note}
The `INITIALLY_STOPPED` function can only be set during engine creation and cannot be modified afterward. 

















