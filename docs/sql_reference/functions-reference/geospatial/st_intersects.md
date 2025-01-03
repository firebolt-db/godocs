---
layout: default
title: ST_INTERSECTS
description: Reference material for ST_INTERSECTS function
parent: Geospatial functions
published: true
---

# ST_INTERSECTS

The `ST_INTERSECTS` function determines whether two input `GEOGRAPHY` objects intersect each other.

If either input is empty, `ST_INTERSECTS` will return `FALSE`.

Before performing the intersection check, the two inputs are aligned through a snapping process, ensuring precise calculation. For more details on snapping, refer to the [snapping documentation](../../geography-data-type.md#snapping).

## Syntax
{: .no_toc}

```sql
ST_INTERSECTS(<geo1>, <geo2>)
```

## Parameters 
{: .no_toc}

| Parameter | Description                                                                                                         | Supported input types |
| :--------- | :------------------------------------------------------------------------------------------------------------------- | :-------------------|
| `<geo1>`   | The first `GEOGRAPHY` object to check for intersection with the second object. | `GEOGRAPHY` |
| `<geo2>`   | The second `GEOGRAPHY` object to check for intersection with the first object. | `GEOGRAPHY` |

## Return Type
`ST_INTERSECTS` returns a value of type `BOOLEAN`.

## Example
{: .no_toc}

{% include sql_examples/st_intersects.md %}
