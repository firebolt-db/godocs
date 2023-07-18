---
layout: default
title: TO_INT
description: Reference material for TO_INT function
grand_parent: SQL functions
parent: String functions
great_grand_parent: SQL reference
---

# TO\_INT

Converts a string to a numeric `INTEGER` data type.

## Syntax
{: .no_toc}

```sql
TO_INT(<expression>)
```
## Parameters 
{: .no_toc}

| Parameter | Description                                                                                              | Supported Input Types | 
| :--------- | :-------------------------------------------------------------------------------------------------------- | :-----------|
| `<expression>`  | The expression to become an integer | A numeric data type expression that resolves to a `TEXT` data type |

## Return Types
`NUMERIC` 

## Example
{: .no_toc}

The following examplesadjusts the inputted string value as the integer `10`: 
```sql
SELECT
	TO_INT('10');
```

**Returns**: `10`
