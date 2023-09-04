---
layout: default
title: REVERSE
description: Reference material for REVERSE function
grand_parent: SQL functions
parent: String functions
great_grand_parent: SQL reference
---

# REVERSE

Returns a string of the same size as the original string, with the elements in reverse order.

## Syntax
{: .no_toc}

```sql
REVERSE(<expression>)
```

## Parameters 
{: .no_toc}

| Parameter  | Description                |Supported Input Types |
| :---------- | :--------------------------|:---------------------|
| `<expression>` | The string to be reversed. | `TEXT` | 

## Return Type
`TEXT`

## Example
{: .no_toc}
The following example returns the player's username with the characters reversed: 

```sql
SELECT
	REVERSE('esimpson') AS username; 
```

**Returns**: `'nospmise'`
