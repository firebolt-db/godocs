---
layout: default
title: HASH
description: Reference material for HASH function
parent: Conditional and miscellaneous functions
published: true
---

# HASH

Takes one or more input parameters of any data type and returns a 64-bit non-cryptographic hash value. `HASH` uses the CityHash algorithm for string data types, implementation-specific algorithms for other data types, and the CityHash combinator to produce the resulting hash value. `NULL` values of any type get the same fixed value. See [CITY_HASH](./city-hash.md) if `NULL` values should produce `NULL`.

## Syntax
{: .no_toc}

```sql
HASH(<expression>, [, expression [,...]])
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
SELECT HASH('esimpson', '08-25-2016')
```

**Returns:** `-6,509,667,128,195,191,394`

```sql
SELECT HASH(NULL, '08-25-2016')
```

**Returns:** `7610523868633494549`
