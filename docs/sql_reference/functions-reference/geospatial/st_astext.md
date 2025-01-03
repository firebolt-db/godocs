---
layout: default
title: ST_ASTEXT
description: Reference material for ST_ASTEXT function
parent: Geospatial functions
published: true
---

# ST_ASTEXT

Converts shapes of the `GEOGRAPHY` data type to the [Well-Known Text (WKT)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) format.

## Syntax
{: .no_toc}

```sql
ST_ASTEXT(<object>)
```

## Parameters 
{: .no_toc}

| Parameter | Description                                                                                                         | Supported input types |
| :--------- | :------------------------------------------------------------------------------------------------------------------- | :-------------------|
| `<object>`   | The `GEOGRAPHY` object to convert to WKT format. | `GEOGRAPHY` |

## Return Type
`ST_ASTEXT` returns a value of type `TEXT`.

## Example
{: .no_toc}

{% include sql_examples/st_astext.md %}
