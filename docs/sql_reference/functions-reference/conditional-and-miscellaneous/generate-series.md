---
layout: default
title: GENERATE_SERIES
description: Reference material for GENERATE_SERIES function
grand_parent: SQL functions
parent: Conditional and miscellaneous functions
---

# GENERATE_SERIES
Generates a single rowset of values from `start` to `stop`, with a step size of `step`. `GENERATE_SERIES` is a table-valued function. 

## Syntax
{: .no_toc}

```sql
GENERATE_SERIES ( <start>, <stop> [, <step> ] )
```

## Parameters
{: .no_toc}

| Parameter | Description |Supported input types |
| :--------- |:------------ |:--------- |
| `<start>`  | The first value in the interval. | `BIGINT`, `INTEGER` |
| `<stop>` | The last value in the interval. <br/>The series stops once the last generated step value exceeds the stop value. |  `BIGINT`, `INTEGER` |
| `<step>` | Optional literal integer value to set step. If not included, the default step is 1. | `BIGINT`, `INTEGER` |


## Return Type
{: .no_toc}

Setof `INTEGER` if all operands are of type `INTEGER`, otherwise setof `BIGINT`.


## Example
{: .no_toc}


```sql
SELECT n, DATE_ADD('DAY', n, '2023-02-02') result 
FROM GENERATE_SERIES(1, 10, 2) s(n)
```

**Returns**:

| n | result |
| :--- | :--- |
| 1 | 2023-02-03 00:00:00 |
| 3 | 2023-02-05 00:00:00 |
| 5 | 2023-02-07 00:00:00 |
| 7 | 2023-02-09 00:00:00 |
| 9 | 2023-02-11 00:00:00 |
