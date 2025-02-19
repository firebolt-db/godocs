---
redirect_from:
  - /working-with-semi-structured-data/mapping-json-to-table.html
layout: default
title: Load semi-structured JSON data
description: Learn how to map semi-structured data from a JSON document to a Firebolt table.
nav_order: 1
parent: Work with semi-structured data
---

# Load semi-structured JSON data

Semi-structured data does not follow a strict table format but contains structured tags or key-value pairs. JSON is an example of semi-structured data. Firebolt supports the following three ways to ingest JSON based on how your data changes and how you query it:

- [Transform the input during load](#transform-the-input-during-load) if your table must always contain certain fields.
- [Store JSON as text](#store-json-as-text) if you need only specific fields on demand or if the table structure changes frequently.
- [Load JSON into a fixed schema](#load-json-into-a-fixed-schema) if your JSON data has a stable set of fields with shallow nesting.

This document shows you how to load data using each of the previous methods and the sample JSON dataset in the following section.

### Sample JSON dataset

The following JSON data shows two session records for a website, where each line represents a single JSON object. This sample data is used in each of the examples in this document.

```json
[
  {
    "id": 1,
    "StartTime": "2020-01-06 17:00:00",
    "Duration": 450,
    "tags": ["summer-sale", "sports"],
    "user_agent": {
      "agent": "Mozilla/5.0",
      "platform": "Windows NT 6.1",
      "resolution": "1024x4069"
    }
  },
  {
    "id": 2,
    "StartTime": "2020-01-05 12:00:00",
    "Duration": 959,
    "tags": ["gadgets", "audio"],
    "user_agent": {
      "agent": "Safari",
      "platform": "iOS 14"
    }
  }
]
```

## Transform the input during load

Parsing JSON data during ingestion eliminates the need for query-time parsing, simplifying and accelerating queries. However, transforming data during load also requires well-defined JSON paths that remain consistent. If the JSON paths change, the load might fail.

The following code example parses JSON data as it loads and inserts extracted fields into a Firebolt table named `visits`. It shows how to handle mandatory scalar fields, an array field, and a `user_agent` map by storing keys and values in separate arrays:

```sql
CREATE TABLE doc_visits_source (
  raw_json TEXT
);

-- Insert raw JSON data (each row contains a single JSON object) into column named 'raw_json'
INSERT INTO doc_visits_source (raw_json)
VALUES
('{"id": 1, "StartTime": "2020-01-06 17:00:00", "Duration": 450, "tags": ["summer-sale", "sports"], "user_agent": {"agent": "Mozilla/5.0", "platform": "Windows NT 6.1", "resolution": "1024x4069"}}'),
('{"id": 2, "StartTime": "2020-01-05 12:00:00", "Duration": 959, "tags": ["gadgets", "audio"], "user_agent": {"agent": "Safari", "platform": "iOS 14"}}');

-- Create the target table 'visits'
CREATE FACT TABLE visits (
  id INT,
  start_time TIMESTAMP,
  duration INT,
  tags ARRAY(TEXT),
  agent_props_keys ARRAY (TEXT),
  agent_props_vals ARRAY (TEXT)
)
PRIMARY INDEX start_time;

-- Insert parsed JSON data into the 'visits' table
INSERT INTO visits
SELECT
  JSON_POINTER_EXTRACT(raw_json, '/id')::INT AS id,
  TO_TIMESTAMP(TRIM(BOTH '"' FROM JSON_POINTER_EXTRACT(raw_json, '/StartTime')), 'YYYY-MM-DD HH24:MI:SS') AS start_time,
  JSON_POINTER_EXTRACT(raw_json, '/Duration')::INT AS duration,
  JSON_POINTER_EXTRACT(raw_json, '/tags')::ARRAY(TEXT) AS tags,
  JSON_POINTER_EXTRACT_KEYS(raw_json, '/user_agent') AS agent_props_keys,
  JSON_POINTER_EXTRACT_VALUES(raw_json, '/user_agent') AS agent_props_vals
FROM doc_visits_source;
```

{: .note}
The data type is shown in capital letters beside the column name for clarity and is not part of the column name.

A common error may occur if a field path does not exist in the JSON document. Firebolt returns an error because `NULL` values cannot be cast to `INT`. Use a default value or conditional expression to avoid this error, as shown in the following code example:

```sql
INSERT INTO visits
SELECT
  JSON_POINTER_EXTRACT(raw_json, '/unknown_field')::INT AS id
FROM doc_visits_source;
```

The following table shows the expected output:

| id | start_time      | duration | tags                           | user_agent                                                        |
|----|-----------------|----------|--------------------------------|-------------------------------------------------------------------|
| 2  | 1/5/2020 12:00  | 959      | ["gadgets","audio"]            | {"agent": "Safari", "platform": "iOS 14"}                         |
| 1  | 1/6/2020 17:00  | 450      | ["summer-sale","sports"]       | {"agent": "Mozilla/5.0", "platform": "Windows NT 6.1", "resolution": "1024x4069"} |


Important characteristics of the previous table:

* The mandatory scalar fields, `id`, `start_time`, and `duration`, are stored in separate columns, which makes it easier to filter, sort, or join by these fields.
* A `tags` column is stored as type ARRAY(TEXT), which accommodates variable-length lists of strings without needing to modify the schema.
* The `user_agent` object is stored in two arrays: `agent_props_keys` and `agent_props_vals`. Splitting keys and values into parallel arrays offers flexibility if the `user_agent` map changes and avoids schema changes for new or removed fields.

## Store JSON as text

You can store JSON as a single text column if the data structure changes frequently or if you only need certain fields in some queries. This approach simplifies ingestion since no parsing occurs during loading, but it requires parsing fields at query time, which can make queries more complex if you need to extract many fields regularly.

The following code example creates a table that stores raw JSON, allowing you to parse only what you need on demand:

```sql
-- Create a staging table to hold the raw JSON data
CREATE TABLE doc_visits_source (
  raw_json TEXT
);

-- Insert raw JSON data as individual rows (one JSON object per row)
INSERT INTO doc_visits_source (raw_json)
VALUES
('{"id": 1, "StartTime": "2020-01-06 17:00:00", "Duration": 450, "tags": ["summer-sale", "sports"], "user_agent": {"agent": "Mozilla/5.0", "platform": "Windows NT 6.1", "resolution": "1024x4069"}}'),
('{"id": 2, "StartTime": "2020-01-05 12:00:00", "Duration": 959, "tags": ["gadgets", "audio"], "user_agent": {"agent": "Safari", "platform": "iOS 14"}}');

-- Create the target table 'visits_raw'
CREATE FACT TABLE visits_raw (
  raw_json TEXT
)
PRIMARY INDEX raw_json;

-- Insert data into the 'visits_raw' table from the staging table
INSERT INTO visits_raw
SELECT raw_json
FROM doc_visits_source;
```
The following table shows the expected output:

| raw_json |
| -------- |
| {"id": 1, "StartTime": "2020-01-06 17:00:00", "Duration": 450, "tags": ["summer-sale", "sports"], "user_agent": {"agent": "Mozilla/5.0", "platform": "Windows NT 6.1", "resolution": "1024x4069"}} |
| {"id": 2, "StartTime": "2020-01-05 12:00:00", "Duration": 959, "tags": ["gadgets", "audio"], "user_agent": {"agent": "Safari", "platform": "iOS 14"}} |


Important characteristics of the table:

* The entire JSON object is stored in a single `TEXT` column, which is beneficial when you do not know which fields you need or if the structure evolves quickly. 
* Parsing occurs at query time, which can save upfront processing when data is loaded, but it might increase query complexity and cost if you need to parse many fields frequently.
* Subsequent queries need to extract fields manually with JSON functions as needed.

## Load JSON into a fixed schema

If your JSON data has a stable set of fields with shallow nesting, you can load it into a table with a fixed schema to simplify queries. Missing keys are assigned default values, while extra keys are ignored, making this approach less flexible for changing data. This method allows you to query columns directly without additional parsing, making queries faster and easier to write.

The following code example defines columns that map directly to known keys:

```sql
-- Create a staging table for raw JSON data (one JSON object per row)
DROP TABLE IF EXISTS doc_visits_source;
CREATE TABLE doc_visits_source (
  raw_json TEXT
);

-- Insert raw JSON data as individual rows
INSERT INTO doc_visits_source (raw_json)
VALUES
('{"id": 1, "StartTime": "2020-01-06 17:00:00", "Duration": 450, "tags": ["summer-sale", "sports"], "user_agent": {"agent": "Mozilla/5.0", "platform": "Windows NT 6.1", "resolution": "1024x4069"}}'),
('{"id": 2, "StartTime": "2020-01-05 12:00:00", "Duration": 959, "tags": ["gadgets", "audio"], "user_agent": {"agent": "Safari", "platform": "iOS 14"}}');

-- Create the target table 'visits_fixed' with a fixed schema
CREATE FACT TABLE visits_fixed (
  id INT DEFAULT 0,
  start_time TIMESTAMP DEFAULT '1970-01-01 00:00:00',
  duration INT DEFAULT 0,
  tags ARRAY(TEXT) DEFAULT []
)
PRIMARY INDEX start_time;

-- Insert data into 'visits_fixed' by extracting values from the raw JSON
INSERT INTO visits_fixed
SELECT
  JSON_POINTER_EXTRACT(raw_json, '/id')::INT AS id,
  TO_TIMESTAMP(TRIM(BOTH '"' FROM JSON_POINTER_EXTRACT(raw_json, '/StartTime')), 'YYYY-MM-DD HH24:MI:SS') AS start_time,
  JSON_POINTER_EXTRACT(raw_json, '/Duration')::INT AS duration,
  JSON_POINTER_EXTRACT(raw_json, '/tags')::ARRAY(TEXT) AS tags
FROM doc_visits_source;
```
The following table shows the expected output:

| id | start_time     | duration | tags                          |
|----|----------------|----------|-------------------------------|
| 2  | 1/5/2020 12:00 | 959      | ["gadgets", "audio"]          |
| 1  | 1/6/2020 17:00 | 450      | ["summer-sale", "sports"]     |

Important characteristics of the table:

* Each column maps directly to a known JSON key, allowing for simpler queries without the need for JSON functions.
* Default values ensure that the table loads even if some fields are missing or additional keys appear. Extra JSON fields are ignored and not stored in the table.
* Array columns are used to store `tags`, which supports arbitrary numbers of values without schema changes.
