---
layout: default
title: ARRAY_SUM_GLOBAL
description: Reference material for ARRAY_SUM_GLOBAL function
parent: Aggregate array functions
grand_parent:  SQL functions
---

# ARRAY\_SUM\_GLOBAL

Returns the sum of elements in the array column accumulated over the rows in each group.

For more information and the sample data used in the example below, please refer to [Aggregate Array Functions](./aggregate-array-functions.md).

## Syntax
{: .no_toc}

```sql
ARRAY_SUM_GLOBAL(<array>)
```
## Parameters
| Parameter | Description                                                    | Supported input types | 
| :--------- | :-------------------------------------------------------------- | :-------|
| `<array>`   | The array column over which the function will sum the elements | Any `<array>` column |

## Return Types
`ARRAY`

## Example
{: .no_toc}

The example below uses the following table `Scores`:

| nickname        | recent_scores |
| :---------------| :-------------|
| steven70        | \[1,3,4]      |
| sanderserin     | \[3,5,6,7]    |
| esimpson        | \[30,50,60]   |

<!-- | Parameter | Description                                                               |
| :--------- | :------------------------------------------------------------------------- |
| `<arr>`   | The function returns the maximum element from the provided array column | -->

In this example, the function calculates the sum of each player's recent scores. For example, the user `esimpson` received a sum of `140` points, so this value is returned in the `score_sum` column. 

```sql
SELECT
	nickname,
	ARRAY_MAX_GLOBAL(recent_scores) AS max_score
FROM
	Scores
GROUP BY
	nickname;
```

**Returns**:

| nickname         | score_sum     |
| :----------------| :------------ |
| steven70         | 8             |
| sanderserin      | 21            |
| esimpson         | 140           |