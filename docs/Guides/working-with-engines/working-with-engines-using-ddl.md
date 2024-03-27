---
layout: default
title: Work with engines using DDL
description: Learn how to create, modify and run Firebolt engines.
nav_order: 2
parent: Work with engines
grand_parent: Guides
---


# Create Engines
**UI** <br /> {. .fs-8}
1. Choose "Engines" <br />
  ![](../../assets/images/Engines_Section.png){: width="600" .centered}
 <br /> 

2. Click the “+” sign and choose “Create new engine” <br />
 ![](../../assets/images/Engine_Create_Popup.png){: width="600" .centered}
 <br /> 

3. Enter the engine name, type and number of nodes and click the "Create new engine" button <br />
![](../../assets/images/Create_Engine_Dialog.png){: width="600" .centered}
 <br />  

**API** <br /> {. fs-8}
Use the [CREATE ENGINE](../../sql_reference/commands/engines/create-engine.md) command. <br />

The following statement creates an engine with one cluster that has two nodes of type 'S'.
```sql
CREATE ENGINE MyEngine;
```  

The following statement creates an engine with one cluster that has two nodes of type 'M'.

```sql
CREATE ENGINE MyEngine WITH
TYPE='M' NODES=2 CLUSTERS=1;
```  

For more details with a full list of attributes and more example, see the [CREATE ENGINE](../../sql_reference/commands/engines/create-engine.md) command.
<br />

# Starting an Engine or Resuming a Stopped Engine
**UI** <br />
1. From the list of engines, next to the engine that you want to start or resume, click the drop-down and select **Start engine**. <br />
![](../../assets/images/Start_Engine.png){: width="600" .centered}
 <br /> 
Once the engine is started, the engine state will change to "Running".

**API** <br />
Use the [START ENGINE](../../sql_reference/commands/engines/start-engine.md) command as show below:

```sql
START ENGINE MyEngine;
```  
<br />

# Stopping an Engine
**UI** <br />
From the engines list, next to the engine that you want to stop, click the drop-down and select "Stop engine".
![](../../assets/images/Stop_Engine.png){: width="600" .centered}
 <br /> 

**API** <br />
Use the [STOP ENGINE](../../sql_reference/commands/engines/stop-engine.md) command as shown below:

```sql
STOP ENGINE MyEngine;
```  
Note that stopping an engine results in emptying the cache. So, any queries after starting an engine that was previously stopped will have a cold start, resulting in some performance impact till the engine is warmed up again. 
<br />

# Resizing an Engine
**Scaling Up or Scaling Down** <br />
You can dynamically scale up or scale down an engine by modifying the “TYPE” attribute of your engine.
**UI** <br />
   1. For the engine that you want to modify, hover next to the drop-down and click the ellipsis (three vertical dots). Then select “Modify engine".
![](../../assets/images/Alter_Engine_Popup.png){: width="600" .centered}
 <br /> 

    2. Choose the appropriate Node type that you want and click the “Modify engine” button.
    ![](../../assets/images/Modify_Engine_Type.png){: width="600" .centered}
 <br /> 

**API** <br />
Use the [ALTER ENGINE](../../sql_reference/commands/engines/alter-engine.md) command, specifying the new node type (TYPE)  you want to use with your engine. For example, to scale up an engine from ‘S’ to ‘M’, you can use the following command:

```sql
ALTER ENGINE my_prod_engine SET TYPE = “M”;
```

Note that nodes across all the clusters in the engine will be switched to using the ‘M’ type node after the successful execution of the above command.


**Scaling Out or Scaling In** <br />
You can dynamically scale out or scale in an engine by modifying the “NODES” attribute of your engine. <br />
**UI** <br />
 1. For the engine that you want to modify, hover next to the drop-down and click the ellipsis (three vertical dots). Then select “Modify engine”.
![](../../assets/images/Alter_Engine_Popup.png){: width="600" .centered}
 <br /> 

 2. Choose the appropriate “Number of nodes”  that you want and click “Modify engine”
![](../../assets/images/Scale_Out_Engine.png){: width="600" .centered}
 <br /> 

 **API** <br />
 Use the [ALTER ENGINE](../../sql_reference/commands/engines/alter-engine.md) command, specifying the number of nodes (NODES) you want to use with your engine. For example, to scale out an engine from two nodes to three nodes, you can use the following command: 

```sql
ALTER ENGINE my_prod_engine SET NODES = 3;
```

Note that all the clusters in the engine will have three nodes after the above command completes successfully.














