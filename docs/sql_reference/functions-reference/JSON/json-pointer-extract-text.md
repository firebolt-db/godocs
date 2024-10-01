---
layout: default
title: JSON_POINTER_EXTRACT_TEXT
description: Reference material for JSON_POINTER_EXTRACT_TEXT function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: JSON functions
---

# JSON_POINTER_EXTRACT_TEXT

Accepts a JSON document and pointer expression. If the key exists and holds a JSON string, `JSON_POINTER_EXTRACT_TEXT` returns it as SQL `TEXT`, removing outer quotes and decoding characters. Otherwise, it returns `NULL`.

## Syntax

{: .no_toc}

```sql
JSON_POINTER_EXTRACT_TEXT
(<json>, <json_pointer_expression>)
```

## Parameters

{: .no_toc}

| Parameter                   | Description                                                                                                                                                                              | Supported input types |
|:----------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| `<json>`                    | The JSON document.                                                                                                                                                                       | `TEXT`                |
| `<json_pointer_expression>` | A JSON pointer expression to the location of the desired sub-document in the JSON. For more information, see [JSON pointer expression syntax](./index.md#json-pointer-expression-syntax). | `TEXT`                |

## Return Type

`TEXT`

* If any input values are `NULL`, the function will return `NULL`.

## Examples

{: .no_toc}

For the JSON document indicated by `<json_common_example>` below,
see [JSON common example](./index.md#json-common-example). The **returned result** is based on the following example.

**Example**
The following code example extracts the value at path `/value/uid` from the JSON document, removes the outermost quotes, and returns the result as SQL `TEXT`, labeled as `res`:

```sql
SELECT JSON_POINTER_EXTRACT_TEXT(<json_common_example>, '/value/uid') AS res
```

**Returns**
The previous code example returns the following:

| res (TEXT) |
|:-----------|
| 987654     |

**Example**
The following code example attempts to extract the value at the path `/value/no_such_key` from the JSON document:

```sql
SELECT JSON_POINTER_EXTRACT_TEXT(<json_common_example>, '/value/no_such_key') AS res
```

**Returns**
The previous code example returns the `NULL` with the result labeled as `res`, because the key does not exist:

| res (TEXT) |
|:-----------|
| NULL       |

**Example**

The following code example attempts to extract the value at the path `/value/keywords` from the JSON document:

```sql
SELECT JSON_POINTER_EXTRACT_TEXT(<json_common_example>,'/value/keywords') AS res
```

**Returns**
The previous code example returns `NULL`, labeled as `res` because the value at the specified path is an array, not a string:

| res (TEXT) |
|:-----------|
| NULL       |

**Example**
The following code example navigates to the third element at index `2` of the array at `/value/keywords` in the JSON document, removes the outermost quotes, and returns it as SQL `TEXT`, labeled as `res`:

```sql
SELECT JSON_POINTER_EXTRACT_TEXT(<json_common_example>,'/value/keywords/2') AS res
```

**Returns**
The previous code example returns `"analytics"`, which is the third element in the JSON array, which uses zero-based indexing:

| res (TEXT) |
|:-----------|
| analytics  |
 

