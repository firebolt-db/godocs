---
layout: default
title: JSON_EXTRACT
description: Reference material for JSON_EXTRACT function
parent: JSON functions
---

# JSON_EXTRACT

Takes an expression containing a JSON document, a JSON path expression, and an optional path syntax. If the key
specified using the JSON path expression exists, `JSON_EXTRACT` returns the sub JSON document pointed by the given JSON
path. Otherwise, returns NULL.

## Syntax

{: .no_toc}

```sql
JSON_EXTRACT(<json>, <json_path_expression>, path_syntax => <path_syntax>)
```

### Aliases

```sql
JSON_POINTER_EXTRACT(<json>, <json_path_expression>) ->
JSON_EXTRACT(<json>, <json_path_expression>, path_syntax => 'JSONPointer')
```

## Parameters

{: .no_toc}

| Parameter                | Description                                                                                      | Supported input types |
|:-------------------------|:-------------------------------------------------------------------------------------------------|:----------------------|
| `<json>`                 | The JSON document.                                                                               | `TEXT`                |
| `<json_path_expression>` | A JSON path to the location of the desiered sub-document in the JSON.                            | `TEXT`                |
| `<path_syntax>`          | The expected syntax of the `<json_path_expression>`, supports only 'JSONPointer' at the moment. For more information, see [JSON pointer expression syntax](./index.md#json-pointer-expression-syntax). | `TEXT`                | 

## Return Type

`TEXT`
* If any of the input is `NULL` the output is `NULL` (propagate nulls).

## Example

{: .no_toc}

For the JSON document indicated by `<json_common_example>` below,
see [JSON common example](./index.md#json-common-example). The **returned result** is based on this example.

```sql
SELECT JSON_EXTRACT(<json_common_example>, '/value/dyid', 'JSONPointer')
```

**Returns**: `'987'`

```sql
SELECT JSON_EXTRACT(<json_common_example>, '/value/no_such_key', 'JSONPointer')
```

**Returns**: `NULL`

```sql
SELECT JSON_POINTER_EXTRACT(<json_common_example>, '/value/uid')
```

**Returns**: `'"987654"'`

```sql
SELECT JSON_POINTER_EXTRACT(<json_common_example>,'/value/keywords')
```

**Returns**: `'["insanely","fast","analytics"]'`

```sql
SELECT JSON_POINTER_EXTRACT(<json_common_example>,'/value/keywords/2')
```

**Returns**: `'"analytics"'`
