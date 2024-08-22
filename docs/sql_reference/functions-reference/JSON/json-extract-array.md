---
layout: default
title: JSON_EXTRACT_ARRAY
description: Reference material for JSON_EXTRACT_ARRAY function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: JSON functions
---

# JSON_EXTRACT_ARRAY

Takes an expression containing a JSON document, a JSON path expression, and an optional path syntax. If the key
specified using the JSON path expression exists and its value is a JSON array, 
`JSON_EXTRACT_ARRAY` returns SQL `ARRAY(TEXT)` contains all JSON elements as raw text inside the JSON array pointed by the given JSON
path. Otherwise, returns NULL.

## Syntax

{: .no_toc}

```sql
JSON_EXTRACT_ARRAY(<json>, <json_path_expression>, path_syntax => <path_syntax>)
```

### Aliases

```sql
JSON_POINTER_EXTRACT_ARRAY(<json>, <json_path_expression>) ->
JSON_EXTRACT_ARRAY(<json>, <json_path_expression>, path_syntax => 'JSONPointer')
```

## Parameters

{: .no_toc}

| Parameter                | Description                                                                                      | Supported input types |
|:-------------------------|:-------------------------------------------------------------------------------------------------|:----------------------|
| `<json>`                 | The JSON document.                                                                               | `TEXT`                |
| `<json_path_expression>` | A JSON path to the location of the desiered sub-document in the JSON.                            | `TEXT`                |
| `<path_syntax>`          | The expected syntax of the `<json_path_expression>`, supports only 'JSONPointer' at the moment. For more information, see [JSON pointer expression syntax](./index.md#json-pointer-expression-syntax). | `TEXT`                | 

## Return Type

`ARRAY(TEXT)`
* If any of the inputs is `NULL` the output is `NULL` (propagates nulls).

## Example

{: .no_toc}

For the JSON document indicated by `<json_common_example>` below,
see [JSON common example](./index.md#json-common-example). The **returned result** is based on this example.

```sql
SELECT JSON_EXTRACT_ARRAY(<json_common_example>, '/value/dyid', 'JSONPointer')
```

**Returns**: `NULL` because it does not point to an array.

```sql
SELECT JSON_EXTRACT_ARRAY(<json_common_example>, '/value/no_such_key', 'JSONPointer')
```

**Returns**: `NULL` because the key does not exist.

```sql
SELECT JSON_POINTER_EXTRACT_ARRAY(<json_common_example>,'/value/keywords')
```

**Returns**: `{"insanely", "fast", "analytics"}`

```sql
SELECT JSON_POINTER_EXTRACT_ARRAY(<json_common_example>,'/value/events')
```

**Returns** (SQL array of 2 text elements):
```
{
        '{
            "EventId": 547,
            "EventProperties" :
            {
                "UserName":"John Doe",
                "Successful": true
            }
        }',
        '{
            "EventId": 548,
            "EventProperties" :
            {
                "ProductID":"xy123",
                "items": 2
            }
        }'
}
```
