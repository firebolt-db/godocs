---
layout: default
title: AVG (aggregation function)
description: Reference material for AVG
grand_parent: SQL functions
parent: Aggregation functions
---


# AVG

Calculates the average of an expression.

## Syntax
{: .no_toc}

```sql
AVG(<value>)
```

| Parameter | Description                                  | Supported input types                                                                                                                                  |
| :---------| :--------------------------------------------|:-----------------------------------------------|
| `<value>`  | The expression used to calculate the average | Names of columns that contain numeric values | 

Valid values for the expression include column names or functions that return a column name or columns that contain numeric values.

{: .note}
The `AVG()` aggregation function ignores rows with NULL. For example, an `AVG` from 3 rows containing `1`, `2`, and NULL returns `1.5` because the NULL row is not counted. To calculate an average that includes NULL, use `SUM(COLUMN)/COUNT(*)`.

## Return Types
`NUMERIC`, `REAL`, `DOUBLE PRECISION`

## Example

The example below uses the following table `LevelPoints`. This table includes the maximum points a player can score at each level of the game:

| levels   | maxpoints |
| :--------| :---------|
| 1        | 50        |
| 2        | 100       |
| 3        | 150       |
| 4        | 200       |
| 5        | 250       |

In this example, the average of the `maxpoints` values is returned. 

```sql
SELECT 
    AVG(maxpoints) AS AverageMaxPoints 
FROM levels;
```

**Returns**:
| averagemaxpoints | 
| :----------------| 
| 150              |
