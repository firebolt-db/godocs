---
redirect_from:
  - /sql-reference/commands/attach-engine.html
layout: default
title: Engine commands
description: Reference for engine commands
nav_order: 4
parent: SQL commands
grand_parent: SQL reference
has_toc: false 
has_children: true
---

## Engine commands

Engine commands allow you to create, modify, start, stop, and manage Firebolt engines. Engines are compute resources that process queries and handle data ingestion. These commands help control engine availability, configuration, and resource allocation based on workload needs.  

Use the following to manage Firebolt engines:  

* [ALTER ENGINE]({% link sql_reference/commands/engines/alter-engine.md %}) &ndash; Modify an existing engine’s configuration, such as node type, cluster count, or concurrency settings.  
* [CREATE ENGINE]({% link sql_reference/commands/engines/create-engine.md %}) &ndash; Define and provision a new Firebolt engine with specific compute resources.  
* [DROP ENGINE]({% link sql_reference/commands/engines/drop-engine.md %}) &ndash; Remove an existing engine.  
* [START ENGINE]({% link sql_reference/commands/engines/start-engine.md %}) &ndash; Activate an engine to make it available for running queries.  
* [STOP ENGINE]({% link sql_reference/commands/engines/stop-engine.md %}) &ndash; Shut down an engine to free up resources when not in use.  
* [USE ENGINE]({% link sql_reference/commands/engines/use-engine.md %}) &ndash; Set an active engine for running queries in the current session.  

Each command provides fine-grained control over compute resources, ensuring that queries run efficiently while managing costs. Select a command from the list for syntax and usage details.