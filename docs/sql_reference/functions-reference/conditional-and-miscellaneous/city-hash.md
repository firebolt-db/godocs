---
layout: default
title: CITY_HASH
description: Reference material for CITY_HASH function
great_grand_parent: SQL reference
grand_parent: SQL functions
parent: Conditional and miscellaneous functions
published: true
---

# CITY_HASH

Takes one or more input parameters of any data type and returns a 64-bit non-cryptographic hash value. `CITY_HASH` uses the CityHash algorithm for string data types, implementation-specific algorithms for other data types, and the CityHash combinator to produce the resulting hash value. If any of the inputs is `NULL`, the result will be `NULL`. See [HASH](./hash.md) if `NULL` values should not produce `NULL`.

## Syntax
{: .no_toc}

```sql
CITY_HASH(<expression>, [, expression [,...]])
```
## Parameters 
{: .no_toc}

| Parameter | Description                          |Supported input types | 
| :--------- | :---------------------------------- | :----------|
| `<expression>`   | An expression that returns any data type that Firebolt supports. | Any | 

## Return type
`BIGINT`

## Example
{: .no_toc}

```sql
SELECT CITY_HASH('esimpson', '08-25-2016')
```

**Returns:** `-6,509,667,128,195,191,394`

```sql
SELECT CITY_HASH(NULL, '08-25-2016')
```

**Returns:** `NULL`
