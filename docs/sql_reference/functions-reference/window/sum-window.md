---
layout: default
title: SUM OVER
description: Reference material for SUM function
grand_parent: SQL functions
parent: Window functions
great_grand_parent: SQL reference
---

# SUM OVER

Calculate the sum of the values within the requested window.

The SUM function works with numeric values and ignores `NULL` values.

For more information on usage, please refer to [Window Functions](./index.md).

## Syntax
{: .no_toc}

```sql
SUM([ DISTINCT ] <value> ) OVER ( [ PARTITION BY <partition_by> ] )
```

## Parameters 
{: .no_toc}

| Parameter | Description                                      |Supported input types | 
| :--------- | :------------------------------------------------ | :------------| 
| `<value>`   | The expression used for the `SUM` function       | Any numeric type |
| `<partition_by>`  | An expression used for the `PARTITION BY` clause | Any |

## Return Types
`NUMERIC` 

When `DISTINCT` is specified, duplicate values from `<expression>` are removed before calculating the sum.

## Example
{: .no_toc}

The example below shows how many players are on a specific level. 

```sql
SELECT
	level,
	SUM(players) OVER (PARTITION BY level ) AS current_players
FROM
	players;
```

**Returns**:

| level | current_players |
|:-----|:------|
| 1 | 156 |
| 2 | 108 |
| 3 | 127 |
| 4 | 198 |
| 5 | 207 |
