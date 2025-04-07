---
redirect_from:
  - /sql-reference/functions-reference/param.html
layout: default
title: PARAM
description: Reference material for PARAM function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Numeric functions
---

# PARAM

Evaluates a provided query parameter and returns its value as `TEXT`.

## Syntax
{: .no_toc}

```sql
PARAM(<parameter>)
```

| Parameter | Description                         |Supported input types |
| :--------- | :----------------------------------- | :---------------------|
| `<parameter>` | Constant string containing the name of the query parameter to evaluate. | `TEXT` |

## Return Type
`TEXT`

## Specifying query parameters
To use the `PARAM` function, you need to define query parameters using the `SET PARAM` command. The function relies on a request property named `query_parameters` in JSON format. Use the following schema:

```sql
query_parameters: json_array | json_object
json_array: [ json_object, … ]
json_object: { "name" : parameter_name, "value" : parameter_value }
```

You can include a single query parameter in the request properties, for example: 

`{ "name": "country", "value": "USA" }`


or multiple query parameters:

`[ 
  { "name": "country", "value": "USA" },
  { "name": "states", "value": "WA, OR, CA" },
  { "name": "max_sales", "value": 10000 }
]`

## Example
{: .no_toc}

The following example shows how to use a Common Table Expression (CTE), through a `WITH` clause, to generate input data and apply a query parameter in a computation. The `WITH` clause defines a temporary dataset, and the query evaluates whether each row matches the parameter value using `PARAM`.

```sql
SET query_parameters = [{ "name": "level_type_value", "value": "Drift" }];

WITH Table AS (
  SELECT 'Drift' AS col1
  UNION ALL
  SELECT 'FastestLap'
)
SELECT col1,
       (col1 = PARAM('level_type_value')) AS match_status
FROM Table;
```

**Returns**

| col1       | match_status |
| ---------- | ------------ |
| Drift      | 1            |
| FastestLap | 0            |

