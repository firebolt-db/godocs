---
layout: default
title: CONCAT
description: Reference material for CONCAT function
grand_parent: SQL functions
parent: String functions
great_grand_parent: SQL reference
---

# CONCAT

Concatenates, i.e. combines, the text representations of all the input parameters without a separator, in the order they are provided.

## Syntax
{: .no_toc}

```sql
CONCAT( <expression>[, <expression>[, ...n]] );
```

**&mdash;OR&mdash;**

```sql
<expression> || <expression>
```

## Parameters 
{: .no_toc}

### `CONCAT` function

| Parameter | Description                         |Supported input types |
| :--------- | :----------------------------------- | :---------------------|
| `<expression>[, ...n]` | The expressions to be concatenated. | Any type |

The parameters to the `CONCAT` function can be of any data type, and will be converted to their text representation before concatenation. `NULL` parameters to the `CONCAT` function are treated as empty strings and ignored. If all parameters are `NULL`, the result will be an empty string.

### `||` operator

| Parameter | Description                         |Supported input types |
| :--------- | :----------------------------------- | :---------------------|
| `<expression>` | The expressions to be concatenated. | Any non-array type, but at least one `TEXT` |

One parameter to the `||` operator must be of type `TEXT`, while the other parameter may be of any non-array data type. Array types are not supported to avoid ambiguity with the array concatenation operator. If necessary, explicit type casts can be used to circumvent this restriction. If any parameter to the `||` operator is `NULL`, the result will also be `NULL`.

## Return Type
`TEXT`

## Example
{: .no_toc}

The following example concatenates users' `nicknames` and `emails` from the players table: 

```sql
SELECT
	CONCAT(nickname, ': ', email) as user_info
FROM players
LIMIT 5;
```

**Returns**:

| user_info                              |
| :--------------------------------------|
| steven70: daniellegraham@example.net   | 
| burchdenise: keith84@example.org       | 
| stephanie86: zjenkins@example.org      |
| sabrina21: brianna65@example.org       |
| kennethpark: williamsdonna@example.com |
