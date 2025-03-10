---
layout: default
title: DATE
description: Reference material for DATE function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Date and time functions
---

# DATE

Converts a `TIMESTAMP`, `TIMESTAMPTZ`, `DATE`, or `TEXT` value to a `DATE` value. If the conversion cannot be performed, the `DATE` function raises an error.

## Syntax
{: .no_toc}

```sql
DATE(<expression>)
```

### Aliases
```sql
CAST(<expression> AS DATE)
<expression>::DATE
```

## Parameters
{: .no_toc}

| Parameter | Description |
| :-------- | :---------- |
| `<expression>` | The expression that should be converted to a `DATE`. |

## Return Type

The `DATE` function returns a result of type `DATE`. If the conversion cannot be performed, the `DATE` function raises an error. For more information on conversion rules, check out the documentation of the [DATE data type]({% link sql_reference/date-data-type.md %}).

## Example

The following code example converts the `TEXT` value `1990-01-01` to a `DATE` value representing that date:

```sql
SELECT DATE('1990-01-01');
```

**Returns**

```
1990-01-01
```
