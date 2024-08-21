---
layout: default
title: COUNT OVER
description: Reference material for COUNT function
parent: Window functions
---

# COUNT

Count the number of values within the requested window.

For more information on usage, please refer to [Window Functions](./index.md)  

## Syntax
{: .no_toc}

```sql
COUNT( <value> ) OVER ( [ PARTITION BY <partition_by> ] )
```
## Parameters 
{: .no_toc}

| Parameter | Description                                      | Supported input types | 
| :--------- | :------------------------------------------------ | :------------| 
| `<value>`   | A value used for the `COUNT()` function.   | Any numeric type | 
| `<partition_by>`  | An expression used for the `PARTITION BY` clause. | Any | 

## Return Type
`NUMERIC`

## Example
{: .no_toc}

The following example generates a count of how many video game players have registered on a specific day: 

```sql
SELECT
	registeredon,
	COUNT(agecategory) OVER (PARTITION BY registeredon) AS count_of_players
FROM
	players;
```

**Returns**:

| registeredon | count_of_players                                 | 
| :--------- | :------------------------------------------------ |
| 2020-11-15  | 12 |
| 2020-11-16  | 8 | 
|  2020-11-17 | 4 |
| 2020-11-18 | 9 | 
