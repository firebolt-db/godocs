---
layout: default
title: HASH_AGG
description: Reference material for HASH_AGG
parent: Aggregation functions
---


# HASH_AGG

Calculates a hash value over all rows on a list of arguments. When `*` is specified as an argument - calculates a hash aggregation over all columns in the input. Performing a hash aggregation operation is useful for warming up table data or to check if the same values exist in two different tables.

**Alias:** `CHECKSUM`

## Syntax
{: .no_toc}

```sql
HASH_AGG( <expression1> [, <expression2>] [, <expression3>] [, ...<expressionN>] )
HASH_AGG(*)
```

## Parameters 
{: .no_toc}

| Parameter   | Description                                   | Supported input types | 
| :----------- | :---------------------------------------------------- | :-----------| 
| `<expression>`    | A column name for specific results for the `HASH_AGG` function to be applied to | Any `<column>` name | 

## Return Type
`BIGINT`

## Example
{: .no_toc}

For this example, we'll create a new table `tournament_information` as shown below.

```sql
CREATE DIMENSION TABLE tournament_information (name TEXT, prizedollars DOUBLE PRECISION, tournamentid INTEGER);

INSERT INTO
	tournament_information
VALUES
	('The Snow Park Grand Prix', 20903, 1),
	('The Acceleration Championsip', 19274, 2),
	('The Acceleration Trials', 13877, 3)
```

The example below calculates a hash aggregation based on all columns in the table `tournament_information`.

```sql
SELECT HASH_AGG(*) FROM tournament_information;
```

**Returns**: `1,889,915,309,908,437,919`

The next example calculates a hash aggregation based on columns `prizedollars` and `tournamentid` only.

```sql
SELECT HASH_AGG(prizedollars, tournamentid) FROM tournament_information;
```

**Returns**: `3,058,600,455,882,068,351`
