---
layout: default
title: JSON_EXTRACT_ARRAY_RAW
description: Reference material for JSON_EXTRACT_ARRAY_RAW function
<<<<<<< HEAD:docs/sql_reference/functions-reference/JSON/json-extract-array-raw.md
grand_parent: SQL functions
parent: Semi-structured data functions
great_grand_parent: SQL reference
=======
parent:  SQL functions
>>>>>>> rn/gh-pages:docs/sql-reference/functions-reference/json-extract-array-raw.md
---

# JSON_EXTRACT_ARRAY_RAW

Returns a string representation of a JSON array pointed by the supplied JSON pointer. The returned string represents a Firebolt array with elements that are string representations of the scalars or objects contained in the JSON array under the specified key, if the key exists. If the key does not exist, the function returns an empty array.

<<<<<<< HEAD:docs/sql_reference/functions-reference/JSON/json-extract-array-raw.md
This function is useful when working with heterogeneously typed arrays and arrays containing JSON objects in which case each object will be further processed by functions such as [TRANSFORM](../Lambda/transform.md).
=======
This function is useful when working with heterogeneously typed arrays and arrays containing JSON objects in which case each object will be further processed by functions such as [TRANSFORM](./transform.md).
>>>>>>> rn/gh-pages:docs/sql-reference/functions-reference/json-extract-array-raw.md

## Syntax
{: .no_toc}

```sql
JSON_EXTRACT_ARRAY_RAW(<json>, '<json_pointer_expression>')
```

## Parameters
{: .no_toc}

| Parameter                   | Description                                               | Supported input types | 
| :--------------------------- | :--------------------------------------------------------- | :----------|
| `<json>`                    | The JSON document from which the array is to be extracted. | `TEXT` | 
| `<json_pointer_expression>` | A JSON pointer to the location of the array in the JSON. For more information, see [JSON pointer expression syntax](./index.md#json-pointer-expression-syntax).    | `TEXT` | 

## Return Types
* If the key exists, returns a string representation of a JSON `ARRAY`
* If the key does not exist, returns an empty `ARRAY`

## Example
{: .no_toc}

For the JSON document indicated by `<json_common_example>` below, see [JSON common example](./index.md#json-common-example). The **Returns** result is based on this common example.

```sql
SELECT
    JSON_EXTRACT_ARRAY_RAW(<json_common_example>, '/value/events')
```

**Returns**: `["{\"EventId\":547,\"EventProperties\":{\"UserName\":\"John Doe\",\"Successful\":true}}","{\"EventId\":548,\"EventProperties\":{\"ProductID\":\"xy123\",\"items\":2}}"]`
