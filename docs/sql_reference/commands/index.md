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

* [Queries](#queries-and-query-optimization)  
  Analyze data with `SELECT`. Tune and optimize query performance with other commands.

* [Data management](#data-ingest-and-movement)  
  Move data between your data lake and Firebolt and between Firebolt resources.

* [Data definition](#database-objects)  
  Data definition language. Create, alter, drop, and otherwise manage objects like databases, tables, and views in your Firebolt account.

* [Engines](#engines)  
  Start, stop, and manage Firebolt engines.

* [Metadata](#metadata)  
  Query the Firebolt information schema for metadata related to its objects and resources.

* [Access control](#access-control)   
  Access control language. Create, alter and drop, and otherwise manage users, logins, service accounts and roles. 
  
## Queries

* [EXPLAIN](./queries/explain.md)
* [SELECT](./queries/select.md)

## Data management

* [COPY TO](./data-management/copy-to.md)
* [CREATE EXTERNAL TABLE](./data-management/create-external-table.md)
* [DELETE](./data-management/delete.md)
* [INSERT INTO](./data-management/insert-into.md)
* [UPDATE](./data-management/update.md)
* [VACUUM](./data-management/vacuum.md)

## Data definition

* [ALTER ACCOUNT](./data-definition/alter-account.md)
* [ALTER DATABASE](./data-definition/alter-database.md)
* [ALTER NETWORK POLICY](./data-definition/alter-network-policy.md)
* [ALTER TABLE](./data-definition/alter-table.md)
* [CREATE ACCOUNT](./data-definition/create-account.md)
* [CREATE AGGREGATING INDEX](./data-definition/create-aggregating-index.md)
* [CREATE DATABASE](./data-definition/create-database.md)
* [CREATE FACT or DIMENSION TABLE](./data-definition/create-fact-dimension-table.md)
* [CREATE NETWORK POLICY](./data-definition/create-network-policy.md)
* [CREATE VIEW](./data-definition/create-view.md)
* [DROP ACCOUNT](./data-definition/drop-account.md)
* [DROP DATABASE](./data-definition/drop-database.md)
* [DROP INDEX](./data-definition/drop-index.md)
* [DROP NETWORK POLICY](./data-definition/drop-network-policy.md)
* [DROP TABLE](./data-definition/drop-table.md)
* [DROP VIEW](./data-definition/drop-view.md)
* [TRUNCATE TABLE](./data-definition/truncate-table.md)

## Engines

* [ALTER ENGINE](./engines/alter-engine.md)
* [ATTACH ENGINE](./engines/attach-engine.md)
* [CREATE ENGINE](./engines/create-engine.md)
* [DROP ENGINE](./engines/drop-engine.md)
* [START ENGINE](./engines/start-engine.md)
* [STOP ENGINE](./engines/stop-engine.md)

## Metadata

* [DESCRIBE](./metadata/describe.md)
* [SHOW CACHE](./metadata/show-cache.md)
* [SHOW COLUMNS](./metadata/show-columns.md)
* [SHOW DATABASES](./metadata/show-databases.md)
* [SHOW ENGINES](./metadata/show-engines.md)
* [SHOW INDEXES](./metadata/show-indexes.md)
* [SHOW TABLES](./metadata/show-tables.md)
* [SHOW VIEWS](./metadata/show-views.md)

## Access control

* [ALTER LOGIN](./access-control/alter-login.md)
* [ALTER SERVICE ACCOUNT](./access-control/alter-service-account.md)
* [ALTER USER](./access-control/alter-user.md)
* [CREATE LOGIN](./access-control/create-login.md)
* [CREATE ROLE](./access-control/create-role.md)
* [CREATE SERVICE ACCOUNT](./access-control/create-service-account.md)
* [CREATE USER](./access-control/create-user.md)
* [DROP LOGIN](./access-control/drop-login.md)
* [DROP ROLE](./access-control/drop-role.md)
* [DROP SERVICE ACCOUNT](./access-control/drop-service-account.md)
* [DROP USER](./access-control/drop-user.md)
* [GRANT](./access-control/grant.md)
* [REVOKE](./access-control/revoke.md)