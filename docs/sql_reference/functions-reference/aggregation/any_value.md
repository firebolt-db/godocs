---
layout: default
title: ANY_VALUE
description: Reference material for ANY_VALUE
grand_parent: SQL functions
parent: Aggregation functions
great_grand_parent: SQL reference

---

# ANY_VALUE

Returns a single arbitrary value from the specified column.

**Synonym:** `ANY`

## Syntax
{: .no_toc}

```sql
ANY_VALUE(<expression>)
```
## Parameters
{: .no_toc}


| Parameter | Description                                  |Supported input types |
| :-------- | :-------------------------------------------- | :--------- |
| `<expression>`  | Any expression | Any       |

This function ignores `NULL` inputs. It returns `NULL` only when all inputs are `NULL` or there are no inputs.

## Return Type
{: .no_toc}

Same as input type

## Example
{: .no_toc}

```sql
SELECT
	ANY_VALUE(nickname)
FROM
	UNNEST (ARRAY['kennethpark', NULL, 'sabrina21', 'ruthgill', 'steven70']) AS players(nickname);
```

**Returns** Any value of the `nickname` column, excluding `NULL`. The first time the query below runs, the nickname `kennethpark` might be returned. The second time the query runs, `sabrina21` or any other value, such as `ruthgill` or `steven70`, might be returned, but `NULL` will never be returned while non-`NULL` options exist.

```sql
SELECT ANY_VALUE(data) FROM UNNEST (ARRAY[NULL, NULL, NULL]) arr(data);
SELECT ANY_VALUE(data) FROM UNNEST (ARRAY[1,2,3]) arr(data) WHERE false;
```
**Returns** `NULL` as no non-`NULL` values are available.
