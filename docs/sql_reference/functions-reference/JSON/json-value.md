---
layout: default
title: JSON_VALUE
description: Reference material for JSON_VALUE function
grand_parent: SQL functions
parent: JSON functions
great_grand_parent: SQL reference
---

# JSON_VALUE

Takes a JSON document and extracts a JSON scalar value to SQL `TEXT` value.
For JSON strings, removes the outermost quotes and unescapes the values.
Other JSON scalars are not changed.
Returns a SQL `NULL` if a non-scalar value is given.

This function pairs with the [`JSON_EXTRACT`](json-extract.md) function, which doesn't convert the JSON values to SQL values.

## Syntax

{: .no_toc}

```sql
JSON_VALUE(<json>)
```

## Parameters

{: .no_toc}

| Parameter                | Description                                                                                      | Supported input types |
|:-------------------------|:-------------------------------------------------------------------------------------------------|:----------------------|
| `<json>`                 | The JSON document.                                                                               | `TEXT`                |

## Return Type

`TEXT`
* If any of the input is `NULL` the output is `NULL` (propagates nulls).

## Example

{: .no_toc}

For the JSON document indicated by `<json_common_example>` below,
see [JSON common example](./index.md#json-common-example). The **returned result** is based on this example.

```sql
SELECT JSON_VALUE(JSON_POINTER_EXTRACT(<json_common_example>, '/value/uid')), JSON_POINTER_EXTRACT(<json_common_example>, '/value/uid')
```

**Returns**: `'987654', '"987654"'`

```sql
SELECT JSON_VALUE(JSON_POINTER_EXTRACT(<json_common_example>, '/key'))::INT
```

**Returns**: `123`

```sql
SELECT JSON_VALUE(JSON_POINTER_EXTRACT(<json_common_example>,'/value/keywords'))
```

**Returns**: `NULL`

```sql
SELECT JSON_VALUE(NULL)
```

**Returns**: `NULL`
