---
layout: default
title: JSON_VALUE_ARRAY
description: Reference material for JSON_VALUE_ARRAY function
parent: JSON functions
---

# JSON_VALUE_ARRAY

Takes a JSON document and extracts a JSON array of scalar values to SQL `ARRAY(TEXT)` value.
For JSON strings, removes the outermost quotes and unescapes the values.
Other JSON scalars are not changed.
Returns a SQL `NULL` if a non-array is given, or non-scalar value is given (inside the array).

This function pairs with the [`JSON_EXTRACT`](json-extract.md) function, which doesn't convert the JSON values to SQL values.

## Syntax

{: .no_toc}

```sql
JSON_VALUE_ARRAY(<json>)
```

## Parameters

{: .no_toc}

| Parameter                | Description                                                                                      | Supported input types |
|:-------------------------|:-------------------------------------------------------------------------------------------------|:----------------------|
| `<json>`                 | The JSON document.                                                                               | `TEXT`                |

## Return Type

`ARRAY(TEXT)`
* If any of the input is `NULL` the output is `NULL` (propagates nulls).

## Example

{: .no_toc}

For the JSON document indicated by `<json_common_example>` below,
see [JSON common example](./index.md#json-common-example). The **returned result** is based on this example.

```sql
SELECT JSON_VALUE_ARRAY(JSON_POINTER_EXTRACT(<json_common_example>, '/value/uid')), JSON_POINTER_EXTRACT(<json_common_example>, '/value/uid')
```

**Returns**: `NULL, '"987654"'`

```sql
SELECT JSON_VALUE_ARRAY(JSON_POINTER_EXTRACT(<json_common_example>,'/value/keywords'))
```

**Returns**: `{'insanely','fast','analytics'}`

```sql
SELECT JSON_VALUE_ARRAY(NULL)
```

**Returns**: `NULL`
