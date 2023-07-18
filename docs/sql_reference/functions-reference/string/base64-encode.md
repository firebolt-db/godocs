---
layout: default
title: BASE64_ENCODE
description: Reference material for BASE64_ENCODE function
grand_parent: SQL functions
parent: String functions
great_grand_parent: SQL reference
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
| `<expression>`  | Any expression to be encoded | Any expression that evaluates to a `TEXT` data type |

### Return Types
{: .no_toc}
`VARCHAT(8000)`, `VARCHAR(MAX)`

## Example
{: .no_toc}
The following examples encodes a video game user's nickname to Base64 notation: 

```sql
SELECT
	BASE64_ENCODE('esimpson');
```

**Returns**: `SZXNpbXBzb24=`
