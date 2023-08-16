---
layout: default
title: SQL commands
description: Reference for SQL commands and operators in Firebolt.
parent: SQL reference
has_children: true
has_toc: false
---

# SQL commands

Use the alphabetical list in the navigation pane to find the syntax for commands that you already know.

Use the functional list below to find commands for a specific task area that you're working in.

* [Engines](#engines)  
  Start, stop, and manage Firebolt engines.

* [Data management](#data-ingest-and-movement)  
  Move data between your data lake and Firebolt and between Firebolt resources.

 

* [Data ](#database-objects)  
  Data Definition Language. Create, alter, drop, and otherwise manage objects like databases, tables, and views in your Firebolt account.

* [Access control]
* [Data manipulation](#data-manipulation)  
  Data Manipulation Language. Update or delete data from tables in your Firebolt account. 

* [Queries](#queries-and-query-optimization)  
  Analyze data with `SELECT`. Tune and optimize query performance with other commands.

* [Metadata](#metadata)  
  Query the Firebolt information schema for metadata related to its objects and resources.


## Engines

* [ALTER ENGINE](./engines/alter-engine.md)
* [ATTACH ENGINE](./engines/attach-engine.md)
* [CREATE ENGINE](./engines/create-engine.md)
* [DROP ENGINE](./engines/drop-engine.md)
* [SHOW CACHE](./engines/show-cache.md)
* [SHOW ENGINES](./engines/show-engines.md)
* [START ENGINE](./engines/start-engine.md)
* [STOP ENGINE](./engines/stop-engine.md)

## Data ingest and movement

* [ALTER TABLE...DROP PARTITION](./data-ingest/alter-table-drop-partition.md)
* [COPY TO](./data-ingest/copy-to.md)
* [CREATE EXTERNAL TABLE](./data-ingest/create-external-table.md)
* [INSERT INTO](./data-ingest/insert-into.md)

## Database objects

* [ALTER ACCOUNT](./database-objects/alter-account.md)
* [ALTER DATABASE](./database-objects/alter-database.md)
* [ALTER LOGIN](./database-objects/alter-login.md)
* [ALTER NETWORK POLICY](./database-objects/alter-network-policy.md)
* [ALTER SERVICE ACCOUNT](./database-objects/alter-service-account.md)
* [ALTER USER](./database-objects/alter-user.md)
* [CREATE ACCOUNT](./database-objects/create-account.md)
* [CREATE AGGREGATING INDEX](./database-objects/create-aggregating-index.md)
* [CREATE DATABASE](./database-objects/create-database.md)
* [CREATE FACT or DIMENSION TABLE](./database-objects/create-fact-dimension-table.md)
* [CREATE LOGIN](./database-objects/create-login.md)
* [CREATE NETWORK POLICY](./database-objects/create-network-policy.md)
* [CREATE ROLE](./database-objects/create-role.md)
* [CREATE SERVICE ACCOUNT](./database-objects/create-service-account.md)
* [CREATE USER](./database-objects/create-user.md)
* [CREATE VIEW](./database-objects/create-view.md)
* [DROP ACCOUNT](./database-objects/drop-account.md)
* [DROP DATABASE](./database-objects/drop-database.md)
* [DROP INDEX](./database-objects/drop-index.md)
* [DROP LOGIN](./database-objects/drop-login.md)
* [DROP NETWORK POLICY](./database-objects/drop-network-policy.md)
* [DROP ROLE](./database-objects/drop-role.md)
* [DROP SERVICE ACCOUNT](./database-objects/drop-service-account.md)
* [DROP TABLE](./database-objects/drop-table.md)
* [DROP USER](./database-objects/drop-user.md)
* [DROP VIEW](./database-objects/drop-view.md)
* [GRANT](./database-objects/grant.md)
* [REVOKE](./database-objects/revoke.md)
* [TRUNCATE TABLE](./database-objects/truncate-table.md)

## Data manipulation

* [DELETE](./data-manipulation/delete.md)
* [UPDATE](./data-manipulation/update.md)
* [VACUUM](./data-manipulation/vacuum.md)

## Queries and query optimization

* [EXPLAIN](./query-optimization/explain.md)
* [SELECT](./query-optimization/select.md)


## Metadata

* [DESCRIBE](./metadata/describe.md)
* [SHOW COLUMNS](./metadata/show-columns.md)
* [SHOW DATABASES](./metadata/show-databases.md)
* [SHOW INDEXES](./metadata/show-indexes.md)
* [SHOW TABLES](./metadata/show-tables.md)
* [SHOW VIEWS](./metadata/show-views.md)
