---
layout: default
title: REPEAT
description: Reference material for REPEAT function
grand_parent: SQL functions
parent: String functions
great_grand_parent: SQL reference
---

# REPEAT

This function repeats the provided string a requested number of times.

## Syntax
{: .no_toc}

```sql
REPEAT(<expression>, <value>)
```

## Parameters 
{: .no_toc}

| Parameter            | Description                  | Supported input types | 
| :-------------------- | :---------------------------|:----------------------|
| `<expression>`           | The string to be repeated | Any string               |                                                                     |
| `<value>` | The number of needed repetitions | Any integer greater than 0 |

## Return types 
`TEXT`

## Example
{: .no_toc}

The following example repeats the author of a a video game 5 times. 

```sql
SELECT
	REPEAT('UFG Inc.' , 5);
```

**Returns**: `UFG Inc. UFG Inc. UFG Inc. UFG Inc. UFG Inc.`
