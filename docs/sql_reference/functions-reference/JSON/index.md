---
layout: default
title: JSON functions
description: Reference for JSON functions
nav_order: 9
parent: SQL functions
grand_parent: SQL reference
great_grand_parent: SQL reference
has_children: true
---


## JSON Functions Overview

The JSON functions provide a way to extract specific values from JSON documents, particularly from those stored in a column.

There are three types of JSON functions:
1. These functions extract part of the document, but preserve the original data in the result:
    * [JSON_EXTRACT](./json-extract.md)
    * [JSON_EXTRACT_ARRAY](./json-extract-array.md)
    * [JSON_POINTER_EXTRACT_VALUES](./json-pointer-extract-values.md)
2. These functions convert a JSON value to a SQL value:
    * [JSON_VALUE](./json-value.md)
    * [JSON_VALUE_ARRAY](./json-value-array.md)
    * [JSON_POINTER_EXTRACT_KEYS](./json-pointer-extract-keys.md)
3. This function extracts a JSON value and converts it to a SQL value, combining the functionalities of the previous two types of functions:
    * [JSON_POINTER_EXTRACT_TEXT](./json-pointer-extract-text.md)

The first two types of functions can be used in conjunction with each other to extract and convert JSON values to SQL values.
The following code uses `JSON_POINTER_EXTRACT` to extract a value from a JSON document and `JSON_VALUE` to convert it into a SQL value:
```sql
SELECT JSON_VALUE(JSON_POINTER_EXTRACT('{"key1":{"key3":"val1" }, "key2":"val2", "key3":5}', '/key1/key3'));
```
**Returns**
Returns `val1` as a SQL `TEXT` value, rather than the original JSON value `"val1"` with the double quotes.

Currently, JSON functions support only JSON pointer expressions, which provide a method for accessing specific elements within a JSON document.
For convenience, the following aliases are available for JSON functions that use JSON pointer expressions:
* `JSON_POINTER_EXTRACT` is an alias for `JSON_EXTRACT` with the `path_syntax` parameter set to `'JSONPointer'`.
* `JSON_POINTER_EXTRACT_ARRAY` is an alias for `JSON_EXTRACT_ARRAY` with the `path_syntax` parameter set to `'JSONPointer'`.


### JSON pointer expression syntax

The placeholder `<json_pointer_expression>` indicates where you should use a JSON pointer, which allows access to specific elements in a JSON document. For a formal specification, see [RFC6901](https://tools.ietf.org/html/rfc6901).

A JSON pointer begins with a forward slash (`/`), indicating the root of the JSON document, followed by a sequence of property (key) names or zero-based ordinal numbers separated by slashes. Property names identify specific keys, while index numbers specify the Nth element in an array or object.

The tilde (`~`) and forward slash (`/`) characters have special meanings and need to be escaped as follows:

* To specify a literal tilde (`~`), use `~0`.
* To specify a literal forward slash (`/`), use `~1`.

For example, consider the following JSON document:

```javascript
{
    "key": 123,
    "key~with~tilde": 2,
    "key/with/slash": 3,
    "value": {
      "dyid": 987,
      "keywords" : ["insanely","fast","analytics"]
    }
}
```

In the previous JSON document, the JSON pointer expressions evaluate to the following:

| Pointer              | Result                             | Notes           |
| :------------------- | :--------------------------------- | :-------------- |
| `/`                  | `{` <br>`   "key": 123,` <br>`   "key~with~tilde": 2,` <br>`   "key/with/slash": 3,` <br>`   "value": {` <br>`      "dyid": 987,` <br>`      "keywords" : ["insanely","fast","analytics"]` <br>`   }` | Returns the whole document. |
| `/key`               | 123                                |                 |
| `/key~0with~0tilde`  | 2                                  | Indicates the value associated with the `key~with~tilde` property name. |
| `/key~1with~1slash`  | 3                                  | Indicates the value associated with the `key/with/slash` property name. |
| `/0`                 | 123                                | Uses an ordinal to indicate the value associated with the `key` property name. The `key` property is in the first 0-based position.        |
| `/value/keywords/2`  | analytics                          | Indicates the element "analytics", which is in the third 0-based position of the array value associated with the keywords property. |

### JSON common example

The following JSON document, represented by the `<json_common_example>` placeholder, is used as a basis for all JSON function examples in this reference.

```javascript
{
    "key": 123,
    "value": {
      "dyid": 987,
      "uid": "987654",
      "keywords" : ["insanely","fast","analytics"],
      "tagIdToHits": {
        "map": {
          "1737729": 32,
          "1775582": 35
        }
      },
      "events":[
        {
            "EventId": 547,
            "EventProperties" :
            {
                "UserName":"John Doe",
                "Successful": true
            }
        },
        {
            "EventId": 548,
            "EventProperties" :
            {
                "ProductID":"xy123",
                "items": 2
            }
        }
    ]
    }
}
```