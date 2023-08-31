---
layout: default
title: IFNULL
description: Reference material for IFNULL function
grand_parent: SQL functions
parent: Conditional and miscellaneous functions
great_grand_parent: SQL reference
---

# IFNULL
Compares two expressions. Returns `<expression1>` if it’s non-NULL, otherwise returns `<expression2>`.

## Syntax
{: .no_toc}

```sql
IFNULL(<expression1>, <expression2>)
```

## Parameters 
{: .no_toc}

| Parameter | Description | Supported input types | 
| :-------- | :---------- |:---------|
| `<expression1>`, `<expression2>` | Expressions that evaluate to any data type that Firebolt supports. | Any | 

## Return Types
Same as input type 

## Remarks
{: .no_toc}

Use `ZEROIFNULL(<expression>)` as a synonym shorthand for `IFNULL(<expression1>, 0)`.

## Example
{: .no_toc}

The following truth table demonstrates values that `IFNULL` returns based on the values of two columns: `level` and `player_id`:

```sql
SELECT level, player_id, IFNULL(level,player_id), IFNULL(player_id,level)
FROM players;
```


| level     |   player_id    | IFNULL(level,player_id) | IFNULL(player_id,level) |
|:-----------|:-----------|:-------------------|:---------------|
| 0         | 32        | 0                 | 32                |
| 1         | [NULL]    | 30                 | 30                 |
| [NULL]    | 33        | 33                | 33                |
| [NULL]    | [NULL]    | [NULL]            | [NULL]            |
-----------+-----------+-------------------+-------------------+

