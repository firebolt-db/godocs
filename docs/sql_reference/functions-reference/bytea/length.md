---
layout: default
title: LENGTH (array function)
description: Reference material for LENGTH function
grand_parent: SQL functions
parent: Binary functions
great_grand_parent: SQL reference
---

# LENGTH

Returns the length (number of elements) of the given array.

## Syntax
{: .no_toc}

```sql
LENGTH(<arr>)
```

| Parameter | Description                         |
| :--------- | :----------------------------------- |
| `<arr>`   | The array to be checked for length. |

## Example
{: .no_toc}

```sql
SELECT
	LENGTH([ 1, 2, 3, 4 ]) AS res;
```

**Returns**: `4`
