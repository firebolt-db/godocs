---
layout: default
title: ARRAY_MIN_GLOBAL
description: Reference material for ARRAY_MIN_GLOBAL function
parent: Aggregate array functions
grand_parent:  SQL functions
---

# ARRAY\_MIN\_GLOBAL

Returns the minimal element taken from all the array elements in each group.

For more information and the sample data used in the example below, please refer to [Aggregate Array Functions](./aggregate-array-functions.md).

## Syntax
{: .no_toc}

```sql
ARRAY_MIN_GLOBAL(<array>)
```

| Parameter | Description                                                              | Supported input types |
| :--------- | :------------------------------------------------------------------------ |: ------------------|
| `<array>`   | The array column from which the function will return the minimal element | Any `<array>` column        |

## Return Types
`NUMERIC`

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

In this example, the function calculates the minimum score earned by each player's recent scores. For example, the user `esimpson` received a minimum score of `30`, so this value is returned as `min_score`. 

```sql
SELECT
	nickname,
	ARRAY_MAX_GLOBAL(recent_scores) AS min_score
FROM
	Scores
GROUP BY
	nickname;
```

**Returns**:

| nickname         | min_score     |
| :----------------| :------------ |
| steven70         | 1             |
| sanderserin      | 3             |
| esimpson         | 30            |



