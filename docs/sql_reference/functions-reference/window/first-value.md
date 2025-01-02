---
layout: default
title: FIRST_VALUE
description: Reference material for FIRST_VALUE function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Window functions
published: true
---

# FIRST_VALUE

Returns the first value evaluated in the specified window frame. If there are no rows in the window frame, returns NULL.

## Syntax

{: .no_toc}

```sql
FIRST_VALUE( <expression> ) OVER ( [ PARTITION BY <partition_by> ] ORDER BY <order_by> [ASC|DESC] )
```

## Parameters

{: .no_toc}

| Parameter        | Description                                       | Supported input types | 
|:-----------------|:--------------------------------------------------|:----------------------| 
| `<expression>`   | A SQL expression of any type to evaluate.         | Any                   |
| `<partition_by>` | An expression used for the `PARTITION BY` clause. | Any                   |
| `<order_by>`     | An expression used for the order by clause.       | Any                   |

## Return Types

Same as the input type of `<expression>`.

This function respects `NULL` values, and the results will be ordered with the default `NULL` ordering `NULLS LAST` unless

otherwise specified in the `ORDER BY` clause. If no `ORDER BY` clause is applied, the order will be undefined.


## Examples

The following code example selects the `nickname`, `level`, `current_score`, and `highest_score` for each level, using the `NTH_VALUE` function to retrieve the top score within each level, ordered by `current_score` in descending order.

{: .no_toc}
{% include sql_examples/first_value.md %}
