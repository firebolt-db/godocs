---
layout: default
title: UPPER
description: Reference material for UPPER function
grand_parent: SQL functions
parent: String functions
great_grand_parent: SQL reference
---

# UPPER

Converts the string to uppercase format.

## Syntax
{: .no_toc}

```sql
UPPER(<expression>)
```

| Parameter  | Description                                             | Supported input types |
| :---------- | :------------------------------------------------------- |:---------|
| `<expression>` | The string to be converted to all uppercase characters. | Any data type that is convertible to `VARCHAR` | 

## Return Type
`VARCHAR` 

## Example
{: .no_toc}

The following example converts a video game player's username from lower case syntax to all uppercase syntax:

```sql
SELECT
	UPPER('esimpson')
```

**Returns**: `ESIMPSON`
