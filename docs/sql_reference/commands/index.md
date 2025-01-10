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

* [Queries](#queries)  
  Analyze data with `SELECT`. Tune and optimize query performance with other commands.

* [Data management](#data-management)  
  Move data between your data lake and Firebolt and between Firebolt resources.

* [Data definition](#data-definition)  
  Data definition language. Create, alter, drop, and otherwise manage objects like databases, tables, and views in your Firebolt account.

* [Engines](#engines)  
  Start, stop, and manage Firebolt engines.

* [Metadata](#metadata)  
  Query the Firebolt information schema for metadata related to its objects and resources.

* [Access control](#access-control)   
  Access control language. Create, alter and drop, and otherwise manage users, logins, service accounts and roles. 
  
## Queries

* [EXPLAIN](./queries/explain.md)
* [RECOMMEND DDL](./queries/recommend_ddl.md)
* [SELECT](./queries/select.md)

## Data management

* [COPY FROM](./data-management/copy-from.md)
* [COPY TO](./data-management/copy-to.md)
* [DELETE](./data-management/delete.md)
* [INSERT](./data-management/insert.md)
* [TRUNCATE TABLE](./data-management/truncate-table.md)
* [UPDATE](./data-management/update.md)
* [VACUUM](./data-management/vacuum.md)

## Data definition

* [ALTER ACCOUNT](./data-definition/alter-account.md)
* [ALTER DATABASE](./data-definition/alter-database.md)
* [ALTER TABLE](./data-definition/alter-table.md)
* [CREATE ACCOUNT](./data-definition/create-account.md)
* [CREATE AGGREGATING INDEX](./data-definition/create-aggregating-index.md)
* [CREATE DATABASE](./data-definition/create-database.md)
* [CREATE EXTERNAL TABLE](./data-definition/create-external-table.md)
* [CREATE FACT or DIMENSION TABLE](./data-definition/create-fact-dimension-table.md)
* [CREATE VIEW](./data-definition/create-view.md)
* [DROP ACCOUNT](./data-definition/drop-account.md)
* [DROP DATABASE](./data-definition/drop-database.md)
* [DROP INDEX](./data-definition/drop-index.md)
* [DROP TABLE](./data-definition/drop-table.md)
* [DROP VIEW](./data-definition/drop-view.md)
* [USE DATABASE](./data-definition/use-database.md)

## Engines

* [ALTER ENGINE](./engines/alter-engine.md)
* [CREATE ENGINE](./engines/create-engine.md)
* [DROP ENGINE](./engines/drop-engine.md)
* [START ENGINE](./engines/start-engine.md)
* [STOP ENGINE](./engines/stop-engine.md)
* [USE ENGINE](./engines/use-engine.md)

## Metadata

* [DESCRIBE](./metadata/describe.md)
* [SHOW CACHE](./metadata/show-cache.md)
* [SHOW CATALOGS](./metadata/show-catalogs.md)
* [SHOW COLUMNS](./metadata/show-columns.md)
* [SHOW ENGINES](./metadata/show-engines.md)
* [SHOW INDEXES](./metadata/show-indexes.md)
* [SHOW TABLES](./metadata/show-tables.md)
* [SHOW VIEWS](./metadata/show-views.md)

## Access control

* [ALTER LOGIN](./access-control/alter-login.md)
* [ALTER NETWORK POLICY](./access-control/alter-network-policy.md)
* [ALTER SERVICE ACCOUNT](./access-control/alter-service-account.md)
* [ALTER USER](./access-control/alter-user.md)
* [CREATE LOGIN](./access-control/create-login.md)
* [CREATE NETWORK POLICY](./access-control/create-network-policy.md)
* [CREATE ROLE](./access-control/create-role.md)
* [CREATE SERVICE ACCOUNT](./access-control/create-service-account.md)
* [CREATE USER](./access-control/create-user.md)
* [DROP LOGIN](./access-control/drop-login.md)
* [DROP NETWORK POLICY](./access-control/drop-network-policy.md)
* [DROP ROLE](./access-control/drop-role.md)
* [DROP SERVICE ACCOUNT](./access-control/drop-service-account.md)
* [DROP USER](./access-control/drop-user.md)
* [GRANT](./access-control/grant.md)
* [REVOKE](./access-control/revoke.md)
