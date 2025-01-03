---
layout: default
title: RANDOM
description: Reference material for RANDOM function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Numeric functions
---

# RANDOM

Returns a pseudo-random unsigned value greater than 0 and less than 1 of type `DOUBLE PRECISION`.

## Syntax
{: .no_toc}

```sql
RANDOM()
```
## Return Types
`DOUBLE PRECISION`

## Examples
{: .no_toc}

**Example**

The following code example demonstrates using `RANDOM` without any other numeric functions. This generates a `DOUBLE PRECISION` value less than 1:

```sql
SELECT RANDOM()
```

**Returns:**

`0.8544004706537051`

**Example**

To create a random integer number between two values, you can use `RANDOM` with the `FLOOR` function as demonstrated below. `a` is the lesser value and `b` is the greater value.

```sql
SELECT
	FLOOR(RANDOM() * (b - a + 1)) + a;
```

The following code example generates a random integer between 50 and 100:

```sql
SELECT
	FLOOR(RANDOM() * (100 - 50 + 1)) + 50;
```

**Returns**

`61`
