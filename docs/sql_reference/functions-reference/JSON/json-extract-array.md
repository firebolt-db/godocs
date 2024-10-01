---
layout: default
title: JSON_EXTRACT_ARRAY
description: Reference material for JSON_EXTRACT_ARRAY function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: JSON functions
---

# JSON_EXTRACT_ARRAY

Accepts a JSON document, path expression, and optional path syntax. If the key exists and holds a JSON array, `JSON_EXTRACT_ARRAY` returns an SQL ARRAY(TEXT) with the array's elements as raw text, and otherwise returns `NULL`.

## Syntax

{: .no_toc}

```sql
JSON_EXTRACT_ARRAY
(<json>, <json_path_expression>, path_syntax => <path_syntax>)
```

### Aliases

```sql
JSON_POINTER_EXTRACT_ARRAY
(<json>, <json_path_expression>) ->
JSON_EXTRACT_ARRAY(<json>, <json_path_expression>, path_syntax => 'JSONPointer')
```

## Parameters

{: .no_toc}

| Parameter                | Description                                                                                                                                                                                            | Supported input types |
|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| `<json>`                 | The JSON document.                                                                                                                                                                                     | `TEXT`                |
| `<json_path_expression>` | A JSON path to the location of the desired element within the JSON document.                                                                                                                                  | `TEXT`                |
| `<path_syntax>`          | The expected syntax of the `<json_path_expression>` currently only supports 'JSONPointer'. For more information, see [JSON pointer expression syntax](./index.md#json-pointer-expression-syntax). | `TEXT`                | 

## Return Type

`ARRAY(TEXT)`

* If any input values are `NULL`, the function will return `NULL`.

## Examples

{: .no_toc}

For the JSON document indicated by `<json_common_example>` below,
see [JSON common example](./index.md#json-common-example). The **returned result** is based on the following example.

**Example**
The following code extracts the value at the path `value/dyid` from the JSON document represented by `<json_common_example>`, and returns it as an SQL array using the `JSONPointer` syntax:
```sql
SELECT JSON_EXTRACT_ARRAY(<json_common_example>, '/value/dyid', 'JSONPointer')
```

**Returns**
The previous example returns `NULL` because the specified path does not reference an array.

**Example**
The following code example attempts to extract an array from a path `/value/no_such_key` in the JSON document represented by `<json_common_example>`:

```sql
SELECT JSON_EXTRACT_ARRAY(<json_common_example>, '/value/no_such_key', 'JSONPointer')
```

**Returns**
The previous code example returns `NULL` because the key does not exist.

**Example**
The following code example extracts the array at the path `/value/keywords` from the JSON document represented by `<json_common_example>` using the JSON pointer syntax:

```sql
SELECT JSON_POINTER_EXTRACT_ARRAY(<json_common_example>,'/value/keywords')
```

**Returns**
The previous code example returns the following: `{"insanely", "fast", "analytics"}`.

**Example**
The following code example extracts the array located at the path `/value/events` from the JSON document represented by `<json_common_example>` using the JSON pointer syntax:

```sql
SELECT JSON_POINTER_EXTRACT_ARRAY(<json_common_example>,'/value/events')
```

**Returns** 
The previous code example returns the following SQL array, containing two text elements:

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
