---
layout: default
title: EXPLAIN
great_grand_parent: SQL reference
grand_parent: SQL commands
parent: Queries
---

# CANCEL QUERY

The `CANCEL QUERY` statement is used to cancel a running query within the Firebolt engine. This statement provides a mechanism to terminate the execution of a specific query identified by its unique query_id.

## Syntax

```sql
CANCEL QUERY WHERE query_id = '<query_id>';
```

## Parameters

| Parameter              | Description |
| :--------------------- | :---------- |
| `<query_id>`  | A unique identifier assigned to the query that needs to be canceled. |

## Example

```sql
CANCEL QUERY WHERE query_id = '12345';
```

## Notes
* The query_id is typically obtained from the `information_schema.running_queries` view.
* Cancelling a query may result in the termination of the associated query process, releasing resources and stopping further execution.
* This statement is designed for administrative use and may require appropriate privileges to execute.

## Example Use Case

Suppose there is a long-running query that needs to be canceled to free up system resources. The following statement can be used to obtain the query_id:
```sql
select status, duration_usec, query_text, query_id from information_schema.running_queries;
```

Suppose the long-running query is identified with query_id '12345':
```sql
CANCEL QUERY WHERE query_id = '12345';
```
This will initiate the cancellation process for the specified query_id. While the query is not completely terminated, its status in `information_schema.running_queries` can be observed as `CANCELING`.
Once the query is canceled, it disappears from running_queries. Its status in `information_schema.query_history`:
```sql
select query_id, status from information_schema.query_history;
```
will be observed as `CANCELED`.


## Caution

Care should be taken when cancelling queries, as it may impact transactions and ongoing operations. Users should have a clear understanding of the query being canceled and its potential side effects.