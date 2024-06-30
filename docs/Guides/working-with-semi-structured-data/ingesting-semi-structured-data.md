---
layout: default
title: Ingest semi-structured data
description: Learn how to ingest (load) semi-structured data from your data lake into the Firebolt data warehouse.
nav_order: 2
parent: Work with semi-structured data
grand_parent: Guides
---

# Ingest semi-structured data

There are three major approaches to ingest and handle semi-structured data as shown below. All approaches can be
combined depending on the nature of the input data and the queries to run over the data.

1. Transforming the input using JSON and `ARRAY` functions to fit the target schema during ingestion.

2. Ingesting the JSON object as raw `TEXT` rows, and later using JSON and `ARRAY` functions to query and manipulate
   them.

3. When the input JSON adheres to a fixed schema&mdash;that is, each object has a known set of keys, and the nesting
   level of at most two (not including nesting of arrays, which can be arbitrary)&mdash;the data can be ingested
   directly. Omitted keys can be handled by specifying default values for the respective columns, but keys that are
   defined at table creation time are ignored. This approach is not common with true, semi-structured sources. This
   approach usually applies to exports from table-oriented storage.

Assume that each JSON record is stored as plain text in the column `raw_json` of a (potentially external) table
named `source_json` in the format shown below.

```javascript
// 1st record
{
    "id": 1,
    "StartTime": "2020-01-06 17:00:00",
    "Duration": 450,
    "tags": ["summer-sale","sports"],
    "user_agent":{
        "agent": "Mozilla/5.0",
        "platform": "Windows NT 6.1",
        "resolution": "1024x4069"
    }
}

// 2nd record
{
    "id": 2,
    "StartTime": "2020-01-05 12:00:00",
    "Duration": 959,
    "tags": ["gadgets","audio"],
    "user_agent":{
        "agent": "Safari",
        "platform": "iOS 14"
    }
}
```

Recall that we want the target Firebolt table named `visits` to have columns and values similar to the table shown
below.

| id (INTEGER) | start_time (DATETIME) | duration (INTEGER) | tags (ARRAY(TEXT))         |
|:-------------|:----------------------|:-------------------|:---------------------------|
| 1            | 2020-01-06 17:00:00   | 450                | \["summer-sale","sports"\] |
| 2            | 2020-01-05 12:00:00   | 959                | \["gadgets","audio"\]      |

## Extracting top-level scalars and arrays

For the top-level keys (`id`, `Duration`, and `tags`), the task is straightforward using
the [JSON_EXTRACT](../../sql_reference/functions-reference/JSON/json-extract.md) function.

The following statement takes the raw JSON input and uses `INSERT` to load the results into the table `visits`. The
result is provided as an illustration, since an `INSERT` returns only the number of affected rows.

```sql
INSERT INTO visits
SELECT JSON_POINTER_EXTRACT(raw_json, '/id')::INTEGER          as id,
       JSON_POINTER_EXTRACT(raw_json, '/StartTime')::TIMESTAMP as StartTime,
       JSON_POINTER_EXTRACT(raw_json, '/Duration')::INTEGER    as duration,
       JSON_POINTER_EXTRACT(raw_json, '/tags')::ARRAY(TEXT)    as tags
FROM doc_visits_source
```

Result (if the script had been excecuted without the `INSERT` clause):

| id | StartTime           | duration | tags                       |
|:---|:--------------------|:---------|:---------------------------|
| 1  | 2020-01-06 17:00:00 | 450      | \["summer-sale","sports"\] |
| 2  | 2020-01-05 12:00:00 | 959      | \["gadgets","audio"\]      |
