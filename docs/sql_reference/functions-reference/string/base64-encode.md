---
layout: default
title: BASE64_ENCODE
description: Reference material for BASE64_ENCODE function
nav_exclude: true
search_exclude: true
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: String functions
published: false
---

# BASE64\_ENCODE

Encodes a string into Base64 notation.

## Syntax
{: .no_toc}

```sql
BASE64_ENCODE(<expression>)
```
## Parameters
{: .no_toc}

| Parameter | Description                                                                 | Supported input types| 
| :--------- | :--------------------------------------------------------------------------|:----------|
| `<expression>`  | Any expression to be encoded | `TEXT`  |

### Return Type
`TEXT`

## Example
{: .no_toc}

The following examples encodes a user's nickname to Base64 notation: 

```sql
SELECT
	BASE64_ENCODE('esimpson');
```

**Returns**: `SZXNpbXBzb24=`
