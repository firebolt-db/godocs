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

## Parameters
{: .no_toc}

| Parameter | Description                         |Supported input types |
| :--------- | :----------------------------------- | :---------------------|
| `<expression>`  | The expression to covert to an integer. | `TEXT` |

## Return Type
`INTEGER` 

## Example
{: .no_toc}

The following example converts the input string to the integer `10`: 

```sql
SELECT
	TO_INT('10');
```

**Returns**: `10`
