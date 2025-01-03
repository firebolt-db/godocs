---
layout: default
title: ST_ASBINARY
description: Reference material for ST_ASBINARY function
parent: Geospatial functions
published: true
---

# ST_ASBINARY

Converts shapes of the `GEOGRAPHY` data type to the [Well-Known Binary (WKB)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry#Well-known_binary) format for geographic objects.

## Syntax
{: .no_toc}

```sql
ST_ASBINARY(<object>)
```

## Parameters 
{: .no_toc}

| Parameter | Description                                                                                                         | Supported input types |
| :--------- | :------------------------------------------------------------------------------------------------------------------- | :-------------------|
| `<object>`   | The `GEOGRAPHY` object to convert to WKB format. | `GEOGRAPHY` |

## Return Type
`ST_ASBINARY` returns a value of type `BYTEA`.

## Example
{: .no_toc}

{% include sql_examples/st_asbinary.md %}
