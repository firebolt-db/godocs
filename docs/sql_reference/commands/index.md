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

* [Access control](#access-control)

* [Data definition](#database-objects)  
  Data Definition Language. Create, alter, drop, and otherwise manage objects like databases, tables, and views in your Firebolt account.

* [Data management](#data-ingest-and-movement)  
  Move data between your data lake and Firebolt and between Firebolt resources.

* [Engines](#engines)  
  Start, stop, and manage Firebolt engines.

* [Metadata](#metadata)  
  Query the Firebolt information schema for metadata related to its objects and resources.
  
* [Queries](#queries-and-query-optimization)  
  Analyze data with `SELECT`. Tune and optimize query performance with other commands.

## Access control

* [ALTER ACCOUNT](./access-control/alter-account.md)
* [ALTER LOGIN](./access-control/alter-login.md)
* [ALTER NETWORK POLICY](./access-controls/alter-network-policy.md)
* [ALTER SERVICE ACCOUNT](./access-control/alter-service-account.md)
* [ALTER USER](./access-control/alter-user.md)
* [CREATE ACCOUNT](./access-control/create-account.md)
* [CREATE LOGIN](./access-control/create-login.md)
* [CREATE NETWORK POLICY](./access-control/create-network-policy.md)
* [CREATE ROLE](./access-control/create-role.md)
* [CREATE SERVICE ACCOUNT](./access-control/create-service-account.md)
* [CREATE USER](./access-control/create-user.md)
* [DROP ACCOUNT](./access-controls/drop-account.md)
* [DROP LOGIN](./access-control/drop-login.md)
* [DROP NETWORK POLICY](./access-control/drop-network-policy.md)
* [DROP ROLE](./access-control/drop-role.md)
* [DROP SERVICE ACCOUNT](./access-control/drop-service-account.md)
* [DROP USER](./access-control/drop-user.md)
* [GRANT](./access-control/grant.md)
* [REVOKE](./access-control/revoke.md)

## Data definition

* [ALTER DATABASE](./data-definition/alter-database.md)
* [CREATE AGGREGATING INDEX](./data-definition/create-aggregating-index.md)
* [CREATE DATABASE](./data-definition/create-database.md)
* [CREATE FACT or DIMENSION TABLE](./data-definition/create-fact-dimension-table.md)
* [CREATE VIEW](./data-definition/create-view.md)
* [DROP DATABASE](./data-definition/drop-database.md)
* [DROP INDEX](./data-definition/drop-index.md)
* [DROP TABLE](./data-definition/drop-table.md)
* [DROP VIEW](./data-definition/drop-view.md)
* [TRUNCATE TABLE](./data-definition/truncate-table.md)

## Data management

* [ALTER TABLE...DROP PARTITION](./data-management/alter-table-drop-partition.md)
* [COPY TO](./data-management/copy-to.md)
* [CREATE EXTERNAL TABLE](./data-management/create-external-table.md)
* [DELETE](./data-management/delete.md)
* [INSERT INTO](./data-management/insert-into.md)
* [UPDATE](./data-management/update.md)
* [VACUUM](./data-management/vacuum.md)

## Engines

* [ALTER ENGINE](./engines/alter-engine.md)
* [ATTACH ENGINE](./engines/attach-engine.md)
* [CREATE ENGINE](./engines/create-engine.md)
* [DROP ENGINE](./engines/drop-engine.md)
* [SHOW CACHE](./engines/show-cache.md)
* [SHOW ENGINES](./engines/show-engines.md)
* [START ENGINE](./engines/start-engine.md)
* [STOP ENGINE](./engines/stop-engine.md)

## Metadata

* [DESCRIBE](./metadata/describe.md)
* [SHOW COLUMNS](./metadata/show-columns.md)
* [SHOW DATABASES](./metadata/show-databases.md)
* [SHOW INDEXES](./metadata/show-indexes.md)
* [SHOW TABLES](./metadata/show-tables.md)
* [SHOW VIEWS](./metadata/show-views.md)

## Queries

* [EXPLAIN](./queries/explain.md)
* [SELECT](./queries/select.md)
