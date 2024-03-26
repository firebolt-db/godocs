---
layout: default
title: Work with engines using DDL
description: Learn how to create, modify and run Firebolt engines.
nav_order: 2
parent: Work with engines
grand_parent: Guides
---


# Create Engines
## UI
1. Choose "Engines"
  ![](../../assets/images/Engines_Section.png){: width="600" .centered}
 <br /> 

2. Click the “+” sign and choose “Create new engine”
 ![](../../assets/images/Engine_Create_Popup.png){: width="600" .centered}
 <br /> 

3. Enter the engine name, type and number of nodes
![](../../assets/images/Create_Engine_Dialog.png){: width="600" .centered}
 <br />  

## API <br />
Use the [CREATE ENGINE](../../sql_reference/commands/engines/create-engine.md) command.

```sql
CREATE ENGINE MyEngine;
```  
The statement creates an engine with one cluster that has two nodes of type 'S'

```sql
CREATE ENGINE MyEngine WITH
TYPE='M' NODES=2 CLUSTERS=1;
```  
The statement creates an engine with one cluster that has two nodes of type 'M'.

For more details with a full list of attributes and more example, see the [CREATE ENGINE](../../sql_reference/commands/engines/create-engine.md) command.




