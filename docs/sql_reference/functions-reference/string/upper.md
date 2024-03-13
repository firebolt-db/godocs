---
layout: default
title: UPPER
description: Reference material for UPPER function
grand_parent: SQL functions
parent: String functions
great_grand_parent: SQL reference
---

# UPPER

Converts the input string to uppercase characters. Note that Firebolt uses the `ucs_basic` collation, therefore `upper` only converts ASCII characters to uppercase. Non-ASCII characters remain unchanged.

## Syntax
{: .no_toc}

```sql
UPPER(<expression>)
```

## Parameters
{: .no_toc}

| Parameter | Description                         |Supported input types |
| :--------- | :----------------------------------- | :---------------------|
| `<expression>` | The string to be converted to uppercase characters. | `TEXT` |

## Return Type
`TEXT`

## Example
{: .no_toc}

The following example converts a game player's username from lowercase to uppercase characters:

```sql
SELECT
	UPPER('esimpson') as username
```

**Returns**: `ESIMPSON`


Because Firebolt uses the `ucs_basic` collation, non-ASCII characters are not uppercased:
```sql
SELECT UPPER('München')
```

**Returns**: `MüNCHEN`
