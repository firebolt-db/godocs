---
layout: default
title: CASE
description: Reference material for CASE function
grand_parent: SQL functions
parent: Conditional and miscellaneous functions
great_grand_parent: SQL reference
---

# CASE

Conditional expression similar to if-then-else statements.
If the result of the condition is true, then the value of the CASE expression is the result that follows the condition.  If the result is false, any subsequent WHEN clauses (conditions) are searched in the same manner.  If no WHEN condition is true, then the value of the case expression is the result specified in the ELSE clause.  If the ELSE clause is omitted and no condition matches, the result is NULL.

## Syntax
{: .no_toc}

```sql
CASE
    WHEN <condition> THEN <result>
    [WHEN ...n]
    [ELSE <result>]
END;
```

## Parameters 
{: .no_toc}

| Parameter     | Description      | Supported input types | 
| :------------- | :-------------------------- | :--------|
| `<condition>` | A condition can be defined for each `WHEN`, and `ELSE` clause.    | Any expression that returns a boolean result | 
| `<result>`    | The result of any condition. Every `THEN` clause receives a single result. All results in a single `CASE` function must share the same data type. | Any |

## Return type 
Same data type as `<result>`

## Example
{: .no_toc}

This example references a table `player_level` with the following columns and values: 

| player              | currentlevel |
| :-------------------- | :------ |
| kennethpark         | 3   |
| esimpson       | 8     |
| sabrina21 | 11   |
| rileyjon      | 15    |
| burchdenise     | 4    |


The following example categorizes each entry by length. If the movie is longer than zero minutes and less than 50 minutes it is categorized as SHORT. When the length is 50-120 minutes, it's categorized as Medium, and when even longer, it's categorized as Long.

```sql
SELECT
	player,
	currentlevel,
	CASE
		WHEN length > 0
		AND length <= 5 THEN 'Beginner'
		WHEN length > 5
		AND length <= 12 THEN 'Intermediate'
		WHEN length > 12 THEN 'Expert'
	END ranking
FROM
	player_level
ORDER BY
	player;
```

**Returns**:

| player              | currentlevel | ranking | 
| :-------------------- | :------ | :-------|
| kennethpark         | 3   | Beginner | 
| esimpson       | 8     | Intermediate | 
| sabrina21 | 11   | Intermediate |
| rileyjon      | 15    | Expert |
| burchdenise     | 4    | Beginner | 

